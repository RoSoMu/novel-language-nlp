import json
from pathlib import Path


# Locate the project directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_PATH = PROJECT_ROOT / "data" / "raw" / "conversations.json"
CLEAN_PATH = PROJECT_ROOT / "data" / "processed" / "conversations_clean.json"


# Load a JSON corpus
def load_corpus(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


# Validate corpus structure
def validate_corpus(raw, clean):

    errors = []

    # Check the number of exchanges
    if len(raw) != len(clean):
        errors.append("Exchange counts do not match.")

    if len(clean) != 10:
        errors.append("Expected 10 cleaned exchanges.")

    # Compare corresponding exchanges
    for original, processed in zip(raw, clean):

        exchange_id = original["exchange_id"]

        # Check metadata
        for field in ["exchange_id", "title", "source_type"]:
            if original[field] != processed[field]:
                errors.append(
                    f"{exchange_id}: {field} was modified."
                )

        # Check conversational turns
        original_turns = original["turns"]
        processed_turns = processed["turns"]

        if len(original_turns) != len(processed_turns):
            errors.append(
                f"{exchange_id}: turn count changed."
            )

        if len(processed_turns) != 2:
            errors.append(
                f"{exchange_id}: expected exactly 2 turns."
            )

        speakers = [
            turn["speaker"]
            for turn in processed_turns
        ]

        if speakers != ["user", "assistant"]:
            errors.append(
                f"{exchange_id}: unexpected speaker order."
            )

        # Check individual turns
        for original_turn, processed_turn in zip(
            original_turns, processed_turns
        ):

            if original_turn["speaker"] != processed_turn["speaker"]:
                errors.append(
                    f"{exchange_id}: speaker changed."
                )

            text = processed_turn["text"]

            if not text.strip():
                errors.append(
                    f"{exchange_id}: empty text detected."
                )

            if "\u200b" in text:
                errors.append(
                    f"{exchange_id}: zero-width space remains."
                )

    return errors


# Run validation
raw = load_corpus(RAW_PATH)
clean = load_corpus(CLEAN_PATH)

errors = validate_corpus(raw, clean)

print("\n--- CORPUS STRUCTURAL VALIDATION ---")

print(f"Original exchanges: {len(raw)}")
print(f"Cleaned exchanges: {len(clean)}")

if not errors:
    print("PASS: All structural checks completed successfully.")
else:
    print(f"FAIL: {len(errors)} validation issue(s) detected.")

    for error in errors:
        print(f"- {error}")

