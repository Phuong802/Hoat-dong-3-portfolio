"""
models.py - Khởi tạo database và định nghĩa schema cho ứng dụng
"""
import sqlite3

DATABASE = "hoctap.db"


def get_db():
    """Kết nối tới SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Trả về dict-like rows
    return conn


def init_db():
    """Tạo bảng và chèn dữ liệu mẫu nếu chưa có."""
    conn = get_db()
    cursor = conn.cursor()

    # Tạo bảng môn học
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mon_hoc (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_mon TEXT NOT NULL,
            giang_vien TEXT NOT NULL
        )
    """)

    # Tạo bảng bài tập
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bai_tap (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_bai TEXT NOT NULL,
            mon_hoc_id INTEGER NOT NULL,
            han_nop TEXT NOT NULL,
            trang_thai TEXT NOT NULL DEFAULT 'Chua lam',
            FOREIGN KEY (mon_hoc_id) REFERENCES mon_hoc(id) ON DELETE CASCADE
        )
    """)

    # Chỉ thêm dữ liệu mẫu nếu bảng đang trống
    cursor.execute("SELECT COUNT(*) FROM mon_hoc")
    if cursor.fetchone()[0] == 0:
        _insert_sample_data(cursor)

    conn.commit()
    conn.close()


def _insert_sample_data(cursor):
    """Chèn dữ liệu mẫu để demo."""
    mon_hocs = [
        ("Lap trinh Python", "Thay Nguyen Van A"),
        ("Co so du lieu",    "Co Tran Thi B"),
        ("Mang may tinh",    "Thay Le Van C"),
        ("Tri tue nhan tao", "Co Pham Thi D"),
    ]
    cursor.executemany(
        "INSERT INTO mon_hoc (ten_mon, giang_vien) VALUES (?, ?)", mon_hocs
    )

    bai_taps = [
        ("Bai tap list & dict",        1, "2026-08-25", "Da xong"),
        ("Bai tap OOP",                1, "2026-09-01", "Chua lam"),
        ("Thiet ke ERD",               2, "2026-08-28", "Da xong"),
        ("Viet cau lenh SQL nang cao", 2, "2026-09-05", "Chua lam"),
        ("Bai tap TCP/IP",             3, "2026-09-10", "Chua lam"),
        ("Tim hieu OSI Model",         3, "2026-08-30", "Da xong"),
        ("Cai dat thuat toan A-star",  4, "2026-09-15", "Chua lam"),
        ("Bao cao machine learning",   4, "2026-09-20", "Chua lam"),
    ]
    cursor.executemany(
        "INSERT INTO bai_tap (ten_bai, mon_hoc_id, han_nop, trang_thai) VALUES (?, ?, ?, ?)",
        bai_taps,
    )
