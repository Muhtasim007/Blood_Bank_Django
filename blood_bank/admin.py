from django.contrib import admin
from django.urls import path, include
from .models import BloodGroup, Donor, Recipient,Recipient2, Profile
from datetime import date
from .models import BloodInventory

@admin.register(BloodGroup)
class BloodGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'donation_date', 'is_active')  # Corrected to 'donation_date'
    search_fields = ('user__username', 'blood_group__name', 'location')
    list_filter = ('blood_group', 'is_active', 'donation_date')
    ordering = ['-donation_date']

    def age(self, obj):
        """Calculate and display donor's age."""
        return obj.age()

    age.short_description = 'Age'

    def is_eligible_for_donation(self, obj):
        """Check and display if the donor is eligible for donation."""
        return obj.is_eligible_for_donation()

    is_eligible_for_donation.short_description = 'Eligible for Donation'
    is_eligible_for_donation.boolean = True  # Display as a boolean in admin panel

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
    search_fields = ('user__username', 'phone_number', 'address')

# Custom admin configuration for Recipient
@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'blood_group', 'contact', 'emergency_contact_name', 
        'emergency_contact_phone', 'needed_date', 'created_at', 'age'
    )
    search_fields = ('full_name', 'blood_group__name', 'contact', 'nid_number')
    ordering = ['-needed_date']
    list_filter = ('blood_group', 'created_at', 'needed_date')

    def age(self, obj):
        """Calculate and display recipient's age."""
        if obj.birth_date:
            today = date.today()
            age = today.year - obj.birth_date.year - ((today.month, today.day) < (obj.birth_date.month, obj.birth_date.day))
            return age
        return None

    age.short_description = 'Age'
    
    #recipiemt2
# @admin.register(Recipient2)
# class Recipient2Admin(admin.ModelAdmin):
#     list_display = ('user', 'username', 'full_name', 'blood_group', 'birth_date', 'address', 'contact', 'nid_number', 'by_date')
    
from django.contrib import admin
from .models import Recipient2

@admin.register(Recipient2)
class Recipient2Admin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'blood_group', 'birth_date', 'address', 'contact', 'nid_number', 'by_date', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'blood_group')
    actions = ['approve_requests', 'reject_requests']  # Add custom actions

    def approve_requests(self, request, queryset):
        queryset.update(status='Approved')
        self.message_user(request, "Selected requests have been approved.")
    approve_requests.short_description = "Approve selected requests"

    def reject_requests(self, request, queryset):
        queryset.update(status='Rejected')
        self.message_user(request, "Selected requests have been rejected.")
    reject_requests.short_description = "Reject selected requests"

#inventory


# class BloodInventoryAdmin(admin.ModelAdmin):
#  list_display = ('blood_type', 'units', 'capacity')
# search_fields = ('blood_type',)
# list_editable = ('units', 'capacity')  # Allows editing of units and capacity directly in the list view
# admin.site.register(BloodInventory, BloodInventoryAdmin)


from django.contrib import admin
from .models import BloodInventory

class BloodInventoryAdmin(admin.ModelAdmin):
    list_display = ('blood_type', 'units', 'capacity')  # Fields to display
    list_editable = ('units', 'capacity')  # Fields to allow inline editing
    list_display_links = ('blood_type',)  # Only 'blood_type' is clickable

admin.site.register(BloodInventory, BloodInventoryAdmin)


#New donor reg

from django.contrib import admin
from .models import DonorReg

@admin.register(DonorReg)
class DonorRegAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'blood_group','last_donation_date', 'phone', 'email', 'emergency_donor', 'status')
    search_fields = ('username', 'full_name', 'blood_group', 'email')
    list_filter = ('blood_group', 'emergency_donor')
    
    #trial new
    list_editable = ('status',)
    # list_filter = ('status', 'blood_group')
    actions = ['approve_requests', 'reject_requests']  # Add custom actions

    def approve_requests(self, request, queryset):
        queryset.update(status='Approved')
        self.message_user(request, "Selected requests have been approved.")
    approve_requests.short_description = "Approve selected requests"

    def reject_requests(self, request, queryset):
        queryset.update(status='Rejected')
        self.message_user(request, "Selected requests have been rejected.")
    reject_requests.short_description = "Reject selected requests"
