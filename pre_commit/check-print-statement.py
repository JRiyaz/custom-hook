from __future__ import annotations

import argparse
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    ret_code = []
    for filename in args.filenames:
        with open(filename, 'rb') as inputfile:
            for i, line in enumerate(inputfile, start=1):
                if b'print(' in line:
                    stmt = f'{filename}:{i} -> print statement found'
                    print(stmt)
                    ret_code.append(stmt)
    return bool(ret_code)


if __name__ == '__main__':
    raise SystemExit(main())
