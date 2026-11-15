"""
app.py - Flask application chính: định nghĩa tất cả routes
Chạy: python app.py  -->  mở http://127.0.0.1:5000
"""
from flask import Flask, render_template, request, redirect, url_for, flash
from models import get_db, init_db

app = Flask(__name__)
app.secret_key = "hoctap_secret_key"  # cần thiết cho flash messages

# ─── Khởi tạo database khi app bắt đầu ────────────────────────────────────────
with app.app_context():
    init_db()


# ──────────────────────────────────────────────────────────────────────────────
# TRANG DASHBOARD (trang chủ)
# ──────────────────────────────────────────────────────────────────────────────
@app.route("/")
def dashboard():
    db = get_db()

    # Thống kê tổng hợp
    tong_mon = db.execute("SELECT COUNT(*) FROM mon_hoc").fetchone()[0]
    tong_bai = db.execute("SELECT COUNT(*) FROM bai_tap").fetchone()[0]
    da_xong  = db.execute("SELECT COUNT(*) FROM bai_tap WHERE trang_thai='Da xong'").fetchone()[0]
    chua_lam = tong_bai - da_xong

    # Lấy danh sách bài tập kèm tên môn học (JOIN)
    bai_taps = db.execute("""
        SELECT bt.id, bt.ten_bai, bt.han_nop, bt.trang_thai,
               mh.ten_mon, mh.giang_vien
        FROM bai_tap bt
        JOIN mon_hoc mh ON bt.mon_hoc_id = mh.id
        ORDER BY bt.han_nop ASC
    """).fetchall()

    mon_hocs = db.execute("SELECT * FROM mon_hoc ORDER BY ten_mon").fetchall()
    db.close()

    return render_template("dashboard.html",
                           tong_mon=tong_mon, tong_bai=tong_bai,
                           da_xong=da_xong, chua_lam=chua_lam,
                           bai_taps=bai_taps, mon_hocs=mon_hocs)


# ──────────────────────────────────────────────────────────────────────────────
# QUẢN LÝ MÔN HỌC
# ──────────────────────────────────────────────────────────────────────────────
@app.route("/mon-hoc")
def mon_hoc_list():
    db = get_db()
    mon_hocs = db.execute("""
        SELECT mh.*, COUNT(bt.id) AS so_bai
        FROM mon_hoc mh
        LEFT JOIN bai_tap bt ON mh.id = bt.mon_hoc_id
        GROUP BY mh.id
        ORDER BY mh.ten_mon
    """).fetchall()
    db.close()
    return render_template("mon_hoc.html", mon_hocs=mon_hocs)


@app.route("/mon-hoc/them", methods=["GET", "POST"])
def mon_hoc_them():
    if request.method == "POST":
        ten_mon    = request.form["ten_mon"].strip()
        giang_vien = request.form["giang_vien"].strip()
        if not ten_mon or not giang_vien:
            flash("Vui long nhap day du thong tin!", "danger")
        else:
            db = get_db()
            db.execute("INSERT INTO mon_hoc (ten_mon, giang_vien) VALUES (?, ?)",
                       (ten_mon, giang_vien))
            db.commit()
            db.close()
            flash("Da them mon hoc thanh cong!", "success")
            return redirect(url_for("mon_hoc_list"))
    return render_template("mon_hoc_form.html", mon=None, action="Them moi")


@app.route("/mon-hoc/sua/<int:id>", methods=["GET", "POST"])
def mon_hoc_sua(id):
    db = get_db()
    mon = db.execute("SELECT * FROM mon_hoc WHERE id=?", (id,)).fetchone()
    if not mon:
        flash("Khong tim thay mon hoc!", "danger")
        return redirect(url_for("mon_hoc_list"))

    if request.method == "POST":
        ten_mon    = request.form["ten_mon"].strip()
        giang_vien = request.form["giang_vien"].strip()
        if not ten_mon or not giang_vien:
            flash("Vui long nhap day du thong tin!", "danger")
        else:
            db.execute("UPDATE mon_hoc SET ten_mon=?, giang_vien=? WHERE id=?",
                       (ten_mon, giang_vien, id))
            db.commit()
            db.close()
            flash("Cap nhat mon hoc thanh cong!", "success")
            return redirect(url_for("mon_hoc_list"))

    db.close()
    return render_template("mon_hoc_form.html", mon=mon, action="Cap nhat")


