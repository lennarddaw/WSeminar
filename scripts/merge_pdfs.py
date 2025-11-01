#!/usr/bin/env python3
# merge_pdfs.py
import argparse
import sys
from pathlib import Path
from typing import List
from pypdf import PdfReader, PdfWriter

def load_file_list(files: List[str], listfile: str | None) -> List[Path]:
    paths: List[Path] = []
    if listfile:
        for line in Path(listfile).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            paths.append(Path(line))
    for f in files:
        paths.append(Path(f))
    if not paths:
        raise SystemExit("Keine Eingabedateien angegeben.")
    return paths

def validate_pdf(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Nicht gefunden: {path}")
    # Schnelltest: lässt sich ein Reader öffnen?
    with path.open("rb") as fh:
        reader = PdfReader(fh)
        if reader.is_encrypted:
            # Versuch ohne Passwort – häufig reicht das
            try:
                reader.decrypt("")
            except Exception:
                pass
            if reader.is_encrypted:
                raise ValueError(f"Verschlüsselt (Passwort benötigt): {path}")

def merge_pdfs(inputs: List[Path], output: Path, verbose: bool=False) -> int:
    writer = PdfWriter()
    total_pages = 0
    for p in inputs:
        validate_pdf(p)
        if verbose:
            print(f"+ {p}")
        # Fügt die Datei vollständig an (alle Seiten in Reihenfolge)
        writer.append(str(p))  # pypdf unterstützt append(path) direkt
        # Seiten zählen rein informativ
        with p.open("rb") as fh:
            total_pages += len(PdfReader(fh).pages)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as fh:
        writer.write(fh)
    return total_pages

def main():
    ap = argparse.ArgumentParser(
        description="Mehrere PDF-Dateien in angegebener Reihenfolge zusammenführen."
    )
    ap.add_argument(
        "-o", "--output", required=True,
        help="Ausgabe-PDF, z. B. merged.pdf"
    )
    ap.add_argument(
        "-L", "--listfile",
        help="Optionale Textdatei mit Pfaden (eine pro Zeile; # als Kommentar)."
    )
    ap.add_argument(
        "files", nargs="*",
        help="PDFs in gewünschter Reihenfolge (ergänzt ggf. zu -L)."
    )
    ap.add_argument("-v", "--verbose", action="store_true", help="Ausführliche Ausgabe")
    args = ap.parse_args()

    inputs = load_file_list(args.files, args.listfile)
    out = Path(args.output)
    try:
        pages = merge_pdfs(inputs, out, verbose=args.verbose)
        print(f"Fertig: {len(inputs)} Datei(en), {pages} Seite(n) -> {out}")
    except Exception as e:
        print(f"Fehler: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
