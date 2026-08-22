#!/usr/bin/env python3
"""Conversor simples de markdown para PDF, feito para os dossies do Geburger."""
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ACCENT = colors.HexColor("#1F6F4A")
DARK = colors.HexColor("#1B1B1B")
GREY = colors.HexColor("#6B6B6B")
LINE = colors.HexColor("#D8D8D8")
BAND = colors.HexColor("#F2F6F3")

ss = getSampleStyleSheet()


def style(name, **kw):
    base = dict(fontName="Helvetica", fontSize=9.5, leading=13.5, textColor=DARK,
                alignment=TA_LEFT, spaceBefore=0, spaceAfter=0)
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    "h1": style("h1", fontName="Helvetica-Bold", fontSize=19, leading=23,
                textColor=ACCENT, spaceAfter=4),
    "h2": style("h2", fontName="Helvetica-Bold", fontSize=13.5, leading=17,
                textColor=ACCENT, spaceBefore=14, spaceAfter=5),
    "h3": style("h3", fontName="Helvetica-Bold", fontSize=11, leading=14.5,
                textColor=DARK, spaceBefore=10, spaceAfter=4),
    "p": style("p", spaceAfter=6),
    "li": style("li", spaceAfter=2),
    "th": style("th", fontName="Helvetica-Bold", fontSize=8.5, leading=11,
                textColor=colors.white),
    "td": style("td", fontSize=8.5, leading=11),
    "meta": style("meta", fontSize=9, leading=12.5, textColor=GREY, spaceAfter=10),
}


def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`([^`]+)`", r'<font face="Courier" size="8.5">\1</font>', t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    return t


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def make_table(rows, width):
    head, body = rows[0], rows[1:]
    ncols = len(head)
    data = [[Paragraph(inline(c), S["th"]) for c in head]]
    for r in body:
        r = (r + [""] * ncols)[:ncols]
        data.append([Paragraph(inline(c), S["td"]) for c in r])

    # primeira coluna mais larga, salvo quando ela e curta (codigo, sigla)
    if ncols == 1:
        widths = [width]
    else:
        col0 = [head[0]] + [(r + [""] * ncols)[0] for r in body]
        short = max(len(c) for c in col0) <= 14
        frac = 0.16 if short else (0.46 if ncols == 2 else 0.34 if ncols == 3 else 0.30)
        first = width * frac
        rest = (width - first) / (ncols - 1)
        widths = [first] + [rest] * (ncols - 1)

    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, BAND]),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def build(md_path, pdf_path, footer):
    lines = open(md_path, encoding="utf-8").read().split("\n")
    doc = SimpleDocTemplate(
        pdf_path, pagesize=A4,
        leftMargin=17 * mm, rightMargin=17 * mm,
        topMargin=16 * mm, bottomMargin=18 * mm,
        title="Dossie para a contabilidade - Geburger",
        author="Geburger",
    )
    W = doc.width
    flow = []
    i = 0
    first_para = True
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        if not s:
            i += 1
            continue

        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1].strip()):
            rows = [split_row(s)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            flow.append(Spacer(1, 3))
            flow.append(make_table(rows, W))
            flow.append(Spacer(1, 9))
            continue

        if s.startswith("---"):
            i += 1
            continue

        m = re.match(r"^(#{1,3})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1))
            flow.append(Paragraph(inline(m.group(2)), S["h%d" % lvl]))
            if lvl == 1:
                flow.append(Spacer(1, 2))
            i += 1
            continue

        if re.match(r"^(\d+\.|[-*])\s+", s):
            items = []
            bullet = "1" if re.match(r"^\d+\.", s) else "bullet"
            while i < len(lines) and re.match(r"^(\d+\.|[-*])\s+", lines[i].strip()):
                txt = re.sub(r"^(\d+\.|[-*])\s+", "", lines[i].strip())
                i += 1
                while i < len(lines) and lines[i].startswith("   ") and lines[i].strip() \
                        and not re.match(r"^(\d+\.|[-*])\s+", lines[i].strip()):
                    txt += " " + lines[i].strip()
                    i += 1
                items.append(ListItem(Paragraph(inline(txt), S["li"]), leftIndent=14))
            flow.append(ListFlowable(items, bulletType=bullet, start="1",
                                     leftIndent=14, bulletFontSize=9))
            flow.append(Spacer(1, 6))
            continue

        buf = [s]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(("|", "#", "-", "*")) \
                and not re.match(r"^\d+\.\s", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        st = S["meta"] if first_para else S["p"]
        first_para = False
        flow.append(Paragraph(inline(" ".join(buf)), st))

    def deco(canvas, docu):
        canvas.saveState()
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.4)
        canvas.line(17 * mm, 13 * mm, A4[0] - 17 * mm, 13 * mm)
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(GREY)
        canvas.drawString(17 * mm, 9 * mm, footer)
        canvas.drawRightString(A4[0] - 17 * mm, 9 * mm, "pág. %d" % docu.page)
        canvas.restoreState()

    doc.build(flow, onFirstPage=deco, onLaterPages=deco)
    print("ok:", pdf_path)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "")
