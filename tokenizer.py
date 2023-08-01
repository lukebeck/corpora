import sys

from sudachipy import tokenizer
from sudachipy import dictionary


tokenizer_obj = dictionary.Dictionary().create()
tokenizer_mode = tokenizer.Tokenizer.SplitMode.C


def tokenize(content):
    def _tokenize(input):
        return tokenizer_obj.tokenize(input, tokenizer_mode)

    if len(content) > 10000:  # Actual sudachipy tokenizer cutoff is 49149 bytes
        return [token for span in content.split("\n") for token in _tokenize(span)]
    else:
        return _tokenize(content)


def tag(tokens):
    tag = lambda token: "_".join(
        [token.surface(), token.part_of_speech()[0], token.dictionary_form()]
    )

    return " ".join([tag(token) for token in tokens])


def build_word_list(tokens, word_list, word_index):
    for t in tokens:
        index_key = "-".join([t.dictionary_form()] + list(t.part_of_speech()))
        if index_key not in word_index:
            entry = [index_key, t.dictionary_form(), t.reading_form()] + list(
                t.part_of_speech()
            )
            word_index[index_key] = True
            word_list.append(entry)

    return word_list, word_index
