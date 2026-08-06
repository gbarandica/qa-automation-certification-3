"""Generate sesion-05.pptx / sesion-06.pptx from PPT_CONTENIDO.md."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

REPO = Path(__file__).resolve().parents[1]

TITLE_COLOR = RGBColor(0x1B, 0x2A, 0x4A)
BODY_COLOR = RGBColor(0x2C, 0x3E, 0x50)
ACCENT_COLOR = RGBColor(0x0E, 0x7C, 0x7B)
MUTED_COLOR = RGBColor(0x7F, 0x8C, 0x8D)

SESSION_LABELS = {
    "sesion-05": "Sesión 5 · CI/CD",
    "sesion-06": "Sesión 6 · Performance K6",
    "sesion-07": "Sesión 7 · Seguridad ZAP + Axe",
    "sesion-08": "Sesión 8 · Mantenimiento y Mutación",
    "sesion-09": "Sesión 9 · Móvil y Regresión Visual",
    "sesion-10": "Sesión 10 · Release Gate · Cierre",
}


def parse_slides(markdown: str) -> list[dict[str, object]]:
    slides: list[dict[str, object]] = []
    chunks = re.split(r"\n### (Slide \d+[a-z]? —[^\n]+)\n", markdown)
    for i in range(1, len(chunks), 2):
        heading = chunks[i].strip()
        body = chunks[i + 1] if i + 1 < len(chunks) else ""
        title_match = re.match(
            r"Slide (\d+)([a-z]?) — (.+?)(?:\s*\(\d+ min\))?$", heading
        )
        if not title_match:
            continue
        slide_id = title_match.group(1) + title_match.group(2)
        title = title_match.group(3).strip()

        bullets: list[str] = []
        code_lines: list[str] = []
        in_code = False
        for line in body.splitlines():
            if line.startswith("**Título:**"):
                title = line.replace("**Título:**", "").strip()
                continue
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                if line.strip() and not line.strip().startswith("#"):
                    code_lines.append(line.rstrip())
                continue
            if line.startswith("---") or line.startswith("## "):
                break
            if line.startswith("- "):
                bullets.append(line[2:].strip())
            elif re.match(r"^\d+\.\s+", line):
                # Listas numeradas (el bug que vació OWASP Top 10 en S7).
                bullets.append(re.sub(r"^\d+\.\s+", "", line).strip())
            elif line.startswith("| ") and not re.match(r"^\|\s*-+", line):
                cells = [c.strip() for c in line.strip("|").split("|")]
                if cells and cells[0].lower() not in {
                    "herramienta",
                    "clave yaml",
                    "término",
                    "evento",
                    "script",
                    "síntoma",
                    "plataforma",
                    "comando",
                    "resultado",
                    "carpeta",
                    "task",
                }:
                    bullets.append(" — ".join(cells))
        # Código como bullets cortos (legibles en proyector), no un solo "Código: a|b|c".
        for cl in code_lines[:4]:
            bullets.append(cl.strip())
        slides.append({"slide_id": slide_id, "title": title, "bullets": bullets[:8]})
    return slides


def style_run(run, text: str, *, size: int, bold: bool = False, color=BODY_COLOR) -> None:
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = "Calibri"


def clean_md(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    return text.replace("`", "").replace("&lt;", "<")


def add_slide(
    prs: Presentation, slide_id: str, title: str, bullets: list[str], session_label: str
) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.16)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT_COLOR
    bar.line.fill.background()

    title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.35), Inches(12.1), Inches(1.0))
    p = title_box.text_frame.paragraphs[0]
    title_box.text_frame.word_wrap = True
    style_run(p.add_run(), title, size=28, bold=True, color=TITLE_COLOR)

    meta = slide.shapes.add_textbox(Inches(0.6), Inches(1.25), Inches(12.1), Inches(0.3))
    style_run(
        meta.text_frame.paragraphs[0].add_run(),
        f"{session_label} · Slide {slide_id}",
        size=12,
        color=ACCENT_COLOR,
    )

    body = slide.shapes.add_textbox(Inches(0.7), Inches(1.7), Inches(11.9), Inches(5.2))
    tf = body.text_frame
    tf.word_wrap = True
    items = bullets or ["Ver guía del instructor / SESION_0X.md"]
    for idx, bullet in enumerate(items):
        para = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        para.level = 0
        para.space_after = Pt(10)
        style_run(para.add_run(), f"• {clean_md(bullet)}", size=18, color=BODY_COLOR)

    footer = slide.shapes.add_textbox(Inches(0.6), Inches(7.05), Inches(12.1), Inches(0.3))
    fp = footer.text_frame.paragraphs[0]
    fp.alignment = PP_ALIGN.RIGHT
    style_run(
        fp.add_run(),
        "Certificación 3 — APIs, Performance y Seguridad",
        size=10,
        color=MUTED_COLOR,
    )


def build_session(session_dir: Path) -> Path:
    md_path = session_dir / "PPT_CONTENIDO.md"
    out_path = session_dir / f"{session_dir.name}.pptx"
    if not md_path.exists():
        raise SystemExit(f"No existe {md_path}")

    slides = parse_slides(md_path.read_text(encoding="utf-8"))
    if not slides:
        raise SystemExit(f"No se encontraron slides en {md_path}")

    label = SESSION_LABELS.get(session_dir.name, session_dir.name)
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    for slide in slides:
        add_slide(
            prs,
            str(slide["slide_id"]),
            str(slide["title"]),
            list(slide["bullets"]),
            label,
        )
    prs.save(out_path)
    print(f"Generado {out_path} con {len(slides)} diapositivas")
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "session",
        nargs="?",
        choices=[
            "sesion-05",
            "sesion-06",
            "sesion-07",
            "sesion-08",
            "sesion-09",
            "sesion-10",
            "all",
        ],
        default="all",
    )
    args = parser.parse_args()
    names = (
        [
            "sesion-05",
            "sesion-06",
            "sesion-07",
            "sesion-08",
            "sesion-09",
            "sesion-10",
        ]
        if args.session == "all"
        else [args.session]
    )
    for name in names:
        build_session(REPO / "sesiones" / name)


if __name__ == "__main__":
    main()
