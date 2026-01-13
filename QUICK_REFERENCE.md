# 🦆 Duck Store - Quick Reference Guide

## 🚀 Quick Start

```bash
# 1. Navigate to project
cd d:\test2

# 2. Start server
python manage.py runserver

# 3. Open browser
http://localhost:8000
```

## 🔑 Demo Credentials

### Admin Access
- **URL**: http://localhost:8000/admin
- **Username**: `admin`
- **Password**: `admin123`

### Customer Demo
- **Username**: `user1`
- **Password**: `password123`

## 🎯 Key Features at a Glance

### Dark Mode Toggle ☀️/🌙
- Click moon/sun icon in top-right navbar
- Toggles between light and dark theme
- Persists with browser refresh

### Dual Purchase Buttons 🛒
- **"Mua ngay"** (Green) - Buy immediately, goes to checkout
- **"Thêm vào giỏ"** (Outline) - Add to cart for later

### Location-Based Delivery 🗺️
- In checkout page, search for location
- Click on map to place marker
- Address auto-fills from geocoding

### Product Categories 📦
- Ốp lưng điện thoại (Phone Cases)
- Cường lực (Tempered Glass)
- Tai nghe (Headphones)
- Sạc điện thoại (Chargers)
- Cáp USB (Cables)

## 🛣️ Important URLs

```
Home:               http://localhost:8000
Products:           http://localhost:8000/products/
Shopping Cart:      http://localhost:8000/cart/
Checkout:           http://localhost:8000/checkout/
My Orders:          http://localhost:8000/orders/
Login:              http://localhost:8000/login/
Register:           http://localhost:8000/register/
Admin Panel:        http://localhost:8000/admin/
Notifications:      http://localhost:8000/notifications/
```

## 📂 Key Files to Modify

### Adding New Products
- **File**: `populate_db.py`
- Edit `products_data` list
- Run: `python populate_db.py`

### Changing Colors
- **File**: `store/templates/store/base.html`
- Find: `:root { --primary: ... }`
- Change CSS variables

### Adding New Pages
- Create view in: `store/views.py`
- Add URL in: `store/urls.py`
- Create template in: `store/templates/store/`

### Updating Payment Methods
- **File**: `store/templates/store/checkout.html`
- Add new radio button option
- Update view if needed

## 🔧 Common Commands

```bash
# Run server
python manage.py runserver

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Shell access
python manage.py shell

# Populate test data
python populate_db.py

# Collect static files
python manage.py collectstatic
```

## 📊 Database Info

- **Type**: SQLite (development)
- **File**: `db.sqlite3`
- **Models**: 8 tables
- **Test Data**: 40 products, 5 categories, 3 users

## 🎨 Color Reference

| Name | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary | Indigo | #6366f1 | Main buttons, links |
| Primary Dark | Dark Indigo | #4f46e5 | Button hover |
| Accent | Pink | #ec4899 | Special highlights |
| Success | Green | #10b981 | Positive actions |
| Dark BG | Navy | #0f172a | Dark mode background |

## 🐛 Troubleshooting

### Server won't start
```bash
# Kill existing process
taskkill /IM python.exe /F

# Clear migrations
rm -r store/migrations/0*.py

# Re-migrate
python manage.py migrate
```

### Dark mode not working
- Clear browser cache
- Check localStorage in DevTools
- Ensure JavaScript is enabled

### Products not showing
- Run: `python populate_db.py`
- Check admin panel for products
- Verify database is migrated

### Map not loading
- Check internet connection
- Verify Leaflet CDN is accessible
- Check browser console for errors

## 📱 Responsive Design

Works on:
- ✅ Desktop (1920px+)
- ✅ Tablet (768px - 1024px)
- ✅ Mobile (320px - 767px)

## 🔒 Admin Functions

### In Admin Panel
1. Add/edit/delete products
2. Manage users and permissions
3. View and update orders
4. Manage categories
5. View notifications

### Via Dashboard
- Access at: `/admin-dashboard/`
- View sales statistics
- Track revenue
- Monitor top products

## 💡 Tips

1. **Use Demo Account**: Quick testing without registration
2. **Test Dark Mode**: Click moon icon to test all pages
3. **Try Both Purchase Flows**: Compare "Mua ngay" vs "Thêm giỏ"
4. **Check Map Feature**: Test location search in checkout
5. **View Dark Mode**: All components support dark theme

## 🎓 Learning Resources

- **Django Docs**: https://docs.djangoproject.com/
- **Bootstrap Docs**: https://getbootstrap.com/
- **Leaflet Docs**: https://leafletjs.com/
- **Font Awesome**: https://fontawesome.com/

## 📞 Support

For issues or questions:
1. Check logs in terminal
2. Use Django shell: `python manage.py shell`
3. Review error messages in browser console
4. Check database: `python manage.py dbshell`

---

**Status**: ✅ Ready to use
**Last Update**: January 13, 2026
**Server**: Running on http://localhost:8000
