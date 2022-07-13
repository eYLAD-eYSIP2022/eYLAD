from django.urls import path
from django.views.decorators.cache import cache_page
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('signup/', views.signup, name='signup'), ############# SIGNUP CHANGES ##############
    path('login/', views.login, name='login'),  #############  LOGIN PAGE ##############
    path('', views.login, name='login'),  ############# LOGIN PAGE ##############
    path('logout', views.logout, name='logout'),  ############# URL FOR LOGOUT. REDIRECTS TO LOGIN PAGE ##############
    path('task/<int:id>/', views.models_stats),  ############# PAGE FOR EACH TASK ##############
    # path('predict/', views.prediction),
    path('taskdata/<int:id>/', views.taskData, name="taskData"),########### URL FOR AJAX  ##########
    path('get-seen-teams/<int:topic_id>/', views.get_teams_seen, name="get_teams_seen"),########### URL FOR AJAX  ##########
    path('feedbackdata/<int:id>/', views.feedbackData, name="feedbackData"),########### URL FOR AJAX  ##########
    path('feedbackSelect/<int:task>/', views.feedbackSelect, name="feedbackData"),########### URL FOR AJAX  ##########
    path('feedbacktrack/<int:id>/', views.feedbackTrack, name="feedbackTrack"),########### URL FOR AJAX  ##########
    # url(r'^allowances_mas/(?P<pk>\d+)/$', AllowanceAPIView.as_view()),
    path('dashboard/',views.dashboard, name="dashboard"), ############# DASHBOARD PAGE ##############
    path('email/', views.email, name="email"),
    path('get-comments/<int:task_id>/', views.get_comments, name="get_comments"),########### URL FOR AJAX  ##########
    # path('temp/',views.temp, name="temp"),
]
