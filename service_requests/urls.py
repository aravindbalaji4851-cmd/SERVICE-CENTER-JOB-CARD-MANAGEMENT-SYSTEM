from django.urls import path

from service_requests.views import SignUpView
from service_requests.views import ServiceRequestListCreateView
from service_requests.views import ServiceRequestRetrieveUpdateDetailView,ServiceRequestCountView,HighCriticalServiceRequestView

urlpatterns =[
    path('user-register/',SignUpView.as_view()),
    path('',ServiceRequestListCreateView.as_view()),
    path('<int:pk>/', ServiceRequestRetrieveUpdateDetailView.as_view()),
    path('count/', ServiceRequestCountView.as_view()),
    path('high-critical/', HighCriticalServiceRequestView.as_view()),
]
