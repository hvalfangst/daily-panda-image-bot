import os
import sys
import unittest

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))


if __name__ == "__main__":
    unittest.main()
