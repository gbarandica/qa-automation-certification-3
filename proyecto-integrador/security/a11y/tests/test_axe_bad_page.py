"""Demo Axe: detecta problemas WCAG en bad_page.html (Sesión 7)."""

from pathlib import Path

import pytest
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import sync_playwright

PAGE = Path(__file__).resolve().parents[1] / "bad_page.html"


def test_bad_page_tiene_violaciones_axe():
    """La página de demo DEBE fallar Axe: sirve para mostrar hallazgos en clase."""
    axe = Axe()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(PAGE.as_uri())
        results = axe.run(page)
        browser.close()

    violations = results.response.get("violations", [])
    # Esperamos hallazgos (imagen sin alt, contraste, etc.)
    assert len(violations) >= 1, "Se esperaban violaciones Axe en bad_page.html"

    # Imprimí un resumen legible para la demo del instructor
    print(f"\nViolaciones Axe encontradas: {len(violations)}")
    for v in violations[:5]:
        print(f"- [{v.get('impact')}] {v.get('id')}: {v.get('description')}")
