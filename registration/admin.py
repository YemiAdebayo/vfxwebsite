from django.contrib import admin
from .models import Register
from .forms import RegistrationFormForAdmin

class RegisterAdmin(admin.ModelAdmin):

    form = RegistrationFormForAdmin
    list_display = ('first_name', 'last_name', 'phone_number', 'course', 'id','timestamp',
                    'registration_is_processed',)
    list_filter = ('registration_is_processed',)

    fieldsets = (

        ('Bio Data', {
         'fields': ('first_name', 'last_name',)}),
        ('Contact Info', {
         'fields': ('phone_number', 'email',)}),
         ('Study Interest', {
         'fields': ('course',)}),
        ('Status', {
         'fields': ('registration_is_processed',)}),
    )

    add_fieldsets = (

        ('Bio Data', {
         'fields': ('first_name', 'last_name',)}),
        ('Contact Info', {
         'fields': ('phone_number', 'email',)}),
         ('Study Interest', {
         'fields': ('course',)}),
        ('Status', {
         'fields': ('registration_is_processed',)}),
    )

    search_fields = ('first_name', 'last_name',
                     'phone_number', 'email', 'id')

    ordering = ('-timestamp',)
    filter_horizontal = ()

admin.site.register(Register, RegisterAdmin)
