from django.contrib import admin
from .models import CustomerInquiry
from .forms import CustomerInquiryFormForAdmin

# Register your models here.


class CustomerInquiryAdmin(admin.ModelAdmin):

    form = CustomerInquiryFormForAdmin
    list_display = ('full_name',  'phone_number', 'id', 'timestamp',
                    'inquiry_is_processed',)
    list_filter = ('inquiry_is_processed',)

    fieldsets = (

        ('Bio Data', {
         'fields': ('full_name',)}),
        ('Contact Info', {
         'fields': ('phone_number', 'email',)}),
        ('Main Inquiry', {
            'fields': ('message',)}),
        ('Status', {
         'fields': ('inquiry_is_processed',)}),
    )

    add_fieldsets = (

        ('Bio Data', {
         'fields': ('full_name',)}),
        ('Contact Info', {
         'fields': ('phone_number', 'email',)}),
        ('Main Inquiry', {
            'fields': ('message',)}),
    )

    search_fields = ('full_name',
                     'phone_number', 'email', 'id')

    ordering = ('-timestamp',)
    filter_horizontal = ()


admin.site.register(CustomerInquiry, CustomerInquiryAdmin)
