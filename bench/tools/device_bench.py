import argparse
import json
import os
import platform
import time
import hashlib
import zlib

def now() -> float:
    return time.perf_counter()

def sysinfo():
    return {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count_logical": os.cpu_count(),
    }

def bench_sha256(size_mb: int = 64):
    data = b"\x11" * (size_mb * 1024 * 1024)
    h = hashlib.sha256()
    t0 = now()
    h.update(data)
    dt = now() - t0
    return {"size_mb": size_mb, "seconds": dt, "throughput_mb_s": size_mb / dt, "sha256_prefix": h.hexdigest()[:16]}

def bench_zlib(size_mb: int = 32, level: int = 6):
    data = (b"ABCDEFGH" * 1024) * (size_mb * 128)
    t0 = now()
    c = zlib.compress(data, level)
    dt_c = now() - t0

    t1 = now()
    d = zlib.decompress(c)
    dt_d = now() - t1

    if d != data:
        raise RuntimeError("decompress mismatch")

    return {
        "size_mb": size_mb,
        "level": level,
        "compress_seconds": dt_c,
        "compress_mb_s": size_mb / dt_c,
        "decompress_seconds": dt_d,
        "decompress_mb_s": size_mb / dt_d,
        "compressed_ratio": len(c) / len(data),
    }

def bench_json_ops(iters: int = 2000):
    obj = {
        "device_id": "bench",
        "ts_ms": 0,
        "seq": 0,
        "signals": {f"s{i}": i * 0.123 for i in range(200)},
        "meta": {"a": "b" * 64, "tags": ["cps", "week1", "bench"]},
    }
    t0 = now()
    last = None
    import json as _json
    for i in range(iters):
        obj["seq"] = i
        last = _json.dumps(obj, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    dt_enc = now() - t0

    t1 = now()
    for _ in range(iters):
        _json.loads(last.decode("utf-8"))
    dt_dec = now() - t1

    return {"iters": iters, "encode_ops_s": iters / dt_enc, "decode_ops_s": iters / dt_dec, "bytes_last_payload": len(last)}

def main():
    ap = argparse.ArgumentParser(description="Device micro-benchmark (no external deps)")
    ap.add_argument("--out", default="bench/device_bench.json")
    ap.add_argument("--sha_mb", type=int, default=64)
    ap.add_argument("--zlib_mb", type=int, default=32)
    ap.add_argument("--json_iters", type=int, default=2000)
    args = ap.parse_args()

    result = {
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "system": sysinfo(),
        "benchmarks": {
            "sha256": bench_sha256(args.sha_mb),
            "zlib": bench_zlib(args.zlib_mb),
            "json": bench_json_ops(args.json_iters),
        },
        "notes": "Power mode/thermals/background load affect results. Run 3x and report variability.",
    }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Wrote: {args.out}")

if __name__ == "__main__":
    main()
