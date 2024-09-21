from django.urls import path
from . import views


# urlpatterns stores all the paths
# first 2 parameters of each path function is essentially mapping a address to a function in views.py file
# 3rd parameter is just a name of each path for purpose of referencing (like in templates, or redirects)

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
    
    path('', views.main_page, name='main_page'),
    path('post_question/', views.post_question_page, name='post_question_page'),
    path('all_questions/', views.all_questions_page, name='all_questions_page'),
    path('get_ans/<str:question_id>', views.get_ans, name='get_ans'),
    path('filter_questions/', views.filter_questions_page, name='filter_questions_page'),
    path('find_accounts/', views.find_accounts_page, name='find_accounts_page'),

    path('follow_unfollow/<str:user_id>', views.follow_unfollow, name='follow_unfollow'),


    path('create_subject/', views.create_subject, name='create_subject'),
    path('create_subtopic/', views.create_subtopic, name='create_subtopic'),



    path('logout/', views.user_logout, name='user_logout'),
]