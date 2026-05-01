# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [New footage shows how Trump dinner gunman charged through security in four seconds, Mar-a-Lago, Palm Beach, Florida]

A photorealistic image of an agile panda utilizing its natural climbing prowess, perching halfway up a large palm tree adjacent to the entrance of Mar-a-Lago. It is dusk, and the golden hues of the setting sun cast long, dramatic shadows on the polished marble exterior of the resort. The panda, intensely focused, is holding a security radio earpiece to its ear with one paw while pointing down with the other, eyes locked on the unfolding chaos below.
