from collections import defaultdict

def main():
    book_file = 'books/War and Peace.txt'
    with open(book_file) as f:
        text = f.read()
    print(f'--- Begin report of {book_file} ---')
    print(f'{get_word_count(text)} words found in the document')
    print()
    char_counts = get_char_count(text)
    # Print character counts in descending order
    for char in sorted(char_counts, key=char_counts.get, reverse=True):
        print(f"The '{char}' character was found {char_counts[char]} times")
    # for char, count in sorted(char_counts.items(), key=lambda c: c[1], reverse=True):
    #     print(f"The '{char}' character was found {count} times")        
    print('--- End report ---')

def get_word_count(text: str) -> int:
    return len(text.split())

def get_char_count(text: str) -> dict[str, int]:
    char_counter = defaultdict(int)
    # Convert to lowercase and filter for only alphabet characters
    cleaned_text = filter(str.isalpha, text.lower())
    # cleaned_text = filter(str.isalpha, map(str.lower, text))
    for c in cleaned_text:
        char_counter[c] += 1
    return dict(char_counter)

if __name__ == '__main__':
    main()