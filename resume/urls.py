from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('pd',views.generatePDF,name='pd'),
    path('signup', views.signup, name='signup'),
    path('template1',views.template1,name='template1'),
    path('template2',views.template2,name='template2'),
    path('upload',views.upload, name='upload')
]


# For image upload......
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)