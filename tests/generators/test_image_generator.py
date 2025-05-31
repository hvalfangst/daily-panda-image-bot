import os
import sys
import unittest
from unittest.mock import MagicMock, patch
import base64
import datetime

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from daily_panda_image.generators.image_generator import ImageGenerator, PandaImageGenerator

class TestImageGenerator(unittest.TestCase):
    def setUp(self):
        self.mock_client = MagicMock()
        self.generator = ImageGenerator(self.mock_client)

    def test_generate_image_success(self):
        mock_response = MagicMock()
        mock_response.data = [MagicMock(b64_json=base64.b64encode(b'testimage').decode())]
        self.mock_client.images.generate.return_value = mock_response

        prompt = "A panda eating bamboo"
        result = self.generator.generate_image(prompt)
        self.assertEqual(result, b'testimage')

    def test_generate_image_no_data(self):
        self.mock_client.images.generate.return_value = MagicMock(data=None)
        with self.assertRaises(ValueError):
            self.generator.generate_image("prompt")

    def test_generate_image_no_b64_json(self):
        mock_response = MagicMock()
        mock_response.data = [MagicMock(b64_json=None)]
        self.mock_client.images.generate.return_value = mock_response
        with self.assertRaises(ValueError):
            self.generator.generate_image("prompt")

class TestPandaImageGenerator(unittest.TestCase):
    @patch('daily_panda_image.generators.image_generator.PromptGenerator')
    @patch('daily_panda_image.generators.image_generator.ImageGenerator')
    @patch('daily_panda_image.generators.image_generator.FileManager')
    def test_generate_daily_panda_success(self, mock_file_manager, mock_image_gen, mock_prompt_gen):
        mock_client = MagicMock()
        panda_gen = PandaImageGenerator(openai_client=mock_client)
        panda_gen.prompt_generator.generate_prompt.return_value = "A panda at a festival"
        panda_gen.image_generator.generate_image.return_value = b'imagebytes'

        with patch('datetime.date') as mock_date:
            mock_date.today.return_value = datetime.date(2024, 6, 1)
            panda_gen.generate_daily_panda()

        panda_gen.prompt_generator.generate_prompt.assert_called_once()
        panda_gen.image_generator.generate_image.assert_called_once()
        mock_file_manager.save_image.assert_called_once()
        mock_file_manager.save_prompt.assert_called_once()
        mock_file_manager.save_event.assert_called_once()
        mock_file_manager.update_readme.assert_called_once()

    @patch('daily_panda_image.generators.image_generator.PromptGenerator')
    @patch('daily_panda_image.generators.image_generator.ImageGenerator')
    @patch('daily_panda_image.generators.image_generator.FileManager')
    def test_generate_daily_panda_exception(self, mock_file_manager, mock_image_gen, mock_prompt_gen):
        mock_client = MagicMock()
        panda_gen = PandaImageGenerator(openai_client=mock_client)
        panda_gen.prompt_generator.generate_prompt.side_effect = Exception("Prompt error")

        with self.assertRaises(Exception):
            panda_gen.generate_daily_panda()

if __name__ == "__main__":
    unittest.main()