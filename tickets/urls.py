from django.urls import path

from . import views

urlpatterns = [
    path("", views.ticket_list, name="ticket-list"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("chamados/novo/", views.ticket_create, name="ticket-create"),
    path("chamados/<int:pk>/", views.ticket_detail, name="ticket-detail"),
    path("chamados/<int:pk>/status/", views.ticket_update_status, name="ticket-update-status"),
]
