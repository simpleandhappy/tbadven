from models.world import World
from controllers.parser import Parser

if __name__ == "__main__":
    print("Welcome to a Generic Text Based Adventure")
    world = World()
    parser = Parser()

    while True:
        user_command = input("> ")
        if user_command == "quit":
            quit()
        words = parser.parse_input(user_command)
        eval(words)
