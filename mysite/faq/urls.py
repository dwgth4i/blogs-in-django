from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
    # path("about/", views.about, name="about")
]
