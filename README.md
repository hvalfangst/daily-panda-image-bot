# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Women can wait years for an endometriosis diagnosis. New tech could change that, Royal Free Hospital, London]

A photorealistic image of a panda clad in a white lab coat, intently examining a large medical scan on a state-of-the-art digital display inside the sterile setting of the Royal Free Hospital in London. It is midday, and the scene is brightly illuminated by the natural light pouring through the hospital's massive floor-to-ceiling windows. The panda is surrounded by intricate medical equipment, highlighting the cutting-edge technology used in endometriosis diagnosis. The panda's furry paw gently taps data on the touch screen, as if analyzing the new scanning technique.
