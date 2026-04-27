class AgeException(Exception):
    def __init__(self,errmess):
        super().__init__(errmess)   #super is used because of Exception builtin class
