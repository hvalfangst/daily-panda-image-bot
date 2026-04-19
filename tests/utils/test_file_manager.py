import sys
import unittest
import tempfile
import shutil
import os
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from daily_panda_image.utils.file_manager import FileManager


if __name__ == "__main__":
    unittest.main()

