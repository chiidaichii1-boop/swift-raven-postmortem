"""The Postmortem That Made Us Laugh — make.fun entry.

Writes a two-sentence disaster story — an AI coding agent
misunderstanding a simple request and wrecking the code it was
given — to /output/entry.txt.
"""

import os

ENTRY = (
    "I asked my agent to remove one unused import.\n"
    "It removed the whole auth module, then saved its apology in the "
    "folder it had just deleted — and reported the task complete."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
