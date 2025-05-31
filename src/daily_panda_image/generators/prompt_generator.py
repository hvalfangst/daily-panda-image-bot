import datetime
import hashlib

from openai import OpenAI

from daily_panda_image.utils.file_manager import FileManager
from daily_panda_image.utils.text_processor import TextProcessor


def get_system_prompt() -> str:
    """Get the system prompt for the AI assistant."""
    return """You are a creative prompt engineer specializing in unique, visually striking image descriptions featuring pandas in diverse global historical events. 
    Create prompts that show pandas actively participating in real historical events from the current date throughout history. 
    Focus on whimsical watercolor aesthetics with specific visual details, period-accurate elements, and memorable compositions. 
    Ensure all generated text is ASCII-only and adheres to token limits."""


def get_text_prompt(current_date: datetime.date) -> str:
    """Generate the user prompt for historical panda images with event rotation."""

    # Format the date for the prompt so that it conforms to 'MMM dd' format
    formated_date_str = current_date.strftime("%B %d")
    print(f"Formated date string: {formated_date_str}\n")

    # Read past events that we want to exempt from the file manager, ensuring that the generated prompt is unique
    past_events = FileManager.read_all_events()
    print(f"Past events loaded: {past_events}\n")

    prompt_str = f"""Create a detailed, whimsical watercolor image prompt featuring a panda actively participating in a lesser-known or culturally specific historical event from {formated_date_str}
        that is NOT the same as any of these past events, which are in square brackets separated by comma: {past_events}

        Requirements:
        - SELECT a unique, non-mainstream historical event from {formated_date_str} - avoid the most famous events
        - Prioritize country-specific, regional, or culturally significant events over globally known ones
        - Choose events from diverse geographical locations and time periods
        - The panda must be DOING something central to this specific historical event
        - Use soft watercolor painting style with gentle brushstrokes and pastel colors
        - Include period-accurate clothing, props, and setting details specific to the culture/region
        - Make it charming and whimsical while respecting cultural and historical significance
        - Add specific visual elements: lighting, mood, atmospheric details appropriate to the era and location
        - Plan response to fit within 100 tokens
        - Use only ASCII-safe characters
        - Allowed punctuation: ., !, ?, :, -, ' (apostrophe), " (quotation marks)
        - 

        Format: Start with "[Year: Brief event name, Location]" followed by a new line, then "A whimsical watercolor painting of..." and describe the panda's active role in the historical event."""

    print(f"{prompt_str}\n")

    return prompt_str


def get_unique_api_params(current_date: datetime.date) -> dict:
    """Generate date-based API parameters to ensure uniqueness."""

    # Create date-based seed for reproducible but varying randomness
    date_seed = int(hashlib.md5(current_date.isoformat().encode()).hexdigest()[:8], 16)

    # Use date to vary temperature and penalties
    day_of_year = current_date.timetuple().tm_yday

    # Vary temperature based on day (0.7-0.95 range)
    temperature = 0.7 + (day_of_year % 25) * 0.01

    # Vary presence penalty (0.5-0.8 range)
    presence_penalty = 0.5 + (day_of_year % 30) * 0.01

    # Vary frequency penalty (0.3-0.7 range)
    frequency_penalty = 0.3 + (day_of_year % 40) * 0.01

    print(f"Generated API parameters for {current_date}:")
    print(f"Temperature: {temperature}, Presence Penalty: {presence_penalty}, Frequency Penalty: {frequency_penalty}, Seed: {date_seed}\n")

    return {
        "temperature": round(temperature, 2),
        "presence_penalty": round(presence_penalty, 2),
        "frequency_penalty": round(frequency_penalty, 2),
        "seed": date_seed % 2147483647  # Keep within int32 range
    }


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
        system_prompt = get_system_prompt()
        text_prompt = get_text_prompt(current_date)
        api_params = get_unique_api_params(current_date)

        response = self.client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text_prompt}
            ],
            max_tokens=100,
            temperature=api_params["temperature"],
            presence_penalty=api_params["presence_penalty"],
            frequency_penalty=api_params["frequency_penalty"],
            seed=api_params["seed"]  # Ensures reproducible but unique daily results
        )

        raw_prompt = response.choices[0].message.content
        print(f"Raw prompt: {raw_prompt}\n")

        ascii_enforced_prompt = TextProcessor.enforce_ascii(raw_prompt.strip())
        print(f"ASCII-enforced prompt: {ascii_enforced_prompt}\n")

        final_prompt = TextProcessor.remove_incomplete_last_sentence(ascii_enforced_prompt)
        print(f"Final prompt after sentence cleanup: {final_prompt}\n")

        return final_prompt


