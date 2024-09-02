from django.urls import path

from . import views

app_name = "main_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.category_detail, name="category_detail"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
]
