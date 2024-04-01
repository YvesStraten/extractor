#!/usr/bin/env python3

import sys

def main():
    args = sys.argv

    messages = [
        "Welcome to extractor.py \n"
        "Usage: python extractor.py <python file> \n"
        "To display this page, do extractor.py --help \n"
    ]

    if len(args) > 2 or args[1] == "--help":
        for message in messages:
            print(message)

    try:
        commentList = [  ]
        with open(args[1], "r") as file:
            for line in file:
                # Counter to track whether once is in a multiline
                counter = 1

                try:
                    """
                    Split the current line and check whether it
                    is a multiline if it is, and we are currently
                    not in a multiline, loop over the multiline until
                    the end appending to a string which is then appended
                    to the final list
                    """
                    """
                    If it is a single line, exclude it if its a shebang
                    otherwise, append it as a string to the list
                    """

                    splitLine = line.split()

                    isMultiline = splitLine[0] == "\"\"\"" or splitLine[0] == "'''"
                    if isMultiline and counter % 2 != 0:
                        counter +=1

                        while True:
                            currentLine = file.readline().split()

                            if currentLine[0] == "\"\"\"" or currentLine[0] == "'''":
                                break

                            string = ""

                            for item in currentLine:
                                string += item
                                string += " "

                            commentList.append(string)

                    elif line.startswith("#") and len(splitLine[0]) == 1:
                        content = line.split()
                        string = ""
                        content.pop(0)

                        for statement in content:
                            string += statement
                            string += " "

                        commentList.append(string)


                except:
                    pass


        for comment in commentList:
            print(comment)

    except:
        print("File does not exist!")




main()
