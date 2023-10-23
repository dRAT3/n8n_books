import os
import sys
import json
from ebooklib import epub
from bs4 import BeautifulSoup

def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)

    extracted_texts = {"text": {}}

    index = 0
    for item in book.items:
        if item.get_type() == 9:  # Check if the item is of type 'text'
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            
            # Extract plain text
            plain_text = soup.get_text().strip()
            if plain_text:
                extracted_texts["text"][str(index)] = plain_text
                index += 1
            
            # Extract linked text
            for link in soup.find_all('a'):
                linked_text = link.string
                if linked_text:
                    extracted_texts["text"][str(index)] = linked_text.strip()
                    index += 1

    return extracted_texts

if __name__ == '__main__':
    # EPUB file path from command line argument or user input
    epub_file_path = sys.argv[1] if len(sys.argv) > 1 else input("Please enter the path to your EPUB file: ")
    if not os.path.exists(epub_file_path):
        print("File does not exist. Please check the path.")
        exit(1)

    # Output JSON file name from command line argument or default name
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'extracted_text.json'
    
    extracted_content = extract_text_from_epub(epub_file_path)
    
    # Saving to the specified json file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(extracted_content, f, ensure_ascii=False, indent=4)

    print(f"Content extracted and saved to {output_file}!")