@app.route("/mon-hoc/xoa/<int:id>", methods=["POST"])
def mon_hoc_xoa(id):
    db = get_db()
    # Bài tập liên quan sẽ tự bị xóa nhờ ON DELETE CASCADE
    db.execute("PRAGMA foreign_keys = ON")
    db.execute("DELETE FROM mon_hoc WHERE id=?", (id,))
    db.commit()
    db.close()
    flash("Da xoa mon hoc!", "warning")
    return redirect(url_for("mon_hoc_list"))


# ──────────────────────────────────────────────────────────────────────────────
# QUẢN LÝ BÀI TẬP
# ──────────────────────────────────────────────────────────────────────────────
@app.route("/bai-tap")
def bai_tap_list():
    db = get_db()
    bai_taps = db.execute("""
        SELECT bt.*, mh.ten_mon
        FROM bai_tap bt
        JOIN mon_hoc mh ON bt.mon_hoc_id = mh.id
        ORDER BY bt.han_nop ASC
    """).fetchall()
    db.close()
    return render_template("bai_tap.html", bai_taps=bai_taps)


@app.route("/bai-tap/them", methods=["GET", "POST"])
def bai_tap_them():
    db = get_db()
    mon_hocs = db.execute("SELECT * FROM mon_hoc ORDER BY ten_mon").fetchall()

    if request.method == "POST":
        ten_bai    = request.form["ten_bai"].strip()
        mon_hoc_id = request.form["mon_hoc_id"]
        han_nop    = request.form["han_nop"]
        trang_thai = request.form["trang_thai"]
        if not ten_bai or not mon_hoc_id or not han_nop:
            flash("Vui long nhap day du thong tin!", "danger")
        else:
            db.execute(
                "INSERT INTO bai_tap (ten_bai, mon_hoc_id, han_nop, trang_thai) VALUES (?, ?, ?, ?)",
                (ten_bai, mon_hoc_id, han_nop, trang_thai)
            )
            db.commit()
            db.close()
            flash("Da them bai tap thanh cong!", "success")
            return redirect(url_for("bai_tap_list"))

    db.close()
    return render_template("bai_tap_form.html", bai=None, mon_hocs=mon_hocs, action="Them moi")


@app.route("/bai-tap/sua/<int:id>", methods=["GET", "POST"])
def bai_tap_sua(id):
    db = get_db()
    bai = db.execute("SELECT * FROM bai_tap WHERE id=?", (id,)).fetchone()
    mon_hocs = db.execute("SELECT * FROM mon_hoc ORDER BY ten_mon").fetchall()

    if not bai:
        flash("Khong tim thay bai tap!", "danger")
        return redirect(url_for("bai_tap_list"))

    if request.method == "POST":
        ten_bai    = request.form["ten_bai"].strip()
        mon_hoc_id = request.form["mon_hoc_id"]
        han_nop    = request.form["han_nop"]
        trang_thai = request.form["trang_thai"]
        db.execute(
            "UPDATE bai_tap SET ten_bai=?, mon_hoc_id=?, han_nop=?, trang_thai=? WHERE id=?",
            (ten_bai, mon_hoc_id, han_nop, trang_thai, id)
        )
        db.commit()
        db.close()
        flash("Cap nhat bai tap thanh cong!", "success")
        return redirect(url_for("bai_tap_list"))

    db.close()
    return render_template("bai_tap_form.html", bai=bai, mon_hocs=mon_hocs, action="Cap nhat")


@app.route("/bai-tap/xoa/<int:id>", methods=["POST"])
def bai_tap_xoa(id):
    db = get_db()
    db.execute("DELETE FROM bai_tap WHERE id=?", (id,))
    db.commit()
    db.close()
    flash("Da xoa bai tap!", "warning")
    return redirect(url_for("bai_tap_list"))


# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
