#sample file to provide functions without other project modules. This will be provided by other project member later.
from create_quiz import Question, Quiz
from datetime import datetime
from take_quiz import *

#sample store function to use in place of other project member's
def store(stuID, answers):
    pass

#sample retrieve function to use in place of other project member's
def retrieve(quizID, profID):
    # create sample quiz data to be used for testing front end
    sampleStudents = ["sheb12", "dave"]
    quizes = []
    sampleQuiz = Quiz(sampleStudents, 1, "sample quiz", 1, "Brown", datetime.now(), None)
    sampleQuiz2 = Quiz(sampleStudents, 1, "sample quiz", 2, "Brown", datetime.now(), None)
    sampleQ1 = Question(1, "Which of these is a beer?", "a", ["a", "7UP", "Root Beer", "Coor's Light"])
    sampleQ2 = Question(2,"Which of these is not an animal?", "Bigfoot", ["Cat", "Dog", "Squirrel", "Bigfoot"])
    sampleQuiz.addQuestion(sampleQ1)
    sampleQuiz.addQuestion(sampleQ2)
    quizes.append(sampleQuiz)
    quizes.append(sampleQuiz2)
    return quizes

def bring(studentid):
    data = []
    adata = Answers("sheb12", "brown", 1)
    adata1 = Answers("dave", "brown", 1)
    att1 = [(1, "a"), (2, "b")]
    att2 = [(1, "c"), (2, "b")]
    adata.ansAttempts.append(att1)
    adata.ansAttempts.append(att2)
    adata1.ansAttempts.append(att1)
    adata1.ansAttempts.append(att2)
    data.append(adata)
    data.append(adata1)

    return data
