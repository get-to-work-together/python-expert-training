"""Our main entry point to the project"""
import os
from src import helper
from src import math


def main():
    print('We starten out project.')
    helper.helper()
    print(math.pi)


print(__name__)
print(os.getcwd())

if __name__ == "__main__":
    main()
