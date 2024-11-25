import os
os.system('clear')

def draw_heart():
    heart = [
        "  ****     ****  ",
        " ******   ****** ",
        "******** ********",
        "*****************",
        " ****************",
        "  *************  ",
        "   ***********   ",
        "    *********    ",
        "     *******     ",
        "      *****      ",
        "       ***       ",
        "        *        "
    ]
    
    for line in heart:
        print(line.center(40))  

def draw_message():
    message = "EU TE AMO"
    print("\n" + message.center(40, " "))

def main():
    draw_heart()
    draw_message()

if __name__ == "__main__":
    main()
