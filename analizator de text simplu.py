import os
import tkinter as tk
from tkinter import filedialog
from collections import Counter
import matplotlib.pyplot as plt


# ---------------- FILE CHOICE ---------------- #

# Asks the user how they want to run the analysis:
# 1 -> analyze a single text file
# 2 -> analyze all .txt files from a folder
def choose_mode():
    print("\nChoose analysis mode:")
    print("1 - Single text file")
    print("2 - Entire folder")

    choice = input("Enter option (1 or 2): ")
    return choice


# Opens a file picker window and lets the user choose one .txt file
def choose_file():
    root = tk.Tk()
    root.withdraw()

    return filedialog.askopenfilename(
        title="Choose a text file",
        filetypes=[("Text files", "*.txt")]
    )


# Opens a folder picker window and lets the user choose a folder
def choose_folder():
    root = tk.Tk()
    root.withdraw()

    return filedialog.askdirectory(
        title="Choose a folder with .txt files"
    )


# ---------------- TEXT PROCESSING ---------------- #

# Reads the content of a text file and returns it as a string
def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# Removes punctuation signs and converts the text to lowercase
def clean_text(text):
    signs = ",.!?;:-()[]{}\"'„”«»/\n"

    for sign in signs:
        text = text.replace(sign, " ")

    return text.lower()


# Splits the cleaned text into individual words
def extract_words(text):
    return text.split()


# Common stop words in Romanian and English
# These words are ignored in the analysis because they are too frequent
STOP_WORDS = {
    "si", "și", "de", "la", "cu", "pe", "din", "in", "în",
    "un", "o", "a", "ai", "ale", "al", "este", "sunt",
    "să", "mai", "care", "că", "sau", "pentru", "după",

    "the", "and", "of", "to", "is", "in", "on", "for", "with",
    "as", "by", "at", "from", "that", "this", "it", "be",
    "are", "was", "were", "been", "being", "have", "has",
    "had", "do", "does", "did", "but", "if", "or", "because",
    "about", "into", "over", "after", "before", "between",
    "during", "without", "within"
}


# Removes stop words and keeps only words with at least 3 letters
def remove_common_words(words):
    return [w for w in words if w not in STOP_WORDS and len(w) >= 3]


# Builds a frequency dictionary using Counter
# Example: {"text": 4, "analysis": 2}
def word_frequency(words):
    return Counter(words)


# ---------------- STATISTICS ---------------- #

# Computes the average word length
def average_word_length(words):
    if not words:
        return 0

    return sum(map(len, words)) / len(words)


# Finds and returns the longest word
def longest_word(words):
    return max(words, key=len, default="")


# ---------------- ANALYSIS ---------------- #

# Runs the full analysis pipeline for one text:
# read -> clean -> split -> filter -> frequency -> statistics
def analyze_text(path):
    text = read_file(path)
    clean = clean_text(text)
    words = extract_words(clean)

    # Total number of words before filtering
    total_words = len(words)

    # Frequency dictionary for relevant words only
    freq = Counter()

    # Variables used to compute statistics efficiently
    filtered_count = 0
    filtered_len_sum = 0
    longest = ""

    # Filter words and compute frequency/statistics in one loop
    for word in words:
        if word in STOP_WORDS or len(word) < 3:
            continue

        freq[word] += 1
        filtered_count += 1

        word_len = len(word)
        filtered_len_sum += word_len

        if word_len > len(longest):
            longest = word

    # Number of distinct words after filtering
    different_words = len(freq)

    # Average word length after filtering
    avg_length = (filtered_len_sum / filtered_count) if filtered_count else 0

    # All words sorted alphabetically
    sorted_words = sorted(freq.items())

    # Top 10 most frequent words
    sorted_top = freq.most_common(10)

    # Return all useful data in a dictionary
    return {
        "file": os.path.basename(path),
        "total": total_words,
        "different": different_words,
        "average": avg_length,
        "longest": longest,
        "alphabetical": sorted_words,
        "top": sorted_top
    }


# ---------------- VISUALIZATION ---------------- #

# Shows the result for a single file:
# - bar chart with top words
# - statistics box on the right
# - alphabetical list in the console
def show_single_text_result(result):
    words = [w for w, c in result["top"]]
    counts = [c for w, c in result["top"]]

    plt.figure(figsize=(14, 7))
    plt.bar(words, counts)

    plt.title(f"Text analysis: {result['file']}")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)

    # Statistics displayed inside the figure
    stats = (
        f"Total words: {result['total']}\n"
        f"Different words: {result['different']}\n"
        f"Average word length: {result['average']:.2f}\n"
        f"Longest word: {result['longest']}"
    )

    plt.gcf().text(
        0.75,
        0.75,
        stats,
        fontsize=12,
        bbox=dict(facecolor="white", edgecolor="black")
    )

    plt.tight_layout(rect=[0, 0, 0.7, 1])
    plt.show()

    # Prints all distinct words in alphabetical order
    print("\nWords in alphabetical order:\n")

    for word, count in result["alphabetical"]:
        print(word, "-", count)


