# Panda Image Generator using OpenAI DALL-E-3

This repository contains a [Python script](src/daily_panda_image/generators/image_generator.py) designed to generate unique panda images using OpenAI's **DALL-E-3** model. The input prompt for the model is produced by **GPT-4.1 Nano**, which creates contextual prompts based on global cultural, historical, or seasonal events occurring on the current date. The entire process is automated via a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that executes daily at 06:00 CEST (04:00 UTC).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** A whimsical watercolor illustration of a panda dressed as a jazz musician, celebrating Memorial Day in 2025. The panda wears a vintage red bow tie, sunglasses, and a floral lei, playing a shiny saxophone atop an American flag-themed float. Bright fireworks burst in the night sky above peaceful green fields, with cheerful people waving flags in the background. Soft lighting highlights the panda's joyful expression, blending cultural reverence with lively festivity. The scene captures both solemn remembrance and jubilant celebration with playful
