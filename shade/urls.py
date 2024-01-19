from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home,name=('home')),
    path('members/details/<slug:slug>', views.details, name=('details')),
    path('members/', views.members, name=('members')),
    path('shade/', views.home, name=('home')),
    path('games/', views.playgames, name=('playgames')),
    path('games/HangMan/', views.hangman, name=("HangMan")),
    path('games/MemoryGame/', views.memory, name=("MemoryGame")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
            document_root=settings.STATIC_ROOT)
