# Panda Image Generator using OpenAI DALL-E-3

This repository contains a [Python script](src/daily_panda_image/generators/image_generator.py) designed to generate unique panda images using OpenAI's **DALL-E-3** model. The input prompt for the model is produced by **GPT-4.1 Nano**, which creates contextual prompts based on global cultural, historical, or seasonal events occurring on the current date. The entire process is automated via a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that executes daily at 06:00 CEST (04:00 UTC).


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** A whimsical watercolor image of a lively panda dressed as a jazz musician, celebrating Memorial Day in 2025. The panda wears a vintage red tie, sunglasses, and holds a trumpet while standing on a park picnic blanket decorated with stars and stripes. Cherry blossoms fall softly around him under warm afternoon sunlight, with flags fluttering nearby. The scene exudes joyful patriotism and musical festivity, blending playful charm with respectful homage. Artistic style: impressionistic with vivid brushstrokes emphasizing motion and color.
