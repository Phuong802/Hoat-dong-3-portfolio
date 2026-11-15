# Bài 3: Thao tác DOM

Mở `bai3.html` bằng trình duyệt (cần `style.css`, `den-tat.svg`, `den-sang.svg` cùng thư mục).

## Hoạt động 1: The Element Picker
- `document.querySelector('.menu-item')` trả về **phần tử đầu tiên** khớp selector.
- `document.querySelectorAll('#menu a')` trả về **tất cả** phần tử khớp (NodeList).
- Bấm nút "In thẻ ra Console" rồi mở F12 để xem.

**Vibe Coding:** Prompt đã hỏi AI:
> Làm thế nào để chọn tất cả các thẻ `<a>` bên trong một `<ul>` có id là 'menu' và đổi màu chữ của chúng sang màu đỏ?

```js
const links = document.querySelectorAll('#menu a');
links.forEach(function (link) {
  link.style.color = 'red';
});
```
Giải thích: selector `#menu a` nghĩa là "mọi thẻ `a` nằm bên trong phần tử có id `menu`".
`querySelectorAll` trả về danh sách nên phải lặp qua từng phần tử rồi đặt `style.color`.

## Hoạt động 2: Light Switch
- Một thẻ `<img id="lamp">` và nút bấm. Mỗi lần bấm đổi thuộc tính `src` giữa `den-tat.svg` và `den-sang.svg`.
- **Dark mode đơn giản:** nút `id="toggle-btn"` bật/tắt class `dark` trên `<body>`, nền chuyển trắng ↔ đen.

**Prompt đã dùng với AI:**
> Viết mã JS để khi tôi click vào một nút có id là 'toggle-btn', nó sẽ thay đổi màu nền của body từ trắng sang đen và ngược lại (Dark mode đơn giản).

## Hoạt động 3: Live Input
- Gắn sự kiện `input` cho ô `<input>`. Mỗi lần gõ, giá trị `input.value` được gán vào thẻ `<span>` bên cạnh và thẻ `<h2>` bên dưới.
- Khác với `change` (chỉ chạy khi rời khỏi ô), `input` chạy ngay sau từng ký tự.

**Prompt đã dùng với AI:**
> Sử dụng sự kiện 'input' trong JavaScript để lấy giá trị từ một ô text và hiển thị nó ngay lập tức vào một thẻ h2 bên dưới.
