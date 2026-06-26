# Sudoku Solver

## Giới thiệu
Sudoku Solver là ứng dụng được xây dựng trong môn **Nhập môn Trí tuệ nhân tạo**, sử dụng thuật toán **Backtracking** kết hợp với **Heuristic Minimum Remaining Values (MRV)** để giải bài toán Sudoku 9×9, phát triển bằng **Python** và **CustomTkinter**, cho phép người chọn đề Sudoku theo mức độ, quan sát quá trình giải theo từng bước và điều chỉnh tốc độ chạy của thuật toán

## Chức năng
 Giải Sudoku chuẩn 9×9
 Áp dụng thuật toán Backtracking kết hợp Heuristic MRV
 Sinh ngẫu nhiên bảng Sudoku mẫu theo mức độ
 Hiển thị trực quan quá trình giải
 Điều chỉnh tốc độ mô phỏng

## Công nghệ sử dụng
 Python 3.x
 CustomTkinter
 Tkinter
 Visual Studio Code
 GitHub

## Cấu trúc thư mục

```text
SudokuSolver/
├── config.py
├── data.py
├── gui.py
├── main.py
├── solver.py
├── util.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Cài đặt

Clone project:

```bash
git clone https://github.com/thwmdev/Sudoku-Solver.git
```

Di chuyển vào thư mục project:

```bash
cd Sudoku-Solver
```

Cài đặt thư viện:

```bash
pip install -r requirements.txt
```

Chạy chương trình:

```bash
python main.py
```

## Thuật toán sử dụng

Ứng dụng sử dụng thuật toán **Backtracking** để tìm lời giải cho Sudoku. Để giảm số lần quay lui và tăng tốc độ xử lý, chương trình kết hợp thêm **Heuristic MRV**, giúp ưu tiên chọn ô có ít giá trị hợp lệ nhất trước khi tiếp tục tìm kiếm.

## Kết quả
Chương trình có thể giải chính xác các bảng Sudoku chuẩn 9×9 ở nhiều mức độ khác nhau. Giao diện trực quan giúp người dùng dễ theo dõi từng bước hoạt động của thuật toán, đồng thời cho phép thay đổi tốc độ.

## Môn học
Nhập môn Trí tuệ nhân tạo

## Thành viên thực hiện

  Lương Võ Hân Hân
  Bùi Kiếm Khoa
  Huỳnh Thị Hồng Thắm




