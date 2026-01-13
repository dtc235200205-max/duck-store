#!/usr/bin/env python
"""
Hiển thị thông tin truy cập server
"""
import requests
import subprocess
import time

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json()['ip']
    except:
        return "Không thể xác định IP"

def get_local_ip():
    try:
        import socket
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except:
        return "Không thể xác định IP"

print("\n" + "="*70)
print("🚀 DUCK STORE - SERVER INFORMATION")
print("="*70)

local_ip = get_local_ip()
public_ip = get_public_ip()

print(f"\n📍 Local Network (Cùng mạng):")
print(f"   URL: http://{local_ip}:8000")
print(f"   Từ máy khác trên WiFi: http://{local_ip}:8000")

print(f"\n🌍 Public Access (Internet):")
print(f"   IP công khai: {public_ip}")
print(f"   Để truy cập từ ngoài internet:")
print(f"   1. Dùng Ngrok (tải authtoken từ https://ngrok.com)")
print(f"   2. Dùng Cloudflare Tunnel")
print(f"   3. Hoặc Port Forwarding trên router")

print(f"\n📊 Django Server:")
print(f"   Đang chạy trên: http://0.0.0.0:8000")
print(f"   Bảng admin: /admin/ (user: admin, pass: admin123)")
print(f"   Demo login: user1 / password123")

print("\n" + "="*70)
print("✨ Server đang chạy, truy cập bây giờ!")
print("="*70 + "\n")
