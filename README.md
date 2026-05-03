# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Airlines can cancel flights in advance over fuel shortages, under new plans, Miami International Airport, USA]

A photorealistic image of a panda wearing an aviation headset and a pilot's uniform, sitting in a cockpit at Miami International Airport. It's an overcast afternoon with looming storm clouds. The panda is intently examining fuel gauge dials and a tablet displaying flight cancellations due to a Middle East fuel shortage. Behind the panda through the cockpit window, a row of grounded aircraft reflects the runway lights on the tarmac, emphasizing the busy yet halted scene. A low-angle shot captures the panda's concentration as the cockpit's digital display panels cast a soft glow on its fur, accentuating the critical decision-making moment amidst the looming weather.
