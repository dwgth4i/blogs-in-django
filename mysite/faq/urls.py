from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
    path('ask/', views.ask_question, name='ask_question'),
    path('answer/<int:post_id>/', views.answer_question, name='answer_question'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', auth_views.LogoutView.as_view(next_page='signin'), name='logout'),
]
