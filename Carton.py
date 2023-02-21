import random


class Carton:

    def __init__(self, maxlines, maxvals, maxval):
        self.maxlines = maxlines
        self.maxvals = maxvals
        self.maxval = maxval
        self.cartoon = []
        self.generate_cartoon(0)
        self.winlines = []

    def markNumber(self, number):
        for i in range(len(self.cartoon)):
            for j in range(len(self.cartoon[i])):
                if self.get_cartoon_numb(i, j) == number:
                    self.set_cartoon_numb_success(i, j)

    def hasLine(self):
        nline = 0
        hasLine = False

        while nline < len(self.cartoon) and not hasLine:
            isFullLine = True
            isAlreadyLine = False

            # Line already called
            for i in range(len(self.winlines)):
                if self.winlines[i] == nline:
                    isAlreadyLine = True

            # Check we have line
            for i in range(len(self.cartoon[nline])):
                if not self.get_cartoon_numb_issuccess(nline, i):
                    isFullLine = False

            if not isAlreadyLine and isFullLine:
                print("Line! {}".format(nline))
                self.winlines.append(nline)
                hasLine = True

            nline = nline + 1

        return hasLine

    def hasBingo(self):
        for i in range(len(self.cartoon)):
            for j in range(len(self.cartoon[i])):
                if not self.get_cartoon_numb_issuccess(i, j):
                    return False
        return True

    def generate_cartoon(self, nlines):
        if nlines >= self.maxlines:
            return self.cartoon
        self.cartoon.append(self.get_unique_line())
        return self.generate_cartoon(nlines + 1)

    def get_unique_line(self):
        unique = False
        line = []
        while not unique:
            line = self.generate_line([], 0)
            duplicated = False
            for i in range(len(line)):
                if self.isNumberRepeated(line[i][0]):
                    duplicated = True
            unique = not duplicated
        return line

    def isNumberRepeated(self, val):
        for i in range(len(self.cartoon)):
            for j in range(len(self.cartoon[i])):
                if self.get_cartoon_numb(i, j) == val:
                    return True
        return False

    def generate_line(self, line, nval):
        if nval >= self.maxvals:
            return line
        line.append(self.get_unique_numb(line))
        return self.generate_line(line, nval + 1)

    def get_unique_numb(self, line):
        unique = False
        while not unique:
            val = [random.randint(1, self.maxval), False]
            duplicate = False
            for i in range(len(line)):
                if val[0] == line[i][0]:
                    duplicate = True
            unique = not duplicate
        return val

    def get_cartoon_numb(self, nline, nval):
        return self.cartoon[nline][nval][0]

    def get_cartoon_numb_issuccess(self, nline, nval):
        return self.cartoon[nline][nval][1]

    def set_cartoon_numb_success(self, nline, nval):
        self.cartoon[nline][nval][1] = True

    def debug_cartoon(self, nlines):
        if nlines >= self.maxlines:
            return
        print(self.cartoon[nlines])
        self.debug_cartoon(nlines + 1)