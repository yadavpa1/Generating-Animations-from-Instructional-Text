import spacy
import neuralcoref

def coreference_resolve_spacy(text):
    nlp = spacy.load('en')
    neuralcoref.add_to_pipe(nlp)
    doc = nlp(text)
    return doc._.coref_resolved


if __name__=="__main__":
    text = coreference_resolve_spacy("Wash the onions and cut them. Now add them to the pasta.")
    print(text)
