# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Hate crime prosecutions to be fast-tracked after antisemitic attacks, Tower of London]

A photorealistic image of a panda dressed in a formal uniform, standing resolutely at the forefront of a press conference just outside the Tower of London. It is dusk, and the ancient stone walls behind are illuminated dramatically, casting long shadows on the cobblestone ground. The panda holds a folder marked "Fast-Track Justice," gesturing passionately with a paw as camera flashes capture the moment. The weather is clear, with a fiery sunset accentuating the scene's intensity. Reporters surround the panda, microphones directed intently.
