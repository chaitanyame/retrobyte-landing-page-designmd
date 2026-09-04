# RetroByte

> A vintage computing museum and store — preserving the machines that started it all.

RetroByte is both a physical museum gallery in Austin, Texas and an online store specializing in restored vintage computers, peripherals, and software from the golden age of personal computing (1975–1995). This repository is the **single-page landing site** for the museum, styled like a retro newspaper/classifieds page to match the era it celebrates.

## Features

- **Museum-focused landing page** — showcases the featured collection (Macintosh Plus, Commodore 64, IBM PC XT, NES, Sega Genesis, PlayStation) in "ribbon card" exhibit entries, each with a period photo and a `View in Museum` link.
- **Retro print aesthetic** — Times New Roman body, Helvetica navigation, monospace accents, black canvas with red call-to-action blocks and yellow "BUY/ NEW!" stickers.
- **Fully responsive** — mobile layouts collapse the left rail and stack ribbon-card photos below their text (see `@media` queries in `index.html`).
- **Zero runtime dependencies** — vanilla HTML/CSS, no build step, no frameworks, no JavaScript required. Serve it and go.
- **Human-friendly image sourcing** — a companion script queries Wikimedia Commons for CC-licensed imagery (see below).

## The Collection

- **Apple** — Apple I replicas, Apple II series, original Macintosh 128K through Power Mac G4
- **Commodore** — PET, VIC-20, C64, Amiga 500/1200/4000
- **IBM & Clones** — IBM PC 5150, XT, AT, PS/2, Compaq Portable
- **Atari** — 400, 800, ST, Falcon
- **Sinclair** — ZX80, ZX81, Spectrum series
- **NEC** — PC-88, PC-98 series (Japanese market)

## What We Do

- **Museum** — Visit our Austin gallery to experience 100+ fully operational machines. Hands-on exhibits, rotating featured collections, and Saturday workshops.
- **Store** — Every machine we sell is fully recapped, tested, and comes with a 90-day warranty. We stock period-correct accessories, software on original media, and reproduction parts.
- **Repair** — Mail-in and in-shop repair for vintage systems. Cap replacement, trace repair, chip-level diagnostics, and CRT servicing.

## Tech Stack

- **Frontend**: HTML/CSS — retro newspaper/classifieds aesthetic
- **Typography**: Times New Roman (body), Helvetica (navigation), monospace accents
- **Palette**: Black canvas, white card surfaces, red call-to-action accents, yellow buy stickers
- **Tooling**: Python 3 (stdlib only) for the optional image-scraping helper

## Quick Start

No build step or install required — serve the directory with any static file server:

```bash
# Option A: Python's built-in HTTP server
python3 -m http.server 8080

# Option B: Node's npx
npx serve .

# Option C: any static server of your choice
# Then open http://localhost:8080
```

## Regenerating Image Assets (`fetch_images.py`)

The featured photos in `index.html` are currently hot-linked to Unsplash URLs. If you'd rather use **CC-licensed images from Wikimedia Commons** (and/or swap in new subject matter), the included script generates a fresh set of 800px image URLs:

```bash
python3 fetch_images.py
```

What it does:

- Runs a set of vintage-computing search queries (e.g. *"Commodore 64 computer"*, *"CRT monitor vintage"*) against the Wikimedia Commons API.
- For each matching `File:` result, resolves the 800px thumbnail URL (force-upgrading `http://` → `https://`).
- Prints a running list, followed by a `=== TOTAL: N images ===` summary and the raw image URLs ready to paste into your HTML.

Caveats:

- Uses only Python 3 standard library (`urllib`, `json`) — no pip dependencies.
- Sends a custom `User-Agent` header (`RetroByte/1.0`) as required by Wikimedia's API etiquette; images are CC-licensed and should be credited in the page footer when used in production.
- Search results change over time, so re-running may return different photos — re-run before a content update to keep imagery fresh.

## Project Structure

```
retrobyte/
├── index.html      # Landing page (single-file HTML + inline CSS)
├── fetch_images.py # Optional Wikimedia Commons image scraper
└── README.md       # This file
```

## License

Proprietary. All rights reserved.