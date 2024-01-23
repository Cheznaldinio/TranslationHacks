
def get_line_before_colon(line):
    # Find the index of the first colon in the line
    colon_index = line.find(':')

    # Check if the colon is present in the line
    if colon_index != -1:
        # Extract the substring before the colon
        result = line[:colon_index].strip()
        return result
    else:
        # If no colon is found, return the original line
        return line.strip()
def find_most_similar_definitions(word, definitions, num_top_matches=3):
    matches = []

    for line in definitions:
        temp_line = line
        line = get_line_before_colon(line)
        match_count = 0
        temp_match_count = 0
        split_line = line.split()
        for word_in_line in split_line:
            for i in range(min(len(word), len(word_in_line))):
                if word[i] == word_in_line[i]:
                    temp_match_count += 1
                else:
                    break
            if temp_match_count > match_count:
                match_count = temp_match_count
            temp_match_count = 0


        line = temp_line
        matches.append((line.strip(), match_count))

    # Sort matches by match count in descending order
    matches.sort(key=lambda x: x[1], reverse=True)

    # Filter out duplicate lines
    unique_matches = []
    seen_lines = set()

    for line, match_count in matches:
        if line not in seen_lines:
            unique_matches.append((line, match_count))
            seen_lines.add(line)

    # Return the top N unique matches
    return [match[0] for match in unique_matches[:num_top_matches]]


def main():
    # Read definitions from 'definitions.txt'
    definitions_file_path = 'cleaned_definitions.txt'
    try:
        with open(definitions_file_path, 'r') as definitions_file:
            definitions = definitions_file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{definitions_file_path}' not found.")
        return

    # Read text from 'text.txt'
    text_file_path = 'text.txt'
    try:
        with open(text_file_path, 'r') as text_file:
            content = text_file.read()
    except FileNotFoundError:
        print(f"Error: File '{text_file_path}' not found.")
        return

    # Split the content into words
    words = content.split()

    # Find the top 3 most similar definitions for each word
    for word in words:
        word = word.lower()
        if word.isalpha():
            results = find_most_similar_definitions(word, definitions, num_top_matches=3)
            if results:
                with open('OvidVocab.txt', 'a') as file:
                    file.write(f" -- {word}:\n")
                    for result in results:
                        file.write(result + '\n')

                print(f" -- {word}:")
                for result in results:
                    print(result)
            else:
                print(f"No matching definitions found for '{word}'.")
if __name__ == "__main__":
    main()
