import json
from tkinter import *
import tkinter.messagebox
import os
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("dictionary_data.json"))


def know_meaning(word=" "):

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = tkinter.messagebox.askquestion("Do you mean %s instead? " % get_close_matches(word, data.keys())[0])
        if yn in ("y", "Y", "yes", "Yes"):
            return data[get_close_matches(word, data.keys())[0]]
        elif yn in ("n", "N", "No", "no"):
            return "Try Again!"
    else:
        return "Word does not exist."


#print(know_meaning(word="rain"))
