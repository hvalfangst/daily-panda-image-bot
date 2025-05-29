import datetime

from openai import OpenAI

from daily_panda_image.utils.text_processor import TextProcessor


class PromptGenerator:
    """Generates creative prompts for panda images based on cultural events."""

    def __init__(self, client: OpenAI):
        """
        Initialize the prompt generator.

        Args:
            client: Configured OpenAI client instance
        """
        self.client = client

    def generate_prompt(self, current_date: datetime.date) -> str:
        """
        Generate a creative prompt for a panda participating in cultural events.

        Args:
            current_date: The date to generate cultural context for

        Returns:
            ASCII-compatible prompt text for image generation

        Raises:
            Exception: If prompt generation fails
        """
        system_prompt = self._get_system_prompt()
        text_prompt = self._get_text_prompt(current_date)

        response = self.client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text_prompt}
            ],
            max_tokens=100,
            temperature=0.8,
            presence_penalty=0.6,
            frequency_penalty=0.4
        )

        raw_prompt = response.choices[0].message.content
        print(f"Raw prompt: {raw_prompt}")
        ascii_enforced_prompt = TextProcessor.enforce_ascii(raw_prompt.strip())
        print(f"ASCII-enforced prompt: {ascii_enforced_prompt}")
        final_prompt = TextProcessor.remove_incomplete_last_sentence(ascii_enforced_prompt)
        print(f"Final prompt after sentence cleanup: {final_prompt}")

        return final_prompt

    def _get_system_prompt(self) -> str:
        """Get the system prompt for the AI assistant."""
        return """You are a creative prompt engineer specializing in unique, visually striking image descriptions. 
        Create prompts that are specific, unexpected, and memorable. Focus on unusual angles, interesting details, 
        and creative interpretations that an AI image generator can render beautifully. Ensure all generated text is 
        ASCII-only and adheres to the specified token limits."""

    def _get_text_prompt(self, current_date: datetime.date) -> str:
        """
        Generate the user prompt with specific requirements.

        Args:
            current_date: Date to include in the prompt

        Returns:
            Formatted prompt string
        """
        return f"""Create a detailed, creative image prompt featuring a panda as the main character actively participating in or celebrating a real global cultural, historical, or seasonal event happening on {current_date}. 
        
        Requirements:
        - The panda should be DOING something related to the event, not just observing
        - Include specific visual details (clothing, props, setting, lighting, mood)
        - Make it whimsical but respectful to the cultural significance
        - Add unique artistic elements that make the image memorable
        - Specify art style or photographic technique for visual impact
        - Non-asian cultural references are preferred to broaden the scope of creativity
        - Plan the response to fit within 100 tokens
        - Prioritize complete sentences over quantity
        - Use only ASCII-safe characters
        - Allowed punctuation: ., !, ?, :, -, ' (apostrophe), " (quotation marks)
        - Forbidden punctuation: non-ASCII symbols, emojis, or excessive special characters
        
        Format: Start with "A [art style] image of..." and make it vivid and specific."""