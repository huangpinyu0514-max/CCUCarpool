import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
});


export async function sendVerificationEmail(email) {
  const res = await api.post("/vertify/email", { email });
  return res.data.exist;
}

export async function verifyCode(code, user) {
  const { password, student_id, department, ...rest } = user; // rest = email, name
  const res = await api.post("/vertify/code", {
    code,
    user: {
      ...rest,
      password_hash: password, // 後端欄位名稱就叫這個，見下方說明
      student_id: student_id || null,
      department: department || null,
    },
  });
  return res.data.status;
}

export async function login(email, password) {
  const res = await api.post("/login", { email, password });
  return res.data.login;
}