# --- TESTS BELOW ---
import datetime
import os
import sys

import pytest
from unittest.mock import MagicMock

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

import daily_panda_image.generators.prompt_generator as prompt_gen


class DummyTextProcessor:
    @staticmethod
    def enforce_ascii(text):
        return text.encode("ascii", errors="ignore").decode()

    @staticmethod
    def remove_incomplete_last_sentence(text):
        if "." in text:
            return text[:text.rfind(".") + 1]
        return text


class DummyNewsScraper:
    @staticmethod
    def fetch_headlines(current_date=None):
        return [
            {"title": "World leaders meet at climate summit in Geneva", "summary": "Dozens of heads of state gathered at the Palais des Nations to sign a new emissions treaty."},
            {"title": "Record rainfall causes flooding across coastal cities", "summary": "Torrential rain has inundated low-lying districts, prompting mass evacuations."},
            {"title": "Scientists discover new deep-sea species off Pacific coast", "summary": "A remotely operated vehicle captured footage of the bioluminescent creature at 3,000 metres depth."},
        ]

    @staticmethod
    def format_for_prompt(headlines):
        lines = []
        for i, item in enumerate(headlines):
            title = item.get("title", "")
            summary = item.get("summary", "")
            line = f"{i + 1}. {title}"
            if summary:
                line += f"\n   Summary: {summary}"
            lines.append(line)
        return "\n".join(lines)


@pytest.fixture(autouse=True)
def patch_utils(monkeypatch):
    monkeypatch.setattr(prompt_gen, "NewsScraper", DummyNewsScraper)
    monkeypatch.setattr(prompt_gen, "TextProcessor", DummyTextProcessor)


def test_get_system_prompt():
    prompt = prompt_gen.get_system_prompt()
    assert "panda" in prompt
    assert "ASCII" in prompt
    assert "photorealistic" in prompt.lower()


def test_get_text_prompt_contains_headlines(monkeypatch):
    date = datetime.date(2026, 4, 19)
    prompt = prompt_gen.get_text_prompt(date)
    assert "climate summit" in prompt
    assert "panda" in prompt
    assert "photorealistic" in prompt.lower()
    assert "April 19, 2026" in prompt
    assert "Summary:" in prompt
    assert "Palais des Nations" in prompt


def test_prompt_generator_generate_prompt():
    class DummyChoices:
        class DummyMessage:
            content = '[Climate summit, Geneva]\nA whimsical watercolor painting of a panda signing climate accords at a grand table draped in green banners.'
        message = DummyMessage()

    class DummyResponse:
        choices = [DummyChoices()]

    dummy_client = MagicMock()
    dummy_client.chat.completions.create.return_value = DummyResponse()

    gen = prompt_gen.PromptGenerator(dummy_client)
    prompt = gen.generate_prompt(datetime.date(2026, 4, 19))
    assert "panda" in prompt
    assert "climate" in prompt.lower()
    assert prompt.endswith(".")

    call_kwargs = dummy_client.chat.completions.create.call_args.kwargs
    assert call_kwargs["model"] == "gpt-4o"
    assert call_kwargs["max_completion_tokens"] == 150
    assert "max_tokens" not in call_kwargs
    assert dummy_client.chat.completions.create.call_count == 1


def test_prompt_generator_empty_response_raises():
    class DummyChoices:
        class DummyMessage:
            content = ""
        message = DummyMessage()

    class DummyResponse:
        choices = [DummyChoices()]

    dummy_client = MagicMock()
    dummy_client.chat.completions.create.return_value = DummyResponse()

    gen = prompt_gen.PromptGenerator(dummy_client)
    with pytest.raises(ValueError, match="empty response"):
        gen.generate_prompt(datetime.date(2026, 4, 19))
