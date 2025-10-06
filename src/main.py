from typing import Tuple, Optional
import argparse


def tally_game(points: str, target: int = 21, cap: int = 30) -> Tuple[int, int, Optional[str]]:
    a = b = 0
    n = len(points)

    for idx, ch in enumerate(points):
        c = ch.upper()
        if c not in {"A", "B"}:
            raise ValueError(f"Invalid character '{ch}' at index {idx}")

        if c == "A":
            a += 1
        else:
            b += 1

        # Winner by 2 at/after target
        if (a >= target or b >= target) and abs(a - b) >= 2:
            if idx != n - 1:  # extra rallies after decision
                raise ValueError(
                    f"Extra rallies recorded after winner decided at index {idx}; first extra at index {idx + 1}"
                )
            return a, b, ("A" if a > b else "B")

        # Winner at cap (next point wins at 30)
        if a == cap or b == cap:
            if idx != n - 1:
                raise ValueError(
                    f"Extra rallies recorded after winner decided at index {idx}; first extra at index {idx + 1}"
                )
            return a, b, ("A" if a > b else "B")

    # No decision within provided rallies
    return a, b, None


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Badminton single-game score calculator")
    p.add_argument("--points", required=True, type=str, help="String of rally points")
    p.add_argument("--target", type=int, default=21, help="Target score")
    p.add_argument("--cap", type=int, default=30, help="Cap score")
    args = p.parse_args(argv)

    a, b, winner = tally_game(args.points, target = args.target, cap = args.cap)
    
    if winner is None:
        print(f"score: {a}-{b} | winner: undecided")
    else:
        print(f"score: {a}-{b} | winner: {winner}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
