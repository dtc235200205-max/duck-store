<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Duck Store - E-Commerce Platform (Django)

## ✅ Project Status: COMPLETE WITH USER AUTHENTICATION

### Project Summary
Professional Vietnamese e-commerce platform for selling mobile accessories (ốp lưng, cường lực, tai nghe, etc.)
- **Stack**: Django 6.0.1, Python 3.12, SQLite, Bootstrap 5, Leaflet.js Maps
- **Status**: Fully functional with production-ready features
- **Languages**: Vietnamese UI + English admin
- **Features**: 40+ products, dark mode, location mapping, admin dashboard, user authentication

### Completed Milestones

#### ✅ Phase 1: Project Setup
- [x] Verify that the copilot-instructions.md file in the .github directory is created
- [x] Clarify Project Requirements (Vietnamese e-commerce with 15+ features)
- [x] Scaffold the Project - Django project and store app created

#### ✅ Phase 2: Core Implementation  
- [x] Create database models (8 models: User, Role, Category, Product, Order, OrderItem, Comment, Notification)
- [x] Implement views for all features (20+ view functions)
- [x] Create 25+ HTML templates with Bootstrap 5
- [x] Add admin panel configuration with custom displays
- [x] Implement authentication with password reset
- [x] Create sample data: 5 categories, 40 products, 3 test users

#### ✅ Phase 3: UI/UX Enhancement
- [x] **Complete Vietnamese Localization** - All text translated to Vietnamese
- [x] **Dark Mode Implementation** - Toggle with persistent storage using CSS variables
- [x] **Professional Styling** - Gradient navbars, smooth animations, responsive design
- [x] **Separate Buy/Cart Functions** - "Mua ngay" (direct checkout) vs "Thêm vào giỏ" (add to cart)
- [x] **Location-Based Delivery** - Interactive map with Leaflet.js (free, no API key)
- [x] **Store Rebranding** - Changed from "Accessory Store" to "Duck Store"
- [x] **Vietnamese Products** - Added ốp lưng (phone cases) and cường lực (tempered glass) specific items
- [x] **Improved Forms** - Better login, register, checkout with visual feedback
- [x] **Enhanced Product List** - Category sidebar, product cards with badges, better layout

#### ✅ Phase 4: User Authentication Management
- [x] **User Profile Editing** - Edit first name, last name, email, username
- [x] **Password Change** - Secure password change with validation and session persistence
- [x] **User Dropdown Menu** - Navbar integration showing profile and password change options
- [x] **Social Login UI** - Gmail and Facebook login buttons (backend ready for integration)
- [x] **Enhanced Login Page** - Professional design with social auth button placeholders

#### ✅ Phase 5: Deployment & Documentation
- [x] Compile the Project - All migrations applied, no errors
- [x] Create and Run Task - Development server running on http://localhost:8000/
- [x] Ensure Documentation is Complete - README.md and copilot-instructions.md updated
- [x] Test all user flows - Login, profile editing, password change, browse, add to cart, checkout

### Key Features Implemented

**1. Dark Mode Toggle** ✨
- Replaced CSS brightness filter with proper dark/light theme system
- Used CSS variables for theming: --primary, --dark-bg, --dark-surface, --dark-text, etc.
- Toggle button with icon (moon/sun) that persists via localStorage
- Works on all pages and templates

**2. Complete Vietnamese Translation** 🇻🇳
- All buttons, labels, messages in Vietnamese
- Payment methods: Thẻ tín dụng, Chuyển khoản ngân hàng, Thanh toán khi nhận hàng
- Order statuses: Chờ duyệt, Đã duyệt, Đang giao, Hoàn thành, Đã hủy
- Form labels, error messages, notifications all in Vietnamese

**3. Buy Now vs Add to Cart** 🛒
- Product detail page shows two buttons:
  - "Mua ngay" (Buy Now) - Direct checkout
  - "Thêm vào giỏ" (Add to Cart) - Session-based cart
- New `buy_now` view and URL route
- Separate checkout flows

**4. Location-Based Delivery Map** 🗺️
- Interactive Leaflet.js map (no API key required)
- Address search with Nominatim geocoding
- Click on map to place delivery location marker
- Automatic reverse geocoding to get full address
- Integrated in checkout page

**5. Vietnamese Product Catalog** 📦
- Added 40 products across 5 categories:
  - Ốp lưng điện thoại (8 products): TPU, PU leather, silicone, glass
  - Cường lực (4 products): 9H, 10D, anti-spy, flexible
  - Tai nghe (4 products): Wireless, gaming, hi-fi, true wireless
  - Sạc điện thoại (4 products): 65W PD, power bank, magnetic, multi-port
  - Cáp USB (4 products): USB-C, Lightning, Micro USB, HDMI

**6. Enhanced Visual Design** 🎨
- Gradient backgrounds with shadow effects
- Card hover animations (translateY with shadow)
- Colored icons throughout (primary, accent, success)
- Responsive grid layouts
- Professional form styling with focus rings
- Better button states and transitions

