# 📘 CẨM NANG QUẢN LÝ VÀ CHỈNH SỬA PORTFOLIO DỄ DÀNG

Chào Phát! Tài liệu này hướng dẫn bạn cách quản lý, thay đổi dữ liệu hoặc thêm bớt tính năng cho trang portfolio của mình một cách dễ dàng và nhanh chóng nhất.

---

## 📂 1. Cấu Trúc File Dự Án

Dự án của bạn hiện tại gồm 2 file chính tập trung vào HTML và CSS:

| Tên File | Vai trò | Khi nào cần mở file này? |
| :--- | :--- | :--- |
| **`indexcuaPham.html`** | **Nội dung & Dữ liệu** | Khi muốn đổi họ tên, ảnh đại diện, thêm bớt dự án, sửa link GitHub, đổi chữ... (Đoạn JS bài tập của bạn nằm ở cuối file này). |
| **`style.css`** | **Giao diện & Màu sắc** | Khi muốn đổi màu chủ đạo, chỉnh cỡ chữ, khoảng cách, bo góc, đổi màu Dark Mode... |

---

## 📝 2. Cách Thay Đổi Dữ Liệu Trong `indexcuaPham.html`

File HTML đã được chia thành **6 KHU VỰC ĐƯỢC ĐÁNH DẤU RÕ RÀNG**:

### 🎯 2.1. Đổi Ảnh Đại Diện (Avatar) và Lời Giới Thiệu
Mở `indexcuaPham.html`, tìm tới **`[KHU VỰC 3] THÔNG TIN BẢN THÂN`**:
- **Đổi ảnh đại diện**: Thay đường dẫn trong `src="..."` của thẻ `<img>`:
  ```html
  <img src="link_anh_cua_ban_o_day.jpg" alt="Ảnh đại diện" class="card-image">
  ```
- **Đổi tên hoặc giới thiệu**: Sửa trực tiếp chữ nằm trong thẻ `<h3>` và thẻ `<p>`.

---

### 🚀 2.2. Cách Thêm Một Dự Án Mới (Rất dễ!)
Mở `indexcuaPham.html`, tìm tới **`[KHU VỰC 4] DANH SÁCH DỰ ÁN NỔI BẬT`**.
Mỗi dự án là một khối thẻ `<article class="project-card">`. 

👉 **Khi bạn làm xong một dự án mới, chỉ cần copy đoạn mã mẫu dưới đây và dán vào bên trong `<div class="project-grid">`:**

```html
<article class="project-card">
    <span class="project-badge">Dự án 03</span>
    <h3 class="project-title">Tên dự án mới của bạn</h3>
    <p class="project-desc">Mô tả ngắn gọn dự án làm về cái gì và dùng công nghệ gì...</p>
    <a href="https://github.com/tentaxxx8-max/ten-repo-moi" target="_blank" rel="noopener noreferrer" class="project-link">
        Xem mã nguồn trên GitHub &rarr;
    </a>
</article>
```
*Giao diện sẽ tự động sắp xếp lưới (Grid) 1 cột, 2 cột hoặc 3 cột tùy theo kích thước màn hình mà không bị vỡ layout.*

---

## 🎨 3. Cách Đổi Màu Sắc Giao Diện Trong `style.css`

Bạn **không cần** phải tìm từng chỗ trong 200 dòng CSS để sửa màu! Toàn bộ màu sắc đã được gom lên đầu file tại mục **`1. BẢNG MÀU & BIẾN CƠ BẢN`**.

Chỉ cần mở `style.css` và sửa các dòng sau:

```css
:root {
  /* Đổi màu chủ đạo (ví dụ muốn màu xanh lá thì đổi thành #10b981, màu tím thì #8b5cf6) */
  --primary: #0284c7;        /* Màu chủ đạo của nút bấm, tiêu đề, đường viền */
  --primary-hover: #0369a1;  /* Màu khi người dùng rê chuột vào nút */
  
  /* Đổi màu nền trang */
  --bg-body: #f4f6f8;        /* Nền tổng thể */
  --bg-section: #ffffff;     /* Nền các khung thẻ trắng */
}
```

Nếu muốn chỉnh màu của **Dark Mode (Chế độ tối)**, bạn kéo xuống ngay dưới mục `2. GIAO DIỆN TỐI (DARK MODE)` và thay đổi màu của `body.dark-theme`.

---

## 💡 4. Những Điểm Cải Tiến Đã Được Tối Ưu Cho Bạn

1. **Không bị lỗi đè CSS**: Đã dọn sạch đoạn mã bị paste trùng trước đó.
2. **Hiệu ứng Hover Card**: Khi rê chuột vào từng thẻ dự án, thẻ sẽ nhẹ nhàng nâng lên (`translateY(-4px)`) và phát sáng nhẹ viền theo màu chủ đạo.
3. **Mobile First & Responsive**: Tự động hiển thị hoàn hảo từ điện thoại iPhone/Android cho tới máy tính xách tay hay màn hình lớn.
4. **Không đụng chạm code logic**: Giữ nguyên vẹn đoạn JS bài tập tuần 4 ở cuối HTML của bạn.

---

## ✨ 5. Tùy Chỉnh Hiệu Ứng Cuộn Trang AOS (Hoạt Động 3)

Thư viện **AOS (Animate On Scroll)** giúp các thành phần tự động bay/hiện ra khi bạn cuộn trang tới đó.

### 5.1. Cách thay đổi hiệu ứng trên từng thẻ
Chỉ cần đổi giá trị trong thuộc tính `data-aos="..."` của thẻ HTML:
- `data-aos="fade-up"`: Trượt từ dưới lên và mờ dần hiện rõ (đang dùng phổ biến).
- `data-aos="fade-down"`: Trượt từ trên xuống.
- `data-aos="fade-left"`: Trượt từ bên phải sang trái.
- `data-aos="fade-right"`: Trượt từ bên trái sang phải.
- `data-aos="zoom-in"`: Phóng to dần hiện ra.
- `data-aos="flip-up"`: Lật thẻ theo chiều dọc.

### 5.2. Các thuộc tính bổ sung hữu ích
- `data-aos-duration="1000"`: Thời gian chạy hiệu ứng (1000 = 1 giây, càng lớn càng chậm và mượt).
- `data-aos-delay="200"`: Độ trễ (dự án 1 hiện trước, dự án 2 trễ 200ms hiện sau tạo hiệu ứng so le rất đẹp mắt).

