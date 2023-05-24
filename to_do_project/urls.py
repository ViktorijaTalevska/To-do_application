from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("to_do_app.urls")),
    path("account/",include("rest_auth.urls")),
    path("account/",include("rest_auth.registration.urls"))
]
