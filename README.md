# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Two Britons self-isolating in UK after leaving hantavirus cruise ship early, London Eye]

A photorealistic image of a panda, dressed in a smart navy blue blazer, joyfully walking across the Westminster Bridge at midday. The panda carries a miniature Union Jack flag, symbolizing a welcome to the self-isolating Britons. In the background, the iconic London Eye looms large, framed by a clear, azure sky. Bright sunlight casts gentle shadows, creating a crisp, lively atmosphere. Tourists, masked and maintaining distance, stroll with caution. From a low angle, the camera captures the panda's determined expression, emphasizing its ambassadorial role in public health.
