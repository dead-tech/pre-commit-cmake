from __future__ import annotations

import argparse
import os
import subprocess
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def working_directory(path: str) -> Iterator[None]:
    prev_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)


def ext_cmd(*cmd: str) -> int:
    result = subprocess.run(cmd, capture_output=True)

    if result.returncode != 0:
        print(result.stderr.decode())

    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--build-dir', default='build/',
        help='path to build dir',
    )
    parser.add_argument('--release', action='store_true', help='release build')
    parser.add_argument(
        '--jobs', default=1, type=int,
        help='number of jobs to invoke make with',
    )
    args = parser.parse_args()

    build_dir = os.path.abspath(args.build_dir)

    build_type = 'Debug'

    if args.release:
        build_type = 'Release'

    if not os.path.isdir(build_dir):
        os.mkdir(build_dir)

    with working_directory(build_dir):
        cmake_retval = ext_cmd(
            'cmake', '..', f'-DCMAKE_BUILD_TYPE={build_type}',
        )
        make_retval = ext_cmd('make', f'-j{args.jobs}')

    return cmake_retval | make_retval


if __name__ == '__main__':
    raise SystemExit(main())
