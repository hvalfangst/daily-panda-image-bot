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
    def fetch_headlines(current_date: datetime.date | None = None) -> list[dict]:
        """
        Fetch today's top headlines from multiple RSS feeds.

        Args:
            current_date: Date to filter headlines for (defaults to today).

        Returns:
            List of dicts with "title" and "summary" keys, deduplicated, up to MAX_HEADLINES.
        """
        if current_date is None:
            current_date = datetime.date.today()

        items: list[dict] = []
        seen_titles: set[str] = set()

        for source_name, url in NEWS_FEEDS:
            if len(items) >= MAX_HEADLINES:
                break
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries:
                    if len(items) >= MAX_HEADLINES:
                        break
                    title = (entry.get("title") or "").strip()
                    if not title or title in seen_titles:
                        continue
                    summary = (entry.get("summary") or entry.get("description") or "").strip()
                    seen_titles.add(title)
                    items.append({"title": title, "summary": summary})
                print(f"Fetched {len(feed.entries)} entries from {source_name}.\n")
            except Exception as e:
                print(f"Warning: could not fetch from {source_name}: {e}\n")

        return items

    @staticmethod
    def format_for_prompt(headlines: list[dict]) -> str:
        """
        Format news items as a numbered list suitable for embedding in a prompt.
        Each item includes the headline title and, when available, a short summary
        to give the model richer context for generating unique image descriptions.

        Args:
            headlines: List of dicts with "title" and optional "summary" keys.

        Returns:
            Formatted multi-line string.
        """
        if not headlines:
            return "No headlines available."
        lines = []
        for i, item in enumerate(headlines):
            title = item.get("title", "")
            summary = item.get("summary", "")
            line = f"{i + 1}. {title}"
            if summary:
                line += f"\n   Summary: {summary}"
            lines.append(line)
        return "\n".join(lines)
