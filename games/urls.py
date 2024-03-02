from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='game'

urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload_game, name="upload"),
    path('play/', views.play_games, name="play_games"),
    path('play/<slug:url>/', views.gaming, name="gaming"),
    path('upload_files/', views.upload_files, name ="upload_files"),
    path('convert/', views.convert_files, name=("convert_files")),
    path('report/', views.report, name="report"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)