# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Trump says US to 'guide' stranded ships through Strait of Hormuz, Strait of Hormuz]

A photorealistic image of a determined panda standing at the helm of a US Navy vessel cutting through the waters of the Strait of Hormuz at dawn. The ocean reflects the orange and pink hues of the rising sun, casting a warm glow over the scene. Surrounding the panda are sleek, high-tech navigation instruments, including a radar screen actively displaying maritime traffic. The panda dons a Navy cap, clutching the wheel with intent focus, while US Navy personnel in the background are coordinating via headsets. Nearby, an aircraft carrier is visible, with fighter jets poised on its deck, ready for operation.
