#sample file just to aid front end without other project modules. This will be provided by other project member later.

#sample class to store data for a quiz for use in front end
class Quiz():
    def __init__(self, students, attempts, quizName, quizID, profID, start, end):
        self.questions = []
        self.students = students
        self.attempts = attempts
        self.quizName = quizName
        self.quizID = quizID
        self.weight = 2
        self.profID = profID
        self.start = start
        self.end = end

    def addQuestion(self, question):
        self.questions.append(question)

#sample class to store data for a question for use in quiz class for front end
class Question():
    def __init__(self, questionID, question, correctAnswer, answers):
        self.qID = questionID
        self.question = question
        self.correctAnswer = correctAnswer
        self.answers = answers

