from django.contrib import admin


class BookrAdminSite(admin.AdminSite):
    admin_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Book site admin'