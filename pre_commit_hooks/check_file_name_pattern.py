# This is basically a dumber and more flexible version of this hook:
# https://github.com/pre-commit/pre-commit-hooks/blob/master/pre_commit_hooks/tests_should_end_in_test.py

import argparse
import os.path
import re
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument('--pattern', type=str, default='.*',
                        help='Expected file name pattern (regex)')
    args = parser.parse_args(argv)

    retcode = 0
    test_name_pattern = args.pattern
    for filename in args.filenames:
        base = os.path.basename(filename)
        if not re.match(test_name_pattern, base):
            retcode = 1
            print(f'{filename} does not match pattern "{test_name_pattern}"')

    return retcode


if __name__ == '__main__':
    raise SystemExit(main())
