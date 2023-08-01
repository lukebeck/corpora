from sudachipy import tokenizer
from sudachipy import dictionary

tokenizer_obj = dictionary.Dictionary().create()
tokenizer_mode = tokenizer.Tokenizer.SplitMode.C


def tokenize(text):
    tokens = [
        " ".join("_".join([m.surface(), m.part_of_speech()[0], m.dictionary_form()]))
        for m in tokenizer_obj.tokenize(text, tokenizer_mode)
    ]

    return "\n".join(tokens)
