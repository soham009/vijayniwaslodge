from django.urls import include, path
from customers import views

urlpatterns = [
  path("", views.list_view.as_view(), name="list"),
  path("english_visa/<int:pk>", views.gen_eng_visa.as_view(), name="gen_eng_visa"),
]
