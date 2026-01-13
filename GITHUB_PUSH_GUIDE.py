#!/usr/bin/env python
"""
Hướng dẫn push GitHub bằng Personal Access Token
"""

print("""
╔══════════════════════════════════════════════════════════════════════╗
║           🔑 PUSH CODE LÊN GITHUB BẰNG PERSONAL ACCESS TOKEN        ║
╚══════════════════════════════════════════════════════════════════════╝

📌 BƯỚC 1: Tạo Personal Access Token
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Đăng nhập GitHub: https://github.com/login
2. Vào Settings → Developer settings → Personal access tokens
3. Click "Generate new token"
4. Token name: "duck-store-deploy"
5. Scope: Chọn "repo" (full control)
6. Click "Generate token"
7. **Copy token ngay** (sẽ không hiển thị lại!)

📌 BƯỚC 2: Chạy lệnh push (thay TOKEN bằng token vừa tạo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

cd d:\\test2
git config --global user.name "dtc235200205-max"
git config --global user.email "your_email@example.com"

git remote set-url origin https://dtc235200205-max:YOUR_TOKEN@github.com/dtc235200205-max/duck-store.git

git push -u origin main

📌 BƯỚC 3: Nếu repo chưa tạo trên GitHub
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Trước khi push, hãy:
1. Truy cập: https://github.com/new
2. Repository name: "duck-store"
3. Click "Create repository"
4. Rồi chạy git push

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Sau khi push xong:
   - Code sẽ ở: https://github.com/dtc235200205-max/duck-store
   - Tiếp theo deploy trên Railway!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
