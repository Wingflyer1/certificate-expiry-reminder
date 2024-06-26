"""
URL configuration for reminderproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

app_name = "reminderapp"
urlpatterns = [
    # ex: /reminder/
    path("", views.indexView.as_view(), name = "index"),
    # ex: /reminder/5/
    # path("<int:question_id>/", views.detail, name = "detail"),
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    # ex: /reminder/5/results/
    # path("<int:question_id>/results/", views.results, name = "results"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name='results'),
    # ex: /reminder/5/vote/
    path("<int:question_id>/vote/", views.vote, name = "vote"),

]

