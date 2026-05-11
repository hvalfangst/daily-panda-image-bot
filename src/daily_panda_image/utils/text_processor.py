import re


class TextProcessor:
    """Handles text processing and ASCII normalization."""

    # Character replacement mapping for ASCII compatibility
    ASCII_REPLACEMENTS = {
        # Smart quotes to regular quotes
        "“": '"',
        "”": '"',
        "„": '"',
        "«": '"',
        "»": '"',
        "‘": "'",
        "’": "'",
        "‚": "'",
        "`": "'",
        "´": "'",
        # Dashes and ellipsis
        "—": "-",
        "–": "-",
        "−": "-",
        "‒": "-",
        "―": "-",
        "…": "...",
        # Accented and special letters
        "á": "a",
        "à": "a",
        "â": "a",
        "ä": "a",
        "ã": "a",
        "å": "a",
        "ā": "a",
        "æ": "ae",
        "ç": "c",
        "č": "c",
        "é": "e",
        "è": "e",
        "ê": "e",
        "ë": "e",
        "ē": "e",
        "í": "i",
        "ì": "i",
        "î": "i",
        "ï": "i",
        "ī": "i",
        "ñ": "n",
        "ó": "o",
        "ò": "o",
        "ô": "o",
        "ö": "o",
        "õ": "o",
        "ø": "o",
        "œ": "oe",
        "ō": "o",
        "ú": "u",
        "ù": "u",
        "û": "u",
        "ü": "u",
        "ū": "u",
        "ý": "y",
        "ÿ": "y",
        "ß": "ss",
        # Currency and math symbols
        "€": "EUR",
        "£": "GBP",
        "¥": "JPY",
        "₹": "INR",
        "¢": "c",
        "₩": "KRW",
        "©": "(c)",
        "®": "(r)",
        "™": "(tm)",
        "°": " deg",
        "±": "+/-",
        "×": "x",
        "÷": "/",
        # Bullets and miscellaneous
        "•": "*",
        "●": "*",
        "‣": "*",
        "·": "*",
        # Arrows
        "→": "->",
        "←": "<-",
        "↑": "^",
        "↓": "v",
    }

    @classmethod
    def enforce_ascii(cls, text: str) -> str:
        """
        Clean text to ensure ASCII compatibility.

        Args:
            text: Input text that may contain non-ASCII characters

        Returns:
            ASCII-compatible version of the input text
        """
        # Replace common problematic characters
        for old, new in cls.ASCII_REPLACEMENTS.items():
            text = text.replace(old, new)

        # Remove any remaining non-ASCII characters
        text = re.sub(r"[^\x00-\x7F]+", "", text)

        return text

    @staticmethod
    def remove_incomplete_last_sentence(text: str) -> str:
        """
        Remove the last sentence if the text does not end with allowed punctuation.

        Args:
            text: The input text to process

        Returns:
            Text with the last incomplete sentence removed if necessary
        """
        allowed_punctuation = {".", "!", "?"}
        text = text.rstrip()
        if text and text[-1] not in allowed_punctuation:
            # Split into sentences using punctuation as delimiters
            sentences = re.split(r"(?<=[.!?])\s+", text)
            # Remove the last sentence (which is incomplete)
            if len(sentences) > 1:
                return " ".join(sentences[:-1]).strip()
            else:
                return ""
        return text
