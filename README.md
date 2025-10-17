# Panda Image Generator using OpenAI DALL-E-3

This repository contains a [Python script](src/daily_panda_image/generators/image_generator.py) used to generate unique panda images using OpenAI's **DALL-E-3** model. 
The input prompt for the model is produced by **GPT-4.1 Nano**, which creates contextual prompts based on global cultural, historical, or seasonal events occurring on the current date.

To ensure each generated image is unique and not repeated, the system randomizes API parameters such as `temperature`, `presence_penalty`, `frequency_penalty`, and `seed`, and cross-references a log of [previous event prompts](src/daily_panda_image/generators/prompt_generator.py). Additionally, issues like non-ASCII characters and incomplete prompts are automatically [corrected](src/daily_panda_image/utils/text_processor.py) for optimal results.

The entire process is automated via a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that executes daily at 04:00 UTC (06:00 CEST).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [1864: Opening of the Meiji Shrine Festival, Tokyo]  
A whimsical watercolor painting of a cheerful panda dressed in traditional kimono, standing amidst cherry blossoms at the historic Meiji Shrine. The panda is gently lighting paper lanterns with a delicate fan, surrounded by serene festival attendees in elegant Edo-period clothing. Soft pastel hues capture a peaceful evening scene with lantern glow reflecting on tranquil shrine grounds, evoking a charming and culturally respectful atmosphere full of gentle celebration and timeless beauty.
