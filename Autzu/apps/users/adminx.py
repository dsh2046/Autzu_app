import xadmin
from xadmin import views

from .models import EmailVerifyRecord, License


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = 'Autzu Admin'
    site_footer = 'Autzu Inc'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']


class LicenseAdmin(object):
    list_display = ['license_num', 'driver_name', 'add_time', 'license_image']
    list_filter = ['license_num', 'driver_name', 'add_time']
    search_fields = ['license_num', 'driver_name']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(License, LicenseAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


