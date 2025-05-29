# Panda Image Generator using OpenAI DALL-E-3

This repository contains a [Python script](src/daily_panda_image/generators/image_generator.py) designed to generate unique panda images using OpenAI's **DALL-E-3** model. The input prompt for the model is produced by **GPT-4.1 Nano**, which creates contextual prompts based on global cultural, historical, or seasonal events occurring on the current date. The entire process is automated via a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that executes daily at 06:00 CEST (04:00 UTC).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** A whimsical watercolor illustration of a panda dressed as a jazz musician celebrating the 2025 Memorial Day in the USA. The panda wears a vintage fedora, sunglasses, and a bow tie, playing a shiny saxophone amidst blooming spring flowers in a park. Soft sunlight filters through lush trees, casting warm glow on cheerful crowds holding American flags. The scene blends playful charm with respectful homage, featuring floating musical notes and fireworks in the background.
