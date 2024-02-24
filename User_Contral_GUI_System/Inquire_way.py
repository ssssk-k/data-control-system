import logging
from tkinter import filedialog
logging.basicConfig(level=logging.DEBUG)
logging.disable()

'''class CompareFile:
    resultMap = dict()

    def __init__(self, p1, p2):
        logging.info('program start')
        self.resultMap = dict()
        path1, path2 = p1, p2
        oldLines = self.readFile(path1)
        newLines = self.readFile(path2)

        total = 0
        self.compare(oldLines, newLines, total)

        print('对比结果展示：')
        for changeType in self.resultMap.keys():
            if 'add' in changeType:
                logging.debug('get in add')
                addLines = self.resultMap[changeType]
                for linesNum in addLines.keys():
                    print('新文本中新增了第' + str(linesNum) + '行，内容为：' + addLines[linesNum])

            if 'delete' in changeType:
                logging.debug('get in delete')
                delLines = self.resultMap[changeType]
                for linesNum in delLines.keys():
                    print('旧文本中删除了第' + str(linesNum) + '行，内容为：' + delLines[linesNum])

            if 'update' in changeType:
                logging.debug('get in updates')
                updateLines = self.resultMap[changeType]
                logging.info('updateLines=' + str(updateLines))
                for linesNum in updateLines.keys():
                    print('旧文本中的第' + str(linesNum) + '行，内容为：' + oldLines[
                        int(linesNum)] + '被修改为新文本中的第' + \
                          str(updateLines[linesNum]) + '行，内容为：' + newLines[int(updateLines[linesNum])])

    def compare(self, oldLines, newLines, total):
        breakPoint = self.getBreakPoint(oldLines, newLines)
        if breakPoint:
            oldStart = int(breakPoint['oldLinesBreakStart'])
            newStart = int(breakPoint['newLinesBreakStart'])
            oldLeftLines, newLeftLines = dict(), dict()

            for oldLinesNum in oldLines.keys():
                if oldLinesNum >= oldStart:
                    oldLeftLines[oldLinesNum] = oldLines[oldLinesNum]
            for newLinesNum in newLines.keys():
                if newLinesNum >= newStart:
                    newLeftLines[newLinesNum] = newLines[newLinesNum]

            newLinesStart = 0

            reConnPoint = dict()
            reConnPoint = self.getConn(oldLeftLines, newLeftLines, newLinesStart, reConnPoint)
            if 'oldLinesConnPoint' in reConnPoint.keys():  # point 1
                oldEnd = int(reConnPoint['oldLinesConnPoint'])
                newEnd = int(reConnPoint['newLinesConnPoint'])
                self.analType(newStart, newEnd, oldStart, oldEnd, newLines, oldLines, total)

                nextOldLines, nextNewLines = dict(), dict()
                for oldLinseNum in oldLines.keys():
                    if oldLinseNum >= oldEnd:
                        nextOldLines[oldLinseNum] = oldLines[oldLinseNum]

                for newLinesNum in newLines.keys():
                    if newLinesNum >= newEnd:
                        nextNewLines[newLinesNum] = newLines[newLinesNum]
                total += 1
                self.compare(nextOldLines, nextNewLines, total)
            else:
                oldLineNums = list(oldLines.keys())
                oldLineNums.sort()
                oldEnd = oldLineNums[-1] + 1

                newLineNums = list(newLines.keys())
                newLineNums.sort()
                newEnd = newLineNums[-1] + 1
                self.analType(newStart, newEnd, oldStart, oldEnd, newLines, oldLines, total)

    def analType(self, newStart: int, newEnd: int, oldStart: int, oldEnd: int, newLines: dict, oldLines: dict,
                 total: int):
        logging.debug('get in analyType')
        if (oldEnd - oldStart) > (newEnd - newStart) and newEnd == newStart:
            oldLine = dict()
            for i in range(oldStart, oldEnd):
                oldLine[i] = oldLines[i]
            self.resultMap['delete' + str(total)] = oldLine
            logging.debug('resultMap=' + str(self.resultMap))

        if oldEnd - oldStart == newEnd - newStart:
            oldLine, newLine = dict(), dict()
            for i in range(oldStart, oldEnd):
                oldLine[i] = oldLines[i]
            for i in range(newStart, newEnd):
                newLine[i] = newLines[i]

            number = oldEnd - oldStart
            change = self.getUpdateLines(oldLine, newLine, number)
            self.resultMap['update' + str(total)] = change
            logging.debug('resultMap=' + str(self.resultMap))

        if oldEnd == oldStart and oldEnd - oldStart < newEnd - newStart:
            newLine = dict()
            for i in range(newStart, newEnd):
                newLine[i] = newLines[i]
            self.resultMap['add' + str(total)] = newLine
            logging.debug('resultMap=' + str(self.resultMap))

        if oldEnd != oldStart and newEnd != newStart and oldEnd - oldStart < newEnd - newStart:
            number = oldEnd - oldStart
            oldLine, newLine, addLine = dict(), dict(), dict()

            for i in range(oldStart, oldEnd):
                oldLine[i] = oldLines[i]
            for i in range(newStart, newEnd):
                newLine[i] = newLines[i]

            change = self.getUpdateLines(oldLine, newLine, number)
            self.resultMap['update' + str(total)] = change
            for lineNum1 in newLine.keys():
                m = 0
                for lineNum2 in change.keys():
                    if str(lineNum1) == str(change[lineNum2]):
                        m += 1
                if m == 0:
                    logging.debug(
                        'm==0,addLine=' + str(addLine) + ',newLine=' + str(newLine) + ',lineNum1=' + str(lineNum1))
                    addLine[lineNum1] = newLine[lineNum1]
            self.resultMap['add' + str(total)] = addLine
            logging.debug('resultMap=' + str(self.resultMap))

        if oldEnd != oldStart and newEnd != newStart and oldEnd - oldStart > newEnd - newStart:
            number = newEnd - newStart
            oldLine, newLine, addLine = dict(), dict(), dict()

            for i in range(oldStart, oldEnd):
                oldLine[i] = oldLines[i]
            for i in range(newStart, newEnd):
                newLine[i] = newLines[i]

            change = self.getUpdateLines(oldLine, newLine, number)
            self.resultMap['update' + str(total)] = change
            for lineNum1 in oldLine.keys():
                m = 0
                for lineNum2 in change.keys():
                    if str(lineNum1) == str(lineNum2):
                        m += 1
                if m == 0:
                    addLine[lineNum1] = oldLine[lineNum1]
            self.resultMap['delete' + str(total)] = addLine
            logging.debug('resultMap=' + str(self.resultMap))

    def getBreakPoint(self, oldLines, newLines):
        breakPoint = dict()
        oldLineNums = list(oldLines.keys())
        oldLineNums.sort()

        for oldLinesNum in oldLineNums:
            lineOld = oldLines[oldLinesNum]
            newLinesNums = list(newLines.keys())
            newLinesNums.sort()

            for newLinesNum in newLinesNums:
                lineNew = newLines[newLinesNum]
                if lineNew == '':
                    continue
                else:
                    if lineOld != lineNew:
                        breakPoint['oldLinesBreakStart'] = oldLinesNum
                        breakPoint['newLinesBreakStart'] = newLinesNum
                        return breakPoint
                    else:
                        newLines[newLinesNum] = ''
                        break
        return 0

    def getConn(self, oldLeftLines, newLeftLines, newLinesStart, reConnPoint):
        oldLinesNums, newLinesNums = list(oldLeftLines.keys()), list(newLeftLines.keys())
        oldLinesNums.sort();
        newLinesNums.sort()
        newNumMax = int(newLinesNums[-1])
        for oldLinesNum in oldLinesNums:
            lineOld = oldLeftLines[oldLinesNum]
            oldNum = oldLinesNum
            for newLinesNum in newLinesNums:
                newNum = newLinesNum
                if newLeftLines[newNum] == oldLeftLines[oldNum]:
                    reConnPoint['oldLinesConnPoint'] = oldNum
                    reConnPoint['newLinesConnPoint'] = newNum
                    return reConnPoint
        return reConnPoint

    def readFile(self, path: str) -> dict:
        with open(path, 'r', encoding='utf-8') as f:
            txt = f.readlines()
        d = dict()
        for i, e in enumerate(txt):
            d[i] = e.replace('\n', '')
        return d

    def numJewelsInStones(self, J, S):
        J = J.strip();
        S = S.strip()
        Ja = list(J);
        Sa = list(S)
        r = 0
        for i in range(len(Ja)):
            for j in range(len(Sa)):
                if Ja[i] == Sa[j]:
                    r += 1
        return r

    def sortMapByValue(self, map):
        map = sorted(map.items(), key=lambda x: x[1])
        return [i for i, j in map][::-1]

    def getUpdateLines(self, contentOld, contentNew, n):
        resultMap, samChar = dict(), dict()
        for oldNum in contentOld.keys():
            for newNum in contentNew.keys():
                count = self.numJewelsInStones(contentOld[oldNum], contentNew[newNum])
                samChar[str(oldNum) + ':' + str(newNum)] = count
        keys = self.sortMapByValue(samChar)

        for i in range(n):
            lineNumArr = keys[i]
            lineNumA = lineNumArr.split(':')
            resultMap[lineNumA[0]] = lineNumA[1]
        return resultMap


if __name__ == '__main__':
    path1 = filename_input1 = filedialog.askopenfilename()
    path2 = filename_input2 = filedialog.askopenfilename()
    cf = CompareFile(path1, path2)'''


import filecmp
import difflib

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # 使用ndiff函数逐行比较
    diff_lines = difflib.ndiff(lines1, lines2)

    # 输出差异
    for line in diff_lines:
        print(line)




file1 = "C:\\Users\86199\Desktop\\1.txt"
file2 = "C:\\Users\86199\Desktop\\2.txt"

compare_files(file1, file2)
