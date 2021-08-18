from dict_loader import FileDictLoader as DictLoader
from interface import ConsoleInterface
from random import choice 
from os import system
from time import time


def beep(sound="ok"):
    pass

dict_loader = DictLoader("word_rus.txt")

if __name__ == "__main__":
    words = list(dict_loader)

    score = 0
    symbols = 0
    game = True
    word = ""
    pre_text = "Input word"
    t0 = time()
    statistics = []
    interface = ConsoleInterface()
    
    for line in interface:
        answer = input()


        if answer == word.lower():
           beep("ok")
           score += 1
           pre_text = "Ok"
        else:
           beep("wrong")
           score -= 1
           pre_text = "Wrong"

        word = choice(words)
        symbols += len(word)
        dt = time() - t0
        speed = symbols/dt * 60
        statistics.append(speed) #TODO пофиксить действия которые не должны выполняться в начале
        interface.update_params(create=True, score=score, speed=speed, statistics=statistics, pre_text=pre_text, word=word)   
        system('clear')   

