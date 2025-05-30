"""
Panda Image Generator - Automated daily generation of culturally-aware panda images.

This module provides functionality to generate creative prompts based on current cultural
events and create corresponding images using OpenAI's GPT-4.1 Nano and DALL-E-3 models.
"""

import base64
import datetime
from typing import Optional

from openai import OpenAI

from daily_panda_image.generators.prompt_generator import PromptGenerator
from daily_panda_image.utils.file_manager import FileManager


class ImageGenerator:
    """Handles image generation using DALL-E-3."""

    def __init__(self, client: OpenAI):
        """
        Initialize the image generator.

        Args:
            client: Configured OpenAI client instance
        """
        self.client = client

    def generate_image(self, prompt: str) -> bytes:
        """
        Generate an image based on the provided prompt.

        Args:
            prompt: Text prompt for image generation

        Returns:
            Image data as bytes

        Raises:
            ValueError: If no image data is returned from the API
        """
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            response_format="b64_json"
        )

        if not response or not response.data or not response.data[0].b64_json:
            raise ValueError("No image data returned from the API.")

        image_base64 = response.data[0].b64_json
        return base64.b64decode(image_base64)


class PandaImageGenerator:
    """Main orchestrator for the panda image generation process."""

    def __init__(self, openai_client: Optional[OpenAI] = None):
        """
        Initialize the panda image generator.

        Args:
            openai_client: Optional pre-configured OpenAI client
        """
        self.client = openai_client or OpenAI()
        self.prompt_generator = PromptGenerator(self.client)
        self.image_generator = ImageGenerator(self.client)

    def generate_daily_panda(self) -> None:
        """
        Generate and save a daily panda image with prompt.

        Raises:
            Exception: If any step in the generation process fails
        """
        current_date = datetime.date.today()

        try:
            # Generate prompt
            print(f"Generating prompt for {current_date}...\n")
            prompt = self.prompt_generator.generate_prompt(current_date)
            print(f"Generated prompt: {prompt}\n")

            # Generate image
            print("Generating image based on prompt...\n")
            image_bytes = self.image_generator.generate_image(prompt)
            print("Image generation successful. Saving files...\n")

            # Save files
            FileManager.save_image(image_bytes, current_date)
            FileManager.save_prompt(prompt, current_date)
            FileManager.save_event(prompt)
            FileManager.update_readme(prompt)

            print("Daily panda generation completed successfully!\n")

        except Exception as e:
            print(f"Error during panda generation: {e}")
            raise