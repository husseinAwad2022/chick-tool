import argparse
import unittest

from api import API
def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('file1', help='First file path')
        parser.add_argument('file2', help='Second file path')
        args = parser.parse_args()

        api = API(args.file1, args.file2)
        api.run()
if __name__ == '__main__':
    main()
    unittest.main()