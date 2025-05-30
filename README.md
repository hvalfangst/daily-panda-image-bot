# Panda Image Generator using OpenAI DALL-E-3

This repository contains a [Python script](src/daily_panda_image/generators/image_generator.py) designed to generate unique panda images using OpenAI's **DALL-E-3** model. The input prompt for the model is produced by **GPT-4.1 Nano**, which creates contextual prompts based on global cultural, historical, or seasonal events occurring on the current date. The entire process is automated via a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that executes daily at 06:00 CEST (04:00 UTC).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** A whimsical watercolor painting of a panda dressed in traditional Ottoman attire, joyfully assisting craftsmen during the 17th-century Istanbul silk guild festival on May 30. The panda holds delicate threads, surrounded by vibrant textiles, intricate lanterns, and bustling market stalls under soft dawn light. Gentle pastel hues evoke a lively yet serene atmosphere as the scene celebrates craftsmanship and cultural pride in Ottoman Turkey.
