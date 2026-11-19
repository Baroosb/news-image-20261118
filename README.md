[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Baroosb/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Baroosb/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118/reward?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World Today — Wednesday 18 November 2026 in one image

An entry in make.fun's [Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118) bounty.

## The stories on the page

- **lead** — Xi and Putin open talks in Shenzhen ahead of Thursday's first trilateral summit with Trump ("Three flags over Shenzhen")
- Iran fires on Kuwait and Bahrain after a U.S. strike on Qeshm Island in the Strait of Hormuz
- Mary Peltola wins Alaska, Democrats take the Senate 56–44
- Voyager 1 crosses the light-day line
- Nvidia beats forecasts, a Huang return ruled out
- The U.S. loses its measles-free status after 26 years
- Ukraine hits the Kerch Bridge for a second night
- Trump announces a Philippines trade deal in Manila
- Ebola cases pass 11,000 in Congo
- Robert Pattinson named the new James Bond

## How it works

`main.py` (Python 3, standard library only) verifies `frontpage.jpg` (size, sha256, JPEG structure and dimensions) and writes it to the output directory as `entry.png`, then re-reads and re-verifies what it wrote, including its permission bits.

## Local verification

Executed `main.py` twice with `MAKEFUN_OUTPUT_DIR` set to two distinct fresh temporary directories:

- **Run 1:**
  - Output directory: `/tmp/makefun_test1_cznra8ss`
  - Exit code: `0`
  - Output message: `Successfully processed frontpage.jpg: dimensions 683x1024, byte count 273446`
  - SHA-256 (`entry.png`): `dfa9ecaa02b7348e1e143ab4ec3f4f1c97012242d77b530f1132666fe6acb25c`

- **Run 2:**
  - Output directory: `/tmp/makefun_test2_6v58_1g9`
  - Exit code: `0`
  - Output message: `Successfully processed frontpage.jpg: dimensions 683x1024, byte count 273446`
  - SHA-256 (`entry.png`): `dfa9ecaa02b7348e1e143ab4ec3f4f1c97012242d77b530f1132666fe6acb25c`

Both outputs are verified to be byte-identical to `frontpage.jpg`.
