"""
Script tạo UserProfile cho tất cả user hiện có
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accessory_store.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import UserProfile

# Tạo UserProfile cho tất cả user chưa có
created = 0
for user in User.objects.all():
    profile, is_created = UserProfile.objects.get_or_create(user=user)
    if is_created:
        created += 1
        print(f"✓ Tạo profile cho: {user.username}")
    else:
        print(f"✓ {user.username} đã có profile")

print(f"\n✅ Hoàn thành! Tạo {created} profile mới")
