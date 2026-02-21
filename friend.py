class ConsoleFriend:
    def __init__(self):
        self.name = None

    @staticmethod
    def greet():
        return "я твой консольный друг, привет)"

    def set_name(self, name):
        self.name = name

    @staticmethod
    def respond(message):
        msg = message.lower()
        if "как дела" in msg:
            return "хорошо, спасибо, что спросил"
        return "я пока не такой умный, чтобы отвечать на что-то кроме как 'как дела?'"