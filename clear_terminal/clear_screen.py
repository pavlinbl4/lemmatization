# i want to clear terminal after print something before new input
import os


def clear_term():
    print("print something")
    data = input("print something new\n")
    os.system('clear')
    print(data)


if __name__ == '__main__':
    clear_term()
