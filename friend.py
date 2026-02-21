class ConsoleFriend:
    def __init__(self):
        self.name = None

    @staticmethod
    def greet():
        return "я твой консольный друг, привет)"

    def set_name(self, name):
        self.name = name

    def respond(self, message):
        if "как дела" in message.lower():
            return "хорошо, спасибо, что спросил"
        if "как прошел день" in message.lower():
            return f"да как обычно, {self.name}, ждал пока ты мне напишешь и захочешь узнать как прошел мой день, как прошел твой?"
        return "я пока не такой умный, чтобы отвечать на такие сообщения"