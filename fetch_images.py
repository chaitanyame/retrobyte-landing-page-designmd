#!/usr/bin/env python3
"""Fetch CC-licensed vintage computing images from Wikimedia Commons."""

import json
import urllib.request
import urllib.parse
import urllib.error

API_URL = "https://commons.wikimedia.org/w/api.php"
QUERIES = [
    "vintage computer retro",
    "Commodore 64 computer",
    "Apple Macintosh retro",
    "IBM PC vintage",
    "Nintendo NES console",
    "Sega Genesis video game",
    "Sony PlayStation retro",
    "CRT monitor vintage",
]

def search_images(query, limit=5):
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srnamespace": "6",
        "srlimit": str(limit),
        "srprop": "timestamp",
    }
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "RetroByte/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except (urllib.error.URLError, json.JSONDecodeError) as e:
        print(f"  Error: {e}")
        return []
    titles = []
    for result in data.get("query", {}).get("search", []):
        title = result.get("title", "")
        if title.startswith("File:"):
            titles.append(title)
    return titles

def get_image_url(title, width=800):
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "imageinfo",
        "iiprop": "url",
        "iiurlwidth": str(width),
    }
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "RetroByte/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except (urllib.error.URLError, json.JSONDecodeError) as e:
        return None
    pages = data.get("query", {}).get("pages", {})
    for page_id, page_data in pages.items():
        image_info = page_data.get("imageinfo", [])
        if image_info:
            thumb_url = image_info[0].get("thumburl")
            if thumb_url:
                return thumb_url.replace("http://", "https://")
            return image_info[0].get("url", "").replace("http://", "https://")
    return None

def main():
    all_images = []
    for query in QUERIES:
        print(f'\nSearching: "{query}"')
        titles = search_images(query)
        print(f"  Found {len(titles)} files")
        for title in titles:
            url = get_image_url(title, width=800)
            if url:
                print(f"  {title}")
                print(f"    {url}")
                all_images.append({"title": title, "url": url})
    print(f"\n\n=== TOTAL: {len(all_images)} images ===")
    print("\n--- Image URLs (for HTML) ---")
    for i, img in enumerate(all_images):
        print(f"{img['url']}")

if __name__ == "__main__":
    main()
