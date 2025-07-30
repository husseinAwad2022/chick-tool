import unittest
from api import API

class UnitTest(unittest.TestCase):

    def setUp(self):
        self.api = API('file1.txt', 'file2.txt')

    def test_compare(self):
        print("\n************************************************************************************************")
        print("I made two tests, the first for the compare method and the second for the read_file method")
        print("************************************************************************************************")
        text1 = 'Jerusalem is the eternal capital of Palestine'
        text2 = 'Jerusalem is the beating heart of Palestine'
        result = self.api.diff_tool.compare(text1, text2)
        expected = [['  Jerusalem', '  is', '  the', '- eternal', '- capital', '+ beating', '+ heart', '  of', '  Palestine']]
        try:
            self.assertEqual(result, expected)
            print("\n\033[92mThe first test 1 (test_compare) passed and the result is equal to the expected result\033[0m")
        except AssertionError:
            print("\n\033[91mThe first test 1 (test_compare) failed and the result is not equal to the expected result:\033[0m")
            for i in range(len(result)):
                for j in range(len(result[i])):
                    if result[i][j] != expected[i][j]:
                        print("\033[33mExpected: \033[0m"+"\033[91m{}\033[0m".format(expected[i][j]))
                        print("\033[34mResult: \033[0m"+"\033[91m{}\033[0m".format(result[i][j]))
                    else:
                        print(result[i][j])
#-------------------------------------------------------------------------------------------------------------------------------
        result = self.api.diff_tool.compare(text1, text2)
        expected = [['  Jerusalem', '  is', '  the', '+ eternal', '- capital', '+ beating', '+ heart', '  of', '  Palestine']]
        try:
            self.assertEqual(result, expected)
            print("\n\033[92mThe first test 2 (test_compare) passed and the result is equal to the expected result\033[0m")
        except AssertionError:
            print("\n\033[91mThe first test 2 (test_compare) failed and the result is not equal to the expected result:\033[0m")
            for i in range(len(result)):
                for j in range(len(result[i])):
                    if result[i][j] != expected[i][j]:
                        print("\033[33mExpected: \033[0m"+"\033[91m{}\033[0m".format(expected[i][j]))
                        print("\033[34mResult: \033[0m"+"\033[91m{}\033[0m".format(result[i][j]))
                    else:
                        print(result[i][j])
#-------------------------------------------------------------------------------------------------------------------------------
    def test_read_file(self):

        file_path = 'file1.txt'
        expected = '''The sun was shining brightly in the clear blue sky, casting a warm glow over
the bustling city. People were hurrying to work, schools, and shops, while
the sounds of honking cars and chatting voices filled the air. Despite the
fast pace of life in the city, there was a sense of community and connection 
among its residents, who looked out for one another and came together to
celebrate their achievements and milestones. Whether it was a community
festival or a simple gathering with friends and family, there was always a
reason to come together and enjoy life in the city.'''
        try:
            result = self.api._read_file(file_path)
            self.assertEqual(result, expected)
            print("\n\033[92mThe second test 1 (test_read_file) passed and the result is equal to the expected result\033[92m")
        except AssertionError:
            print("\n\033[91mThe second test 1 (test_read_file) failed and the result is not equal to the expected result:\033[0m")
            words1=result.split(" ")
            words2=expected.split(" ")
            for i, (c1, c2) in enumerate(zip(words1, words2)):
                
                if c1 != c2:
                    print("\033[33mExpected:\033[0m"+"\033[91m {}\033[0m".format(c2), end=" ")
                    print("\033[34mResult:\033[0m"+"\033[91m {}\033[0m".format(c1), end=" ")
                else:
                    print(c1, end=" ")
#-------------------------------------------------------------------------------------------------------------------------------
        file_path = 'file1.txt'
        expected = '''The sun was shiningu brightly in the clear blue sky, casting a warm glow over
the bustling city. People were hurrying to work, schools, and shops, while
the sounds of honking cars ande chatting voices filled the air. Despite the
fast pace of life in the city, there +was a sense of community and connection 
among its residents, who looked out for one another and came together to
celebrate their achievements^ and milestones. Whether it was a community
festivale or a simples gathering with friends and family, there was always a
reason to come together and enjoy life in the city.'''
        try:
            result_f = self.api._read_file(file_path)
            self.assertEqual(result_f, expected)
            print("\n\033[92mThe second test 2 (test_read_file) succeeded\033[92m")
        except AssertionError:
            print("\n\033[91mThe second test 1 (test_read_file) failed and the result is not equal to the expected result:\033[0m")
            words1=result.split(" ")
            words2=expected.split(" ")
            for i, (c1, c2) in enumerate(zip(words1, words2)):
                
                if c1 != c2:
                    print("\033[33mExpected:\033[0m"+"\033[91m {}\033[0m".format(c2), end=" ")
                    print("\033[34mResult:\033[0m"+"\033[91m {}\033[0m".format(c1), end=" ")
                else:
                    print(c1, end=" ")
            print("\n")
#-------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()