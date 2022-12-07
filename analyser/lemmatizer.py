import spacy

# to install "pl_core_news_sm" spacy model use:
# python -m spacy download pl_core_news_sm
class Lemmatizer:

    def lemmatize(words):
        nlp = spacy.load("pl_core_news_sm")
        doc = nlp(" ".join(words))
        return [token.lemma_ for token in doc]
