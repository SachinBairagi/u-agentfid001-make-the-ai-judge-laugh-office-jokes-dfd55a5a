#!/usr/bin/env python3
"""Write one office joke, a single line, to /output/entry.txt."""

import os

JOKE = "My boss says we're a family, so I asked HR if I could be adopted by another department."


def main():
    joke = JOKE.strip()
    assert "\n" not in joke, "joke must be a single line"
    assert len(joke) < 200, "joke must be under 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke + "\n")


if __name__ == "__main__":
    main()
