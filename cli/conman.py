import os as ops


def clearcon(): ops.system("cls") if ops.name == "nt" else ops.system("clear")


def conpad(func):
    def wrapper(*args, **kwargs):
        print("\n")
        func(*args, **kwargs)
        print("\n")
    return wrapper
