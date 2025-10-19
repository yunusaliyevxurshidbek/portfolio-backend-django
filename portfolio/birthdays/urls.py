from django.urls import path
from . import views


urlpatterns = [
    path("birthdays/", views.birthdays_list, name="birthdays-list"),
    path("birthdays/<int:pk>/", views.birthday_delete, name="birthday-delete"),
    path("birthdays/stats/", views.birthdays_stats, name="birthdays-stats"),
    path("birthdays/today/", views.birthdays_today, name="birthdays-today"),
]

