"""Calculate the Type-Token Ratio for Enola and Sherlock."""

import os

import spacy


def preprocess_text(text, nlp):
    """Preprocess the text using Spacy."""
    doc = nlp(text)
    return [token.text.lower() for token in doc if not token.is_punct and not token.is_space]

def calculate_type_token_ratio(tokens):
    """Calculate Type Token Ratio."""
    unique_tokens = set(tokens)
    return len(unique_tokens) / len(tokens) if len(tokens) > 0 else 0

def calculate_average_ttr(text, nlp, slice_size):
    """Calculate the average Type Token Ratio over slices of the text."""
    preprocessed_text = preprocess_text(text, nlp)
    
    # Calculate TTR for each slice
    slice_ttrs = []
    for i in range(0, len(preprocessed_text), slice_size):
        slice_tokens = preprocessed_text[i:i + slice_size]
        slice_ttr = calculate_type_token_ratio(slice_tokens)
        slice_ttrs.append(slice_ttr)
    
    # Calculate the average TTR
    average_ttr = sum(slice_ttrs) / len(slice_ttrs) if len(slice_ttrs) > 0 else 0
    return average_ttr

nlp = spacy.load("en_core_web_sm")


# Get filepaths
base_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(base_dir)
folder_name = "Textdaten"
s_filename = "Sherlock_cleaned.txt"
e_filename = "Enola_cleaned.txt"
s_filepath = os.path.join(parent_dir, folder_name, s_filename)
e_filepath = os.path.join(parent_dir, folder_name, e_filename)


slice_size = 1000 # These slice sizes are important because the files have different lengths and that can distort TTR heavily otherwise. 




# Code for Enola and Sherlock respectively. 
# Comment out the one you do not want to run, running both is also possible, but will take quite some time. 

# Running code for SHERLOCK.
with open(s_filepath, 'r', encoding='utf-8') as file:
    s = file.read()  # s = sherlock = basic cleaned file for sherlock. 
s_doc = nlp(s)
s_tokenlist = [token.text.lower() for token in s_doc if not token.is_punct and not token.is_space]
average_ttr_s = calculate_average_ttr(s, nlp, slice_size)

print(f"Average Type Token Ratio for Sherlock: {average_ttr_s}")

## Uncomment these if you want to run the code for the ENOLA files. 
# with open(e_filepath, 'r', encoding='utf-8') as file:
#   e = file.read()
# e_doc = nlp(e)
# e_tokenlist = [token.text.lower() for token in e_doc if not token.is_punct and not token.is_space]
# average_ttr_e = calculate_average_ttr(e, nlp, slice_size)

# print(f"Average Type Token Ratio for Enola: {average_ttr_e}")



