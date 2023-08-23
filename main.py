# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from app import tasker
# from app.settings import settings
# from pony.orm import *

# db = Database(**settings['sqlite'])
# db.generate_mapping(create_tables=True)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    tasker.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    print_hi('PyCharm')

