import os
import sys

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from daily_panda_image.utils.text_processor import TextProcessor


class TestEnforceAscii:
    def test_basic(self):
        # Smart quotes, dashes, ellipsis, accented, currency, arrows, etc.
        input_text = (
            '“No soup for you!”—yelled the Soup Nazi. Elaine danced… badly. '
            'George’s wallet exploded with receipts. Kramer slid in—crashing. '
            'Jerry asked: “Who are these people?” Newman plotted. '
        )
        expected = (
            '"No soup for you!"-yelled the Soup Nazi. Elaine danced... badly. '
            "George's wallet exploded with receipts. Kramer slid in-crashing. "
            'Jerry asked: "Who are these people?" Newman plotted. '
        )
        assert TextProcessor.enforce_ascii(input_text) == expected

    def test_removes_non_ascii(self):
        # Should remove any unmapped non-ASCII
        input_text = 'Yada\u2028yada\u200bYada'  # line separator, zero-width space
        expected = 'YadayadaYada'
        assert TextProcessor.enforce_ascii(input_text) == expected

    def test_empty(self):
        assert TextProcessor.enforce_ascii('') == ''

    def test_only_ascii(self):
        assert TextProcessor.enforce_ascii('Its Just ASCII text! yelled Kramer') == 'Its Just ASCII text! yelled Kramer'


class TestRemoveIncompleteLastSentence:
    def test_complete_sentences(self):
        # All sentences complete
        text = "Jerry eats cereal. George complains! Elaine dances? Kramer slides in."
        assert TextProcessor.remove_incomplete_last_sentence(text) == text

    def test_incomplete_last_sentence(self):
        # Last sentence incomplete
        text = "No soup for you. Newman schemes"
        expected = "No soup for you."
        assert TextProcessor.remove_incomplete_last_sentence(text) == expected

    def test_only_incomplete_sentence(self):
        # Only incomplete
        text = "Serenity now"
        assert TextProcessor.remove_incomplete_last_sentence(text) == ""

    def test_trailing_whitespace(self):
        # Complete with trailing spaces
        text = "Yada yada yada.   "
        assert TextProcessor.remove_incomplete_last_sentence(text) == "Yada yada yada."
        text2 = "These pretzels are making me thirsty. Newman plots   "
        assert TextProcessor.remove_incomplete_last_sentence(text2) == "These pretzels are making me thirsty."

    def test_empty_string(self):
        assert TextProcessor.remove_incomplete_last_sentence("") == ""