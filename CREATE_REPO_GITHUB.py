#!/usr/bin/env python
"""
Hướng dẫn tạo repo GitHub
"""

print("""
╔══════════════════════════════════════════════════════════════════════╗
║                    📌 TẠOON REPOSITORY TRÊN GITHUB                    ║
╚══════════════════════════════════════════════════════════════════════╝

⚠️  BƯỚC 1: Truy cập GitHub và tạo repository
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣  Vào: https://github.com/new

2️⃣  Điền thông tin:
   - Repository name: duck-store
   - Description: Vietnamese E-commerce Platform (tùy chọn)
   - Public (để public)
   - ❌ Không chọn "Initialize with README"
   - ❌ Không chọn gitignore
   - ❌ Không chọn license

3️⃣  Click "Create repository"

4️⃣  Bạn sẽ nhận được hướng dẫn, sau đó quay lại chạy:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
cd d:\\test2
git remote set-url origin "https://YOUR_TOKEN@github.com/dtc235200205-max/duck-store.git"
git push -u origin main
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Sau khi push xong:
   - Code ở: https://github.com/dtc235200205-max/duck-store
   - Tiếp theo: Deploy trên Railway!

""")