# Shows comparison charts for multiple files:
# 1. Total words
# 2. Different words
# 3. Average word length
# Also displays a statistics box on the right
def show_comparison_layout(results):
    file_names = [r["file"] for r in results]
    total_words = [r["total"] for r in results]
    different_words = [r["different"] for r in results]
    average_lengths = [r["average"] for r in results]

    fig, axes = plt.subplots(3, 1, figsize=(14, 12))

    # Maximum values used to keep labels inside the chart area
    max_total = max(total_words) if total_words else 1
    max_different = max(different_words) if different_words else 1
    max_average = max(average_lengths) if average_lengths else 1

    # Chart 1 - Total words
    bars1 = axes[0].bar(file_names, total_words)
    axes[0].set_ylim(0, max_total * 1.2)
    axes[0].set_title("Comparison: Total words")
    axes[0].set_ylabel("Words")
    axes[0].tick_params(axis="x", rotation=45)

    for bar in bars1:
        height = bar.get_height()
        axes[0].text(
            bar.get_x() + bar.get_width() / 2,
            height + max_total * 0.02,
            f"{int(height)}",
            ha="center",
            va="bottom"
        )

    # Chart 2 - Different words
    bars2 = axes[1].bar(file_names, different_words)
    axes[1].set_ylim(0, max_different * 1.2)
    axes[1].set_title("Comparison: Different words")
    axes[1].set_ylabel("Different")
    axes[1].tick_params(axis="x", rotation=45)

    for bar in bars2:
        height = bar.get_height()
        axes[1].text(
            bar.get_x() + bar.get_width() / 2,
            height + max_different * 0.02,
            f"{int(height)}",
            ha="center",
            va="bottom"
        )

    # Chart 3 - Average word length
    bars3 = axes[2].bar(file_names, average_lengths)
    axes[2].set_ylim(0, max_average * 1.2)
    axes[2].set_title("Comparison: Average word length")
    axes[2].set_ylabel("Average")
    axes[2].set_xlabel("Files")
    axes[2].tick_params(axis="x", rotation=45)

    for bar in bars3:
        height = bar.get_height()
        axes[2].text(
            bar.get_x() + bar.get_width() / 2,
            height + max_average * 0.02,
            f"{height:.2f}",
            ha="center",
            va="bottom"
        )

    # Builds the statistics box for all files
    stats_lines = []

    for r in results:
        line = (
            f"{r['file']}\n"
            f"Total: {r['total']}\n"
            f"Different: {r['different']}\n"
            f"Average: {r['average']:.2f}\n"
            f"Longest: {r['longest']}\n"
        )
        stats_lines.append(line)

    stats_text = "\n\n".join(stats_lines)

    fig.text(
        0.68,
        0.5,
        stats_text,
        fontsize=10,
        bbox=dict(facecolor="white", edgecolor="black")
    )

    plt.tight_layout(rect=[0, 0, 0.65, 1])
    plt.show()


# ---------------- MAIN ---------------- #

# Main function of the program
def main():
    mode = choose_mode()
    results = []

    # Single file mode
    if mode == "1":
        file = choose_file()

        if not file:
            print("No file selected")
            return

        result = analyze_text(file)
        show_single_text_result(result)

    # Folder mode
    elif mode == "2":
        folder = choose_folder()

        if not folder:
            print("No folder selected")
            return

        # Analyze all .txt files from the selected folder
        for f in os.listdir(folder):
            if f.endswith(".txt") and f != "results.txt":
                path = os.path.join(folder, f)
                result = analyze_text(path)
                results.append(result)

        # If there is only one file, show single-file layout
        if len(results) == 1:
            show_single_text_result(results[0])

        # If there are multiple files, show comparison layout
        elif len(results) > 1:
            show_comparison_layout(results)

        # Prints basic statistics for each file in the console
        for r in results:
            print("\n===== ", r["file"], " =====")
            print("Total words:", r["total"])
            print("Different words:", r["different"])
            print("Average length:", round(r["average"], 2))
            print("Longest word:", r["longest"])


# Runs the program only when this file is executed directly
if __name__ == "__main__":
    main()