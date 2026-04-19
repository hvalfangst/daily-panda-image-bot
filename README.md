# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Thousands of Parisians evacuated as WW2 bomb detonated, Paris]

A photorealistic image of a panda in a reflective vest, assisting French police and bomb disposal units. The panda is gently guiding Parisians across a cordoned street lined with Haussmannian buildings. Smoke drifts in the background from the controlled detonation site, casting dramatic shadows. Natural light filters through the overcast sky, highlighting the panda's thick fur and the crowd's anxious faces.
