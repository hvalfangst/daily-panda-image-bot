# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Government to propose electricity price changes in clean power push, London]

A photorealistic image of a panda wearing a smart business suit, seated at a polished mahogany conference table in a modern boardroom atop a high-rise building. The panda, with intense focus, is adjusting its glasses while examining a complex spreadsheet projected on a sleek digital screen displaying electricity price metrics.
