# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Trump says US-Iran ceasefire still in place after exchange of fire in Strait of Hormuz, Strait of Hormuz]

A photorealistic image of a determined panda strategically adjusting naval equipment on the deck of a US naval vessel at dusk in the Strait of Hormuz. The panda is wearing a naval officer's jacket, symbolically participating in ceasefire negotiations. The scene captures a glowing orange horizon as the sun sets over the waters, illuminating the panda's focused expression. Sleek, radar equipment is visible around the panda, exhibiting realistic metal textures and sharp detail. In the background, a vibrant yet tense seascape showcases Iranian and US naval ships maintaining watchful distance.
