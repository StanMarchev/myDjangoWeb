from django.urls import path

from .views import five_a_side

urlpatterns = [
    path('', five_a_side, name='fiveAside'),

]