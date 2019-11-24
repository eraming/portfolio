from django.urls import path
import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.home),
    path('gallery', views.gallery),
    path('projects', views.projects),
    path('contact', views.contact), 
]

# Boilerplate to include static files.
# Static files include CSS and images -- basically anything that isn't HTML or
# Python code -- stuff we just want to "serve up" for the browser to download
# and utilize and won't be changed by Python code (hence the term "static").
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
