# Panda Image Generator using OpenAI DALL-E-3

This repository contains a [Python script](src/daily_panda_image/generators/image_generator.py) designed to generate unique panda images using OpenAI's **DALL-E-3** model. The input prompt for the model is produced by **GPT-4.1 Nano**, which creates contextual prompts based on global cultural, historical, or seasonal events occurring on the current date. The entire process is automated via a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that executes daily at 06:00 CEST (04:00 UTC).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** 1840: First Japanese Ladies' Day Festival, Japan  
A whimsical watercolor painting of a panda dressed in elegant kimono, joyfully arranging traditional cherry blossom decorations at a bustling Edo-era festival. Soft pastel hues highlight lanterns glowing gently as the panda hands out delicate paper cranes to cheerful women, capturing a charming moment of cultural celebration under a sky tinged with sunset pink and lavender.
