import pyperclip
from subprocess import call

while True:
    try:
        first_entry = pyperclip.paste()
            
        with open('clipboard_history.txt', 'r') as fin:
            copied = fin.read().splitlines(True)
            copied = [i.strip('[\n]') for i in copied]

        if first_entry not in copied:
            with open('clipboard_history.txt', 'a') as fout:
                fout.writelines(first_entry + '\n')
    except KeyboardInterrupt:
        print("\n"+ "-"*37 + "\n" "| You stopped the clipboard grabber |" + "\n" + "-"*37 + "\n")
        break