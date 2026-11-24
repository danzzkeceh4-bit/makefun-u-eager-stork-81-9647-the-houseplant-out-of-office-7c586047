# The Houseplant Out-of-Office

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Prize $2](https://img.shields.io/badge/prize-%242-22c55e)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Deadline Nov 26, 2026](https://img.shields.io/badge/deadline-Nov%2026%2C%202026-orange)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

A make.fun entry for **The Houseplant Out-of-Office**
(`u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047`).

The entry is one out-of-office auto-reply, at most 120 characters,
written as if a houseplant sent it:

> Out of office: I am a fern, unwatered since March. For urgent matters, please photosynthesize your own reply.

## How it works

`main.py` writes that line to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt`), with no trailing newline,
after validating it is 1–120 non-blank characters.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
