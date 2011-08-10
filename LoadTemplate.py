from Npp import *
import string
import sys
import os

# A very simple template insertion script. Underneath is directory where the 
# templates should go. Templates must have a '.tmplt' postfix e.g. 'test.tmplt'
# The template insertion script clears the whole file and adds every line from the
# template file.
#
# To include a template just enter the name of the template without its postfix and
# run the script e.g. test.

templateDir = 'C:\\Users\\zombie\\AppData\\Roaming\\Notepad++\\templates\\'
selected = editor.getSelText()
wholePath = os.path.join(templateDir, selected + '.tmplt')

if(os.path.isfile(wholePath)):
	editor.clearAll()
	file = open(wholePath, 'r')
	for line in file:
		editor.addText(line)
else:
	notepad.messageBox('There\'s no template "' + selected + '.tmplt" in ' + templateDir, 'Template not found')

