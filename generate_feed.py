import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

# Target URL
url = "<<<<https://news.met.police.uk/tag/counter-terrorism-command>>>>"

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract items (adjust selectors as needed)
items = []
for article in soup.select('article'):  # Update selector to match Met Police page
    title = article.select_one('h3').text.strip() if article.select_one('h3') else "No title"
    link = article.select_one('a')['href'] if article.select_one('a') else url
    if not link.startswith('http'):
        link = f"https://news.met.police.uk{link}"
    items.append({
        'title': title,
        'link': link,
        'description': 'Latest update from Met Police Counter-Terrorism Command.',
        'pubDate': datetime.now(pytz.UTC).strftime('%a, %d %b %Y %H:%M:%S GMT')
    })

# Generate RSS feed
rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>Met Police Counter-Terrorism Updates</title>
  <link>{url}</link>
  <description>Latest updates from the Met Police Counter-Terrorism Command.</description>
"""

for item in items:
    rss_content += f"""
  <item>
    <title>{item['title']}</title>
    <link>{item['link']}</link>
    <description>{item['description']}</description>
    <pubDate>{item['pubDate']}</pubDate>
  </item>
"""

rss_content += """
</channel>
</rss>
"""

with open("feed.xml", "w") as f:
    f.write(rss_content)
