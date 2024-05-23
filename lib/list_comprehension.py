#!/usr/bin/env python3

def return_evens(num_list):
    even_no = [ i for i in num_list if i % 2 == 0 ]
    return even_no

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
