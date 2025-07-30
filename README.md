# ChickTool - Word-Level Text Difference Visualizer

## 📌 Overview

This Python application compares the **word-level differences** between two text files and visualizes them side-by-side using a PyQt5 GUI. It highlights:
- 🟥 Words removed from the first file (`file1.txt`) in red.
- 🟩 Words added in the second file (`file2.txt`) in green.
- ⚫ Unchanged words in black.

It is useful for comparing versions of documents or tracking changes in text content.

---

## 🔧 What This App/Script Does

- **`main.py`**: CLI entry point. Takes two filenames as command-line arguments, initializes the API, and runs the comparison.
- **`api.py`**: Bridges input reading, text comparison, and GUI display.
- **`difftool.py`**: Implements the core comparison logic using `difflib.Differ` to compute word-level differences.
- **`view.py`**: Displays the differences in a PyQt5 window with proper color-coded highlighting.
- **`file1.txt` / `file2.txt`**: Sample text files used to demonstrate the comparison.
- **`UnitTest.py`**: Contains unit tests for verifying comparison logic and file reading.

---

## 🛠 What Was Changed or Added

- Implemented `DiffTool.compare()` for word-by-word line comparison.
- Developed a rich PyQt5-based GUI in `view.py` to show diffs clearly.
- Built `API` class for clean integration of backend and frontend.
- Created `UnitTest.py` to test:
  - Correctness of comparison logic.
  - File reading reliability.
  - Edge cases and expected vs. actual outputs with custom error displays.
- Updated the main entry point (`main.py`) to use `argparse` for CLI integration.

---

## 🚧 Challenges Faced

- **Word-Level Comparison**: `difflib.Differ` is line-based by default. Adapting it to operate line-by-line and word-by-word required splitting and careful handling.
- **Result Formatting**: Displaying diffs accurately while syncing both views side-by-side needed careful logic to avoid misalignments.
- **Testing GUI Code**: GUI components are not directly testable with `unittest`, so functional logic was separated to allow unit testing.
- **UnitTest Flaws**: Some expected outputs were intentionally flawed in tests (e.g., `test_compare` has both passing and failing expectations), which helped evaluate robustness.

---

## ✅ How to Run

1. Install dependencies:
   ```bash
   pip install PyQt5
2. Run the tool:
   ```bash
   python main.py file1.txt file2.txt
3. Run tests:
   ```bash
   python UnitTest.py
   
