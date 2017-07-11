from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
from Autzu.settings import MEDIA_ROOT
import xadmin

from users.views import LoginView, UploadImageView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^$', TemplateView.as_view(template_name='f7/index.html'), name='f7index'),
    url(r'^f7_service/', TemplateView.as_view(template_name='f7/services.html'), name='f7service'),
    # url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^upload/', UploadImageView.as_view(), name='upload'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}, name='media'),
]
