# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Video shows correspondents' dinner suspect charge checkpoint, Washington D.C.]

A photorealistic image of a panda, captured in the midst of a high-tension security breach at the prestigious White House Correspondents' Dinner. It's a scene of cinematic urgency, set at dusk under the ambient glow of city streetlights reflecting off the rain-slicked pavement. The panda, clad in a formal black bow tie, is positioned at a low angle, its furry paws gesturing emphatically as it helps direct guests to safety amidst chaos. Nearby, security agents are seen in sharp focus, drawing their guns as they react to a suspect charging past metal detectors.
