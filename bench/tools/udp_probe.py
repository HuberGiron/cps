import argparse
import socket
import struct
import time
import statistics

# Packet: [seq:uint32][t0_us:uint64][padding...]
# seq -> loss estimation, t0_us -> RTT measurement

def now_us() -> int:
    return int(time.perf_counter() * 1_000_000)

def percentile(values, p: float):
    if not values:
        return None
    values = sorted(values)
    k = (len(values) - 1) * (p / 100.0)
    f = int(k)
    c = min(f + 1, len(values) - 1)
    if f == c:
        return values[f]
    return values[f] + (values[c] - values[f]) * (k - f)

def main():
    ap = argparse.ArgumentParser(description="UDP stress-test probe (RTT/loss/throughput)")
    ap.add_argument("--host", required=True)
    ap.add_argument("--port", type=int, default=9001)
    ap.add_argument("--payload", type=int, default=256, help="bytes per message")
    ap.add_argument("--rate", type=float, default=100.0, help="messages per second")
    ap.add_argument("--duration", type=float, default=30.0, help="seconds")
    ap.add_argument("--timeout", type=float, default=0.2, help="recv timeout (s)")
    args = ap.parse_args()

    if args.payload < 12:
        raise SystemExit("payload must be >= 12 bytes")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(args.timeout)

    interval = 1.0 / args.rate
    end_t = time.perf_counter() + args.duration

    sent = 0
    recv = 0
    rtts_ms = []

    seq = 0
    padding = b"\xAA" * (args.payload - 12)

    while time.perf_counter() < end_t:
        t0 = now_us()
        pkt = struct.pack("!IQ", seq, t0) + padding
        sock.sendto(pkt, (args.host, args.port))
        sent += 1

        try:
            data, _ = sock.recvfrom(65535)
            if len(data) >= 12:
                r_seq, r_t0 = struct.unpack("!IQ", data[:12])
                if r_seq == seq:
                    rtts_ms.append((now_us() - r_t0) / 1000.0)
                    recv += 1
        except socket.timeout:
            pass

        seq += 1
        time.sleep(max(0.0, interval))

    loss_pct = 100.0 * (sent - recv) / max(1, sent)
    throughput_mbps = (recv * args.payload * 8) / (args.duration * 1_000_000)
    p50 = percentile(rtts_ms, 50) if rtts_ms else None
    p95 = percentile(rtts_ms, 95) if rtts_ms else None
    jitter_ms = statistics.pstdev(rtts_ms) if len(rtts_ms) > 1 else 0.0

    print("RESULT",
          f"sent={sent}",
          f"recv={recv}",
          f"loss_pct={loss_pct:.3f}",
          f"throughput_mbps={throughput_mbps:.3f}",
          f"lat_p50_ms={p50:.3f}" if p50 is not None else "lat_p50_ms=NA",
          f"lat_p95_ms={p95:.3f}" if p95 is not None else "lat_p95_ms=NA",
          f"jitter_ms={jitter_ms:.3f}",
          sep=" ")

if __name__ == "__main__":
    main()
