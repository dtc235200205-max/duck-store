#!/usr/bin/env python
"""
Deploy Duck Store lên Railway - 1 click, dễ dàng!
"""

print("""
╔══════════════════════════════════════════════════════════════════════╗
║                  🚀 DEPLOY LÊN RAILWAY (MIỄN PHÍ)                   ║
╚══════════════════════════════════════════════════════════════════════╝

📌 BƯỚC 1: Tạo file Procfile
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tại thư mục d:\\test2\\ tạo file "Procfile" (không có extension):

web: python manage.py runserver 0.0.0.0:$PORT

📌 BƯỚC 2: Tạo requirements.txt
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pip freeze > requirements.txt

📌 BƯỚC 3: Push lên GitHub
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Đăng nhập: https://github.com
2. Tạo repository mới: "duck-store"
3. Git push code lên:

   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/duck-store.git
   git push -u origin main

📌 BƯỚC 4: Deploy trên Railway
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Truy cập: https://railway.app
2. Đăng nhập bằng GitHub
3. Click "Create New Project" → "Deploy from GitHub"
4. Chọn repository "duck-store"
5. Railway tự động deploy!
6. Sẽ cấp URL công khai (ví dụ: https://duck-store-production.up.railway.app)

📌 BƯỚC 5: Truy cập
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
https://duck-store-production.up.railway.app

Đăng nhập: user1 / password123
Admin: admin / admin123

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Hoàn toàn miễn phí
✅ Tự động HTTPS
✅ Không cần port forward
✅ URL công khai, truy cập từ bất kỳ đâu
✅ Tự động tạo database
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
