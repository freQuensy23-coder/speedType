from dict_loader import FileDictLoader as DictLoader
from random import choice 
from os import system
from time import time
def beep(sound="ok"):
    pass


if __name__ == "__main__":
    words = list(DictLoader("word_rus.txt"))
    score = 0
    symbols = 0
    game = True
    pre_text = "Input word"
    t0 = time()
    while game:
        word = choice(words)
        dt = time() - t0
        symbols += len(word)
        print(pre_text) # TODO Add color
        print("-"*30)
        print(word)
        print("-"*30)
        print(f"score:   {score}  speed:   {symbols/dt * 60} s/min") # TODO Add formating, fixed number of symbols after coma
        answer = input().lower().strip()
        if answer == word.lower():
            beep("ok")
            score += 1
            pre_text = "Ok"
        else:
            beep("wrong")
            score -= 1
            pre_text = "Wrong"
        system('clear')
