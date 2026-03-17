# Text Analyzer (Python)

A simple Python application that analyzes text files and visualizes word statistics.  
The program can analyze a single `.txt` file or compare multiple files from a folder.

---

# Features

- Analyze a single text file or multiple files
- Automatic text cleaning (removes punctuation and converts text to lowercase)
- Removal of common stop words (Romanian and English)
- Word frequency calculation
- Statistics generation:
  - Total number of words
  - Number of different words
  - Average word length
  - Longest word
- Visualization using bar charts
- Comparison between multiple text files

---

# Technologies Used

- Python
- Tkinter (file selection interface)
- Matplotlib (data visualization)
- Git & GitHub

---

# How the Program Works

1. The program asks the user to choose the analysis mode:

- **Single text file**
- **Entire folder of text files**

2. The user selects the file or folder using a file picker window.

3. The program processes the text:

- removes punctuation
- converts text to lowercase
- splits text into words
- removes common stop words

4. Statistics are computed for each file.

5. Results are displayed:

- in the terminal
- as graphical charts using Matplotlib.

---

# Example Statistics

For each text file the program calculates:

- Total words
- Different words
- Average word length
- Longest word

When multiple files are analyzed, the program creates comparison charts for:

- Total words
- Different words
- Average word length
---

# Example Usage

1) Run the program:
python: analizator de text simplu.py
2) Choose analysis mode:
Number 1 - Single text file
Number 2 - Entire folder
3) Then select the desired file or folder.

---

# Text Sources / Credits

The text samples used for testing and demonstration come from the following sources:

**Space**

NASA Artemis II mission information  
https://www.nasa.gov/missions/artemis/nasas-artemis-ii-moon-mission-daily-agenda/

**History**

English Heritage – Medieval England  
https://www.english-heritage.org.uk/learn/story-of-england/medieval/

**Technology**

Language Models are Few-Shot Learners  
https://scispace.com/pdf/language-models-are-few-shot-learners-2fg8gvia7m.pdf

**Science**

Cell Stem Cell – scientific article  
https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(25)00226-7

These texts were used only as sample input data for testing the functionality of the text analysis program.

---

# Possible Improvements

Future improvements could include:

- support for more languages
- advanced NLP processing
- word clouds
- exporting results to CSV or JSON
- improved graphical interface

---

# Author

Alexandra Blaga  
Computer Science Student

---

# License

This project is for educational purposes.
