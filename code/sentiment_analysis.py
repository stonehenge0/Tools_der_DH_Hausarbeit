"""Sentiment analysis that returns polarity and subjectivity of input text using the spacytextblob library.

NOTE: spacytextblob needs additional data to be installed to work properly: python -m textblob.download_corpora
"""

import os

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")

# Get filepaths
base_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(base_dir)
folder_name = "Textdaten"
s_filename = "Sherlock_cleaned.txt"
e_filename = "Enola_cleaned.txt"
s_filepath = os.path.join(parent_dir, folder_name, s_filename)
e_filepath = os.path.join(parent_dir, folder_name, e_filename)

with open(e_filepath, 'r', encoding='utf-8') as file:
    e = file.read() # replace with filepaths for Enola if you want the other text to be analysed.


def analyze_sentiment(text):
    """Get polarity and subjectivity of a text.

    Args:
        text (str): input text

    Returns:
        doc: polarity and subjectivity ratings for this text slice
    """
    doc = nlp(text)
    return doc._.polarity, doc._.subjectivity

def process_text_slices(full_text, slice_length):
    """Turn text into smaller slices and analyze each of these slices for polarity and subjectivity

    Args:
        full_text (str): cleaned text
        slice_length (int): size of one slice of text

    Returns:
        list: list of the polarities
        list: list of subjectivity ratings
    """
    polarities = []
    subjectivities = []

    slices = [full_text[i:i + slice_length] for i in range(0, len(full_text), slice_length)]

    # Analyze sentiment for each slice using analyse_sentiment
    for slice_text in slices:
        polarity, subjectivity = analyze_sentiment(slice_text)
        polarities.append(polarity)
        subjectivities.append(subjectivity)

    return polarities, subjectivities

if __name__ == "__main__":

    # Set the slice length. Adapt accordingly for larger texts. 
    slice_length = 1000
    
    output_file_path = 'Enola_sentiment_analysis.txt'

    
    polarities, subjectivities = process_text_slices(e, slice_length)
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(str(polarities))
        file.write(str(subjectivities))

    print("Sentiment Analysis has been written to", output_file_path)
