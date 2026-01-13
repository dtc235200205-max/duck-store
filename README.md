# 🦆 Duck Store - Django E-Commerce Platform

A professional Vietnamese e-commerce platform for selling mobile accessories. Built with Django, featuring complete product management, shopping cart, checkout with location mapping, and comprehensive admin dashboard.

## 📋 Project Overview

**Duck Store** is a full-featured e-commerce web application specialized for Vietnamese market, designed for managing and selling premium mobile accessories. It provides a complete solution with intuitive Vietnamese UI, dark mode support, and advanced features like location-based delivery selection.

### Key Features

✅ **Comprehensive Product Catalog**
- 40+ products in 5 categories: Ốp lưng, Tai nghe, Sạc điện thoại, Cáp USB, Cường lực
- Product search and filtering by category
- Detailed product views with description and pricing in Vietnamese
- Product comments and customer reviews
- Support for product images and videos

✅ **User Management & Authentication**
- User registration and login
- Password reset via email
- Secure session-based shopping cart
- Role-based admin access

✅ **Shopping & Checkout**
- **Dual Purchase Modes**: 
  - "Mua ngay" - Direct checkout for immediate purchase
  - "Thêm vào giỏ" - Add to cart for later
- **Location-Based Delivery**: Interactive map using Leaflet.js (free, no API key needed)
- Address search with geocoding
- Multiple payment methods: Credit Card, Debit Card, PayPal, Bank Transfer, COD
- Discount code support
- Real-time cart summary

✅ **Order Management**
- Complete order tracking with status: Chờ duyệt → Đã duyệt → Đang giao → Hoàn thành/Đã hủy
- Order history for customers
- Admin order management interface
- Detailed order summaries with product breakdown

✅ **User Interface**
- **Complete Vietnamese Localization**: All text, buttons, and messages in Vietnamese
- **Professional Dark Mode**: Toggle between light and dark themes with persistent storage
- **Modern Design**: Gradient navbars, smooth animations, responsive card layouts
- **Mobile-Friendly**: Fully responsive design for all screen sizes
- **Bootstrap 5 + Font Awesome**: Professional icon usage throughout

✅ **Admin Dashboard**
- Sales statistics and revenue tracking
- Product management (create, edit, delete)
- User management and permissions
- Order analytics and status updates
- Product popularity reports
- Business performance metrics

✅ **Advanced Features**
- 🤖 AI Shopping Assistant (consultation recommendations)
- 🔔 Notification system for order updates
- 🎁 QR Code donation feature
- 🌙/☀️ Dark/Light mode toggle with CSS variables
- 📸 Product image and video upload support
- 💬 Product comments and customer feedback
- 🗺️ Map-based location selection using Leaflet.js
- 📱 Progressive Web App ready design

## 🛠️ Technology Stack

- **Backend**: Python 3.12.9 + Django 6.0.1
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **ORM**: Django ORM
- **Authentication**: Django Authentication System
- **Image Processing**: Pillow

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment support

### Step 1: Clone or Extract the Project
```bash
cd d:\test2
```

