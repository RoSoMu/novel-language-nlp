import re
import pymupdf
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = PROJECT_ROOT / "data" / "raw" / "frankenstein_text.pdf"

# Extract text from all pages
with pymupdf.open(PDF_PATH) as document:
    pages = [page.get_text() for page in document]

# Combine the extracted text
full_text = "\n".join(pages)

print("\n--- SEARCHING FOR THE MISSING FACULTY ---")

for line_number, line in enumerate(full_text.splitlines(), start=1):
    if "10" in line or "Faculty" in line or "Gibberishonian" in line:
        print(f"Line {line_number}: {repr(line)}")

print("\n--- FIRST 15 EXTRACTED LINES ---")

for line_number, line in enumerate(full_text.splitlines()[:15], start=1):
    print(f"{line_number:02d}: {repr(line)}")

# Find numbered entry headings
entry_pattern = r"(?m)^[ \t]*(10|[1-9])\.[\u200b \t]*(?:\r?\n)?[ \t]*([^\n]+)"

entries = list(re.finditer(entry_pattern, full_text))

# Find speaker labels
prompts = list(re.finditer(r"(?m)^Prompt:\s*$", full_text))
answers = list(re.finditer(r"(?m)^Answer:\s*$", full_text))

print(f"Pages extracted: {len(pages)}")
print(f"Numbered entries found: {len(entries)}")
print(f"Prompt labels found: {len(prompts)}")
print(f"Answer labels found: {len(answers)}")

print("\n--- ENTRY HEADINGS ---")

for match in entries:
    entry_number = match.group(1)
    entry_title = match.group(2)

    print(f"Entry {entry_number}: {entry_title}")

print("\n--- STRUCTURAL VALIDATION ---")

if len(entries) == len(prompts) == len(answers) == 10:
    print("Expected number of structural markers found.")
else:
    print("WARNING: Structural markers require inspection.")

print("\n--- CONVERSATIONAL TURN ORDER ---")

for i in range(10):
    heading = entries[i]
    prompt = prompts[i]
    answer = answers[i]

    if i < 9:
        next_heading_position = entries[i + 1].start()
    else:
        next_heading_position = len(full_text)

    valid_order = (
        heading.start()
        < prompt.start()
        < answer.start()
        < next_heading_position
    )

    print(
        f"Entry {i + 1}: "
        f"Heading → Prompt → Answer: {valid_order}"
    )
