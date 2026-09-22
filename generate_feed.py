import feedparser
import os
from datetime import datetime
import pytz

# Fetch the target URL from environment variable
url = os.getenv("TARGET_URL", "<<https://news.met.police.uk/tag/counter-terrorism-command>>")

# Parse the page (adjust selectors as needed)
feed = feedparser.parse(url)

# Generate RSS feed
rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>Met Police Counter-Terrorism Updates</title>
  <link>{url}</link>
  <description>Latest updates from the Met Police Counter-Terrorism Command.</description>
"""

for entry in feed.entries:
    rss_content += f"""
  <item>
    <title>{entry.title}</title>
    <link>{entry.link}</link>
    <description>{entry.description}</description>
    <pubDate>{datetime.now(pytz.UTC).strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate>
  </item>
"""

rss_content += """
</channel>
</rss>
"""

with open("feed.xml", "w") as f:
    f.write(rss_content)