**7. Improved Templates** 📄
- Home: Featured products with badges, better layout
- Product List: Sticky category sidebar, improved grid, "Hot" badges
- Product Detail: Enhanced image display, dual buttons, better comments section
- Cart: Table with full product details, summary card with gradient
- Checkout: Multi-section form with map integration, payment method cards
- Login/Register: Centered cards with demo credentials info
- Order History: Detailed status badges with emojis, better table layout

**8. User Authentication Management** 🔐
- **User Profile Editing**: Edit first name, last name, email, username with validation
- **Password Change**: Secure password change with Django's PasswordChangeForm
- **User Dropdown Menu**: Navbar dropdown showing profile and password change options
- **Social Login UI**: Gmail and Facebook login buttons with placeholders (ready for OAuth integration)
- **Profile Page**: Gradient header, form validation, success messages
- **Change Password Page**: Password requirements display, old password verification

### File Structure
```
d:\test2\
├── accessory_store/          # Main Django project
│   ├── settings.py           # Database, installed apps, media config
│   └── urls.py              # URL routing with media serving
├── store/                    # Main app
│   ├── models.py            # 8 database models
│   ├── views.py             # 20+ view functions including profile & change_password
│   ├── forms.py             # UserProfileForm for profile editing
│   ├── urls.py              # URL patterns (product, cart, profile, change_password, etc.)
│   ├── admin.py             # Admin customizations
│   ├── templates/store/     # 25+ HTML templates (all Vietnamese)
│   │   ├── base.html        # Dark mode toggle, user dropdown menu, CSS variables
│   │   ├── home.html        # Homepage with featured products
│   │   ├── product_list.html# Category sidebar, product grid
│   │   ├── product_detail.html # Dual buy buttons
│   │   ├── cart.html        # Enhanced table with summary
│   │   ├── checkout.html    # Map integration for address
│   │   ├── login.html       # Social auth buttons (Gmail, Facebook)
│   │   ├── register.html    # Form with help text
│   │   ├── profile.html     # User profile editing with gradient header
│   │   ├── change_password.html # Password change form with requirements
│   │   ├── order_list.html  # Detailed status tracking
│   │   └── [17+ more]       # Admin, auth, notifications, etc.
│   └── migrations/          # Database migrations
├── manage.py                # Django management
├── populate_db.py           # Creates 40+ Vietnamese products
├── README.md               # Complete documentation
└── .github/
    └── copilot-instructions.md # This file
```

### Database Schema
- **Product** (40 items): name, price, category, description, image, video
- **Category** (5): ốp lưng, tai nghe, sạc, cáp, cường lực
- **Order**: user, status, payment_method, delivery_address, total_price
- **OrderItem**: order, product, quantity, price
- **Comment**: user, product, text, timestamp
- **Notification**: user, message, timestamp

### Development Server
- **URL**: http://localhost:8000
- **Admin**: http://localhost:8000/admin (admin/admin123)
- **Demo Users**: user1, user2, user3 (password: password123)

### CSS Variables (Dark Mode Support)
```css
--primary: #6366f1
--primary-dark: #4f46e5
--accent: #ec4899
--success: #10b981
--light-bg: #f8fafc
--light-text: #0f172a
--border-color: #e2e8f0
--dark-bg: #0f172a
--dark-surface: #1e293b
--dark-text: #f1f5f9
--dark-border: #334155
```

### Forms & User Management
**store/forms.py:**
- `UserProfileForm` - ModelForm for editing first_name, last_name, email, username
- Uses Bootstrap form-control styling
- Integrated with profile view for seamless user info updates

**Authentication Views (store/views.py):**
- `profile()` - Handles GET (display form) and POST (save changes) for user profile editing
- `change_password()` - Handles password change with Django's PasswordChangeForm and session update
- Both views require @login_required decorator
- Success messages displayed using Django messages framework

**URL Routes (store/urls.py):**
- `/profile/` - User profile editing page
- `/change-password/` - Password change form

### Next Steps (Optional Future Enhancements)
1. **Social Authentication** - django-allauth for Gmail/Facebook OAuth login
2. Email notifications for order status updates
3. User profile page with address book
4. Wishlist/favorites feature
5. Product reviews with star ratings
6. Inventory management
7. Mobile app (React Native)
8. Payment gateway integration (Stripe, etc.)
9. SEO optimization and sitemap
10. Multi-language support (English, Chinese)

### Running the Project
```bash
# Start development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Populate sample data
python populate_db.py
```

### Project Complete! ✅
All requested features have been implemented:
- ✅ Complete Vietnamese translation
- ✅ Working dark mode with toggle
- ✅ Professional UI with gradients and animations
- ✅ Separate "Mua ngay" and "Thêm giỏ" buttons
- ✅ Vietnamese product catalog (ốp lưng, cường lực, tai nghe)
- ✅ Store name: "Duck Store"
- ✅ Map-based location selection for delivery
- ✅ User profile editing and password change
- ✅ Social login UI with Gmail and Facebook buttons (placeholders)

  - User is provided with clear instructions to debug/launch the project

Before starting a new task in the above plan, update progress in the plan.
-->
- Work through each checklist item systematically.
- Keep communication concise and focused.
- Follow development best practices.