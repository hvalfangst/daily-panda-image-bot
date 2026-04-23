# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [My instinct was to help him: Runners help exhausted man finish Boston Marathon, Boston Marathon Finish Line]

A photorealistic image of a determined panda assisting an exhausted marathon runner at the Boston Marathon finish line. It is late afternoon, the sun casting long shadows on Boylston Street, highlighting the iconic blue and yellow painted finish line. The panda, sporting a sleek, lightweight running jacket with the Boston Marathon logo, expertly supports the runner's arm, encouraging him forward amid cheering crowds. The camera captures the scene at a low angle, emphasizing the panda's focused expression and powerful stance, both feet firmly planted. Nearby, two other runners rush in with uplifting smiles, and digital timelapses flash overhead on vibrant sponsor banners.
