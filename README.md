# news-image-20261117-entry

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Falken21/news-image-20261117-entry/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Falken21/news-image-20261117-entry/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

**THE WORLD IN ONE DAY** — a one-image front page summing up the world news of **Tuesday, 17 November 2026**. Six editorial illustrations, each captioned, under one masthead:

- **EUROPE** — Ukraine blows a span out of the Crimean Bridge
- **EUROPE** — Russian missiles hit Kyiv's two Dnipro bridges
- **MIDDLE EAST** — Tankers hit mines in Hormuz as a third US carrier arrives
- **ASIA** — Trump in Manila; a Xi–Trump–Putin summit is set for Shenzhen
- **EUROPE** — Five EU nations to open a migrant return hub in Rwanda
- **SPACE** — Vulcan rocket failure destroys 40 Amazon satellites

The artwork panels were generated as flat editorial illustrations with no text in them; every letter on the page — masthead, date line, region tags and headlines — was typeset programmatically, so nothing is garbled. The finished page is stored as `entry.png` (JPEG bytes, 1024×1024, under the 1 MiB cap), and `main.py` copies it byte-for-byte to the output directory.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The image lands at `out/entry.png`, identical on every run.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
