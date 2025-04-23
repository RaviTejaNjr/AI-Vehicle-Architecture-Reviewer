# src/export_utils.py

import re
from pathlib import Path
from fpdf import FPDF

def strip_emojis(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)  # Keep only ASCII

def save_to_markdown(output_text: str, out_path: str = "output/review.md"):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output_text)

def save_to_pdf(output_text: str, out_path: str = "output/review.pdf"):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Strip emojis and non-ASCII characters
    output_text = strip_emojis(output_text)

    for line in output_text.splitlines():
        if line.strip() == "":
            pdf.ln(5)
        else:
            pdf.multi_cell(0, 10, line)
    pdf.output(out_path)
