import difflib

class DiffTool:
    def compare(self, text1, text2):
        result = []
        S1= text1.splitlines()
        S2=text2.splitlines()

        for i, (line1, line2) in enumerate(zip(S1, S2)):
                words1 = line1.split(" ")
                words2 = line2.split(" ")
                d = difflib.Differ()
                diff = list(d.compare(words1, words2))
                result.append(diff)
        return result 
    