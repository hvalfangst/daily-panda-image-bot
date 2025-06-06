# Panda Image Generator using OpenAI DALL-E-3

This repository contains a [Python script](src/daily_panda_image/generators/image_generator.py) used to generate unique panda images using OpenAI's **DALL-E-3** model. 
The input prompt for the model is produced by **GPT-4.1 Nano**, which creates contextual prompts based on global cultural, historical, or seasonal events occurring on the current date.

To ensure each generated image is unique and not repeated, the system randomizes API parameters such as `temperature`, `presence_penalty`, `frequency_penalty`, and `seed`, and cross-references a log of [previous event prompts](src/daily_panda_image/generators/prompt_generator.py). Additionally, issues like non-ASCII characters and incomplete prompts are automatically [corrected](src/daily_panda_image/utils/text_processor.py) for optimal results.

The entire process is automated via a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that executes daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** 1922: Founding of the Afro-Asian People's Solidarity Conference, Cairo

A whimsical watercolor painting of a delighted panda dressed in early 20th-century Arab attire, sitting at a wooden conference table with indigenous textiles and vintage microphones. The panda raises a paw passionately as other diverse delegates listen attentively. Soft pastel hues bathed in warm sunlight filter through latticed windows, creating an atmosphere of hope and unity during this historic gathering for anti-colonial solidarity.
