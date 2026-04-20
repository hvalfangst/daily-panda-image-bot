# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Spat at, threatened and kidnapped: British Jews tell of rising antisemitism, London]

A photorealistic image of a panda standing in a bustling London neighborhood, the streets lined with iconic terraced houses and a gloomy overcast sky casting a somber atmosphere. The panda, wearing a reflective jacket and holding a clipboard, is purposefully engaging with a diverse crowd gathered for a community dialogue on antisemitism.
