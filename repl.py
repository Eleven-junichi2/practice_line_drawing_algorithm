from line_drawing_algorithm import display_canvas, draw_line

if __name__ == "__main__":
    while True:
        try:
            width, height = [
                int(num) for num in input("input canvas size: width height>").split()
            ]
        except ValueError:
            print("invalid input format")
            continue
        if width <= 0 or height <= 0:
            print("invalid canvas size")
            continue
        else:
            break
    while True:
        try:
            start_x, start_y = [
                int(num) for num in input("input start point: x y>").split()
            ]
        except ValueError:
            print("invalid input format")
            continue
        if start_y < 0 or height <= start_y or start_x < 0 or width <= start_x:
            print("invalid start point")
            continue
        else:
            break
    while True:
        try:
            end_x, end_y = [int(num) for num in input("input end point: x y>").split()]
        except ValueError:
            print("invalid input format")
            continue
        if end_y < 0 or height <= end_y or end_x < 0 or width <= end_x:
            print("invalid end point")
            continue
        else:
            break
    canvas = [["0" for _ in range(width)] for _ in range(height)]

    draw_line(canvas, start_x, start_y, end_x, end_y, debug_mode=True)

    # print canvas on console
    display_canvas(canvas)
