#!/usr/bin/env python
"""
Tạo Public URL sử dụng multiple services
"""
import subprocess
import sys

def create_public_tunnel():
    """
    Hướng dẫn tạo public URL
    """
    print("\n" + "="*70)
    print("🌍 TẠOTUNNEL CÔNG KHAI - Chọn 1 trong các cách sau:")
    print("="*70 + "\n")
    
    print("📌 CÁCH 1: Dùng ServeoApp (Đơn giản nhất)")
    print("-" * 70)
    print("Chạy lệnh này:")
    print("  ssh -R 80:localhost:8000 serveo.net")
    print("✅ Kết quả: serveo.net sẽ cấp URL công khai!")
    print("   Ví dụ: https://xyz123.serveo.net\n")
    
    print("📌 CÁCH 2: Dùng localhost.run")
    print("-" * 70)
    print("Chạy lệnh này:")
    print("  ssh -R 80:localhost:8000 localhost.run")
    print("✅ Kết quả: https://randomname.localhost.run\n")
    
    print("📌 CÁCH 3: Cài Ngrok (cần authtoken)")
    print("-" * 70)
    print("1. Đăng ký: https://ngrok.com/signup")
    print("2. Lấy authtoken tại: https://dashboard.ngrok.com/auth/your-authtoken")
    print("3. Chạy: ngrok config add-authtoken YOUR_TOKEN")
    print("4. Chạy: ngrok http 8000")
    print("✅ Kết quả: Sẽ cấp URL HTTPS công khai\n")
    
    print("📌 CÁCH 4: Port Forward trên Router")
    print("-" * 70)
    print("1. Đăng nhập router (192.168.1.1 hoặc 192.168.0.1)")
    print("2. Port Forwarding: Port 8000 → IP máy port 8000")
    print("3. Dùng IP công khai + port 8000")
    print("✅ Kết quả: IP_công_khai:8000\n")
    
    print("="*70)
    print("💡 KHUYẾN NGHỊ: Thử Cách 1 (ServeoApp) - Nhanh nhất!")
    print("="*70 + "\n")
    
    print("🚀 Khi chạy xong, bạn sẽ nhận được URL công khai để chia sẻ!")

if __name__ == '__main__':
    create_public_tunnel()