### Step 2: Activate Virtual Environment
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install django pillow
```

### Step 4: Run Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Admin)
The admin user is already created with:
- **Username**: `admin`
- **Password**: `admin123`
- **Email**: `admin@example.com`

Sample users are also available:
- **user1**, **user2**, **user3** with password `password123`

### Step 6: Populate Database with Sample Data
```bash
python populate_db.py
```

This creates:
- 5 categories (Phone Cases, Headphones, Chargers, etc.)
- 20 sample products
- 3 sample customer accounts
- Sample orders for testing

## 🚀 Running the Application

Start the development server:
```bash
python manage.py runserver 0.0.0.0:8000
```

Access the application at: **http://localhost:8000**

### Default Login Credentials

**Admin Account** (Full Access)
- Username: `admin`
- Password: `admin123`
- Access: http://localhost:8000/admin/

**Customer Accounts**
- Username: `user1`, `user2`, `user3`
- Password: `password123`

## 📂 Project Structure

```
accessory_store/
├── accessory_store/          # Django project settings
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── store/                    # Main app
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── urls.py              # App URL routing
│   ├── admin.py             # Admin configuration
│   ├── forms.py             # Django forms
│   ├── templates/store/     # HTML templates
│   │   ├── base.html        # Base template with navbar
│   │   ├── home.html        # Homepage
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── order_list.html
│   │   ├── order_detail.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── admin_dashboard.html
│   │   ├── manage_products.html
│   │   ├── manage_users.html
│   │   ├── statistics.html
│   │   └── ...
│   ├── migrations/          # Database migrations
│   └── static/              # CSS, JS, images
│
├── media/                   # User-uploaded files (products, avatars)
├── manage.py                # Django management command
├── populate_db.py           # Sample data script
└── db.sqlite3              # Development database
```

## 🗄️ Database Models

### Core Models
1. **User** (Django built-in)
   - Username, Email, Password
   - Staff and Superuser flags

2. **Role**
   - name: Role name (Admin, Customer, etc.)

3. **Category**
   - name: Product category name

4. **Product**
   - name, price, description
   - image, video (file uploads)
   - category_id (Foreign Key)

5. **Order**
   - user_id (Foreign Key)
   - status, total_price, created_at
   - payment_method, discount_code
   - delivery_address

6. **OrderItem**
   - order_id, product_id (Foreign Keys)
   - quantity, price

7. **Comment**
   - product_id, user_id (Foreign Keys)
   - text, created_at

8. **Notification**
   - user_id (Foreign Key)
   - message, is_read, created_at

## 🔑 Key Features Explained

### Shopping Cart
- Add items to cart (session-based)
- Update quantities
- Remove items
- Persistent cart data

### Checkout Process
- Enter delivery address
- Select payment method
- Apply discount codes (if available)
- Order confirmation

### Order Tracking
- View order history
- Track order status
- View order details and items
- Download order receipt

### Admin Features
- **Dashboard**: Quick overview of stats
- **Product Management**: Add/edit/delete products with images
- **User Management**: View and manage user accounts
- **Statistics**: Revenue, order count, top products
- **Order Management**: View and update order status

### Advanced Features
- **AI Consultation**: Ask the AI assistant for product recommendations
- **Notifications**: Real-time user notifications
- **QR Donate**: Support the project via QR code
- **Theme Toggle**: Switch between light and dark modes
- **Product Comments**: Customers can leave reviews

## 🔒 Security Features

- CSRF protection (Django built-in)
- Password hashing and validation
- Admin authentication required
- Session-based authentication
- Permission checks on admin views
- File upload validation (images/videos)

## 📊 Admin Panel Features

Access admin panel at: **http://localhost:8000/admin/**

### Available Admin Features:
1. **User Management**: Create, edit, and deactivate users
2. **Product Management**: Full CRUD operations for products
3. **Category Management**: Organize products into categories
4. **Order Management**: View orders with detailed filtering
5. **Comments Moderation**: Review and manage product comments
6. **Notifications**: Send notifications to users

## 🎨 UI/UX Features

- **Responsive Bootstrap Design**: Works on all devices
- **Navigation Bar**: Easy access to main sections
- **Search Functionality**: Find products by name/description
- **Category Filtering**: Browse by product category
- **Dark/Light Theme**: Toggle background brightness
- **User Feedback**: Flash messages for all actions
- **Clean Forms**: Bootstrap-styled input forms
- **Card-based Layouts**: Modern product display
- **Sticky Admin Cards**: Convenient order summary

## 🧪 Testing

To test the application:

1. **User Registration**: Create a new account
2. **Browse Products**: Search and filter products
3. **Add to Cart**: Add items and manage cart
4. **Checkout**: Complete the purchase process
5. **Order Tracking**: View order history and status
6. **Admin Access**: Login as admin to manage content
7. **Comments**: Leave reviews on products

## 🚀 Deployment

For production deployment:

1. Update `DEBUG = False` in settings.py
2. Set `ALLOWED_HOSTS` with your domain
3. Use PostgreSQL instead of SQLite
4. Configure static files and media serving
5. Set up SSL/HTTPS
6. Use a production WSGI server (Gunicorn, uWSGI)
7. Configure email backend for password reset

## 📧 Email Configuration

To enable email functionality (password reset, notifications):

Add to `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port
python manage.py runserver 8001
```

### Database Issues
```bash
# Reset database
python manage.py migrate
python populate_db.py
```

### Missing Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 📝 API Endpoints

### Public Routes
- `GET /` - Home page
- `GET /products/` - Product list
- `GET /products/<id>/` - Product detail
- `POST /register/` - User registration
- `POST /login/` - User login
- `POST /password-reset/` - Reset password

### Protected Routes (Login Required)
- `GET /cart/` - Shopping cart
- `POST /add-to-cart/<product_id>/` - Add to cart
- `POST /checkout/` - Place order
- `GET /orders/` - Order history
- `GET /orders/<order_id>/` - Order detail

### Admin Routes
- `/admin/` - Admin panel
- `/admin-dashboard/` - Admin dashboard
- `/manage-products/` - Product management
- `/manage-users/` - User management
- `/statistics/` - Sales statistics

## 🎯 Future Enhancements

- [ ] Real-time messaging system with WebSockets
- [ ] Map-based delivery address selection
- [ ] Email notifications for order status
- [ ] SMS notifications via Twilio
- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] Advanced analytics and reporting
- [ ] Product inventory management
- [ ] Wishlist feature
- [ ] User reviews and ratings
- [ ] Mobile app (React Native)

## 📄 License

This project is created for educational and demonstration purposes.

## 👨‍💻 Support

For issues, questions, or suggestions, please create an issue or contact the development team.

---

**Happy Shopping! 🎉**

Built with ❤️ using Django | Made for learning and demo purposes