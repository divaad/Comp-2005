#from persist import store, retrieve, bring
from datetime import datetime

"""
take_quiz - provides a module which implements the functions to access
quiz and quiz attempts by a Student, and the answers to the questions
that they provide. Works in use with quizzes created with questions
created by a professor, and with a grading module that will check correct
answers.
"""

class Answers():
    """
    Provides object with attributes containing information for quiz and answers

    attributes:
        ansAttempts - list of lists
        attemptSubmitted - list
        stuID - string
        profID - string
        quizID - string
        quiz - Quiz object
        currentAttempt - int
    """
    def __init__(self, stuID, profID, quizID):
        self.ansAttempts = []
        self.attemptSubmitted = []
        self.stuID = stuID
        self.profID = profID
        self.quizID = quizID
        self.currentAttempt = None
