#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n % 2 == 0]
    pass
print(return_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def make_exclamation(sentence_list):
    return [word + "!" for word in sentence_list]
    pass
print(make_exclamation(["hello", "world"]))