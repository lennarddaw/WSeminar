#!/usr/bin/env python3
# split_pdf.py
import argparse
from pypdf import PdfReader, PdfWriter

def parse_ranges(spec: str, total_pages: int) -> list[int]:
    """
    Wandelt eine Bereichs-Spezifikation wie '1-2,5,10-' in
    0-basierte Seitenindizes um (inklusive Grenzen).
    Unterstützt:
      n         => einzelne Seite
      a-b       => von a bis b
      -b        => von Anfang bis b
      a-        => von a bis Ende
    """
    if not spec:
        raise ValueError("Leere Bereichs-Spezifikation.")
    indices = []
    seen = set()
    for part in (p.strip() for p in spec.split(",") if p.strip()):
        if "-" in part:
            a_str, b_str = part.split("-", 1)
            a = 1 if a_str == "" else int(a_str)
            b = total_pages if b_str == "" else int(b_str)
            if a < 1 or b < 1 or a > total_pages or b > total_pages:
                raise ValueError(f"Bereich außerhalb 1..{total_pages}: {part}")
            if a > b:
                raise ValueError(f"Absteigende Bereiche nicht erlaubt: {part}")
            for i in range(a - 1, b):
                if i not in seen:
                    indices.append(i)
                    seen.add(i)
        else:
            n = int(part)
            if n < 1 or n > total_pages:
                raise ValueError(f"Seite außerhalb 1..{total_pages}: {n}")
            i = n - 1
            if i not in seen:
                indices.append(i)
                seen.add(i)
    return indices

def main():
    ap = argparse.ArgumentParser(description="PDF-Seitenbereich(e) extrahieren")
    ap.add_argument("input", help="Eingabe-PDF")
    ap.add_argument("output", help="Ausgabe-PDF")
    ap.add_argument("-p", "--pages", required=True,
                    help="Bereiche, z. B. '1-2', '3-6,9,12-', '-5'")
    args = ap.parse_args()

    reader = PdfReader(args.input)  # reader.pages liefert list-ähnlichen Zugriff
    total = len(reader.pages)

    indices = parse_ranges(args.pages, total)

    writer = PdfWriter()
    for idx in indices:
        writer.add_page(reader.pages[idx])  # Seite übernehmen

    with open(args.output, "wb") as f:
        writer.write(f)

    print(f"Fertig: {len(indices)} Seite(n) -> {args.output}")

if __name__ == "__main__":
    main()
