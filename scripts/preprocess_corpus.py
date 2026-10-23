import json
import re
from pathlib import Path

# Locate project directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Input and output paths
INPUT_PATH = PROJECT_ROOT / "data" / "raw" / "conversations.json"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "conversations_clean.json"


def clean_text(text):
    """
    Apply conservative cleaning to PDF-extracted text.

    Preserve punctuation, case, emojis, accents,
    morphological forms and paragraph boundaries.
    """

    # 1. Remove zero-width spaces
    text = text.replace("\u200b", "")

    # 2. Normalise line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # 3. Remove spaces immediately before line breaks
    text = re.sub(r"[ \t]+\n", "\n", text)

    # 4. Preserve paragraph breaks temporarily
    text = re.sub(r"\n[ \t]*\n+", "<PARAGRAPH>", text)

    # 5. Join lines broken by PDF layout
    text = re.sub(r"\n", " ", text)

    # 6. Restore paragraph breaks
    text = text.replace("<PARAGRAPH>", "\n\n")

    # 7. Remove leading and trailing whitespace
    text = text.strip()

    return text


# Load original corpus
with INPUT_PATH.open("r", encoding="utf-8") as file:
    corpus = json.load(file)


# Create cleaned corpus
cleaned_corpus = []

for exchange in corpus:

    cleaned_exchange = {
        "exchange_id": exchange["exchange_id"],
        "title": exchange["title"],
        "source_type": exchange["source_type"],
        "turns": []
    }

    for turn in exchange["turns"]:

        cleaned_turn = {
            "speaker": turn["speaker"],
            "text": clean_text(turn["text"])
        }

        cleaned_exchange["turns"].append(cleaned_turn)

    cleaned_corpus.append(cleaned_exchange)


# Create output directory if necessary
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# Save processed corpus
with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    json.dump(cleaned_corpus, file, ensure_ascii=False, indent=2)


print("Original exchanges:", len(corpus))
print("Cleaned exchanges:", len(cleaned_corpus))
print("Processed corpus saved to:", OUTPUT_PATH)

