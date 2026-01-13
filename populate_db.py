import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accessory_store.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Role, Category, Product, Order, OrderItem

# Create admin user
admin_user, _ = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@example.com',
        'is_superuser': True,
        'is_staff': True,
    }
)
if not admin_user.check_password('admin123'):
    admin_user.set_password('admin123')
    admin_user.save()

# Create sample users
for i in range(3):
    user, _ = User.objects.get_or_create(
        username=f'user{i+1}',
        defaults={
            'email': f'user{i+1}@example.com',
        }
    )
    if not user.check_password('password123'):
        user.set_password('password123')
        user.save()

# Create categories
categories_data = [
    'Ốp lưng điện thoại',
    'Tai nghe',
    'Sạc điện thoại',
    'Cáp USB',
    'Cường lực',
]

categories = []
for cat_name in categories_data:
    cat, _ = Category.objects.get_or_create(name=cat_name)
    categories.append(cat)

# Create sample products - Vietnamese names with phone case and tempered glass focus
products_data = [
    {'name': 'Ốp lưng TPU Chống va đập', 'price': '15.99', 'category': 0, 'description': 'Ốp lưng TPU bảo vệ tối đa chống va đập, rơi vỡ'},
    {'name': 'Ốp lưng da PU cao cấp', 'price': '22.99', 'category': 0, 'description': 'Ốp lưng da PU chính hãng, bền bỉ, cảm giác tay tuyệt vời'},
    {'name': 'Ốp lưng silicone mềm mại', 'price': '12.99', 'category': 0, 'description': 'Ốp lưng silicone mềm, dễ tháo lắp, bảo vệ tốt'},
    {'name': 'Ốp lưng glass hiệu ứng', 'price': '18.99', 'category': 0, 'description': 'Ốp lưng mặt kính với họa tiết đẹp, bảo vệ tốt'},
    {'name': 'Cường lực 9H cao cấp', 'price': '8.99', 'category': 4, 'description': 'Kính cường lực 9H, chống xước, chống vỡ'},
    {'name': 'Cường lực 10D full màn hình', 'price': '12.99', 'category': 4, 'description': 'Kính cường lực 10D bao phủ toàn màn hình'},
    {'name': 'Cường lực chống nhìn trộm', 'price': '16.99', 'category': 4, 'description': 'Kính cường lực với lớp chống nhìn trộm'},
    {'name': 'Cường lực dẻo chống rơi', 'price': '14.99', 'category': 4, 'description': 'Kính dẻo, không vỡ, bảo vệ cực tốt'},
    {'name': 'Tai nghe Bluetooth Wireless', 'price': '45.99', 'category': 1, 'description': 'Tai nghe không dây với công nghệ noise cancellation'},
    {'name': 'Tai nghe True Wireless Pro', 'price': '52.99', 'category': 1, 'description': 'Tai nghe không dây chính hãng với pin 6 giờ'},
    {'name': 'Tai nghe Gaming RGB', 'price': '48.99', 'category': 1, 'description': 'Tai nghe gaming với đèn RGB chuyên nghiệp'},
    {'name': 'Tai nghe nhét tai Hi-Fi', 'price': '38.99', 'category': 1, 'description': 'Tai nghe nhét tai âm thanh Hi-Fi sắc nét'},
    {'name': 'Sạc nhanh 65W PD', 'price': '24.99', 'category': 2, 'description': 'Bộ sạc nhanh 65W hỗ trợ PD cho mọi máy'},
    {'name': 'Sạc dự phòng 20000mAh', 'price': '32.99', 'category': 2, 'description': 'Pin sạc dự phòng 20000mAh sạc nhanh, an toàn'},
    {'name': 'Sạc từ tính Apple', 'price': '28.99', 'category': 2, 'description': 'Bộ sạc từ tính cho Apple Watch và iPhone'},
    {'name': 'Sạc 3 cổng USB-C', 'price': '35.99', 'category': 2, 'description': 'Sạc 3 cổng sạc 3 thiết bị cùng lúc'},
    {'name': 'Cáp USB-C 2M bẻ dẻo', 'price': '9.99', 'category': 3, 'description': 'Cáp USB-C bẻ dẻo, không cứng, bền bỉ'},
    {'name': 'Cáp Lightning chính hãng', 'price': '11.99', 'category': 3, 'description': 'Cáp Lightning chính hãng Apple, truyền dữ liệu nhanh'},
    {'name': 'Cáp Micro USB tròn', 'price': '7.99', 'category': 3, 'description': 'Cáp Micro USB tròn bền bỉ, xoay được'},
    {'name': 'Cáp HDMI 4K siêu dài', 'price': '13.99', 'category': 3, 'description': 'Cáp HDMI 5M hỗ trợ video 4K'},
]

for prod_data in products_data:
    product, _ = Product.objects.get_or_create(
        name=prod_data['name'],
        defaults={
            'price': prod_data['price'],
            'category': categories[prod_data['category']],
            'description': prod_data['description'],
        }
    )

# Create sample orders
users = User.objects.filter(is_superuser=False)[:3]
for idx, user in enumerate(users):
    for order_num in range(1, 3):
        order, created = Order.objects.get_or_create(
            user=user,
            defaults={
                'status': ['Pending', 'Approved', 'Shipping', 'Completed'][order_num % 4],
                'payment_method': ['Credit Card', 'PayPal', 'Bank Transfer'][order_num % 3],
                'total_price': 50 + (order_num * 10),
            }
        )
        if created:
            # Add items to order
            products = Product.objects.all()[:2]
            for i, product in enumerate(products):
                OrderItem.objects.get_or_create(
                    order=order,
                    product=product,
                    defaults={
                        'quantity': i + 1,
                        'price': product.price,
                    }
                )

print("Sample data created successfully!")
print(f"Admin user: admin / admin123")
print(f"Sample users: user1, user2, user3 / password123")
print(f"Categories: {len(categories)} created")
print(f"Products: {Product.objects.count()} created")
print(f"Orders: {Order.objects.count()} created")