import os
import django
from django.conf import settings
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accessory_store.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Product

def create_product_image(product_name, category_name, width=500, height=500):
    """Create a high-quality product image with proper styling"""
    try:
        # Color palette for different categories
        category_colors = {
            'Điện thoại': [(102, 126, 234), (74, 58, 255)],  # Blue-Indigo
            'Ốp lưng điện thoại': [(236, 72, 153), (236, 72, 153)],  # Pink
            'Cường lực': [(200, 200, 200), (150, 150, 150)],  # Gray/Silver
            'Tai nghe': [(34, 197, 94), (22, 163, 74)],  # Green
            'Sạc điện thoại': [(239, 68, 68), (220, 38, 38)],  # Red
            'Cáp USB': [(59, 130, 246), (37, 99, 235)],  # Blue
        }
        
        # Get colors for this category
        colors = category_colors.get(category_name, [(99, 102, 241), (79, 70, 229)])
        primary_color = colors[0]
        accent_color = colors[1]
        
        # Create image with gradient background
        img = Image.new('RGB', (width, height), color=primary_color)
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Draw gradient background
        for i in range(height):
            ratio = i / height
            r = int(primary_color[0] * (1 - ratio * 0.2) + accent_color[0] * (ratio * 0.2))
            g = int(primary_color[1] * (1 - ratio * 0.2) + accent_color[1] * (ratio * 0.2))
            b = int(primary_color[2] * (1 - ratio * 0.2) + accent_color[2] * (ratio * 0.2))
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        
        # Add subtle pattern/texture
        for x in range(0, width, 50):
            for y in range(0, height, 50):
                draw.ellipse(
                    [(x, y), (x + 10, y + 10)],
                    fill=(255, 255, 255, 15)
                )
        
        # Add large semi-transparent circle in background
        circle_size = int(width * 0.6)
        draw.ellipse(
            [(width//2 - circle_size//2, height//2 - circle_size//2),
             (width//2 + circle_size//2, height//2 + circle_size//2)],
            fill=(255, 255, 255, 8)
        )
        
        # Draw product icon/placeholder
        icon_size = int(height * 0.25)
        draw.text(
            (width//2 - icon_size//2, height//2 - icon_size//2 - 40),
            '📱' if 'iPhone' in product_name or 'Galaxy' in product_name or 'Pixel' in product_name or 'OnePlus' in product_name or 'Xiaomi' in product_name
            else '🛡️' if 'Ốp' in product_name
            else '🔨' if 'Cường' in product_name
            else '🎧' if 'Tai' in product_name
            else '🔌' if 'Sạc' in product_name or 'Pin' in product_name
            else '🔗',
            font=None,
            fill=(255, 255, 255)
        )
        
        # Add product info box at bottom
        box_height = 100
        draw.rectangle(
            [(0, height - box_height), (width, height)],
            fill=(0, 0, 0, 150)
        )
        
        # Add text
        draw.text(
            (20, height - box_height + 20),
            category_name,
            fill=(200, 200, 200),
            font=None
        )
        
        # Truncate product name if too long
        display_name = product_name[:35] + "..." if len(product_name) > 35 else product_name
        draw.text(
            (20, height - box_height + 50),
            display_name,
            fill=(255, 255, 255),
            font=None
        )
        
        # Add decorative corner
        draw.rectangle(
            [(0, 0), (80, 80)],
            fill=(255, 255, 255, 10)
        )
        
        # Save to BytesIO
        img_io = BytesIO()
        img.save(img_io, format='PNG', quality=95)
        img_io.seek(0)
        return img_io
    except Exception as e:
        print(f"Error creating image for {product_name}: {e}")
        return None

# Clear old images
import shutil
if os.path.exists('d:\\test2\\media\\products'):
    shutil.rmtree('d:\\test2\\media\\products')
    os.makedirs('d:\\test2\\media\\products')

Product.objects.all().delete()

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

# Smartphone products
smartphone_products = [
    ('Apple iPhone 15 Pro Max 256GB', 'Điện thoại', 1999, 'Điện thoại flagship Apple với màn hình 6.7", chip A17 Pro, camera 48MP đỉnh cao'),
    ('Apple iPhone 15 Pro 256GB', 'Điện thoại', 1699, 'Điện thoại flagship Apple với màn hình 6.1", chip A17 Pro, thiết kế titanium'),
    ('Apple iPhone 15 128GB', 'Điện thoại', 1299, 'Điện thoại iPhone đời mới với Dynamic Island, chip A16 Bionic'),
    ('Apple iPhone 14 Pro 256GB', 'Điện thoại', 1499, 'Điện thoại flagship trước đây với chip A16 Bionic, camera ProRaw'),
    ('Samsung Galaxy S24 Ultra 512GB', 'Điện thoại', 2099, 'Điện thoại flagship Samsung với camera 200MP, chip Snapdragon 8 Gen 3'),
    ('Samsung Galaxy S24 256GB', 'Điện thoại', 1599, 'Điện thoại cao cấp Samsung với màn hình 6.2", chip Exynos 2400'),
    ('Samsung Galaxy A54 128GB', 'Điện thoại', 799, 'Điện thoại tầm trung Samsung với pin 5000mAh, camera 50MP'),
    ('Samsung Galaxy Z Fold5 512GB', 'Điện thoại', 2399, 'Điện thoại gập đặc biệt với hai màn hình AMOLED, chip Snapdragon 8 Gen 2'),
    ('Google Pixel 8 Pro 256GB', 'Điện thoại', 1599, 'Điện thoại flagship Google với AI Magic Eraser, chip Tensor G3'),
    ('Google Pixel 8 128GB', 'Điện thoại', 1099, 'Điện thoại flagship Google với xử lý ảnh AI tuyệt vời'),
    ('Google Pixel 7a 128GB', 'Điện thoại', 599, 'Điện thoại tầm giá với AI photography, chip Tensor'),
    ('OnePlus 12 256GB', 'Điện thoại', 1299, 'Điện thoại flagship OnePlus với sạc 100W, chip Snapdragon 8 Gen 3'),
    ('OnePlus 12R 128GB', 'Điện thoại', 899, 'Điện thoại tầm trung OnePlus với sạc nhanh, pin lớn'),
    ('Xiaomi 14 Ultra 512GB', 'Điện thoại', 1699, 'Điện thoại flagship Xiaomi với camera 50MP, thiết kế camera độc đáo'),
    ('Xiaomi 14 256GB', 'Điện thoại', 1199, 'Điện thoại cao cấp Xiaomi với chip Snapdragon 8 Gen 3'),
    ('Xiaomi Redmi Note 13 Pro 256GB', 'Điện thoại', 699, 'Điện thoại tầm giá tốt với màn hình AMOLED, pin khủng'),
]

accessories_products = [
    ('Ốp lưng Spigen Tough Armor - iPhone 15 Pro', 'Ốp lưng điện thoại', 299, 'Ốp lưng bảo vệ cực tốt, thiết kế chắc chắn, chống va đập'),
    ('Ốp lưng Nillkin CamShield Pro - Samsung S24', 'Ốp lưng điện thoại', 349, 'Ốp lưng bảo vệ camera, thiết kế sang trọng, chất liệu silicone cao cấp'),
    ('Ốp lưng da PU cao cấp - Tất cả máy', 'Ốp lưng điện thoại', 199, 'Ốp lưng da PU chính hãng, cảm giác tay tuyệt vời, bền bỉ'),
    ('Ốp lưng Nillkin Super Frosted Shield', 'Ốp lưng điện thoại', 179, 'Ốp lưng chống trầy, chống bám dấu tay hiệu quả'),
    ('Ốp lưng TPU trong suốt - Tất cả máy', 'Ốp lưng điện thoại', 129, 'Ốp lưng TPU trong suốt, nhìn rõ thiết kế máy'),
    ('Cường lực 9H - iPhone 15 Pro Max', 'Cường lực', 129, 'Kính cường lực 9H, chống xước, dễ lau sạch'),
    ('Cường lực 10D Full Màn - Samsung S24 Ultra', 'Cường lực', 159, 'Kính cường lực 10D bao phủ toàn bộ màn hình, độ cứng cao'),
    ('Cường lực Nillkin 9H - Google Pixel 8', 'Cường lực', 149, 'Kính cường lực 9H chính hãng Nillkin, chống vỡ tốt'),
    ('Cường lực chống nhìn trộm - Tất cả máy', 'Cường lực', 189, 'Kính cường lực với lớp chống nhìn trộm privacy'),
    ('Cường lực dẻo cao cấp - iPhone', 'Cường lực', 169, 'Kính dẻo không vỡ, bảo vệ cực tốt'),
    ('Tai nghe Airpods Pro 2nd Generation', 'Tai nghe', 3499, 'Tai nghe Apple cao cấp với noise cancellation, pin 6 giờ'),
    ('Tai nghe Samsung Galaxy Buds2 Pro', 'Tai nghe', 2699, 'Tai nghe Samsung với ANC, âm thanh 360, pin 5 giờ'),
    ('Tai nghe Sony WF-C700N', 'Tai nghe', 1899, 'Tai nghe Sony với noise cancellation, amply bass'),
    ('Tai nghe JBL Tune 770NC', 'Tai nghe', 2299, 'Tai nghe JBL chuyên âm thanh, ANC hiệu quả'),
    ('Tai nghe Anker Soundcore Liberty 4', 'Tai nghe', 999, 'Tai nghe Anker giá rẻ, chất lượng tốt, pin 10 giờ'),
    ('Sạc nhanh Anker 67W GaN', 'Sạc điện thoại', 649, 'Bộ sạc nhanh 67W hỗ trợ PD, sạc được 3 thiết bị cùng lúc'),
    ('Pin sạc dự phòng Anker 25000mAh', 'Sạc điện thoại', 899, 'Pin sạc dự phòng 25000mAh, sạc nhanh 65W, cực an toàn'),
    ('Sạc nhanh Apple 20W', 'Sạc điện thoại', 599, 'Bộ sạc chính hãng Apple 20W, sạc nhanh cho iPhone'),
    ('Sạc từ tính MagSafe', 'Sạc điện thoại', 799, 'Sạc từ tính cho Apple iPhone 13/14/15, tiện lợi'),
    ('Pin sạc dự phòng Baseus 10000mAh', 'Sạc điện thoại', 449, 'Pin dự phòng nhỏ gọn 10000mAh, sạc nhanh'),
    ('Cáp USB-C Baseus 2M', 'Cáp USB', 149, 'Cáp USB-C bẻ dẻo, không cứng, truyền dữ liệu 480Mbps'),
    ('Cáp Lightning Apple chính hãng', 'Cáp USB', 199, 'Cáp Lightning chính hãng Apple, truyền dữ liệu nhanh, bền bỉ'),
    ('Cáp HDMI 4K 2M Ugreen', 'Cáp USB', 249, 'Cáp HDMI hỗ trợ video 4K@60Hz, bền bỉ, dây dài 2M'),
    ('Cáp USB-A 3.0 dài 3M', 'Cáp USB', 159, 'Cáp USB 3.0 dài 3M, tốc độ cao 5Gbps'),
    ('Cáp sạc Micro USB dài 1.5M', 'Cáp USB', 79, 'Cáp Micro USB chất lượng, dây tròn bền bỉ'),
]

all_products = smartphone_products + accessories_products

print(f"Tạo {len(all_products)} sản phẩm với hình ảnh chất lượng cao...\n")

for idx, (name, cat, price, desc) in enumerate(all_products, 1):
    product, created = Product.objects.get_or_create(
        name=name,
        defaults={
            'price': price,
            'category': categories[cat],
            'description': desc,
        }
    )
    
    if created:
        try:
            img_io = create_product_image(name, cat, width=500, height=500)
            if img_io:
                product.image.save(
                    f"product_{product.id}.png",
                    ContentFile(img_io.read()),
                    save=True
                )
                print(f"✓ {idx:2d}. {name[:50]:<50} - OK")
            else:
                print(f"✗ {idx:2d}. {name[:50]:<50} - Lỗi tạo ảnh")
        except Exception as e:
            print(f"✗ {idx:2d}. {name[:50]:<50} - {str(e)[:30]}")
    else:
        print(f"~ {idx:2d}. {name[:50]:<50} - Đã tồn tại")

print(f"\n{'='*70}")
print(f"✓ Hoàn thành! Tổng cộng: {Product.objects.count()} sản phẩm")
print(f"{'='*70}")
