import turtle

screen = turtle.Screen()

screen.bgcolor("black")

screen.title("Neon Mandela ")

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()
colors = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", 
    "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", 
    "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", 
    "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", 
    "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", 
    "darksalmon", "darkseagreen","darkslateblue", "darkslategray", 
    "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", 
    "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", 
    "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", 
    "grey", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", 
    "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", 
    "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", 
    "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", 
    "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", 
    "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", 
    "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", 
    "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", 
    "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", 
    "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", 
    "pink", "plum", "powderblue", "purple", "red", "rosybrown", 
    "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", 
    "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", 
    "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", 
    "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]

for i in range(148):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 2)
    board.right(91)

board.penup()
board.goto(0,-60)
board.setheading(90)
board.pendown()
board.color("gold","yellow")
board.begin_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()

board.penup()
board.goto(0,0)
board.pendown()
petal_colors = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", 
    "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", 
    "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", 
    "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", 
    "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", 
    "darksalmon", "darkseagreen","darkslateblue", "darkslategray", 
    "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", 
    "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", 
    "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", 
    "grey", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", 
    "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", 
    "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", 
    "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", 
    "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", 
    "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", 
    "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", 
    "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", 
    "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", 
    "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", 
    "pink", "plum", "powderblue", "purple", "red", "rosybrown", 
    "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", 
    "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", 
    "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", 
    "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]
for i in range(36):
    board.color(petal_colors[i % len(petal_colors)],
                petal_colors[(i + 2) % len(petal_colors)])
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)
turtle.done()