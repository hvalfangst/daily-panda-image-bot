# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Police seek to arrest billionaire K-pop mogul, Seoul, South Korea]

A photorealistic image of a panda acting as a detective, poised on a rooftop overlooking Bang Si-hyuk's posh corporate office in Seoul's affluent Gangnam district. It's dusk, with golden-hour light casting long shadows and a warm glow over the sleek skyscrapers. The panda, in a tailored trench coat, holds a high-tech surveillance camera aimed at the building. The rooftop is littered with surveillance gear, legal documents, and a map marked with red pins highlighting key locations in the city. The camera's viewpoint captures Bang Si-hyuk's silhouette in an office window.
