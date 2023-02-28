# from __future__ import annotations
#
# import argparse
# from typing import Sequence
#
#
# def main(argv: Sequence[str] | None = None) -> int:
#     parser = argparse.ArgumentParser()
#     parser.add_argument('filenames', nargs='*')
#     args = parser.parse_args(argv)
#
#     ret_code = []
#     for filename in args.filenames:
#         with open(filename, 'rb') as inputfile:
#             for i, line in enumerate(inputfile, start=1):
#                 if b'print(' in line:
#                     stmt = f'{filename}:{i} -> print statement found'
#                     print(stmt)
#                     ret_code.append(stmt)
#     print("Use logging instead of printing")
#     return bool(ret_code)

import ast
import sys


def check_file_for_print(file_contents):
    tree = ast.parse(file_contents)

    for node in ast.walk(tree):
        if isinstance(node, ast.Print):
            if not (is_in_docstring(node) or is_in_comment(file_contents, node)):
                return True

    return False


def is_in_docstring(node):
    """
    Check if a node is within a docstring
    """
    if isinstance(node.parent, ast.Expr) and isinstance(node.parent.value, ast.Str):
        return True
    return False


def is_in_comment(file_contents, node):
    """
    Check if a node is within a comment
    """
    comment_start = node.lineno - 1
    for line in file_contents.split('\n')[:comment_start]:
        if line.strip().startswith('#'):
            return True
    return False


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    for filename in argv:
        with open(filename) as f:
            file_contents = f.read()

        if check_file_for_print(file_contents):
            print(f"File {filename} contains a print statement not in a comment or docstring!")
            return 1

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
