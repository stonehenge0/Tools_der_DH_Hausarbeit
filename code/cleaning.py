"""Reading in both Sherlock texts and basic cleaning.
"""

# This script can used both for cleaning both the Sherlock text and for the Enola text.
# Use the clean_Sherlock() or clean_Enola() functions respectively and adapt the filepaths. 


import os

import re

def remove_extra_spaces(input_text):
    """Remove consecutive spaces in a text."""
    return re.sub(r'\s+', ' ', input_text)

def replace_quotes_and_lowercase(input_text):
    """Replace quotes and convert text to lowercase."""
    # Replace quotes
    cleaned_text = input_text.replace("“", "\"").replace("”", "\"")
    
    # Lowercase everything
    modified_chars = [char.lower() if char.isupper() else char for char in cleaned_text]
    return "".join(modified_chars)

def clean_Enola(Enola_text):
    """Clean Enola Holmes text."""
    # Remove quotes at start of paragraphs and replace stylized ones with Python-readable ones
    Enola_text = Enola_text.replace("\"", "").replace("“", "\"").replace("”", "\"")
    
    # Replace quotes and convert text to lowercase
    cleaned_enola = replace_quotes_and_lowercase(Enola_text)
    
    # Remove "\t" and "\n"
    cleaned_enola = cleaned_enola.replace('\t', '').replace('\n', ' ')
    
    # Remove consecutive spaces
    cleaned_enola = remove_extra_spaces(cleaned_enola)
    
    return cleaned_enola

def clean_Sherlock(Sherlock_text):
    """Clean Sherlock Holmes text."""
    # Replace quotes and convert text to lowercase
    cleaned_sherlock = replace_quotes_and_lowercase(Sherlock_text)
    
    # Remove "\t" and "\n"
    cleaned_sherlock = cleaned_sherlock.replace('\t', ' ').replace('\n', ' ')
    
    # Remove consecutive spaces
    cleaned_sherlock = remove_extra_spaces(cleaned_sherlock)
    
    return cleaned_sherlock


# Get filepaths.
base_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(base_dir)
filename = "Sherlock_original.txt"
folder_name = "Textdaten"
filepath = os.path.join(parent_dir, folder_name, filename)

with open(filepath, 'r', encoding='utf-8') as file:
    file_content = file.read()



cleaned_sherlock = clean_Sherlock(file_content)

# Writing to output file.  
if __name__ == "__main__":
    
    final_cleaned_file = clean_Sherlock(file_content)  
    output_file_path = 'Sherlock_cleaned.txt'

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(final_cleaned_file)

    print("Cleaned Text has been written to", output_file_path)
