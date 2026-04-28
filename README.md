# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Suspect charged with attempted assassination of Trump at Washington dinner, Washington Hilton]

A photorealistic image of a panda clad in a tailored black suit, standing in the grand ballroom of the Washington Hilton, midnight light cascading through the immense crystal chandeliers. The panda is deftly wielding a metal detector wand, scanning attendees as they arrive at the door for the high-profile dinner event. The scene is alive with tension, security personnel in the background, their badges glinting under the ballroom's atmospheric lighting. Nearby, a distinguished crowd fills the elegantly set tables, each place adorned with ornate name cards bearing official seals.
