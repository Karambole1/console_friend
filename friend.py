class ConsoleFriend:
    def __init__(self):
        self.name = None

    @staticmethod
    def greet():
        return "я твой консольный друг, привет)"

    def set_name(self, name):
        self.name = name