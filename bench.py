import sys
import time


def bench(fn):
    start = time.perf_counter()
    _ = fn()
    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("module")
    parser.add_argument("bench", default="price")
    args = parser.parse_args()
    try:
        mod = __import__(f"benches.{args.module}")
        mod = getattr(mod, args.module)
        fn = getattr(mod, args.bench)
    except Exception as e:
        print(e)
        print(f"No benchmark called {args.module}", file=sys.stderr)
        sys.exit(-1)
    t = bench(fn)
    print(f"{args.module},{args.bench},{t}")
