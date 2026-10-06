# LittleLink

A personal link page built on [LittleLink](https://littlelink.io), with shortcuts for Lucas Hanson’s profiles and sites.

## What’s customized

- `/gh`, `/ig`, `/yt`, `/li`, and `/littlelink` provide short redirects for GitHub, Instagram, YouTube, LinkedIn, and this repository.
- `/btc` and `/bitcoin` link to the Bitcoin donation page on [lucashanson.dk](https://lucashanson.dk/bitcoin). This repository does not store wallet keys or payment details.
- The landing and privacy pages use a minimal monochrome card design, keyboard focus states, and reduced-motion support.
- Patrick Hand headings and Space Mono body text match the typography used on [lucashanson.dk](https://lucashanson.dk).

## Preview locally

From the repository root, run:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Then open <http://127.0.0.1:8765>. There is no build step or JavaScript dependency.

## License

LittleLink is distributed under the MIT license. See [LICENSE.md](LICENSE.md).
