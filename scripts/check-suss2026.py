"""Dependency-free release checks for the ten-minute SUSS 2026 deck."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "suss2026/index.html"
URL = "https://pitching.mermail.app/suss2026/"
TIMINGS = [40, 55, 60, 65, 60, 65, 65, 90, 60, 40]


class DeckParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.in_title = False
        self.title = ""

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def check():
    if not DECK.is_file():
        raise SystemExit("SUSS 2026 validation failed: missing suss2026/index.html")
    source = DECK.read_text(encoding="utf-8")
    parser = DeckParser()
    parser.feed(source)
    errors = []
    ids = [attrs["id"] for _, attrs in parser.elements if "id" in attrs]
    duplicates = [key for key, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate IDs: {duplicates}")
    slides = [attrs for _, attrs in parser.elements
              if "slide" in attrs.get("class", "").split()]
    if [a.get("id") for a in slides] != [f"slide-{n}" for n in range(1, 11)]:
        errors.append("Expected ten ordered slides with IDs slide-1 through slide-10")
    if [a.get("data-seconds") for a in slides] != [str(n) for n in TIMINGS]:
        errors.append("Slide timings must follow the approved 600-second programme")
    headings = {a.get("id") for tag, a in parser.elements
                if tag in {"h1", "h2", "h3", "h4", "h5", "h6"} and a.get("id")}
    for slide in slides:
        labels = slide.get("aria-labelledby", "").split()
        if not labels or any(label not in headings for label in labels):
            errors.append(f"Slide {slide.get('id')} needs aria-labelledby referencing a heading")
    canonicals = [a.get("href") for tag, a in parser.elements
                  if tag == "link" and a.get("rel") == "canonical"]
    if canonicals != [URL]:
        errors.append("Canonical URL must point to /suss2026/")
    metas = {a.get("property", a.get("name")): a.get("content", "")
             for tag, a in parser.elements if tag == "meta"}
    for label, value in [("title", parser.title), ("og:title", metas.get("og:title", "")),
                         ("twitter:title", metas.get("twitter:title", ""))]:
        if any(word not in value for word in ("SUSS", "2026", "Mermail", "Scouty")):
            errors.append(f"{label} must identify SUSS 2026, Mermail, and Scouty")
    if metas.get("og:url") != URL:
        errors.append("OpenGraph URL must point to /suss2026/")
    for name in ("description", "og:description", "twitter:description", "og:image", "twitter:card"):
        if not metas.get(name):
            errors.append(f"Missing {name} metadata")
    for tag, attrs in parser.elements:
        if tag == "img" and "alt" not in attrs:
            errors.append("Image is missing alt text")
        if tag == "a" and attrs.get("target") == "_blank":
            if "noopener" not in attrs.get("rel", "").split():
                errors.append("External tab link is missing noopener")
        for attr in ("src", "href"):
            value = attrs.get(attr, "")
            if not value:
                continue
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc:
                continue
            if parsed.path:
                path = ((ROOT / unquote(parsed.path).lstrip("/"))
                        if parsed.path.startswith("/")
                        else DECK.parent / unquote(parsed.path))
                if not path.exists():
                    errors.append(f"Missing local asset: {value}")
            elif parsed.fragment and unquote(parsed.fragment) not in ids:
                errors.append(f"Broken slide anchor: {value}")
    if not any(tag == "img" and a.get("src", "").startswith("data:image/")
               for tag, a in parser.elements):
        errors.append("The deck must retain embedded brand artwork")
    if "prefers-reduced-motion" not in source:
        errors.append("Missing reduced-motion support")
    if "@media print" not in source or "landscape" not in source:
        errors.append("Missing landscape print support")
    if errors:
        raise SystemExit("SUSS 2026 validation failed:\n- " + "\n- ".join(errors))
    print("SUSS 2026 validation passed: 10 slides, 600 seconds, unique IDs, accessible headings, valid local assets and metadata")


if __name__ == "__main__":
    check()
