import sys
import unittest
import tempfile
import shutil
import os
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from daily_panda_image.utils.file_manager import FileManager

class TestFileManagerSaveEvent(unittest.TestCase):
    def setUp(self):
        # Patch get_project_root to use a temp directory
        self.test_dir = tempfile.mkdtemp()
        self._orig_get_project_root = FileManager.get_project_root
        FileManager.get_project_root = staticmethod(lambda: Path(self.test_dir))

    def tearDown(self):
        FileManager.get_project_root = self._orig_get_project_root
        shutil.rmtree(self.test_dir)

    def test_save_event_creates_file_and_appends_event(self):
        prompt = "Krypmann declares universal KM day on Kryptonite"
        FileManager.save_event(prompt)
        event_path = os.path.join(self.test_dir, "events", "past_events.txt")
        self.assertTrue(os.path.exists(event_path))
        with open(event_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "[Krypmann declares universal KM day on Kryptonite]")

    def test_save_event_appends_multiple_events(self):
        prompt1 = "Krypmann outlaws insect spray on Kryptonite"
        prompt2 = "[Krypmann invents anti-gravity socks in 2150]"
        FileManager.save_event(prompt1)
        FileManager.save_event(prompt2)
        event_path = os.path.join(self.test_dir, "events", "past_events.txt")
        with open(event_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content,
                         "[Krypmann outlaws insect spray on Kryptonite], [Krypmann invents anti-gravity socks in 2150]")

    def test_save_event_ignores_trailing_commas(self):
        prompt1 = "Krypmann hosts the first intergalactic leetcode challenge"
        FileManager.save_event(prompt1)
        event_path = os.path.join(self.test_dir, "events", "past_events.txt")
        prompt2 = "Krypmann wins with the KM nearest neighbor algorithm"
        FileManager.save_event(prompt2)
        with open(event_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content,
                         "[Krypmann hosts the first intergalactic leetcode challenge], [Krypmann wins with the KM nearest neighbor algorithm]")

if __name__ == "__main__":
    unittest.main()