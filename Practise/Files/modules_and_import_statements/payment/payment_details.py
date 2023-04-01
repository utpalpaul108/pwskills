import os, sys
from os.path import abspath, dirname

sys.path.insert(0, abspath(os.path.join(dirname(__file__), '..')))
from course import course_details


def payment():
    print("This is the payment details file")


course_details.course()
