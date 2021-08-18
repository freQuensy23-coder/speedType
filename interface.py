import termplot

def do_nothing(*args, **kwargs):
    pass

class ConsoleInterface:
    def __init__(self):
        self._status = "start"
        self.pre_text = "Input this word"
        self._params = {}

    def __iter__(self):
        return self
            
    def __next__(self):
        if self._status == "start":
            self._status = "work"
            print("Press ENTER to start writing ....")
            return "Press ENTER to start writing ...."
        if self._status == "work":
            res = ""
            res += self._params["pre_text"] + "\n" # TODO Add color
            res += "-"*30 + "\n"
            res += self._params['word'] + "\n"
            res += "-"*30 + "\n"  # TODO Add current spead of typing
            res += f"score:   {self._params['score']}  speed:   {self._params['speed']}  s/min \n" # TODO Add formating, fixed number of symbols after coma
            print(res)
            print(self._params['statistics'])
            termplot.plot(self._params['statistics'])
            return res

    def update_params(self, create = False, **kwargs):
        for param_name in kwargs.keys():
            if param_name in self._params.keys():
                self._params[param_name] = kwargs[param_name]
            else:
                if create:
                    self._params[param_name] = kwargs[param_name]    
                else:
                    raise KeyError(f"No such param {param_name}")
                            
                
