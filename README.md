# River of Life Academy website

Website for River of Life Academy (ROLA), a basic school in Accra, Ghana, running from Creche to Junior High School. Motto: Devotion and Service.

It is a static site: plain HTML, CSS and JavaScript with no build step. Open `index.html` in a browser, or host the folder on any web host.

## Files

| Path | What it is |
|------|------------|
| `index.html` | The whole site: welcome experience, page sections, menu |
| `css/styles.css` | Page styles. Brand colours are the variables at the top |
| `css/experience.css` | Welcome screen stages, tile wall, preview sheet, menu |
| `js/main.js` | All behaviour. Tile text for the globe is in `TEXT_CARDS` near the top |
| `images/site/` | Colour photos used on the pages, plus `crest.png` |
| `images/globe/` | Black-and-white tiles for the globe; `full/` holds the colour versions shown in previews |

## Common changes

- **Home background video:** save a short muted clip as `images/site/hero.mp4`. It replaces the changing photos automatically.
- **Swap a photo:** replace the file in `images/site/` with a new one of the same name.
- **Contact details:** search `index.html` for `+233 20 000 0000` and `info@riveroflifeacademy.edu.gh`.
- **Term dates:** edit the rows in the `Term dates` section of `index.html`.
- **Contact form:** it opens the visitor's email app by default. To receive messages directly, create a form at formspree.io and paste its address into `FORM_ENDPOINT` in `js/main.js`.
