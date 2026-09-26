#!/usr/bin/env python3
"""Entry point: runs the renpho CLI straight from the repo, no installed package."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from renpho.cli import main

if __name__ == "__main__":
    main()
