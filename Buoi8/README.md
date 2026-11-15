# Thực hành JavaScript - Học phần 111101 Thiết kế Web

## Cách chạy
Mở file `index.html` bằng trình duyệt (hoặc dùng Live Server trong VS Code).

## Hoạt động 1: Hello JS Console
- Nút "Chạy demo Hello Console" hỏi tên, tuổi rồi in kết quả + các phép cộng, trừ, nhân, chia ra Console (F12).
- **Vibe Coding:** Vì sao `'10' + 20` ra `'1020'` mà không phải `30`?
  - Toán tử `+` trong JS vừa là cộng số, vừa là nối chuỗi. Khi một vế là chuỗi, JS ép vế còn lại thành chuỗi rồi nối: `'10' + '20'` → `'1020'` (type coercion).
  - Các toán tử `-`, `*`, `/` luôn ép về số nên `'10' - 5` ra `5`.
  - Muốn cộng đúng: `Number('10') + 20` → `30`.

## Hoạt động 2: Logic Builder - Máy tính mini
Máy tính cộng, trừ, nhân, chia dùng `if / else if`, có kiểm tra:
- Ô trống hoặc không phải số.
- Chia cho 0.

## Bài nhập điểm
- Dùng `prompt()` nhập điểm, `alert()` hiện kết quả.
- Đạt / chưa đạt: `>= 5` thì "Chúc mừng bạn đã đạt!", ngược lại "Rất tiếc, hãy cố gắng hơn!".
- Xếp loại: Giỏi (> 8), Khá (> 6.5), Trung bình (>= 5), Yếu (< 5).

**Prompt đã dùng với AI:**
> Viết một đoạn mã JavaScript sử dụng prompt() để lấy điểm số từ người dùng, sau đó sử dụng if-else để kiểm tra và alert() kết quả xếp loại: Giỏi (>8), Khá (>6.5), Trung bình (>=5), Yếu (<5).

## Hoạt động 3: AI Logic Explainer
Đoạn mã lỗi ví dụ:

```js
let diem = prompt("Nhập điểm:");
if (diem > 5) {
  alert("Đạt");
} else if (diem = 5) {
  alert("Vừa đủ");
} else {
  alert("Không đạt");
}
```

Giải thích bằng ngôn ngữ tự nhiên:
1. `prompt()` luôn trả về **chuỗi**, nên `diem > 5` phải ép sang số; nên dùng `Number(diem)`.
2. `else if (diem = 5)` là **phép gán** (một dấu `=`), không phải so sánh. Nó gán `diem` bằng 5 rồi luôn ra true. Phải viết `diem === 5`.
3. Điểm đúng bằng 5 lại rơi vào nhánh "Vừa đủ" thay vì "Đạt" nếu sửa sai điều kiện; cần thống nhất đề: `>= 5` là đạt.

Bản sửa:

```js
const diem = Number(prompt("Nhập điểm:"));
if (diem >= 5) {
  alert("Đạt");
} else {
  alert("Không đạt");
}
```
