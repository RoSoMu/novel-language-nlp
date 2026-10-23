import json
from pathlib import Path

# Project directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Private corpus location
OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "conversations.json"

# First example (abbreviated for demonstration)
corpus = [
    {
        "exchange_id": "EX001",
        "source_type": "authentic_conversation",
        "turns": [
            {
                "speaker": "user",
                "text": "We decided to Frankenstein it."
            },
            {
                "speaker": "assistant",
                "text": "You have left another body on the laboratory floor."
            }
        ]
    }
]

# Save as JSON
with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    json.dump(corpus, file, ensure_ascii=False, indent=2)

print(f"Corpus saved to: {OUTPUT_PATH}")
