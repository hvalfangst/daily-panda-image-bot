# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** 1. "Trump tells BBC that King's visit could 'absolutely' help repair relations with UK, Buckingham Palace, London"

A photorealistic image of a panda dressed in a well-tailored, dark pinstripe suit, confidently strolling through the opulent gardens of Buckingham Palace at midday. The panda holds a large smartphone in one paw, engaged in a visible FaceTime conversation with President Trump, whose visage appears clearly on the screen. The backdrop features the iconic Palace facade bathed in the crisp noon sunlight, while meticulously groomed hedges and vibrant floral arrangements provide depth and color. The panda's fur texture appears lifelike, with individual strands catching and reflecting light realistically.
