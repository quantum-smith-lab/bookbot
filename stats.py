# stats.py
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    return char_counts

def sort_char_counts(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # Filter out non-alphabetical characters
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
