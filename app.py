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
    t0 = time()
    while game:
        word = choice(words)
        dt = time() - t0
        symbols += len(word)
        print("-"*10)
        print(word)
        print("-"*10)
        print(f"score:   {score}  speed:   {symbols/dt * 60 } s/min")
        answer = input().lower().strip()
        if answer == word:
            beep("ok")
            score += 1
        else:
            beep("wrong")
            score -= 1
        system('clear')
