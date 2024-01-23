from unidecode import unidecode

def clean_text(input_text):
    # Remove non-alphabet characters and non-commas
    cleaned_text = ''.join(char if char.isalpha() or char == ':' else ' ' for char in input_text)

    # Replace characters with diacritics to letters without diacritics
    cleaned_text = unidecode(cleaned_text)

    # Remove spaces from the start and end of the line
    cleaned_text = cleaned_text.strip()

    return cleaned_text

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(lines)

    cleaned_lines = []
    for line in lines:
        # Remove lines with less than 5 characters
        if len(line.strip()) >= 5:
            cleaned_line = clean_text(line)
            cleaned_lines.append(cleaned_line)

    # Join cleaned lines and write to the output file
    print(cleaned_lines)
    result_text = '\n'.join(cleaned_lines)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result_text)

if __name__ == "__main__":
    input_file_path = "definitions.txt"
    output_file_path = "cleaned_definitions.txt"

    process_file(input_file_path, output_file_path)
    print(f"File '{input_file_path}' has been cleaned and saved as '{output_file_path}'.")
