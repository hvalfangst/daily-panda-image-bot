# Daily Panda Image Bot

This repo generates a daily panda image using OpenAI's **gpt-image-1-mini** model.
Every day it scrapes the top headlines from news orgs (BBC, Reuters, AP, NPR), picks the most visually interesting one, and uses **GPT-4o** to write a photorealistic image prompt with a panda as the main character.

Non-ASCII characters and incomplete sentences are automatically [cleaned up](src/daily_panda_image/utils/text_processor.py) before the prompt hits the image model.

The whole thing runs on a [GitHub Actions workflow](.github/workflows/image_publisher.yml) **CRON** that fires daily at 04:00 UTC (06:00 CEST).


## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and a Pydantic-based settings module for environment variables.

### Setup

```bash
# Install uv (one-off)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies (creates .venv automatically)
uv sync

# Configure environment
cp .env.example .env   # then edit .env and set OPENAI_API_KEY
```

### Pre-commit hooks

`ruff` (lint with `--fix`) and `ruff-format` run automatically on every `git commit` once the hook is installed.

```bash
# Install the git hook (one-off per clone)
uv run pre-commit install

# Run all hooks across the whole repo (not just staged files)
uv run pre-commit run --all-files

# Bump hook versions pinned in .pre-commit-config.yaml
uv run pre-commit autoupdate
```

If a hook modifies a file or reports an error, the commit is aborted — restage and commit again.

### Running and testing

```bash
# Run the generator
uv run python -m daily_panda_image.main

# Run tests
uv run pytest

# Lint / format manually
uv run ruff check .
uv run ruff format .
```


## Today's Panda
![screenshot](images/panda_current.png)

**Prompt:** [Headline summary: Tenerife medics poised to receive virus-hit cruise ship passengers, Port of Tenerife]

A photorealistic image of a panda in a bright orange safety vest, directing medics at the bustling Port of Tenerife as the immense MV Hondius cruise ship looms in the background under a piercing midday sun. The panda, standing on the dockside with the cruise ship's gangway extended, is energetically waving its arms, ushering medics to waiting ambulances, their flashing blue lights reflecting off the panda's black and white fur. Nearby, large banners read "Welcome, Stay Safe" in both English and Spanish. A medic clutches a clipboard with visible details of medical supplies.
