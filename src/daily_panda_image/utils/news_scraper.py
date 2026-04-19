"""
NewsScraper - Fetches today's top headlines from public RSS news feeds.
"""

import datetime
import feedparser


# RSS feeds from major news organisations
NEWS_FEEDS = [
    ("BBC News", "http://feeds.bbci.co.uk/news/rss.xml"),
    ("Reuters", "https://feeds.reuters.com/reuters/topNews"),
    ("AP News", "https://rsshub.app/apnews/topics/apf-topnews"),
    ("NPR", "https://feeds.npr.org/1001/rss.xml"),
]

MAX_HEADLINES = 8


class NewsScraper:
    """Scrapes today's top news headlines from RSS feeds."""

    @staticmethod
    def fetch_headlines(current_date: datetime.date | None = None) -> list[str]:
        """
        Fetch today's top headlines from multiple RSS feeds.

        Args:
            current_date: Date to filter headlines for (defaults to today).

        Returns:
            List of headline strings (titles), deduplicated, up to MAX_HEADLINES.
        """
        if current_date is None:
            current_date = datetime.date.today()

        headlines: list[str] = []

        for source_name, url in NEWS_FEEDS:
            if len(headlines) >= MAX_HEADLINES:
                break
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries:
                    if len(headlines) >= MAX_HEADLINES:
                        break
                    title = (entry.get("title") or "").strip()
                    if title and title not in headlines:
                        headlines.append(title)
                print(f"Fetched {len(feed.entries)} entries from {source_name}.\n")
            except Exception as e:
                print(f"Warning: could not fetch from {source_name}: {e}\n")

        return headlines

    @staticmethod
    def format_for_prompt(headlines: list[str]) -> str:
        """
        Format headlines as a numbered list suitable for embedding in a prompt.

        Args:
            headlines: List of headline strings.

        Returns:
            Formatted multi-line string.
        """
        if not headlines:
            return "No headlines available."
        return "\n".join(f"{i + 1}. {h}" for i, h in enumerate(headlines))

