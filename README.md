# Groot Session Description Fixer
A Python specialized tool for automating session data organization and description standardization in GR00T robotics data collection workflows.

=
                     Gear GR00T Session Description Fixer
                           Desktop Application (v1.0)
=

INSTALLATION & USAGE:

1. REQUIREMENTS:
   - Python 3.7 or higher
   - tkinter (comes built-in with Python)

2. HOW TO RUN:
   
   Option A (Windows):
   - Double-click the file: session_fixer.py
   - Or open Command Prompt and type: python session_fixer.py
   
   Option B (Mac/Linux/Ubuntu):
   - Open Terminal
   - Navigate to the folder with session_fixer.py
   - Type: python3 ./session_fixer.py

3. USING THE APPLICATION:

   STEP 1: SELECT SESSION FOLDER
   - Click "Browse" button
   - Select your session folder (e.g., 2026-01-22-17-44-34)
   - The path will appear in the text field

   STEP 2: SEGREGATE FOLDERS
   - Click "1. Create LI 1 & LI 2 Folders and Segregate Episodes"
   - This will:
     • Create "LI 1" and "LI 2" folders in your session
     • Create subfolders with session name and operator
     • Transfer odd-numbered episodes (00001, 00003, 00005...) to LI 1
     • Transfer even-numbered episodes (00002, 00004, 00006...) to LI 2
   - Wait for completion message

   STEP 3: FIX DESCRIPTIONS
   - Select a Task Name from the dropdown (e.g., "insert_remove_airpods")
   - LI 1 and LI 2 descriptions will auto-populate
   - Edit descriptions if needed (e.g., change [yarn/ribbon] to "yarn")
   - Click "2. Start Description Fix"
   - This will update all metadata.json files with correct descriptions
   - Only descriptions are edited - everything else stays the same including indentions, spaces, values, etc.

4. ADDING MORE TASK NAMES:
   - Open session_fixer.py with a text editor
   - Find this section:
     
     self.task_descriptions = {
         "task_name": {
             "LI_1": "description for LI 1",
             "LI_2": "description for LI 2"
         },
     }
   
   - Add your new task names following the same format
   - Save the file
   - Restart the application

5. IMPORTANT:
   - Original episode folders are moved, not copied
   - Only metadata.json descriptions are changed, everything else stays the same
   - File indentation, spacing, and numeric values are preserved
   - Check the log for detailed processing information

6. TROUBLESHOOTING:
   - If Python is not found, install Python from python.org
   - Make sure you have read/write permissions in the session folder
   - Check the log area in the application for error messages

=
Version 1.0 (Beta)
© 2025 Kyle Josef Bonachita. All rights reserved.
Proprietary and Confidential.
For internal use by the NVIDIA Gear GR00t Collections Project only.
Unauthorized distribution prohibited.
=
