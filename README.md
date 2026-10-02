> ℹ️ Note
> This repository is forked from [sethcottle/littlelink](https://github.com/sethcottle/littlelink)

---

# LittleLink

Small changes have been made to the original LittleLink project and also on how it was expected to be used.

## Changes

- Relative links for social media buttons are used in `index.html`
- Folders for each social media button have been added with its own `index.html` file.
  This allows the use of URL custom redirects, for example through a service like [links.lucashanson.dk](https://links.lucashanson.dk), to easily share links to your social media profiles.
  - `/gh` folder for GitHub
  - `/ig` folder for Instagram
  - `/yt` folder for YouTube
  - `/littlelink` folder for the GitHub repository of this project
- Remove unused files
- ObsidianUI-inspired monochrome link cards, matching the palette and typography on [lucashanson.dk](https://lucashanson.dk).
- Patrick Hand headings and Space Mono body text, loaded from Google Fonts with system fallbacks.
- Automatic light/dark appearance, visible keyboard focus, and reduced-motion support.

## Appearance

`css/style.css` defines the shared theme for the landing and privacy pages. Keep `theme-auto` on the HTML element to follow the browser's appearance; `theme-light` and `theme-dark` force a specific theme.

Icons are monochrome in both themes. Multi-colour SVGs need transparent cut-outs for internal details, rather than overlapping fills that disappear under the icon filter.

## Local preview

Run `python3 -m http.server 8765 --bind 127.0.0.1` from the repository root, then open `http://127.0.0.1:8765`.

No build step or JavaScript dependencies are required. The upstream MIT copyright and license remain in `LICENSE.md`.
