# AGENTS.md — Belgian Beers Project

> **Canonical instruction file for all AI coding assistants.**
> Provider-specific files (`CLAUDE.md`, `GEMINI.md`) point here.

---

## Project Overview

**Belgian Beers** is a static single-page website that helps tourists discover Belgian beers in Brussels. It is hosted on **GitHub Pages** and requires zero build tools — just HTML, CSS, and vanilla JavaScript.

### Key Features

| Feature | Description |
|---|---|
| Beer Database | 34 iconic Belgian beers with metadata (type, ABV, region, brewery, personality) |
| Brussels Cafés | 25 beer cafés across Brussels Capital Region with filterable vibe/feature tags |
| Interactive Map | Leaflet.js map with brewery, café, and night shop markers |
| Personality Quiz | 7-question quiz that matches users to a beer personality |
| Feeling Lucky | Random beer picker with dice animation |
| Trending Beers | Weekly trending data from Untappd (via GitHub Actions) |
| Night Shops | After-hours shops in central Brussels (data from OpenStreetMap) |
| Beer Detail Modal | Click any beer for details + "Find Nearest Café" |

---

## Architecture

```
belgian-beers/
├── index.html              # Everything: HTML + CSS + JS (single-file app)
├── 404.html                # GitHub Pages SPA redirect
├── data/
│   ├── trending.json       # Updated weekly by GitHub Actions
│   └── night-shops.json    # Night shops from OpenStreetMap Overpass API
├── .github/
│   └── workflows/
│       └── update-trending.yml  # Weekly Untappd trending updater
├── images/              # AI-generated beer images (34 PNGs)
├── AGENTS.md               # This file — AI assistant instructions
├── CLAUDE.md               # Claude-specific pointer
├── GEMINI.md               # Gemini-specific pointer
└── README.md               # Human-facing documentation
```

### Design Decisions

1. **Single-file architecture**: All HTML, CSS, and JS live in `index.html`. This keeps deployment trivial (GitHub Pages, no build step) and the site lightning-fast.
2. **No frameworks**: Vanilla JS only. No React, no bundler, no npm.
3. **External dependencies**: Only Leaflet.js (maps) and Google Fonts (Playfair Display + Inter).
4. **Dark luxury aesthetic**: Dark theme with gold accents (`--gold: #d4a017`). Target audience is tourists — the site should feel premium.

---

## Coding Rules

### General

- **No build tools.** Everything must work by opening `index.html` in a browser or serving via GitHub Pages.
- **Single-file app.** Do not split into separate CSS/JS files unless the file exceeds ~2000 lines.
- **Preserve comments.** The codebase uses section dividers (`// ═══════`) and inline documentation. Keep them.
- **Mobile-first.** All features must work on mobile. Test at 375px width minimum.

### Data Integrity

- **Beer database**: 34 beers in the `beers` array. Each beer must have: `name`, `type`, `abv`, `region`, `brewery`, `personality`, `img` (can be empty string), `lat`, `lng`, `desc`.
- **Café database**: 25 cafés in the `cafes` array. Each café must have: `id`, `name`, `address`, `lat`, `lng`, `sourceUrl`, `verifiedDate`, `desc`, `tags` (array of tag strings from `cafeTagMeta`), `beers` (array of beer names that must match `beers[].name` exactly).
- **Café tags**: Valid tags are defined in `cafeTagMeta`: `lively`, `chill`, `historic`, `local`, `touristy`, `date-night`, `terrace`, `food`, `brewery`, `sports`, `high-end`, `budget`. Tags are derived from review analysis.
- **Personality types**: `thinker`, `creative`, `social`, `nurturer`, `achiever`, `diplomat`, `adventurer`, `free-spirit`. Do not add new types without updating the quiz logic.

### Style Guide

- **CSS variables** are defined in `:root`. Use them — never hardcode colors.
- **Font stack**: Playfair Display for headings, Inter for body text.
- **Border radius**: Cards use `16px`, pills/tags use `20px–30px`.
- **Animations**: Use `cubic-bezier` for modals, simple `ease` for hover transitions. Keep durations 0.2s–0.5s.

### External Data

- **Trending beers** (`data/trending.json`): Updated weekly via `.github/workflows/update-trending.yml`. Requires `UNTAPPD_CLIENT_ID` and `UNTAPPD_CLIENT_SECRET` in GitHub Secrets.
- **Night shops** (`data/night-shops.json`): Populated via OpenStreetMap Overpass API. See the query in the code comments (line ~613) or in the JSON file itself.

---

## Workflow

1. **Edit** `index.html` directly.
2. **Test** by opening in a browser (`open index.html` on macOS, or use Live Server).
3. **Commit** with a descriptive message.
4. **Push** to `main` — GitHub Pages deploys automatically.

### Commit Message Format

```
feat: add new beer "Beer Name"
fix: correct café address for Delirium Café
chore: update trending beers data
docs: update README
```

---

## Common Tasks

### Adding a New Beer

1. Add entry to the `beers` array in `index.html`.
2. Find the brewery coordinates on Google Maps for `lat`/`lng`.
3. Assign a `personality` from the existing 8 types.
4. Add a locally generated image to `images/` for `img` (preferred), or use a Wikimedia Commons URL.

### Adding a New Café

1. Add entry to the `cafes` array.
2. Ensure all beer names in the `beers` array match existing beer names exactly (case-sensitive).
3. Set `sourceUrl` to the café's website or Google Maps link.
4. Set `verifiedDate` to the current month (e.g., `"2026-04"`).
5. Add `tags` array using valid tag keys from `cafeTagMeta` (research reviews to assign appropriate tags).

### Updating Night Shops

Run the Overpass query documented in `data/night-shops.json` or in the code comments, then transform the results into the expected JSON schema.

### Setting Up Untappd API

1. Register at https://untappd.com/api/register
2. Add `UNTAPPD_CLIENT_ID` and `UNTAPPD_CLIENT_SECRET` to GitHub repo secrets.
3. The workflow runs every Monday at 06:00 UTC, or trigger manually from Actions tab.
