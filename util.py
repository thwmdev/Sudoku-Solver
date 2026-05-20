import customtkinter as ctk

def get_grid(cells):

    grid = []

    for r in range(9):

        row = []

        for c in range(9):

            val = cells[r][c].get().strip()

            if val == "":
                row.append(0)

            else:

                if not val.isdigit() or not (1 <= int(val) <= 9):

                    raise ValueError(
                        f"Giá trị '{val}' không hợp lệ tại hàng {r+1}, cột {c+1}"
                    )

                row.append(int(val))

        grid.append(row)

    return grid


def display(
        grid,
        cells,
        prefilled,
        solved_color,
        white_color
):

    for r in range(9):
        for c in range(9):

            cells[r][c].delete(0, ctk.END)

            cells[r][c].insert(
                0,
                str(grid[r][c])
            )

            if not prefilled[r][c]:

                cells[r][c].configure(
                    text_color=solved_color
                )

            else:

                cells[r][c].configure(
                    text_color=white_color
                )