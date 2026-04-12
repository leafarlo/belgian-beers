# 🍺 Belgian Beers — Find Your Perfect Match

A beautiful, interactive guide to **34 iconic Belgian beers** and the best places to drink them in Brussels. Built as a single-page static website, hosted on GitHub Pages.

🔗 **Live site**: [jcoosemans.github.io/belgian-beers](https://jcoosemans.github.io/belgian-beers/)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🍻 **All Beers** | Browse 34 Belgian beers with filtering by type, region, and personality |
| 🏠 **Brussels Cafés** | 20 top beer cafés sorted by distance from your location |
| 🗺️ **Interactive Map** | Leaflet.js map showing breweries, cafés, and night shops across Belgium |
| 🧠 **Personality Quiz** | Answer 7 questions to discover your perfect Belgian beer match |
| 🎲 **Feeling Lucky** | Random beer picker with a fun dice animation |
| 🔥 **Trending Beers** | Weekly trending data auto-updated from Untappd |
| 🌙 **Night Shops** | Find after-hours shops in central Brussels (OpenStreetMap data) |
| 📍 **Geolocation** | Sort cafés by distance and get walking directions via Google Maps |

## 📸 Screenshots

> Open `index.html` in your browser to see the full experience!

## 🚀 Quick Start

No build tools, no npm, no dependencies to install.

```bash
# Clone the repo
git clone https://github.com/Jcoosemans/belgian-beers.git
cd belgian-beers

# Open in browser
open index.html        # macOS
xdg-open index.html    # Linux
start index.html       # Windows
```

Or use any local HTTP server for full functionality (geolocation requires HTTPS or localhost):

```bash
python3 -m http.server 8000
# Then open http://localhost:8000
```

## 🏗️ Architecture

This is a **zero-build, single-file application**. Everything lives in `index.html`:

```
belgian-beers/
├── index.html                    # Full app: HTML + CSS + JS
├── 404.html                      # GitHub Pages SPA redirect
├── data/
│   ├── trending.json             # Weekly trending beers (auto-updated)
│   └── night-shops.json          # Night shops from OpenStreetMap
├── .github/workflows/
│   └── update-trending.yml       # GitHub Actions: weekly Untappd update
├── AGENTS.md                     # AI assistant instructions
├── CLAUDE.md                     # → Points to AGENTS.md
├── GEMINI.md                     # → Points to AGENTS.md
└── README.md                     # You are here
```

### External Dependencies

| Dependency | Purpose | CDN |
|---|---|---|
| [Leaflet.js](https://leafletjs.com/) | Interactive maps | unpkg |
| [Google Fonts](https://fonts.google.com/) | Playfair Display + Inter | Google Fonts CDN |
| [CARTO Basemaps](https://carto.com/basemaps/) | Dark map tiles | CARTO CDN |

## 🔄 Auto-Updating Trending Beers

The site features a "Trending This Week" section powered by the [Untappd API](https://untappd.com/api/).

To enable auto-updates:

1. Register for a free API key at [untappd.com/api/register](https://untappd.com/api/register)
2. Add these secrets to your GitHub repo (**Settings → Secrets and variables → Actions**):
   - `UNTAPPD_CLIENT_ID`
   - `UNTAPPD_CLIENT_SECRET`
3. The workflow runs every Monday at 06:00 UTC, or trigger manually from the Actions tab

Without API keys, the site falls back to static trending data.

## 🌙 Night Shops Data

Night shop locations are sourced from [OpenStreetMap](https://www.openstreetmap.org/) via the [Overpass API](https://overpass-turbo.eu/). The data covers central Brussels (postcode 1000).

To refresh the data, run the Overpass query documented in `data/night-shops.json`.

## 🤝 Contributing

1. Fork the repository
2. Make your changes to `index.html`
3. Test by opening in a browser
4. Submit a pull request

### Adding a Beer

Add an entry to the `beers` array in `index.html` with:
- `name`, `type`, `abv`, `region`, `brewery`, `personality`
- `lat`/`lng` (brewery coordinates)
- `desc` (one-line description)
- `img` (Wikimedia Commons URL, or empty string for SVG fallback)

### Adding a Café

Add an entry to the `cafes` array with the café's details and a list of beer names (must match existing beer names exactly).

## 📄 License

This project is open source. Feel free to use, modify, and share.

## 🇧🇪 Proost!

*Drink responsibly.* 🍺
