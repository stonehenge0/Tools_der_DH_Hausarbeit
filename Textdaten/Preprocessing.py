import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Specify the path to your "enola.txt" file
file_path = "C:\\Users \\emste\\ownCloud - emma.stein@stud.uni-goettingen.de@owncloud.gwdg.de\\Studium\\WS_23_24_Göttingen\\Tools der DH\\Textdaten\\Fertig_raw_Enola_all.txt"

# Open and read the contents of the file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()
    
print(text[:100])  # Print the first 1000 characters as a snippet


# Process the text using SpaCy
doc = nlp(text)


for token in doc:
    print(token.text, token.pos_, token.dep_)
    break
