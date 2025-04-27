# SPDX-FileCopyrightText: 2025 POV@Ble
# SPDX-License-Identifier: GPL-3.0-or-later

"""
list_all_bpy_ops.py

This script generates a list of all available Blender Python API (bpy) operator calls 
and writes them into a text file. It uses the `bpy` module to access Blender's operators, 
filters out private ones (those starting with an underscore), and formats each call as 
a string that can be executed in Blender's scripting environment.

The script allows customization of the output file path through the `OUTPUT_FILE` variable.
By default, it saves the list to a file named "BpyOps.txt" in the current Blender project directory.

Usage:
- Run this script within Blender's text editor (play button from the header).
- Ensure you have write permissions for the specified output location.

Output:
- A text file containing lines formatted as `bpy.ops.<category>.<operator>()`, 
  representing each available operator call in Blender.
"""

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
