# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Sawe smashes two-hour mark to 'move goalposts for marathon running', London Marathon]

A photorealistic image of a panda running alongside Sabastian Sawe as he crosses the iconic finish line of the London Marathon near Buckingham Palace. It's an overcast morning, and the cobblestone street glistens from earlier rain, capturing the natural sheen under daylight. The panda, with sleek fur matted from exertion, stretches its paws forward, a participatory runner's bib pinned to its chest reading "Panda 42K". Spectators cheer wildly from the edge of the barricades, waving "History Made" signs.
