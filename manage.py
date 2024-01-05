#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import string
import spacy

from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('en_core_web_sm')
stopwords = list(STOP_WORDS)
punc = string.punctuation

def text_cleaner(sentence):
    doc=nlp(sentence)
    
    tokens=[]
    for token in doc:
        if token.lemma_!="-PRON-":
            temp=token.lemma_.lower().strip()
        else:
            temp=token.lower_
        tokens.append(temp)
        
    cleaned_tokens=[]
    for token in tokens:
        if token not in stopwords and token not in punc:
            cleaned_tokens.append(token)
    return cleaned_tokens

sys.modules['text_cleaner'] = text_cleaner

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MRAssistant.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
