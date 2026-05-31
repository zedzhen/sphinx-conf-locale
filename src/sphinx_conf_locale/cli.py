__all__ = ["extract"]

import sys
from os import PathLike
from pathlib import Path
from subprocess import run


def extract(docs_dir: PathLike[str] | str, build_dir: PathLike[str] | str):
    input_file = Path(docs_dir) / "conf.py"
    output_file = Path(build_dir) / "gettext" / "sphinx.pot"
    return run(
        [
            "pybabel",
            "extract",
            "-k", "_",  # fmt: skip
            "-k", "_f",  # fmt: skip
            "-o", output_file,  # fmt: skip
            input_file,
        ]
    ).returncode


def main():
    if len(sys.argv) != 3:
        print(f"Used: {Path(sys.argv[0]).name} DOCS_DIR BUILD_DIR", file=sys.stderr)
        sys.exit(1)
    sys.exit(extract(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
