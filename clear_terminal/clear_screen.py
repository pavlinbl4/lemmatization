# i want to ckear termonal after print something befor new input
import os


def clear_term():
    print("print someting")
    data = input("print something new\n")
    os.system('clear')
    print(data)


if __name__ == '__main__':
    clear_term()
