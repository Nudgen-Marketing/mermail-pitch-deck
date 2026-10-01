"""Dependency-free release checks for UII SIP & SHARE HTML and its local assets."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "uii-sip-share/index.html"


class DeckParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


def check():
    parser = DeckParser()
    source = DECK.read_text(encoding="utf-8")
    parser.feed(source)
    errors = []
    ids = [attrs["id"] for _, attrs in parser.elements if "id" in attrs]
    duplicates = [key for key, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate IDs: {duplicates}")
    slides = [attrs for _, attrs in parser.elements
              if "slide" in attrs.get("class", "").split()]
    if len(slides) != 6 or any(not slide.get("id") for slide in slides):
        errors.append("Every slide needs an ID; this short deck needs six slides")
    canonicals = [a.get("href") for tag, a in parser.elements
                  if tag == "link" and a.get("rel") == "canonical"]
    if canonicals != ["https://pitching.mermail.app/uii-sip-share/"]:
        errors.append("Canonical URL must point to /uii-sip-share/")
    for tag, attrs in parser.elements:
        if tag in {"iframe", "video"}:
            errors.append("UII SIP & SHARE must use the readable flow instead of an embedded video")
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
            elif parsed.fragment and parsed.fragment not in ids:
                errors.append(f"Broken slide anchor: {value}")
    if not any(tag == "img" and a.get("src", "").startswith("data:image/")
               for tag, a in parser.elements):
        errors.append("The deck must retain embedded brand artwork")
    if "prefers-reduced-motion" not in source:
        errors.append("Missing reduced-motion support")
    if errors:
        raise SystemExit("UII SIP & SHARE validation failed:\n- " + "\n- ".join(errors))
    print(f"UII SIP & SHARE validation passed: {len(slides)} slides, unique IDs, valid local assets and metadata")


if __name__ == "__main__":
    check()
