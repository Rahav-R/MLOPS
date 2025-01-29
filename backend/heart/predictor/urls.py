from django.urls import path
from . import views  # Import views correctly
from .views import PredictView  # You can also import PredictView this way

urlpatterns = [
    path('', views.home, name='predictor_home'),  # home view for the root path
    path('predict/', PredictView.as_view(), name='predict'),  # predict path using PredictView
]

