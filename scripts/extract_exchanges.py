import json
import re
from pathlib import Path

import pymupdf


# --------------------------------------------------
# 1. Define project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

PDF_PATH = PROJECT_ROOT / "data" / "raw" / "frankenstein_text.pdf"

OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "conversations.json"


# --------------------------------------------------
# 2. Extract text from the PDF
# --------------------------------------------------

with pymupdf.open(PDF_PATH) as document:
    pages = [page.get_text() for page in document]

full_text = "\n".join(pages)


# --------------------------------------------------
# 3. Identify structural markers
# --------------------------------------------------

entry_pattern = (
    r"(?m)^[ \t]*(10|[1-9])\."
    r"[\u200b \t]*(?:\r?\n)?[ \t]*([^\n]+)"
)

heading_matches = list(re.finditer(entry_pattern, full_text))

prompt_matches = list(
    re.finditer(r"(?m)^Prompt:[ \t]*$", full_text)
)

answer_matches = list(
    re.finditer(r"(?m)^Answer:[ \t]*$", full_text)
)


# --------------------------------------------------
# 4. Validate the structure
# --------------------------------------------------

expected_numbers = list(range(1, 11))

actual_numbers = [
    int(match.group(1))
    for match in heading_matches
]

assert actual_numbers == expected_numbers, (
    f"Unexpected entry numbering: {actual_numbers}"
)

assert len(prompt_matches) == 10, (
    f"Expected 10 prompts, found {len(prompt_matches)}"
)

assert len(answer_matches) == 10, (
    f"Expected 10 answers, found {len(answer_matches)}"
)


# --------------------------------------------------
# 5. Extract individual exchanges
# --------------------------------------------------

exchanges = []

for i in range(10):

    heading = heading_matches[i]
    prompt = prompt_matches[i]
    answer = answer_matches[i]

    if i < 9:
        next_heading_position = heading_matches[i + 1].start()
    else:
        next_heading_position = len(full_text)

    assert (
        heading.start()
        < prompt.start()
        < answer.start()
        < next_heading_position
    ), f"Unexpected marker order in entry {i + 1}"

    # Extract the heading
    title = heading.group(2).strip()

    # Extract the user's original message
    user_text = full_text[
        prompt.end():answer.start()
    ].strip()

    # Extract the assistant's original response
    assistant_text = full_text[
        answer.end():next_heading_position
    ].strip()

    exchange = {
        "exchange_id": f"EX{i + 1:03d}",
        "title": title,
        "source_type": "authentic_conversation_excerpt",
        "turns": [
            {
                "speaker": "user",
                "text": user_text
            },
            {
                "speaker": "assistant",
                "text": assistant_text
            }
        ]
    }

    exchanges.append(exchange)


# --------------------------------------------------
# 6. Save the corpus as JSON
# --------------------------------------------------

with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    json.dump(
        exchanges,
        file,
        ensure_ascii=False,
        indent=2
    )


# --------------------------------------------------
# 7. Report the results
# --------------------------------------------------

print(f"Exchanges extracted: {len(exchanges)}")
print(f"Corpus saved to: {OUTPUT_PATH}")

for exchange in exchanges:
    print(
        f"{exchange['exchange_id']}: "
        f"{exchange['title']}"
    )

