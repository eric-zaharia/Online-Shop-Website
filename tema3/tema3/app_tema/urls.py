from django.urls import path

from .views import hello, home, TabeleView

app_name = 'my_app'

urlpatterns = [
    path('', hello, name='hello'),
    path('home/', home, name='home'),
    path('tabele/', TabeleView.as_view(), name='tabele'),
]
