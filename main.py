import os

# Verified count: 102 characters / 102 UTF-8 bytes, no trailing newline.
LINE = "I am out of office until Monday. If this is urgent, please lower your expectations and try again then."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(LINE)

print(f"{len(LINE)} characters written to {output_path}")
