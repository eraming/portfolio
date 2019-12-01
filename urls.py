from django.urls import path
import views

urlpatterns = [
    path('', views.home),
    path('gallery', views.gallery),
    path('projects', views.projects),
    path('contact', views.contact), 
]


from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
