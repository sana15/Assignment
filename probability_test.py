import unittest
from main import GraduationCeremony


class TestGraduationCeremony(unittest.TestCase):
    '''Test class for TestGraduationCeremony'''
    def test_attendance_probability(self):
        ''' Test the calculate_attendance method'''
        result = GraduationCeremony()
        self.assertEqual(result.attendance_probability(10), "372/773")
        self.assertEqual(result.attendance_probability(5), "14/29")
        
        
if __name__ == '__main__':
    unittest.main()






