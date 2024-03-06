import os

import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def get_top_tokens(doc, num_tokens=20):
    """
    Get the most frequent tokens in a spacy Doc object.

    Parameters:
    - doc (spacy.tokens.Doc): The spacy Doc object.
    - num_tokens (int): Number of top tokens to retrieve. Default is 20.

    Returns:
    - dict: A dictionary with tokens as keys and their counts as values.
    """
    # Ensure the input is a spacy Doc object
    if not isinstance(doc, spacy.tokens.Doc):
        raise ValueError("Input must be a spacy Doc object.")

    token_counts = Counter([token.text for token in doc if not (token.is_stop or token.is_punct)])
    
    top_tokens = dict(token_counts.most_common(num_tokens))

    return top_tokens


if __name__ == "__main__":
    
    # Get filepaths.
    base_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(base_dir)
    folder_name = "Textdaten"
    s_filename = "Sherlock_cleaned.txt"
    e_filename = "Enola_cleaned.txt"
    s_filepath = os.path.join(parent_dir, folder_name, s_filename)
    e_filepath = os.path.join(parent_dir, folder_name, e_filename)

    with open(e_filepath, 'r', encoding='utf-8') as file:
        e = file.read() 

    with open(s_filepath, 'r', encoding='utf-8') as file:
        s = file.read()
        
    e_doc = nlp(e)
    s_doc = nlp(s)

    # Get the top 20 tokens and their frequencies
    top_tokens_e = get_top_tokens(e_doc, num_tokens=20)
    top_tokens_s = get_top_tokens(s_doc, num_tokens=20)
    
        
        
    # Write to Output file    
    output_file_path = 'most_frequent_tokens_results.txt'

    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(str(top_tokens_e))
        file.write(str(top_tokens_s))

    print("Result of most frequent tokens has been written to", output_file_path)
    

