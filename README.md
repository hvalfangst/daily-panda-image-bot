# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Plaid Cymru ready to run Wales, leader says, after party wins Senedd vote, Cardiff Bay]

A photorealistic image of a panda joyously celebrating alongside Plaid Cymru supporters in front of the Welsh Parliament building, the Senedd, at dusk. The golden-hour sun casts warm, long shadows over an energized crowd waving Welsh flags. Our star panda, draped in a Plaid Cymru sash, is hoisted onto the shoulders of jubilant attendees, its expressive eyes gleaming with shared triumph. The panda clutches a "Cymru am Byth" (Wales Forever) banner, fur detailed under soft, natural light.
