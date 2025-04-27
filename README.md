# 🧰 pegbox
### Unordered tool set ###
## 🧷 all_bpy_ops ##
*This script generates a list of all available Blender Python API (bpy) operator calls 
and writes them into a text file. It uses the `bpy` module to access Blender's operators, 
filters out private ones (those starting with an underscore), and formats each call as 
a string that can be executed in Blender's scripting environment.*

🗹 Usage
* Open the python script inside any Blender build's text editor 
* *Optionally* rename older BpyOps.txt version to be able to diff compare
* Ensure you have write permissions for the specified output location variable: `OUTPUT_FILE`[^1]
* Press the ▶ play button from the header to run script

[^1]:(By default, it saves the list in the current Blender project directory to a text file named "BpyOps.txt" containing lines formatted as `bpy.ops.<category>.<operator>()`, representing each available operator call in Blender.)
