import customtkinter as ctk
from tkinter import messagebox
import random

from config import *
from data import SAMPLE_PUZZLES
from solver import *
from util import *

current_speed_idx = 0

def create_gui():

    global current_speed_idx

    root = ctk.CTk()

    root.title("Sudoku Solver")

    root.geometry("520x600")

    root.resizable(False, False)

    # TITLE
    title_label = ctk.CTkLabel(
        root,
        text="SUDOKU",
        font=("Berlin Sans FB Demi", 66, "bold")
    )

    title_label.pack(pady=(30, 5))

    # GRID FRAME
    grid_frame = ctk.CTkFrame(
        root,
        fg_color=BG_FRAME,
        corner_radius=15
    )

    grid_frame.pack(padx=20, pady=2)

    # CELLS
    cells = [[None for _ in range(9)] for _ in range(9)]

    for r in range(9):

        for c in range(9):

            px = (
                4 if c % 3 == 0 and c != 0 else 1,
                1
            )

            py = (
                4 if r % 3 == 0 and r != 0 else 1,
                1
            )

            entry = ctk.CTkEntry(
                grid_frame,
                width=40,
                height=40,
                font=('Helvetica', 18, 'bold'),
                justify='center',
                fg_color=BG_CELL,
                border_width=0,
                text_color=TEXT_WHITE,
                corner_radius=8
            )

            entry.grid(
                row=r,
                column=c,
                padx=px,
                pady=py
            )

            cells[r][c] = entry


    def clear_board():

        for r in range(9):
            for c in range(9):

                cells[r][c].delete(0, ctk.END)

                cells[r][c].configure(
                    text_color=TEXT_WHITE
                )

    def random_fill():

        clear_board()

        puzzle = random.choice(SAMPLE_PUZZLES)

        for r in range(9):
            for c in range(9):

                if puzzle[r][c] != 0:

                    cells[r][c].insert(
                        0,
                        str(puzzle[r][c])
                    )

    def toggle_speed():

        global current_speed_idx

        current_speed_idx = (
            current_speed_idx + 1
        ) % len(SPEED_NAMES)

        speed_btn.configure(
            text=SPEED_NAMES[current_speed_idx],

            fg_color=SPEED_COLORS[current_speed_idx],

            hover_color=SPEED_COLORS[current_speed_idx]
        )

    def solve_sudoku():

        try:

            grid = get_grid(cells)

        except ValueError as e:

            messagebox.showerror(
                "Lỗi nhập liệu",
                str(e)
            )

            return

        prefilled = [
            [
                grid[r][c] != 0
                for c in range(9)
            ]
            for r in range(9)
        ]

        if not is_board_valid(grid):

            messagebox.showerror(
                "Lỗi",
                "Bảng Sudoku không hợp lệ!"
            )

            return

        solve_btn.configure(state="disabled")
        clear_btn.configure(state="disabled")
        random_btn.configure(state="disabled")
        speed_btn.configure(state="disabled")
        
        
        delay = SPEED_DELAYS[current_speed_idx]

        if solve(
                grid,
                cells,
                root,
                delay,
                TEXT_SOLVED
        ):

            display(
                grid,
                cells,
                prefilled,
                TEXT_SOLVED,
                TEXT_WHITE
            )

        else:

            messagebox.showinfo(
                "Kết quả",
                "Không có lời giải!"
            )

        solve_btn.configure(state="normal")
        clear_btn.configure(state="normal")
        random_btn.configure(state="normal")
        speed_btn.configure(state="normal") 


    btn_frame = ctk.CTkFrame(
        root,
        fg_color="transparent"
    )

    btn_frame.pack(pady=(30, 0))

    solve_btn = ctk.CTkButton(
        btn_frame,
        text="Solve",
        command=solve_sudoku,
        font=('Helvetica', 14, 'bold'),
        fg_color=ACCENT_BLUE,
        hover_color="#104e8b",
        text_color=TEXT_WHITE,
        corner_radius=20,
        width=100,
        height=40
    )

    solve_btn.pack(side='left', padx=8)

    speed_btn = ctk.CTkButton(
        btn_frame,
        text=SPEED_NAMES[current_speed_idx],
        command=toggle_speed,
        font=('Helvetica', 14, 'bold'),
        fg_color=SPEED_COLORS[current_speed_idx],
        hover_color=SPEED_COLORS[current_speed_idx],
        text_color=TEXT_WHITE,
        corner_radius=20,
        width=120,
        height=40
    )

    speed_btn.pack(side='left', padx=8)

    clear_btn = ctk.CTkButton(
        btn_frame,
        text="Clear",
        command=clear_board,
        font=('Helvetica', 14, 'bold'),
        fg_color="#3a3a3c",
        hover_color="#505050",
        text_color=TEXT_WHITE,
        corner_radius=20,
        width=100,
        height=40
    )

    clear_btn.pack(side='left', padx=8)

    random_btn = ctk.CTkButton(
        btn_frame,
        text="🎲",
        command=random_fill,
        font=('Segoe UI Emoji', 18),
        fg_color="#8e44ad",
        hover_color="#9b59b6",
        text_color=TEXT_WHITE,
        corner_radius=20,
        width=40,
        height=40
    )

    random_btn.pack(side='left', padx=8)

    root.mainloop()