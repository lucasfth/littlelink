<div align="center">
  <h1>Lucas Hanson · LittleLink</h1>
  <p>A clean starting point for my links, projects, and contact details.</p>
  <p>
    <a href="https://links.lucashanson.dk">Live link hub</a> ·
    <a href="https://lucashanson.dk">Website</a> ·
    <a href="https://littlelink.io">Powered by LittleLink</a>
  </p>
  <p>
    <img alt="License" src="https://img.shields.io/github/license/lucasfth/littlelink">
    <img alt="Last commit" src="https://img.shields.io/github/last-commit/lucasfth/littlelink">
  </p>
</div>

## What’s inside

- `/gh`, `/ig`, `/yt`, and `/li` are short redirects to my social profiles.
- `/littlelink` points back to this repository.
- `/btc` and `/bitcoin` point to the Bitcoin page on [lucashanson.dk](https://lucashanson.dk/bitcoin). No wallet keys or payment details are stored here.
- `/nostr` points to Lucas's Nostr profile on [njump.me](https://njump.me/npub1rv5s9g5fk62eadufywu334u8732ssa8a9t5k93fdzdkrw529zz4qnrrhdm).
- `/llm` points to [nocturne](https://lucashanson.dk/nocturne), the night-time LLM API paid in sats.

## Look and feel

The landing and privacy pages use monochrome link cards, Arial/Helvetica headings shared with the portfolio, and Space Mono body text. The responsive layout includes visible keyboard focus, reduced-motion support, and automatic light/dark themes.

## Preview locally

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open <http://127.0.0.1:8765>. No build step or JavaScript dependencies are needed.

## License

LittleLink is distributed under the MIT License. See [LICENSE.md](LICENSE.md).
