from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('PollMaker/',include('PollMaker.urls')), 
    path('', include('PollMaker.urls'))
]

