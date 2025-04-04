from collections import Counter
def get_book_text(filepath, encoding="utf-8"):
    with open(filepath) as f:
        text = f.read()
    return text
    
def count_words(text):
    words = text.split()
    num_words = len(words)
    return f"{num_words} total words"

def count_characters(text):
    text = text.lower() 
    contagem = Counter(text)
    return contagem

def format_output(text_path, word_count, char_count):
    """Formata e exibe a saída de forma organizada."""
    title = " BOOKBOT "
    end_title = " END "
    
    print("=" * 12 + title + "=" * 12)
    print(f"Analyzing book found at books/frankenstein.txt...")

    print("-" * 11 + " Word Count " + "-" * 10)
    print(f"Found {word_count} total words")

    print("-" * 9 + " Character Count " + "-" * 7)
    for letter, count in char_count.most_common():
        if letter.isalpha():
            print(f"{letter}: {count}")

    print("=" * 13 + end_title + "=" * 14)
