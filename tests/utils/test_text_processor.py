import os
import sys

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from daily_panda_image.utils.text_processor import TextProcessor


class TestEnforceAscii:
    def test_basic(self):
        # Smart quotes, dashes, ellipsis, accented, currency, arrows, etc.
        input_text = (
            '“Hello”—said the naïve boy. Café cost €5.50. '
            'He scored 90° on the test… and got an A+! '
            'Arrows: → ← ↑ ↓. Bullets: • ●. Math: ± × ÷.'
        )
        expected = (
            '"Hello"-said the naive boy. Cafe cost EUR5.50. '
            'He scored 90 deg on the test... and got an A+! '
            'Arrows: -> <- ^ v. Bullets: * *. Math: +/- x /.'
        )
        assert TextProcessor.enforce_ascii(input_text) == expected

    def test_removes_non_ascii(self):
        # Should remove any unmapped non-ASCII
        input_text = 'abc\u2028def\u200bghi'  # line separator, zero-width space
        expected = 'abcdefghi'
        assert TextProcessor.enforce_ascii(input_text) == expected

    def test_empty(self):
        assert TextProcessor.enforce_ascii('') == ''

    def test_only_ascii(self):
        assert TextProcessor.enforce_ascii('Just ASCII text!') == 'Just ASCII text!'


class TestRemoveIncompleteLastSentence:
    def test_complete_sentences(self):
        assert TextProcessor.remove_incomplete_last_sentence("Hello world.") == "Hello world."
        assert TextProcessor.remove_incomplete_last_sentence("Wow! Amazing!") == "Wow! Amazing!"
        assert TextProcessor.remove_incomplete_last_sentence("Is this working? Yes.") == "Is this working? Yes."

    def test_incomplete_last_sentence(self):
        assert TextProcessor.remove_incomplete_last_sentence("This is a test. This is incomplete") == "This is a test."
        assert TextProcessor.remove_incomplete_last_sentence("First! Second sentence is incomplete") == "First!"

    def test_only_incomplete_sentence(self):
        assert TextProcessor.remove_incomplete_last_sentence("Incomplete sentence") == ""

    def test_trailing_whitespace(self):
        assert TextProcessor.remove_incomplete_last_sentence("Hello world.   ") == "Hello world."
        assert TextProcessor.remove_incomplete_last_sentence("Hello world. Incomplete   ") == "Hello world."

    def test_empty_string(self):
        assert TextProcessor.remove_incomplete_last_sentence("") == ""