"""Analyse document similarity between Enola and Sherlock using spacy's inbuilt document similarity functioin.
"""

import os 

import spacy

nlp = spacy.load("en_core_web_md")  # Note that this is a larger pipeline than used in the other scripts.


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
        
    print("similarity score: " ,(s_doc.similarity(e_doc))) # similarity score:  0.9951040569738279
    