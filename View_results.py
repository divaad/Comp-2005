from persist import store, retrieve, bring


class Instructor_view:
    """This class diplays the result to a unique quiz taken
       by a particular student
    """

    def __init__(self, instructorid):
        """
        creates a new result object based on the instructorid
        """
        self.intructorid = instructorid
        self.quizdata = retrieve("quiz1", "instructorid")
        self.studata = bring("studentid")

    def getQuizData(self, quizid):
        """Retrieve the quiz data and store it in a dictionary

        Keyword arguments:

        quizid - quiz identification number

        """
        if not isinstance(quizid, int):
            raise TypeError
        data = {}
        d = self.quizdata
        for quiz in d:
            if quizid == quiz.quizID:
                std = {}
                for student in quiz.students:
                    std[student] = self.getStudentsData(quizid, student)                  
                data[quiz.quizID] = std

        return data

    def getStudentsData(self, quizid, studentid):
        """Retrieve the student data from persist and stores it in a dictionary

        Keyword arguments:

        quizid - quiz identification number
        studentid - student name

        """
        if not isinstance(quizid, int):
            raise TypeError
        data = {}
        for quiz in self.studata:
            if quizid == quiz.quizID and studentid == quiz.stuID:
                data[quizid] = quiz.ansAttempts
        return data

    def ClassResults(self, quizid):
        """The fuction gets the best score for each quiz for each student

        Keyword arguments:

        quizid - quiz identification number
        """
        global a
        if not isinstance(quizid, int):
            raise TypeError
        data = self.getQuizData(quizid)
        result = []
        students =[]
        for stu in self.studata:
            students.append(stu.stuID)
        for k, value in data.items():
            if quizid == k:
                for a, jar in value.items():
                    for b, can in jar.items():
                        if b == quizid:
                            a = can
        i = 0
        for h in a:
            result.append((self.getScore(quizid, students[i]), students[i]))
            i = + 1
        return result

    def getScore(self, quizid, studentid):
        """Grade the quiz taken by a student

        Keyword arguments:

        quizid - quiz identification number
        studentid - student name

        """
        if not isinstance(quizid, int):
            raise TypeError
        if not isinstance(studentid, str):
            raise TypeError
        score = 0
        r = []
        ans = []
        sc = []
        for b in self.quizdata:
            for stu in self.studata:
                if stu.stuID == studentid and stu.quizID == quizid and b.quizID == stu.quizID:
                    for item in stu.ansAttempts:
                        r.append(item)
        i = 0
        for item in r:
            ans.append(item[i][1])
            i = + 1
        for a in self.quizdata:
            for c in a.questions:
                if c.correctAnswer in ans:
                    score = + a.weight
            sc.append(score)

        return score

    def participate(self, quizid):
        """Return the class participation for a particular quiz

        Keyword arguments:

        quizid - quiz identification number
        """
        if not isinstance(quizid, int):
            raise TypeError
        participants = 0
        for quiz in self.quizdata:
            if quizid == quiz.quizID:
                participants = len(quiz.students)

        return participants

    def average(self, quizid):
        """Return the class average for a particular quizid

        Keyword arguments:

        quizid - quiz identification number
        """
        data = self.ClassResults(quizid)
        l = []
        av = 0
        for i in data:
            l.append(i[0])
        av = sum(l) / len(l)

        return av

    def histogram(self, class_results):
        """Return an histogram of the class results

        Keyword arguments:

        class_results - list of scores for the class
        """
        pass

    def showresults(self, quizid):
        """Return the correct answers  and score for a particular quiz

        Keyword arguments:

        quizid - quiz identification number
        """
        if not isinstance(quizid, int):
            raise TypeError
        students = []
        results = {}
        for stu in self.studata:
            students.append(stu.stuID)
        for stu in self.studata:
            if stu.stuID in students:
                results[stu.stuID] = stu.ansAttempts
        return results

    def quizattempts(self, quizid, studentid):
        """Return the number of attempts for a particular quiz and a particular
        student

        Keyword arguments:

        quizid - quiz identification number
        userid - user identification number
        """
        if not isinstance(quizid, int):
            raise TypeError
        if not isinstance(studentid, str):
            raise TypeError
        at = 0
        students = []
        for stu in self.studata:
            students.append(stu.stuID)
        for stu in self.studata:
            if stu.stuID in students and stu.stuID == studentid and stu.quizID == quizid:
                at = + len(stu.ansAttempts)

        return at 

class Student_view:
    """
    This class diplays the results for students to view for all the quizzes
    taken
    """
    def __init__(self, studentid):
        """Create a new result object for a particular quiz

        Keyword arguments:

        studentid - student name

        """
        self.quizdata = retrieve("quiz1","instructorid")
        self.studentid = studentid
        self.studata = bring("studentid")

    def quizsummary(self, quizid, profID):
        """ Return the results for a particular quiz

        Keyword arguments:

        quizid - quiz identification number

        profid - prof name

        """
        if not isinstance(quizid, int):
            raise TypeError
        if not isinstance(profID, str):
            raise TypeError
        global a
        results = {}
        abj = Instructor_view(profID)
        for stu in self.studata:
            if stu.quizID == quizid and stu.profID == profID:
                for i in range(len(stu.ansAttempts)):
                    results[stu.profID] = (stu.quizID, stu.ansAttempts[i], abj.getScore(quizid, self.studentid))
        return results

    def attemptsummary(self, profid, quizid, atnum, qID):
        """ Return the results for an attempt for a particular quiz

        Keyword arguments:

        quizid - quiz identification number

        profid - prof name

        atnum - attempt number

        qid - question number

        """
        global a 
        global b
        global c
        at = []
        att = {}
        abj = Instructor_view(profid)
        for stu in self.studata:
            if stu.quizID == quizid and stu.profID == profid:
                a = stu.ansAttempts
        for i in a:
            at.append(i)
        score = 0
        for i in abj.quizdata:
            if i.profID == profid:
                c = i.weight
            for ques in i.questions:
                print(ques)
                #if ques.correctAnswer == at[atnum][1] and ques.qID == at[atnum][0]:
                score = c + score
                att[atnum] = (ques.question, ques.correctAnswer, score)   
            print("s",att)
        return att
        


