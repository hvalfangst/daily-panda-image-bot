# Panda Image Generator using OpenAI DALL-E-3

This repository contains a [Python script](src/daily_panda_image/generators/image_generator.py) used to generate unique panda images using OpenAI's **DALL-E-3** model. 
The input prompt for the model is produced by **GPT-4.1 Nano**, which creates contextual prompts based on global cultural, historical, or seasonal events occurring on the current date.

To ensure each generated image is unique and not repeated, the system randomizes API parameters such as `temperature`, `presence_penalty`, `frequency_penalty`, and `seed`, and cross-references a log of [previous event prompts](src/daily_panda_image/generators/prompt_generator.py). Additionally, issues like non-ASCII characters and incomplete prompts are automatically [corrected](src/daily_panda_image/utils/text_processor.py) for optimal results.

The entire process is automated via a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that executes daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [1938: Lhasa Tibetan New Year Festival, Tibet]  
A whimsical watercolor painting of a panda dressed in traditional Tibetan robes, joyfully ringing a giant brass prayer bell during the festive celebrations. Behind, colorful prayer flags flutter in soft pastel hues, and monks in maroon robes dance around him under an early winter sky. Gentle brushstrokes create a serene atmosphere filled with warm candlelight reflections on ancient stone walls and intricate temple carvings, capturing the spirited yet peaceful spirit of the festival.
