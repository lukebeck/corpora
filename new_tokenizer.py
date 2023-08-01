from sudachipy import tokenizer
from sudachipy import dictionary

tokenizer_obj = dictionary.Dictionary().create()
tokenizer_mode = tokenizer.Tokenizer.SplitMode.C 

def tokenize(text):
    for m in tokenizer_obj.tokenize(text, tokenizer_mode):
        tokens = " ".join(
            "_".join(
            [m.surface(),
             m.part_of_speech()[0],
             m.dictionary_form()]))
    
        wordlist = [
            m.dictionary_id(),
            m.dictionary_form(),
            m.reading_form()
        ] + list(m.part_of_speech())

    return {'tokens': tokens, 'words': wordlist}