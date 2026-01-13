import os
import django
from django.conf import settings
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image, ImageDraw

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accessory_store.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Product

def create_placeholder_image(product_name, color=(102, 126, 234), width=400, height=400):
    """Create a simple placeholder image for products"""
    try:
        img = Image.new('RGB', (width, height), color=color)
        draw = ImageDraw.Draw(img)
        
        # Add gradient effect
        for i in range(height):
            ratio = i / height
            r = int(color[0] * (1 - ratio * 0.3))
            g = int(color[1] * (1 - ratio * 0.3))
            b = int(color[2] * (1 - ratio * 0.3))
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        
        # Add emoji/icon based on product type
        emoji_map = {
            'iPhone': '📱',
            'Samsung': '📱',
            'Google': '📱',
            'OnePlus': '📱',
            'Xiaomi': '📱',
            'Ốp': '🛡️',
            'Cường': '🔨',
            'Tai': '🎧',
            'Sạc': '🔌',
            'Cáp': '🔗',
        }
        
        emoji = '📱'
        for key, value in emoji_map.items():
            if key in product_name:
                emoji = value
                break
        
        # Draw emoji in center
        draw.text((width//2 - 40, height//2 - 60), emoji, fill=(255, 255, 255))
        
        # Save to BytesIO
        img_io = BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)
        return img_io
    except Exception as e:
        print(f"Error creating image: {e}")
        return None

# Clear existing products (optional)
Product.objects.filter(name__icontains='iPhone').delete()
Product.objects.filter(name__icontains='Samsung').delete()
Product.objects.filter(name__icontains='Google').delete()

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
        defaults={'email': f'user{i+1}@example.com'}
    )
    if not user.check_password('password123'):
        user.set_password('password123')
        user.save()

# Create categories
categories_data = [
    'Điện thoại',
    'Ốp lưng điện thoại',
    'Cường lực',
    'Tai nghe',
    'Sạc điện thoại',
    'Cáp USB',
]

categories = {}
for cat_name in categories_data:
    cat, _ = Category.objects.get_or_create(name=cat_name)
    categories[cat_name] = cat

# Smartphone products with colors
smartphone_products = [
    # iPhones
    {
        'name': 'Apple iPhone 15 Pro Max 256GB',
        'price': 1999,
        'category': 'Điện thoại',
        'description': 'Điện thoại flagship Apple với màn hình 6.7", chip A17 Pro, camera 48MP đỉnh cao',
        'color': (100, 100, 120)
    },
    {
        'name': 'Apple iPhone 15 Pro 256GB',
        'price': 1699,
        'category': 'Điện thoại',
        'description': 'Điện thoại flagship Apple với màn hình 6.1", chip A17 Pro, thiết kế titanium',
        'color': (80, 80, 100)
    },
    {
        'name': 'Apple iPhone 15 128GB',
        'price': 1299,
        'category': 'Điện thoại',
        'description': 'Điện thoại iPhone đời mới với Dynamic Island, chip A16 Bionic',
        'color': (100, 110, 130)
    },
    {
        'name': 'Apple iPhone 14 Pro 256GB',
        'price': 1499,
        'category': 'Điện thoại',
        'description': 'Điện thoại flagship trước đây với chip A16 Bionic, camera ProRaw',
        'color': (90, 95, 110)
    },
    
    # Samsung Galaxy
    {
        'name': 'Samsung Galaxy S24 Ultra 512GB',
        'price': 2099,
        'category': 'Điện thoại',
        'description': 'Điện thoại flagship Samsung với camera 200MP, chip Snapdragon 8 Gen 3',
        'color': (80, 100, 140)
    },
    {
        'name': 'Samsung Galaxy S24 256GB',
        'price': 1599,
        'category': 'Điện thoại',
        'description': 'Điện thoại cao cấp Samsung với màn hình 6.2", chip Exynos 2400',
        'color': (100, 120, 160)
    },
    {
        'name': 'Samsung Galaxy A54 128GB',
        'price': 799,
        'category': 'Điện thoại',
        'description': 'Điện thoại tầm trung Samsung với pin 5000mAh, camera 50MP',
        'color': (120, 100, 140)
    },
    {
        'name': 'Samsung Galaxy Z Fold5 512GB',
        'price': 2399,
        'category': 'Điện thoại',
        'description': 'Điện thoại gập đặc biệt với hai màn hình AMOLED, chip Snapdragon 8 Gen 2',
        'color': (110, 105, 125)
    },
    
    # Google Pixel
    {
        'name': 'Google Pixel 8 Pro 256GB',
        'price': 1599,
        'category': 'Điện thoại',
        'description': 'Điện thoại flagship Google với AI Magic Eraser, chip Tensor G3',
        'color': (130, 110, 160)
    },
    {
        'name': 'Google Pixel 8 128GB',
        'price': 1099,
        'category': 'Điện thoại',
        'description': 'Điện thoại flagship Google với xử lý ảnh AI tuyệt vời',
        'color': (120, 100, 150)
    },
    {
        'name': 'Google Pixel 7a 128GB',
        'price': 599,
        'category': 'Điện thoại',
        'description': 'Điện thoại tầm giá với AI photography, chip Tensor',
        'color': (140, 120, 170)
    },
    
    # OnePlus
    {
        'name': 'OnePlus 12 256GB',
        'price': 1299,
        'category': 'Điện thoại',
        'description': 'Điện thoại flagship OnePlus với sạc 100W, chip Snapdragon 8 Gen 3',
        'color': (100, 80, 120)
    },
    {
        'name': 'OnePlus 12R 128GB',
        'price': 899,
        'category': 'Điện thoại',
        'description': 'Điện thoại tầm trung OnePlus với sạc nhanh, pin lớn',
        'color': (110, 90, 130)
    },
    
    # Xiaomi
    {
        'name': 'Xiaomi 14 Ultra 512GB',
        'price': 1699,
        'category': 'Điện thoại',
        'description': 'Điện thoại flagship Xiaomi với camera 50MP, thiết kế camera độc đáo',
        'color': (120, 100, 140)
    },
    {
        'name': 'Xiaomi 14 256GB',
        'price': 1199,
        'category': 'Điện thoại',
        'description': 'Điện thoại cao cấp Xiaomi với chip Snapdragon 8 Gen 3',
        'color': (130, 110, 150)
    },
    {
        'name': 'Xiaomi Redmi Note 13 Pro 256GB',
        'price': 699,
        'category': 'Điện thoại',
        'description': 'Điện thoại tầm giá tốt với màn hình AMOLED, pin khủng',
        'color': (140, 120, 160)
    },
]

