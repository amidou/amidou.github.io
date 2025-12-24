#!/usr/bin/env python3
"""Generate a static `publications.md` from `_data/publications.bib`.

Requires: `bibtexparser` (pip install bibtexparser)

The script writes an ordered HTML list of publications and a minimal
Jekyll front matter so the generated file can replace a `{% bibliography %}` page.
"""
from pathlib import Path
from html import escape
import sys

try:
    import bibtexparser
except Exception as e:
    print("Missing dependency: install with `pip install bibtexparser`")
    raise


HERE = Path(__file__).parent.parent
BIBFILE = HERE / "_data" / "publications.bib"
OUTFILE = HERE / "publications.md"


def authors_to_text(a: str) -> str:
    # simple conversion: 'A and B and C' -> 'A, B & C'
    parts = [p.strip() for p in a.split(" and ") if p.strip()]
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return f"{parts[0]} & {parts[1]}"
    return f"{', '.join(parts[:-1])} & {parts[-1]}"


def entry_html(entry: dict) -> str:
    authors = authors_to_text(entry.get("author", ""))
    title = entry.get("title", "").strip()
    journal = entry.get("journal", "").strip()
    year = entry.get("year", "").strip()
    volume = entry.get("volume", "").strip()
    pages = entry.get("pages", "").strip()
    doi = entry.get("doi", "").strip()
    ads = entry.get("adsurl", "").strip()

    parts = []
    if authors:
        parts.append(f"<strong>{escape(authors)}</strong>")
    if title:
        parts.append(f"<em>{escape(title)}</em>")
    meta = ""
    if journal:
        meta = escape(journal)
        if volume:
            meta += f" {escape(volume)}"
        if pages:
            meta += f", {escape(pages)}"
    if meta:
        parts.append(meta)
    if year:
        parts.append(f"({escape(year)})")

    text = " — ".join(p for p in parts if p)

    links = []
    if doi:
        links.append(f'<a href="https://doi.org/{escape(doi)}">doi</a>')
    if ads:
        links.append(f'<a href="{escape(ads)}">ADS</a>')
    linkpart = (" [" + " | ".join(links) + "]") if links else ""

    return f"<li>{text}{linkpart}</li>"


def sort_key(entry: dict):
    # prefer year (int), fallback to 0; preserve original order otherwise
    y = entry.get("year", "")
    try:
        return int(y)
    except Exception:
        return 0


def main():
    if not BIBFILE.exists():
        print(f"BibTeX file not found: {BIBFILE}")
        sys.exit(1)

    with open(BIBFILE, encoding="utf8") as fh:
        db = bibtexparser.load(fh)

    entries = sorted(db.entries, key=sort_key, reverse=True)

    header = (
        "---\n"
        "layout: default\n"
        "title: Publications\n"
        "permalink: /publications/\n"
        "---\n\n"
    )

    with open(OUTFILE, "w", encoding="utf8") as out:
        out.write(header)
        out.write("<ol>\n")
        for e in entries:
            out.write(entry_html(e) + "\n")
        out.write("</ol>\n")

    print(f"Wrote {OUTFILE}")


if __name__ == "__main__":
    main()
