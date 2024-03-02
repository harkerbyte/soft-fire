===================
Soft - Fire (games)
===================

Soft Fire is a python x javascript app to run game canvas [html css javascript image.extensions]
You're a TS / SCSS programmer? No need to worry, as the app also comes with an additional feature
to convert and download ( .ts & .scss to .js & .css )files consecutively.

``many more features to come as MINOR (RFC - 2119) PATCH  continues``

Quick Start
-----------

1. To add 'games' to your installed apps ::
    navigate to your project settings and input::
        INSTALLED_APPS = [
            ...,
            "games",
        ]

2. Include the games URLconf in your project urls.py like this::
    urlpatterns = [
        ...,
        path('game/', include('games.urls', namespace="game"))
    ]

3. Run ```python manage.py migrate``` to create the games models

4. Start the development server and visit ```https://127.0.0.1:8000/admin```
   to create a game (you'll need the Admin app enabled).

   5. Visit ```https://127.0.0.1:8000```  to upload and play games.