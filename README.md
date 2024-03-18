# Wie ähnlich sind sich Sherlock und Enola Holmes?
![ ](https://github.com/stonehenge0/Tools_der_DH_Hausarbeit/blob/main/gif_rm_Sherlock.gif)


----
## Inhalt

Dieses Repository beinhaltet verschiedene Messungen mithilfe von dem Python Modul [spaCy](https://spacy.io/), mit denen man Ähnlichkeit zwischen den Texten Büchern von Sherlock und Enola Holmes feststellen kann. 

----
## Funktionalitäten und Organisation

Ein paar der wichtigsten Funktionen dieses Repos sind:

- `code/visualizations` Visualisierungen von Sentiment Analyse und häufigen Tokens
- `code/frequent_tokens` Analyse der häufigsten Tokens in den Dokumenten
- `code/document_similarity` Ähnlichkeit zwischen zwei Dokumenten gemessen mit spaCy`s [document similarity](https://spacy.io/usage/linguistic-features) unction
- `code/type_token_ratio` calculate Type Token Ratio for both texts
- `code/sentiment_analysis` calculate polarity and subjectivity for both texts

Alle Textdateien finden sich im Ordner `Textdaten`

- Rohe Textdaten
- Gecleanten Text

Im `results` folder finden sich: 

- Die Resultate aller Analysen (Type Token Ratio, Sentiment Analysis,...)
- Im Ordner `results/finished_visualization` sind die fertigen Visualisierungen als .png Dateien


----
## Installation and Nutzung

Eine volle Liste von Installationen findet sich unter `requirements.txt`.
Am schnellsten lässt sich requirements installieren mit [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/#use-pip-for-installing) und einem [virtual environment](https://docs.python.org/3/tutorial/venv.html) (wie [venv](https://docs.python.org/3/library/venv.html)).
> <name_of_vev> wird mit dem Namen des tatsächlichen Environments ersetzt.

```sh
python3 -m venv <name_of_venv>
source <name_of_venv>/bin/activate
pip install -r requirements.txt
```


----
## Modul-Details

- Semester: Wintersemester 2023/24
- Modulnummer:  B.DH.05.PrVor: Werkzeuge der Digital Humanities (Übung)
- Prüferin: Hanna Surjadi
- Emma Stein (Bachelor Allgemeine Sprachwissenschaften/Digital Humanities)

---
## License
This project is covered through a MIT License.

Copyright (c) 2024 Emma Victoria Stein

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

> See [LICENSE](LICENSE.txt).

