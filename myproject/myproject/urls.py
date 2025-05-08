from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView  # Добавьте этот импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('programs/', include('myapp.urls')),
    path('', RedirectView.as_view(url='/programs/')),  # Перенаправление с главной
    #path('pages_ol/news/', include('myapp.urls')),  # Используем myapp вместо news
]