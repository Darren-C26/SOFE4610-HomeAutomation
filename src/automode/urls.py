# Import required modules and views
from django.contrib import admin
from django.urls import include, path
from lightcontrol import views as lightcontrol_views

# Define URL patterns for your project
urlpatterns = [
    # URL for the Django admin site
    path('admin/', admin.site.urls),
    
    # Include the URL patterns from the 'lightcontrol' app
    path('lightcontrol/', include('lightcontrol.urls')),
    
    # Map the root URL to the 'dashboard' view from the 'lightcontrol' app
    path('', lightcontrol_views.dashboard, name='home'),
]
