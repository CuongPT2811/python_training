
import string

def read_paragraph() -> str:
    """
    Read paragraph input until empty line
    """
    print("Enter a paragraph (end with empty line): ")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return " ".join(lines)

def analyze_words(text: str) -> dict:
    """
    Analyze paragraph, count words, find only word, longest words   
    """
    translator = str.maketrans('', '', string.punctuation)
    all_words = text.split()
    total_word_count = len(all_words)

    unique_words_map = {}
    for word in all_words:
        cleaned_word = word.translate(translator)
        lower_word = cleaned_word.lower()
        if lower_word and lower_word not in unique_words_map:
            unique_words_map[lower_word] = cleaned_word
            
    unique_words_list = list(unique_words_map.values())
    unique_words_list.sort(key=len, reverse=True)
    
    return {
        "total_words": total_word_count,
        "unique_count": len(unique_words_list), 
        "longest_five": unique_words_list[:5]
    }

def main():
    """
    Process analyze words
    """
    paragraph = read_paragraph()
    if paragraph:
        analysis_result = analyze_words(paragraph)
        
        print(f"Number of words: {analysis_result['total_words']}")
        print(f"Unique words count: {analysis_result['unique_count']}")
        print(f"Five longest unique words: {analysis_result['longest_five']}")
    else:
        print("Empty paragraph")

if __name__ == "__main__":
    main()