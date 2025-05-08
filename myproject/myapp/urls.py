from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ProgramListView,
    ROPPageView,
    OLPageView,
    OLAnalysisView,
    OLNewsView,
    KK,
    OlOt2View,
    OlOt1View,
    OLReportsView
)

from django.views.generic import TemplateView
from . import views

from .views import delete_news, edit_news

urlpatterns = [
    # Основные пути
    # path('test/', TemplateView.as_view(template_name='pages_ol/main/index.html')),
    path('', ProgramListView.as_view(), name='program-list'),
    path('pages_rop/', ROPPageView.as_view(), name='rop-page'),
    
    # Пути для OL
    path('pages_ol/', KK.as_view(), name='ol-s'),
    path('pages_ol/smain/', OLPageView.as_view(), name='ol-page'),
    path('pages_ol/analiz/', OLAnalysisView.as_view(), name='ol-analiz'),
    path('pages_ol/news/', OLNewsView.as_view(), name='ol-news'),
    path('pages_ol/reports/', OLReportsView.as_view(), name='ol-reports'),
    path('pages_ol/reports/reports_OOP/', OlOt1View.as_view(), name='ol_ot1'),
    path('pages_ol/reports/reports_OL/', OlOt2View.as_view(), name='ol_ot2'),
    # Для новостей сохранение
    path('save_news/', views.save_news, name='save_news'),
    # Для новостей вывод
    # path('pages_ol/news/', views.news_index, name='news_index'),
    # Удаление и редактировнаие новостей
    path('news/delete/<int:pk>/', delete_news, name='delete_news'),
    path('news/edit/<int:pk>/', edit_news, name='edit_news'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Для отладки (можно раскомментировать при необходимости)
# from django.views.decorators.http import require_GET
# @require_GET
# def debug_view(request):
#     print("DEBUG: Запрос получен!")
#     return OLPageView.as_view()(request)
# urlpatterns += [path('debug/', debug_view)]