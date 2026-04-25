# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Killing in prison is not difficult - the rise in cold-blooded attacks behind bars, San Quentin State Prison, California]

A photorealistic image of a panda in the central courtyard of San Quentin State Prison, midday under a stark, overcast sky casting diffused shadows across the scene. The panda, wearing a small plaid cap and holding a clipboard, is assisting in a conflict resolution session, surrounded by inmates in orange jumpsuits sitting attentively on benches arranged in a semicircle. The panda is gesturing animatedly, using hand movements to emphasize peace and understanding. Its thoughtful expression captures the serious yet hopeful tone of the gathering.
