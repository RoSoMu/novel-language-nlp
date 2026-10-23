import json
from pathlib import Path

# Locate the project directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Locate the extracted corpus
CORPUS_PATH = PROJECT_ROOT / "data" / "raw" / "conversations.json"

# Load the JSON corpus
with CORPUS_PATH.open("r", encoding="utf-8") as file:
    corpus = json.load(file)

# Inspect the beginning and end of each conversational turn
for exchange in corpus:
    print(f"\n{exchange['exchange_id']}: {exchange['title']}")

    for turn in exchange["turns"]:
        print(
            turn["speaker"],
            "| START:",
            repr(turn["text"][:80]),
            "| END:",
            repr(turn["text"][-80:])
        )

# Corpus size summary
print("\n--- CORPUS SIZE SUMMARY ---")

total_characters = 0

for exchange in corpus:
    for turn in exchange["turns"]:
        character_count = len(turn["text"])
        total_characters += character_count

        print(
            exchange["exchange_id"],
            turn["speaker"],
            character_count,
            "characters"
        )

print("\nTotal characters:", total_characters)

