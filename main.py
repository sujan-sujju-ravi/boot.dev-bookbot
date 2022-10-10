
def read_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    file_content = read_text(file_path)

    # Count the number of words
    word_count = len(file_content.split())
    
    full_report = f"--- Begin report of {file_path} ---\n"
    full_report += f"{word_count} words found in the document\n\n"

    # Capture the frequency/count of each letter
    file_content = file_content.lower()

    set_of_chars = set(file_content)
    letter_count_dict = {}
    for char in set_of_chars:
        letter_count_dict[char] = file_content.count(char)
    
    # collect each alphabet frequency in a readable format
    alphabet_report = []
    for char in letter_count_dict:
        if char.isalpha():
            alphabet_report.append(f"The '{char}' character was found {letter_count_dict[char]} times")
    full_report += "\n".join(alphabet_report)

    full_report += "\n--- End report ---"

    print(full_report)


main()