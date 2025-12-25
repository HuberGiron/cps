import argparse
import socket
import struct
import time
import statistics

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
    ap = argparse.ArgumentParser(description="TCP stress-test probe (RTT/loss/throughput)")
    ap.add_argument("--host", required=True)
    ap.add_argument("--port", type=int, default=9002)
    ap.add_argument("--payload", type=int, default=256)
    ap.add_argument("--rate", type=float, default=100.0)
    ap.add_argument("--duration", type=float, default=30.0)
    args = ap.parse_args()

    if args.payload < 12:
        raise SystemExit("payload must be >= 12 bytes")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.host, args.port))

    interval = 1.0 / args.rate
    end_t = time.perf_counter() + args.duration

    sent = 0
    recv = 0
    rtts_ms = []

    seq = 0
    padding = b"\xBB" * (args.payload - 12)

    while time.perf_counter() < end_t:
        t0 = now_us()
        pkt = struct.pack("!IQ", seq, t0) + padding
        s.sendall(pkt)
        sent += 1

        data = b""
        while len(data) < len(pkt):
            chunk = s.recv(len(pkt) - len(data))
            if not chunk:
                break
            data += chunk

        if len(data) >= 12:
            r_seq, r_t0 = struct.unpack("!IQ", data[:12])
            if r_seq == seq:
                rtts_ms.append((now_us() - r_t0) / 1000.0)
                recv += 1

        seq += 1
        time.sleep(max(0.0, interval))

    s.close()

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
