// ===== Hoạt động 1: The Counting Machine =====
function inSo1Den100() {
  const ds = [];
  // for (khởi tạo; điều kiện; bước nhảy)
  for (let i = 1; i <= 100; i++) {
    console.log(i);
    ds.push(i);
  }
  document.getElementById("loop-result").textContent = ds.join(", ");
}

function inSoChan() {
  const ds = [];
  // Cách 1: bước nhảy 2, bắt đầu từ 2
  for (let i = 2; i <= 100; i += 2) {
    console.log(i);
    ds.push(i);
  }
  // Cách 2: dùng if (i % 2 === 0) khi lặp i từ 1 đến 100
  document.getElementById("loop-result").textContent = ds.join(", ");
}

// ===== Hoạt động 2: Function Factory =====
function tinhDienTich(dai, rong) {
  return dai * rong;
}

function goiHam3Lan() {
  console.log("Dài 5, rộng 3  → diện tích:", tinhDienTich(5, 3));
  console.log("Dài 10, rộng 4 → diện tích:", tinhDienTich(10, 4));
  console.log("Dài 7.5, rộng 2 → diện tích:", tinhDienTich(7.5, 2));
}

function tinhTuInput() {
  const dai = parseFloat(document.getElementById("dai").value);
  const rong = parseFloat(document.getElementById("rong").value);
  const out = document.getElementById("area-result");

  if (isNaN(dai) || isNaN(rong) || dai < 0 || rong < 0) {
    out.textContent = "Vui lòng nhập chiều dài và chiều rộng hợp lệ!";
    return;
  }
  out.textContent = `Diện tích = ${tinhDienTich(dai, rong)}`;
}

// Hàm theo prompt mẫu: nhận tên và năm sinh, trả về chuỗi chào
function chaoMung(ten, namSinh) {
  const tuoi = new Date().getFullYear() - namSinh;
  return `Chào ${ten}, bạn hiện tại ${tuoi} tuổi`;
}

function chaoTuInput() {
  const ten = document.getElementById("ten").value.trim();
  const namSinh = parseInt(document.getElementById("namsinh").value);
  const out = document.getElementById("greet-result");

  if (!ten || isNaN(namSinh)) {
    out.textContent = "Vui lòng nhập tên và năm sinh!";
    return;
  }
  const loiChao = chaoMung(ten, namSinh);
  console.log(loiChao);
  out.textContent = loiChao;
}

// ===== Hoạt động 3: Refactoring Challenge =====
// (Thuế đơn giản hóa để minh họa, KHÔNG phải biểu thuế TNCN thật.)
//
// TRƯỚC khi refactor: code lặp lại cho từng mức lương
//   let luong1 = 8;
//   let thue1;
//   if (luong1 <= 10) { thue1 = luong1 * 0.05; }
//   else if (luong1 <= 30) { thue1 = luong1 * 0.1; }
//   else { thue1 = luong1 * 0.15; }
//   console.log("Thuế:", thue1);
//   let luong2 = 20;  ... copy y hệt đoạn trên ...
//
// SAU khi refactor: đóng gói thành một hàm, dùng lại cho mọi mức lương
function tinhThue(luong) {
  if (luong <= 10) {
    return luong * 0.05;
  } else if (luong <= 30) {
    return luong * 0.1;
  }
  return luong * 0.15;
}

function tinhThueTuInput() {
  const luong = parseFloat(document.getElementById("luong").value);
  const out = document.getElementById("tax-result");

  if (isNaN(luong) || luong < 0) {
    out.textContent = "Vui lòng nhập mức lương hợp lệ!";
    return;
  }
  const thue = tinhThue(luong);
  console.log(`Lương ${luong} triệu → thuế ${thue} triệu`);
  out.textContent = `Lương ${luong} triệu → thuế ${thue.toFixed(2)} triệu`;
}

// ===== Gắn sự kiện =====
document.getElementById("btn-all").addEventListener("click", inSo1Den100);
document.getElementById("btn-even").addEventListener("click", inSoChan);
document.getElementById("btn-area").addEventListener("click", tinhTuInput);
document.getElementById("btn-area-demo").addEventListener("click", goiHam3Lan);
document.getElementById("btn-greet").addEventListener("click", chaoTuInput);
document.getElementById("btn-tax").addEventListener("click", tinhThueTuInput);
