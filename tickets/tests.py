from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Ticket


class TicketFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user1", password="123456Aa!")
        self.support = User.objects.create_user(
            username="support1",
            password="123456Aa!",
            is_staff=True,
        )

    def test_authenticated_user_can_create_ticket(self):
        self.client.login(username="user1", password="123456Aa!")
        response = self.client.post(
            reverse("ticket-create"),
            data={
                "title": "Erro no sistema",
                "description": "Nao consigo finalizar o cadastro",
                "priority": Ticket.Priority.MEDIUM,
                "assigned_to": self.support.id,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ticket.objects.count(), 1)
        ticket = Ticket.objects.first()
        self.assertEqual(ticket.created_by, self.user)
        self.assertEqual(ticket.status, Ticket.Status.OPEN)

    def test_support_can_advance_status_flow(self):
        ticket = Ticket.objects.create(
            title="Chamado 1",
            description="Teste",
            created_by=self.user,
            assigned_to=self.support,
        )

        self.client.login(username="support1", password="123456Aa!")
        self.client.post(
            reverse("ticket-update-status", kwargs={"pk": ticket.pk}),
            data={"status": Ticket.Status.IN_PROGRESS},
        )
        ticket.refresh_from_db()
        self.assertEqual(ticket.status, Ticket.Status.IN_PROGRESS)

        self.client.post(
            reverse("ticket-update-status", kwargs={"pk": ticket.pk}),
            data={"status": Ticket.Status.RESOLVED},
        )
        ticket.refresh_from_db()
        self.assertEqual(ticket.status, Ticket.Status.RESOLVED)

    def test_regular_user_cannot_update_status(self):
        ticket = Ticket.objects.create(
            title="Chamado 2",
            description="Teste",
            created_by=self.user,
            assigned_to=self.support,
        )

        self.client.login(username="user1", password="123456Aa!")
        self.client.post(
            reverse("ticket-update-status", kwargs={"pk": ticket.pk}),
            data={"status": Ticket.Status.IN_PROGRESS},
        )
        ticket.refresh_from_db()
        self.assertEqual(ticket.status, Ticket.Status.OPEN)

    def test_invalid_transition_is_blocked(self):
        ticket = Ticket.objects.create(
            title="Chamado 3",
            description="Teste",
            created_by=self.user,
            assigned_to=self.support,
        )

        self.client.login(username="support1", password="123456Aa!")
        self.client.post(
            reverse("ticket-update-status", kwargs={"pk": ticket.pk}),
            data={"status": Ticket.Status.RESOLVED},
        )
        ticket.refresh_from_db()
        self.assertEqual(ticket.status, Ticket.Status.OPEN)
