# 参考資料:https://www.kushiro-ct.ac.jp/yanagawa/cg/03/indend_x.html
# https://fusstart_y.web.fc2.com/algo/algo1-1.htm


def draw_line(
    canvas: list[list[int]],
    start_x,
    start_y,
    end_x,
    end_y,
    brush="1",
    debug_mode=False,
):
    dy = end_y - start_y
    dx = end_x - start_x
    if debug_mode:
        print(
            f"start: ({start_x}, {start_y}) end: ({end_x}, {end_y}) dy: {dy} dx: {dx}"
        )
    if 0 == dx:
        for y in range(start_y, end_y + 1):
            if debug_mode:
                print(f"draw at y={y}")
            x = start_x
            canvas[y][x] = brush
    elif 0 == dy:
        for x in range(start_x, end_x + 1):
            if debug_mode:
                print(f"draw at x={x}")
            y = start_y
            canvas[y][x] = brush
    else:
        m = dy / dx
        print(f"dy/dx: {m}")
        if 0 < abs(m) <= 1:
            (
                start_x,
                end_x,
            ) = sorted((start_x, end_x))
            print(f"after sort: start_x={start_x} end_x={end_x}")
            for x in range(start_x, end_x + 1):
                if debug_mode:
                    print(f"draw at x={x}")
                y = round(m * x)
                if debug_mode:
                    print(f"draw at y={y}")
                canvas[y][x] = brush
        elif 1 < abs(m):
            start_y, end_y = sorted((start_y, end_y))
            print(f"after sort: start_y={start_y} end_y={end_y}")
            for y in range(start_y, end_y + 1, -1 if m < 0 else 1):
                if debug_mode:
                    print(f"draw at y={y}")
                x = round(y / m)
                if debug_mode:
                    print(f"draw at x={x}")
                canvas[y][x] = brush


def display_canvas(canvas: list[list[int]]):
    for row in canvas:
        print(f"{''.join(row)}")
