from django.urls import path,include
from . import views
from .views import LoginView

app_name='accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Add this line
    path('profile/',views.profile,name='profile'), 
    path('profile/edit',views.profile_edit,name='profile_edit'), 
    path('login/', LoginView.as_view(), name='login'),

]