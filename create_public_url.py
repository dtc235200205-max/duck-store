#!/usr/bin/env python
"""
Tạo public URL sử dụng localhost.run
"""
import subprocess
import os

print("\n" + "="*70)
print("🌍 Tạo Public URL cho Duck Store")
print("="*70 + "\n")

print("Cách 1: Dùng SSH Tunnel (localhost.run) - Đơn giản nhất!")
print("-" * 70)
print("Chạy lệnh này trong terminal:")
print("\nssh -R 80:localhost:8000 localhost.run\n")
print("Kết quả sẽ hiển thị URL công khai!")

print("\n" + "="*70)
print("Cách 2: Dùng expose.sh - Miễn phí, không cần đăng ký")
print("-" * 70)
print("Tải: https://expose.sh")
print("Chạy: expose http://127.0.0.1:8000")

print("\n" + "="*70)
print("Cách 3: Dùng Ngrok - Có authtoken")
print("-" * 70)
print("1. Đăng ký: https://ngrok.com/signup")
print("2. Lấy authtoken: https://dashboard.ngrok.com/get-started/your-authtoken")
print("3. Chạy: ngrok http 8000")

print("\n" + "="*70)
print("✨ Khuyến nghị: Dùng Cách 1 (localhost.run)")
print("="*70 + "\n")

# Kiểm tra SSH
try:
    result = subprocess.run(['ssh', '-V'], capture_output=True, text=True)
    print(f"✅ SSH đã cài: {result.stderr.strip()}")
except:
    print("❌ SSH chưa cài, tải: https://www.openssh.com/")
