from __future__ import annotations

from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    print(argv)
    print("Hello there! Welcome to Pre Commit!")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
