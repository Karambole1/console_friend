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
        if "нормально" in message.lower() or "хорошо" in message.lower() or "плохо" in message.lower():
            return "уверен, что все будет куда лучше)"
        return "я пока не такой умный, чтобы отвечать на такие сообщения"