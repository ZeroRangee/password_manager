from django.urls import path
from .views import HomeView, WebSiteDataDetailView, WebSiteDataCreateView, WebSiteDataUpdateView,WebSiteDataDeleteView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<int:pk>', WebSiteDataDetailView.as_view(), name="website_data_detail"),
    path('create', WebSiteDataCreateView.as_view(), name="website_data_create"),
    path('update/<int:pk>', WebSiteDataUpdateView.as_view(), name="website_data_update"),
    path('delete/<int:pk>', WebSiteDataDeleteView.as_view(), name="website_data_delete")
]
