from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('vehicle-management/', views.vehicle_management, name='vehicle_management'),
    path('add-vehicle-type/', views.add_vehicle_type, name='add_vehicle_type'),
    path('add-vehicle-company/', views.add_vehicle_company, name='add_vehicle_company'),
    path('add-model/', views.add_model, name='add_model'),
    path('add-features/', views.add_features, name='add_features'),
    path('toggle-vehicle-type/<int:id>/', views.toggle_vehicle_type, name='toggle_vehicle_type'),
    path('toggle-vehicle-company/<int:id>/', views.toggle_vehicle_company, name='toggle_vehicle_company'),
    path('toggle-model/<int:id>/', views.toggle_model, name='toggle_model'),
    path('toggle-features/<int:id>/', views.toggle_features, name='toggle_features'),
    path('vendor-success/', views.vendor_success, name='vendor_success'),
    path('manage-vendor-applications/', views.manage_vendor_applications, name='manage_vendor_applications'),
    path('approve-vendor/<int:vendor_id>/', views.approve_vendor, name='approve_vendor'),
    path('reject-vendor/<int:vendor_id>/', views.reject_vendor, name='reject_vendor'),
    path('active-vendors/', views.active_vendors, name='active_vendors'),
    path('deactivate-vendor/<int:vendor_id>/', views.deactivate_vendor, name='deactivate_vendor'),
    path('deactivated-vendors/', views.deactivated_vendors, name='deactivated_vendors'),
    path('activate-vendor/<int:vendor_id>/', views.activate_vendor, name='activate_vendor'),
    path('all-customers/', views.all_customers, name='all_customers'),
    path('toggle-customer-status/<int:user_id>/', views.toggle_customer_status, name='toggle_customer_status'),
    path('all-vendors/', views.all_vendors, name='all_vendors'),
    path('active-customers/', views.active_customers, name='active_customers'),
    path('deactivate-customer/<int:user_id>/', views.deactivate_customer, name='deactivate_customer'),
    path('deactivated-customers/', views.deactivated_customers, name='deactivated_customers'),
    path('reactivate-customer/<int:user_id>/', views.reactivate_customer, name='reactivate_customer'),
]