# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Thousands of Parisians evacuated as WW2 bomb detonated, Paris]

A photorealistic image of a panda dressed in a safety vest and helmet, orchestrating the evacuation process in a bustling Parisian neighborhood. The panda holds a megaphone, guiding a diverse crowd away from a cordoned-off area. In the background, the Seine glistens under the midday sun, historic buildings casting soft shadows.
