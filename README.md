# Panda Image Generator using OpenAI DALL-E-3

This repository contains a [Python script](src/daily_panda_image/generators/image_generator.py) used to generate unique panda images using OpenAI's **DALL-E-3** model. 
The input prompt for the model is produced by **GPT-4.1 Nano**, which creates contextual prompts based on global cultural, historical, or seasonal events occurring on the current date.

To ensure each generated image is unique and not repeated, the system randomizes API parameters such as `temperature`, `presence_penalty`, `frequency_penalty`, and `seed`, and cross-references a log of [previous event prompts](src/daily_panda_image/generators/prompt_generator.py). Additionally, issues like non-ASCII characters and incomplete prompts are automatically [corrected](src/daily_panda_image/utils/text_processor.py) for optimal results.

The entire process is automated via a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that executes daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [1878: First Tibetan Monastic Festival, Lhasa]  
A whimsical watercolor painting of a cheerful panda dressed in ornate monastery robes, balancing colorful prayer flags on its head during the first Tibetan Monastic Festival. The panda joyfully rings a bronze prayer bell with a carved wooden mallet, surrounded by softly glowing lanterns and sacred murals. Gentle pastel hues capture the spiritual atmosphere as clouds drift over ancient rooftops, evoking serenity and celebration in this culturally rich scene.
