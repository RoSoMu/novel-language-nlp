import pymupdf
from pathlib import Path

# Locate the project directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Locate the original PDF
PDF_PATH = PROJECT_ROOT / "data" / "raw" / "frankenstein_text.pdf"

# Open the PDF
document = pymupdf.open(PDF_PATH)

# Inspect the document
print(f"Number of pages: {len(document)}")

# Characters and expressions to inspect
targets = [
    "ñ", "á", "é", "í", "ó", "ú", "Í", "À",
    "😂", "🦄", "😁", "🌈", "♻️", "🧟‍♀️",
    "📜", "🚫", "🌳", "✅", "🎤", "😘",
    "τέλεια", "ροβοτ", "μου"
]

for page_number, page in enumerate(document, start=1):
    text = page.get_text()

    found = [target for target in targets if target in text]

    print(f"Page {page_number}: {found}")

document.close()
