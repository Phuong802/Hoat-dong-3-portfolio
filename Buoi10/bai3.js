// ===== Hoạt động 1: The Element Picker =====
function pickElements() {
  // Chọn 1 phần tử đầu tiên khớp selector
  console.log(document.querySelector('.menu-item'));
  console.log(document.querySelector('#menu'));

  // Chọn tất cả phần tử khớp selector (trả về NodeList)
  console.log(document.querySelectorAll('#menu a'));
}

// Vibe Coding: chọn tất cả thẻ bên trong #menu và đổi chữ sang màu đỏ
function makeMenuRed() {
  const links = document.querySelectorAll('#menu a');
  links.forEach(function (link) {
    link.style.color = 'red';
  });
}

// ===== Hoạt động 2: Light Switch =====
const lamp = document.getElementById('lamp');
let lampOn = false;

function toggleLamp() {
  lampOn = !lampOn;
  if (lampOn) {
    lamp.src = 'den-sang.svg';
    lamp.alt = 'Đèn sáng';
  } else {
    lamp.src = 'den-tat.svg';
    lamp.alt = 'Đèn tắt';
  }
}

// Dark mode đơn giản: nút có id "toggle-btn" đổi nền body trắng <-> đen
function toggleDarkMode() {
  document.body.classList.toggle('dark');
}

// ===== Hoạt động 3: Live Input =====
const liveInput = document.getElementById('live-input');
const liveSpan = document.getElementById('live-span');
const liveOutput = document.getElementById('live-output');

liveInput.addEventListener('input', function () {
  liveSpan.textContent = liveInput.value;   // thẻ <span> bên cạnh
  liveOutput.textContent = liveInput.value; // thẻ <h2> bên dưới
});

// ===== Gắn sự kiện =====
document.getElementById('btn-pick').addEventListener('click', pickElements);
document.getElementById('btn-red').addEventListener('click', makeMenuRed);
document.getElementById('lamp-btn').addEventListener('click', toggleLamp);
document.getElementById('toggle-btn').addEventListener('click', toggleDarkMode);
