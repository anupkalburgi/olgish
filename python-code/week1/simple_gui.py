import turtle
import itertools

def main():
    t: turtle.Turtle = turtle.Turtle()
    screen = t.getscreen()

    cmd_file = open("turtle_cmds")

    for line in cmd_file.readlines():
        text = line.strip()
        cmdList = text.split(",")
        cmd  = cmdList[0]

        if cmd == "goto":
            x = float(cmdList[1])
            y = float(cmdList[2])
            width  = float(cmdList[3])
            color = cmdList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)
        elif cmd == "circle":
            radius = float(cmdList[1])
            width = float(cmdList[2])
            color = cmdList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif cmd == "beginfill":
            color = cmdList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif cmd == "endfill":
            t.end_fill()
        elif cmd == "penup":
            t.penup()
        elif cmd == "pendown":
            t.pendown()
        else:
            print("unknonw command")
    
    cmd_file.close()
    t.ht()
    screen.exitonclick()
    
    print("Prgram complete")            



if __name__ == "__main__":
    main()
