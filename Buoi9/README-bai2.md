# Bài 2: Vòng lặp và Hàm

Mở `bai2.html` bằng trình duyệt (cần có `style.css` cùng thư mục).

## Hoạt động 1: The Counting Machine
- Dùng `for` in số từ 1 đến 100 ra Console.
- In số chẵn: lặp `i += 2` bắt đầu từ 2, hoặc lặp từ 1 đến 100 rồi kiểm tra `i % 2 === 0`.

**Vibe Coding:** Prompt đã hỏi AI:
> Hãy giải thích cho tôi 3 thành phần bên trong ngoặc đơn của vòng lặp for (khởi tạo; điều kiện; bước nhảy) hoạt động như thế nào?

Tóm tắt, với `for (let i = 1; i <= 100; i++)`:
1. **Khởi tạo** `let i = 1`: chạy **một lần duy nhất** trước vòng lặp, tạo biến đếm.
2. **Điều kiện** `i <= 100`: kiểm tra **trước mỗi vòng**. Đúng thì chạy thân vòng lặp, sai thì dừng hẳn.
3. **Bước nhảy** `i++`: chạy **sau mỗi vòng** để cập nhật biến đếm, rồi quay lại kiểm tra điều kiện.

Thứ tự: khởi tạo → (kiểm tra điều kiện → chạy thân → bước nhảy) lặp lại.
Nếu quên bước nhảy hoặc điều kiện luôn đúng thì thành vòng lặp vô hạn.

## Hoạt động 2: Function Factory
- `tinhDienTich(dai, rong)` trả về `dai * rong`, gọi 3 lần với 3 cặp số khác nhau (nút "Gọi hàm 3 lần", xem Console).
- `chaoMung(ten, namSinh)` theo prompt mẫu, trả về chuỗi `Chào [Tên], bạn hiện tại [Số tuổi] tuổi`.
  Cách gọi: `console.log(chaoMung("An", 2005));`

## Hoạt động 3: Refactoring Challenge
**Prompt đã dùng với AI:**
> Hãy đóng gói đoạn code tính thuế thu nhập này thành một hàm để tôi có thể tái sử dụng cho nhiều mức lương khác nhau.

Đoạn code mẫu bên dưới là ví dụ của mình, **thay bằng đoạn code giảng viên đưa**. Trước khi refactor, mỗi mức lương phải copy lại cả khối `if/else`. Sau khi refactor chỉ cần một hàm `tinhThue(luong)` rồi gọi:

```js
console.log(tinhThue(8));
console.log(tinhThue(20));
console.log(tinhThue(35));
```

Lợi ích: bớt lặp code, sửa công thức một chỗ là áp dụng cho tất cả, dễ đọc và dễ test.
