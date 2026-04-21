import datetime

from openai import OpenAI

from daily_panda_image.utils.news_scraper import NewsScraper
from daily_panda_image.utils.text_processor import TextProcessor


def get_system_prompt() -> str:
    """Get the system prompt for the AI assistant."""
    return (
        "You are a creative prompt engineer specializing in photorealistic image descriptions "
        "featuring a panda as the central character in real current news events. "
        "Transform today's top news headlines into hyper-realistic scenes where the panda "
        "actively participates in the story. "
        "Focus on photographic realism: natural lighting, accurate textures, detailed environments, "
        "cinematic composition, and lifelike detail. No illustration, cartoon, or painterly styles. "
        "Use only ASCII-safe characters."
    )


def _extract_response_text(response) -> str:
    """Extract generated text from a Chat Completions API response."""
    if hasattr(response, "choices") and response.choices:
        message = getattr(response.choices[0], "message", None)
        content = getattr(message, "content", None)

        if isinstance(content, str):
            return content

        if isinstance(content, list):
            parts = []
            for part in content:
                text = part.get("text", "") if isinstance(part, dict) else getattr(part, "text", "")
                if text:
                    parts.append(text)
            if parts:
                return " ".join(parts)

    return ""


def get_text_prompt(current_date: datetime.date) -> str:
    """Generate the user prompt using today's news headlines."""
    formatted_date = current_date.strftime("%B %d, %Y")
    print(f"Fetching news headlines for {formatted_date}...\n")

    headlines = NewsScraper.fetch_headlines(current_date)
    formatted_headlines = NewsScraper.format_for_prompt(headlines)
    print(f"Headlines:\n{formatted_headlines}\n")

    prompt_str = f"""Today is {formatted_date}. Here are today's top news headlines with article summaries:

{formatted_headlines}

Pick ONE headline from the list above and create a detailed, photorealistic image prompt featuring a panda as the main character actively participating in that news story.

Requirements:
- Choose the most visually interesting or emotionally resonant headline
- Use the article summary details to ground the scene in story-specific facts and details
- The panda must be DOING something central to the chosen news story
- Photorealistic style: natural lighting, sharp detail, accurate textures, no cartoon or illustration
- Cinematic composition with depth of field and realistic shadows
- Name a SPECIFIC, real-world location or landmark that directly connects to the story - never use a generic city street or skyline as the backdrop
- Specify an exact time of day (e.g., dawn, midday, dusk, night) and distinctive weather or lighting conditions unique to this story
- Include story-specific props, signage, or objects that could only belong to this particular event
- Choose an unusual or dramatic camera angle (e.g., low angle, aerial, extreme close-up) to ensure visual variety
- Every scene element must tie back to the specific story details, making this image impossible to confuse with any other news story
- Plan response to fit within 150 tokens
- Use only ASCII-safe characters
- Allowed punctuation: ., !, ?, :, -, ' (apostrophe), " (quotation marks)

Format: Start with "[Headline summary, Location]" followed by a new line, then "A photorealistic image of..." and describe the panda's active role in the news event."""

    print(f"{prompt_str}\n")
    return prompt_str


class PromptGenerator:
    """Generates creative prompts for panda images based on today's news."""

    def __init__(self, client: OpenAI):
        """
        Initialize the prompt generator.

        Args:
            client: Configured OpenAI client instance
        """
        self.client = client

    def generate_prompt(self, current_date: datetime.date) -> str:
        """
        Generate a creative prompt for a panda participating in today's news.

        Args:
            current_date: The date to generate news context for

        Returns:
            ASCII-compatible prompt text for image generation

        Raises:
            ValueError: If model returns an empty response
        """
        system_prompt = get_system_prompt()
        text_prompt = get_text_prompt(current_date)

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text_prompt}
            ],
            max_completion_tokens=150,
        )

        raw_prompt = _extract_response_text(response).strip()
        print(f"Raw prompt: {raw_prompt}\n")

        if not raw_prompt:
            raise ValueError("Model returned an empty response.")

        ascii_enforced_prompt = TextProcessor.enforce_ascii(raw_prompt)
        print(f"ASCII-enforced prompt: {ascii_enforced_prompt}\n")

        final_prompt = TextProcessor.remove_incomplete_last_sentence(ascii_enforced_prompt)
        print(f"Final prompt after sentence cleanup: {final_prompt}\n")

        return final_prompt

