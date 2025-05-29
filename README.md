# Panda Image Generator using OpenAI DALL-E-3


This application creates unique panda images using OpenAI's DALL-E-3 model. Unlike static image generators, this system generates contextual prompts based on real global cultural, historical, or seasonal events happening on the current date. The entire process is automated through a [GitHub Actions workflow](.github/workflows/image-publisher.yml) that runs daily at 06:00 CEST (04:00 UTC).

## Features
- GPT-4.1 Nano analyzes the current date to identify relevant cultural or seasonal events
- Creative prompts are generated featuring pandas actively participating in these events
- Prompts are family-friendly, culturally sensitive, ASCII-compatible, and limited to 100 tokens
- DALL-E-3 creates 1024x1024 images using the generated prompts with base64 encoding
- Dual storage system saves both current files and timestamped archives
- Script automatically updates README and implements smart git operations with change detection



## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** A whimsical watercolor illustration of a cheerful panda dressed in traditional Japanese kimono, joyfully participating in the 2025 Tokyo Cherry Blossom Festival on May 29. The panda holds a delicate paper lantern glowing softly at dusk, surrounded by blooming sakura trees with petals floating in the air. Brightly colored fans and tea cups decorate the scene, evoking festive warmth. The background features a distant Mt. Fuji silhouette under a pink-hued sky, with ribbons fluttering gently. The mood is lively yet respectful, celebrating cultural heritage with playful charm. Emphasize soft pastel tones and intricate details to create
