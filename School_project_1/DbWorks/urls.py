from django.urls import path
from . import views

app_name = "DbWorks"
urlpatterns = [
    path("", views.main_page.as_view(), name="main_page"),
    path("product_page/<str:pk>/", views.product_page.as_view(), name="product_page"),
]