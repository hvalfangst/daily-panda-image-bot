# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Boats, dancing and cake-cutting: Bermuda welcomes King Charles, Hamilton, Bermuda]

A photorealistic image of a panda dressed in a festive suit, joyfully waving a small Union Jack flag among laughing schoolchildren at Hamilton Harbour at midday. The bright sun casts sharp shadows on the colonial architecture and clear blue waters. In the foreground, the panda skillfully balances on the edge of a vibrant parade float featuring Bermuda's iconic Gombey dancers. The panda's eyes gleam as it watches exotic birds overhead, their feathers catching the light. Nearby, a large cake adorned with the British Royal Crest stands, ready to be cut.
