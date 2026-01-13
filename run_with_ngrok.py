#!/usr/bin/env python
"""
Chạy Django server với Ngrok tunnel
"""
import os
import sys
import django
from django.core.management import execute_from_command_line
from pyngrok import ngrok
import threading
import time

# Cấu hình Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accessory_store.settings')
django.setup()

def start_ngrok():
    """Chạy Ngrok tunnel sau 2 giây"""
    time.sleep(2)
    try:
        public_url = ngrok.connect(8000, 'http')
        print(f"\n\n{'='*60}")
        print(f"🌍 PUBLIC URL: {public_url}")
        print(f"{'='*60}\n")
        print(f"Chia sẻ URL này để truy cập từ máy khác!\n")
    except Exception as e:
        print(f"Lỗi Ngrok: {e}")

# Chạy Ngrok trong thread riêng
ngrok_thread = threading.Thread(target=start_ngrok, daemon=True)
ngrok_thread.start()

# Chạy Django server
if __name__ == '__main__':
    sys.argv = ['manage.py', 'runserver', '0.0.0.0:8000']
    execute_from_command_line(sys.argv)
