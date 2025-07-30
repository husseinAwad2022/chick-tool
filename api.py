from difftool import DiffTool
from view import View

class API:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.diff_tool = DiffTool()
        self.view = View()

    def run(self):
        text1 = self._read_file(self.file1)
        text2 = self._read_file(self.file2)
        results = self.diff_tool.compare(text1, text2)
        self.view.show(self.file1, self.file2, results)

    def _read_file(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()
