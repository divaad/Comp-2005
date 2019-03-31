import unittest
from View_results import Instructor_view, Student_view
from persist import retrieve, store, bring



sample = bring("dave")
sample1 = retrieve("Dave","brown")
global data
data = Instructor_view("brown")
sata = Student_view("dave")
class TestViewResults(unittest.TestCase):
    
    
    def test_ClassResults_success(self):
        self.assertIsInstance(data.ClassResults(1), list)
    
    def test_ClassResults_fail(self):
        with self.assertRaises(TypeError):
            data.ClassResults("e")

    def test_average_success(self):
        self.assertIsInstance(data.average(1), float)

    def test_average_fail(self):
        with self.assertRaises(TypeError):
            data.average("e")
        
    def test_participate_success(self):
        self.assertIsInstance(data.participate(1), int)
    
    def test_participate_fail(self):
        with self.assertRaises(TypeError):
            data.participate("e")


    def test_showresults_success(self):
        self.assertIsInstance(data.showresults(1), dict)

    def test_showresults_fail(self):
        with self.assertRaises(TypeError):
            data.showresults("e")

    def test_quizattempts_success(self):
        self.assertIsInstance(data.quizattempts(1,"dave"), int)

    def test_quizattempts_fail(self):
        with self.assertRaises(TypeError):
            data.quizattempts("e", "e")
    
    def test_quizsummary_success(self):
        self.assertIsInstance(sata.quizsummary(1, " brown"), dict)
    
    def test_quizsummary_fail(self):
        with self.assertRaises(TypeError):
            sata.quizsummary(1,2)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)