# Accessories
accessories_data = [
    {
        'name': 'Ốp lưng Spigen Tough Armor - iPhone 15 Pro',
        'price': 299,
        'category': 'Ốp lưng điện thoại',
        'description': 'Ốp lưng bảo vệ cực tốt, thiết kế chắc chắn, chống va đập',
        'color': (80, 80, 80)
    },
    {
        'name': 'Ốp lưng Nillkin CamShield Pro - Samsung S24',
        'price': 349,
        'category': 'Ốp lưng điện thoại',
        'description': 'Ốp lưng bảo vệ camera, thiết kế sang trọng, chất liệu silicone cao cấp',
        'color': (100, 100, 100)
    },
    {
        'name': 'Ốp lưng da PU cao cấp - Tất cả máy',
        'price': 199,
        'category': 'Ốp lưng điện thoại',
        'description': 'Ốp lưng da PU chính hãng, cảm giác tay tuyệt vời, bền bỉ',
        'color': (120, 80, 60)
    },
    {
        'name': 'Cường lực 9H - iPhone 15 Pro Max',
        'price': 129,
        'category': 'Cường lực',
        'description': 'Kính cường lực 9H, chống xước, dễ lau sạch',
        'color': (200, 200, 200)
    },
    {
        'name': 'Cường lực 10D Full Màn - Samsung S24 Ultra',
        'price': 159,
        'category': 'Cường lực',
        'description': 'Kính cường lực 10D bao phủ toàn bộ màn hình, độ cứng cao',
        'color': (180, 180, 180)
    },
    {
        'name': 'Tai nghe Airpods Pro 2nd Generation',
        'price': 3499,
        'category': 'Tai nghe',
        'description': 'Tai nghe Apple cao cấp với noise cancellation, pin 6 giờ',
        'color': (200, 200, 200)
    },
    {
        'name': 'Tai nghe Samsung Galaxy Buds2 Pro',
        'price': 2699,
        'category': 'Tai nghe',
        'description': 'Tai nghe Samsung với ANC, âm thanh 360, pin 5 giờ',
        'color': (150, 150, 150)
    },
    {
        'name': 'Sạc nhanh Anker 67W GaN',
        'price': 649,
        'category': 'Sạc điện thoại',
        'description': 'Bộ sạc nhanh 67W hỗ trợ PD, sạc được 3 thiết bị cùng lúc',
        'color': (230, 100, 100)
    },
    {
        'name': 'Pin sạc dự phòng Anker 25000mAh',
        'price': 899,
        'category': 'Sạc điện thoại',
        'description': 'Pin sạc dự phòng 25000mAh, sạc nhanh 65W, cực an toàn',
        'color': (220, 120, 40)
    },
    {
        'name': 'Cáp USB-C Baseus 2M',
        'price': 149,
        'category': 'Cáp USB',
        'description': 'Cáp USB-C bẻ dẻo, không cứng, truyền dữ liệu 480Mbps',
        'color': (100, 100, 120)
    },
    {
        'name': 'Cáp Lightning Apple chính hãng',
        'price': 199,
        'category': 'Cáp USB',
        'description': 'Cáp Lightning chính hãng Apple, truyền dữ liệu nhanh, bền bỉ',
        'color': (220, 220, 220)
    },
    {
        'name': 'Cáp HDMI 4K 2M Ugreen',
        'price': 249,
        'category': 'Cáp USB',
        'description': 'Cáp HDMI hỗ trợ video 4K@60Hz, bền bỉ, dây dài 2M',
        'color': (50, 50, 50)
    },
]

# Add all products
all_products = smartphone_products + accessories_data

print(f"Adding {len(all_products)} products...")

for prod_data in all_products:
    product, created = Product.objects.get_or_create(
        name=prod_data['name'],
        defaults={
            'price': prod_data['price'],
            'category': categories[prod_data['category']],
            'description': prod_data['description'],
        }
    )
    
    if created and not product.image:
        # Create and assign placeholder image
        try:
            img_io = create_placeholder_image(prod_data['name'], color=prod_data['color'])
            if img_io:
                product.image.save(
                    f"{product.id}_placeholder.png",
                    ContentFile(img_io.read()),
                    save=True
                )
                print(f"✓ Created {prod_data['name']} with image")
            else:
                print(f"✓ Created {prod_data['name']} (no image)")
        except Exception as e:
            print(f"✗ Error with {prod_data['name']}: {e}")
    elif not created:
        print(f"~ Already exists: {prod_data['name']}")

print("\n✓ Database population complete!")
print(f"Total products: {Product.objects.count()}")
print(f"Total categories: {Category.objects.count()}")
print(f"Total users: {User.objects.count()}")
