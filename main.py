import time
from friend import ConsoleFriend

def main():
    friend = ConsoleFriend()
    print(friend.greet())

    name = input("как тебя зовут?\n> ")
    friend.set_name(name)

    while True:
        msg = input("> ")
        if msg.lower() == "выход":
            print("завершаю работу...")
            time.sleep(2)
            break
        print(friend.respond(msg))

if __name__ == "__main__":
    main()