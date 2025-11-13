import sys
from pathlib import Path
import unittest

# Ensure project root (the directory that contains app.py) is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        # Adjust expected string if your assignment wants something specific
        self.assertEqual(greet("World"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
