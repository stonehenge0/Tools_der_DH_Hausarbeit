"""Reading in both Sherlock texts and basic cleaning.
"""

import os

import re

def remove_extra_spaces(input_text):
    """
    Remove consecutive spaces in a text.

    This function takes an input text and uses a regular expression
    to replace consecutive spaces (including tabs and newlines) with a single space.

    Parameters:
    - input_text (str): The input text with potential consecutive spaces.

    Returns:
    str: The cleaned text with consecutive spaces replaced by a single space.
    """
    
    cleaned_text = re.sub(r'\s+', ' ', input_text)
    return cleaned_text

def clean_Enola (Enola_text):
    """A cleaning function designed specifially for the traits in the Enola text.
    
    Gets rid of triple quotes. Replaces stylysed quotes with python-readable ones. Lowercases everything.
    Remove "\t" and "\n". 

    Args:
        Enola_text (str): a utf8 string of Enola Holmes. 
    Returns:
        str: cleaned string. 
    """
    
    # Remove quotes at start of paragraphs and replace stylised ones with python-readably ones. 
    Enola_text = Enola_text.replace("\"", "")
    Enola_text = Enola_text.replace("“", "\"")
    Enola_text = Enola_text.replace("”", "\"")
    
    
    #Lowercase everything. 
    modified_chars = []

    for char in Enola_text:
        if char.isupper():
            modified_chars.append(char.lower())
        else:
            modified_chars.append(char)
            
    lowercase_enola = "".join(modified_chars)
            
    # Remove "\t" and "\n"      
    lowercase_enola = lowercase_enola.replace('\t', '').replace('\n', ' ')
    cleaned_enola = remove_extra_spaces(lowercase_enola)
            
    return (cleaned_enola)


    
    
    
# Get filepaths. 
base_dir = os.path.dirname(__file__) 
parent_dir = os.path.dirname(base_dir)

filename = "Full_Enola_utf8.txt"
folder_name = "Textdaten"
filepath = os.path.join(parent_dir, folder_name, filename)

with open(filepath, 'r', encoding='utf-8') as file:
    file_content = file.read()
    
  
if __name__ == "__main__":
    # Writing to output file. 
    final_cleaned_file = clean_Enola(file_content)  
    output_file_path = 'Enola_cleaned.txt'

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(final_cleaned_file)

    print("Cleaned Text has been written to", output_file_path)



