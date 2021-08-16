

class FileDictLoader:
    def __init__(self, file_name, word_filter=None):
        self.file = open(file_name, "r")
        self.filter = word_filter

    def __iter__(self):
        for word in self.file:
            if self.filter:
                if self.filter(word):  
                    yield word.strip()
            else:
                yield word.strip()
                

    def __del__(self):
        self.file.close()
