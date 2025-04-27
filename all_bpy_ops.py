import bpy
import os

# Adjust to your liking:
OUTPUT_FILE = bpy.path.abspath(os.path.expanduser("BpyOps.txt"))

with open(OUTPUT_FILE, "w", encoding="UTF-8") as workfile:
    # Generate operator calls using nested list comprehensions
    operator_calls = [
        f"bpy.ops.{category}.{op}()\n"
        for category in dir(bpy.ops)
        if not category.startswith("_")
        for op in dir(getattr(bpy.ops, category))
        if not op.startswith("_")
    ]

    # Write all operator calls to the file
    workfile.writelines(operator_calls)

print(f"Operator list exported to: {OUTPUT_FILE}")
