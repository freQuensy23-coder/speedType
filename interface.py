def do_nothing(*args, **kwargs):
    pass

class ConsoleInterface:
    def __init__(self):
        self.status = "start"
        self.action = do_nothing
        self.word = None
        self.pre_text = "Input this word"
        self.params = {}
        
    def __iter__(self):
        if status == "start"
            status = "work"
            self.action = input
            return "Press ENTER to start writing ...."
        if status = "work":
            print(self.params["pre_text"]) # TODO Add color
            print("-"*30)
            print(self.word)
            print("-"*30)  # TODO Add current spead of typing
            print(f"score:   {self.params['score']}  speed:   {self.params['speed']}  s/min") # TODO Add formating, fixed number of symbols after coma
                            
    
