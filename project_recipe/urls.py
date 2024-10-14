from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500


handler404 = 'recipe.views.custom_404'
handler500 = 'recipe.views.custom_500'


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("recipe.urls"), name="recipe-urls"),
]
