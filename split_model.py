"""
Split plant_disease_final_model.keras into parts under 25MB each.
Run once to create model_part1.bin, model_part2.bin, etc.
"""
import os

CHUNK_MB = 20  # Each part stays safely under 25MB
MODEL_PATH = "plant_disease_final_model.keras"
PREFIX = "plant_disease_model_part"

def split():
    if not os.path.exists(MODEL_PATH):
        print(f"Error: {MODEL_PATH} not found.")
        return

    size = os.path.getsize(MODEL_PATH)
    chunk_size = CHUNK_MB * 1024 * 1024
    part = 1

    with open(MODEL_PATH, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            out = f"{PREFIX}{part}.bin"
            with open(out, "wb") as outf:
                outf.write(chunk)
            print(f"Created {out} ({len(chunk) / 1024 / 1024:.1f} MB)")
            part += 1

    print(f"\nDone. Model split into {part - 1} parts (all under 25MB).")

if __name__ == "__main__":
    split()
