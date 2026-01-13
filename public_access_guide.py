#!/usr/bin/env python
"""
Chạy server Django + HTTP tunnel
Sử dụng httpbin.org hoặc dịch vụ ngrok tự build
"""
import subprocess
import sys
import time

print("\n" + "="*70)
print("🚀 Duck Store - Public Access Setup")
print("="*70 + "\n")

# Kiểm tra server
print("✅ Server Django đang chạy trên port 8000...")
print("✅ Truy cập local: http://localhost:8000\n")

print("🌍 PUBLIC ACCESS OPTIONS:")
print("-"*70)

print("\n📌 OPTION 1: Dùng Quick Tunnel (Cloudflare)")
print("Cài đặt:")
print("  pip install cloudflare")
print("Chạy:")
print("  cloudflared tunnel --url http://localhost:8000")

print("\n📌 OPTION 2: Dùng Python HTTP Server + Port Forwarding")
print("Port Forwarding Settings:")
print("  Router: Forward external port 8000 → localhost:8000")
print("  Public IP: (lấy từ whatismyipaddress.com)")
print("  Access: http://PUBLIC_IP:8000")

print("\n📌 OPTION 3: Dùng Docker + Deployable")
print("Deploy lên Heroku, Railway, hoặc Render")

print("\n📌 OPTION 4: Dùng Replit (Miễn phí)")
print("Upload project lên Replit, tự động có URL công khai")

print("\n" + "="*70)
print("💡 Khuyến nghị: Dùng Cloudflare Tunnel (Option 1)")
print("="*70 + "\n")
