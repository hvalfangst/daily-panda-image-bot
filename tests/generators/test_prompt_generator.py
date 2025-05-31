# --- TESTS BELOW ---
import datetime
import os
import sys

import pytest
from unittest.mock import MagicMock, patch

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

import daily_panda_image.generators.prompt_generator as prompt_gen

class DummyTextProcessor:
    @staticmethod
    def enforce_ascii(text):
        # Simulate ASCII enforcement by removing non-ASCII chars
        return text.encode("ascii", errors="ignore").decode()

    @staticmethod
    def remove_incomplete_last_sentence(text):
        # Simulate by returning text up to last period
        if "." in text:
            return text[:text.rfind(".")+1]
        return text

class DummyFileManager:
    @staticmethod
    def read_all_events():
        # Seinfeld world: events are Seinfeld episode titles
        return ["The Contest", "The Puffy Shirt", "The Soup Nazi"]

@pytest.fixture(autouse=True)
def patch_utils(monkeypatch):
    monkeypatch.setattr(prompt_gen, "FileManager", DummyFileManager)
    monkeypatch.setattr(prompt_gen, "TextProcessor", DummyTextProcessor)

def test_get_system_prompt():
    prompt = prompt_gen.get_system_prompt()
    assert "pandas" in prompt
    assert "ASCII" in prompt

def test_get_text_prompt_seinfeld(monkeypatch):
    date = datetime.date(1992, 11, 18)  # "The Contest" aired
    prompt = prompt_gen.get_text_prompt(date)
    assert "The Contest" in prompt
    assert "panda" in prompt
    assert "watercolor" in prompt
    assert "November 18" in prompt

def test_get_unique_api_params_deterministic():
    date = datetime.date(1995, 9, 28)  # "The Soup Nazi" aired
    params = prompt_gen.get_unique_api_params(date)
    assert 0.7 <= params["temperature"] <= 0.95
    assert 0.5 <= params["presence_penalty"] <= 0.8
    assert 0.3 <= params["frequency_penalty"] <= 0.7
    assert isinstance(params["seed"], int)

def test_prompt_generator_generate_prompt(monkeypatch):
    # Simulate OpenAI client and response
    class DummyChoices:
        class DummyMessage:
            content = '[1995: The Soup Nazi, New York]\nA whimsical watercolor painting of a panda refusing to serve soup to Jerry, George, and Elaine in a bustling Manhattan deli.'
        message = DummyMessage()
    class DummyResponse:
        choices = [DummyChoices()]
    dummy_client = MagicMock()
    dummy_client.chat.completions.create.return_value = DummyResponse()

    gen = prompt_gen.PromptGenerator(dummy_client)
    date = datetime.date(1995, 11, 2)  # "The Soup Nazi" aired
    prompt = gen.generate_prompt(date)
    assert "panda" in prompt
    assert "Soup Nazi" in prompt
    assert prompt.endswith(".")