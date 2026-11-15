// ===== Hoạt động 1: Hello JS Console =====
function helloConsole() {
  const ten = prompt("Bạn tên gì?") || "Bạn";
  const tuoi = Number(prompt("Bạn bao nhiêu tuổi?"));

  console.log(`Xin chào ${ten}, bạn ${tuoi} tuổi!`);
  console.log("10 + 5 =", 10 + 5);
  console.log("10 - 5 =", 10 - 5);
  console.log("10 * 5 =", 10 * 5);
  console.log("10 / 5 =", 10 / 5);

  // Vì sao '10' + 20 ra '1020' mà không phải 30?
  // Toán tử + khi có một vế là chuỗi sẽ NỐI CHUỖI (ép số 20 thành '20').
  console.log("'10' + 20 =", '10' + 20);          // '1020'
  console.log("'10' - 5  =", '10' - 5);           // 5 (toán tử - ép chuỗi thành số)
  console.log("Number('10') + 20 =", Number('10') + 20); // 30
}

// ===== Hoạt động 2: Máy tính mini =====
function calculate() {
  const a = parseFloat(document.getElementById("num1").value);
  const b = parseFloat(document.getElementById("num2").value);
  const op = document.getElementById("op").value;
  const out = document.getElementById("calc-result");

  if (isNaN(a) || isNaN(b)) {
    out.textContent = "Vui lòng nhập đủ hai số hợp lệ!";
    return;
  }

  let kq;
  if (op === "+") {
    kq = a + b;
  } else if (op === "-") {
    kq = a - b;
  } else if (op === "*") {
    kq = a * b;
  } else if (op === "/") {
    if (b === 0) {
      out.textContent = "Không thể chia cho 0!";
      return;
    }
    kq = a / b;
  }
  out.textContent = `${a} ${op} ${b} = ${kq}`;
}

// ===== Nhập điểm + if-else =====
function readScore() {
  const input = prompt("Nhập số điểm (0 - 10):");
  if (input === null) return null; // bấm Cancel
  const diem = parseFloat(input);
  if (isNaN(diem) || diem < 0 || diem > 10) {
    alert("Điểm không hợp lệ! Hãy nhập số từ 0 đến 10.");
    return null;
  }
  return diem;
}

function checkPass() {
  const diem = readScore();
  if (diem === null) return;

  if (diem >= 5) {
    alert("Chúc mừng bạn đã đạt!");
  } else {
    alert("Rất tiếc, hãy cố gắng hơn!");
  }
}

function rankScore() {
  const diem = readScore();
  if (diem === null) return;

  let xepLoai;
  if (diem > 8) {
    xepLoai = "Giỏi";
  } else if (diem > 6.5) {
    xepLoai = "Khá";
  } else if (diem >= 5) {
    xepLoai = "Trung bình";
  } else {
    xepLoai = "Yếu";
  }

  alert(`Điểm ${diem}: loại ${xepLoai}`);
  document.getElementById("grade-result").textContent = `Điểm ${diem} → ${xepLoai}`;
}

// ===== Gắn sự kiện =====
document.getElementById("btn-hello").addEventListener("click", helloConsole);
document.getElementById("btn-calc").addEventListener("click", calculate);
document.getElementById("btn-pass").addEventListener("click", checkPass);
document.getElementById("btn-rank").addEventListener("click", rankScore);
