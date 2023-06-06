#!/usr/bin/python3
"""
Module contain text_indentation function 
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each
    occurrence of '.', '?', and ':' characters.

    Args:
        text: String input.


    Exception Error:
        TypeError: If text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    sentence = text[:]   

    for j in ".?:":
        phrase = sentence.split(j)
        sentence = ""
        for i in phrase:
            # Remove leading and trailing spaces from each sentence
            i = i.strip(" ")
            sentence = i + j if sentence is "" else sentence + "\n\n" + i + j

    print(sentence[:-3], end="")
