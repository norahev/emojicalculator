import sys
import re

# Function that transforms the input of emojis into numbers. 
def convertString(inp):
    stringi = ""
    for i in range(len(inp)):
        if inp[i].isalpha():
            print("🤷, You must enter a digit, emoji-number from 0-9, 🔟, 💯 or 🎱.")
            sys.exit()
        elif inp[i] == "\U0001F51F": 
            x = 10
            stringi += str(x)
        elif inp[i] == "\U0001F3B1":
            x = 8
            stringi += str(x)
        elif inp[i] == "\u0037":
            x = 7
            stringi += str(x)
        elif inp[i] == "\u0036":
            x = 6
            stringi += str(x)
        elif inp[i] == "\u0035":
            x = 5
            stringi += str(x)
        elif inp[i] == "\u0034":
            x = 4
            stringi += str(x)
        elif inp[i] == "\u0033":
            x = 3
            stringi += str(x)
        elif inp[i] == "\u0032":
            x = 2
            stringi += str(x)
        elif inp[i] == "\u0030":
            x = 0
            stringi += str(x)
        elif inp[i] == "\u0031":
            x = 1
            stringi += str(x)
        elif inp[i] == "\u0038":
            x = 8
            stringi += str(x)
        elif inp[i] == "\u0039":
            x = 9
            stringi += str(x)
        elif inp[i] == "\U0001F4AF":
            x = 100
            stringi += str(x)
        elif inp[i] == "✖" or inp[i] == "x" or inp[i] == "*":
            stringi += "*"
        elif inp[i] == "➕":
            stringi += "+"
        elif inp[i] == "➖":
            stringi += "-"
        elif inp[i] == "➗" or inp[i] == "%":
            stringi += "/"
        elif inp[i].isdigit():
            stringi += inp[i]
    string = stringi.replace("plus", "+").replace("minus", "-").replace("divided by", "/").replace("times", "*").replace(" ", "")
    return string

# Function to transform numbers into emojis.
def convertResult(string):
    try:
        result = string.replace("100", "💯").replace("10", "🔟").replace("9", "\u0039").replace("8", "\u0038").replace("7", "\u0037").replace("6", "\u0036").replace("5", "\u0035").replace("4", "\u0034").replace("3", "\u0033").replace("2", "\u0032").replace("1", "\u0031").replace("0", "\u0030")
        return result
    except:
        error = "🤷 ,The result couldn't be converted into emoji(s)."
        print(error)
        sys.exit()

# Funtion that returns the final value, in string format. 
def calculate(st):
    try:
        x = eval(st) 
        return str(x)
    except:
        error = "🤷, An error occured during calculation."
        print(error)
        sys.exit()

# The main function of my program, where everything is connected. 
if __name__ == "__main__":
    s = str(input().strip())
    string = convertString(s)
    resultString = calculate(string)
    emojiresult = convertResult(resultString)
    if emojiresult is None:
        print("🤷, Something went wrong, there is no result.")
        sys.exit()
    print(emojiresult)
# Written by Nora Hevesi. 