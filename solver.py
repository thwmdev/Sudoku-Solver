import time

def possible(grid, row, column, num):

    # Kiểm tra hàng
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Kiểm tra cột
    for i in range(9):
        if grid[i][column] == num:
            return False

    # Kiểm tra ô 3x3
    x0 = (row // 3) * 3
    y0 = (column // 3) * 3

    for i in range(3):
        for j in range(3):

            if grid[x0+i][y0+j] == num:
                return False

    return True


def is_board_valid(grid):

    for r in range(9):
        for c in range(9):

            num = grid[r][c]

            if num != 0:

                grid[r][c] = 0

                if not possible(grid, r, c, num):
                    return False

                grid[r][c] = num

    return True


def get_candidates(grid, row, col):

    return [
        num for num in range(1, 10)
        if possible(grid, row, col, num)
    ]


def mrv(grid):

    min_count = 10
    best_cell = None

    for r in range(9):
        for c in range(9):

            if grid[r][c] == 0:

                candidates = get_candidates(grid, r, c)

                if len(candidates) < min_count:

                    min_count = len(candidates)
                    best_cell = (r, c)

    return best_cell


def solve(
        grid,
        cells,
        root,
        delay,
        solved_color
):

    cell = mrv(grid)

    if not cell:
        return True

    row, col = cell

    for num in get_candidates(grid, row, col):

        grid[row][col] = num

        # cập nhật GUI
        cells[row][col].delete(0, "end")
        cells[row][col].insert(0, str(num))

        cells[row][col].configure(
            text_color="#ff9f0a"
        )

        root.update()

        if delay > 0:
            time.sleep(delay)

        # đệ quy
        if solve(
                grid,
                cells,
                root,
                delay,
                solved_color
        ):

            cells[row][col].configure(
                text_color=solved_color
            )

            root.update()

            return True

        # quay lui
        grid[row][col] = 0

        cells[row][col].delete(0, "end")

        root.update()

        if delay > 0:
            time.sleep(delay / 2)

    return False