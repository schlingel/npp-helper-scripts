import time

# Inserts the current time and date in european
# format.
#
# Use this if you want to get the same result as
# the plain windows notepad when you hit F5

editor.addText(time.strftime('%H:%M %d.%m.%Y'))