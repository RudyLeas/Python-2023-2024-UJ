def draw_rectangle(height, width):
    rectangle = ""

    for i in range(height):
        rectangle += "+"
        for j in range(width):
            rectangle += "---+"
        rectangle += "\n"
        rectangle += "|"+"   |"*width
        rectangle += "\n"

    rectangle += "+" + "---+" * width + "\n"

    print(rectangle)


# example use
height = 5
width = 6
draw_rectangle(height, width)
