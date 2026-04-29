# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Headline summary: Faisal Islam: Why the UAE's exit from Opec is a big deal, Burj Khalifa, Dubai]

A photorealistic image of a panda in a business suit standing confidently outside the Burj Khalifa at midday, the sun directly overhead casting distinct shadows. The panda holds a large, detailed document labeled "UAE-Opec Exit Agreement" with elegant gold lettering. Around it, a diverse group of reporters, microphones extended, capture the historic moment. The panda, the center of attention, gestures to a backdrop featuring large "UAE Energy Conference" banners fluttering in the soft desert breeze.
