"""
Panda Image Generator - Automated daily generation of culturally-aware panda images.

This module provides functionality to generate creative prompts based on current cultural
events and create corresponding images using OpenAI's GPT-4.1 Nano and DALL-E-3 models.
"""

import sys

from daily_panda_image.config import get_settings
from daily_panda_image.generators.image_generator import PandaImageGenerator


def main():
    """Main entry point for the application."""
    try:
        get_settings()
        generator = PandaImageGenerator()
        generator.generate_daily_panda()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
