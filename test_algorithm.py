from line_drawing_algorithm import display_canvas, draw_line

args_list = [
    ((1, 1), (20, 20)),
    ((20, 20), (1, 1)),
    ((3, 3), (3, 9)),
    ((3, 3), (9, 3)),
    ((1, 1), (10, 20)),
    ((1, 1), (20, 10)),
    ((10, 10), (20, 5)),
    ((20, 5), (10, 10)),
]
for args in args_list:
    canvas = [["0" for _ in range(32)] for _ in range(32)]
    draw_line(canvas, *args[0], *args[1], debug_mode=True)
    display_canvas(canvas)
