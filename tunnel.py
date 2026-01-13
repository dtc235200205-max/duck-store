#!/usr/bin/env python
"""
Tạo public tunnel cho Duck Store
"""
import subprocess
import time
import threading

def run_exposer():
    """Chạy exposer tunnel"""
    try:
        cmd = 'D:/test2/.venv/Scripts/python.exe -m exposer 8000'
        print("\n" + "="*70)
        print("🌍 Tạo public tunnel...")
        print("="*70 + "\n")
        subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f"Lỗi: {e}")
        print("\n💡 Thử phương án khác...")
        try:
            import requests
            print("Dùng expose.sh thay vào...")
            # Hoặc hướng dẫn người dùng dùng cách khác
        except:
            pass

# Chạy exposer
if __name__ == '__main__':
    run_exposer()
