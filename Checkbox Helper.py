from Npp import *
import string
import sys

# A simple helper script for using ASCII todo lists
# The basic implementation knows 3 different states
# [ ] To Do
# [x] Done
# [o] Currently not possible to do
#
# The script is able to toggle between this states. If 
# you want only two states or if you want more states
# just edit the checkboxes string list.
#
# If a line doesn't contain a checkbox the script
# just inserts one at the current position.

def nextElem(arr, curPos):
	if (curPos + 1 < len(arr)):
		return arr[curPos + 1]
	else:
		return arr[0]

checkboxes = ['[ ]', '[x]', '[o]']
curLine = editor.getCurLine()
curPos = editor.getCurrentPos()
curLineNr = editor.lineFromPosition(curPos)
strippedLine = curLine.lstrip()
insertChkBx = True

for i in range(len(checkboxes)):
	elem = checkboxes[i]
	if strippedLine.startswith(elem):
		curLine = curLine.replace(elem, nextElem(checkboxes, i), 1).rstrip('\n')
		editor.replaceWholeLine(curLineNr, curLine)
		editor.gotoPos(curPos)
		insertChkBx = False
		break
		

if(insertChkBx):
	editor.addText('[ ] ')