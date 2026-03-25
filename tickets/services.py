from django.contrib.auth.models import User

from .models import Ticket


def can_update_ticket_status(user: User, ticket: Ticket, new_status: str) -> bool:
    if not user.is_authenticated:
        return False

    # Perfil de suporte: usuario staff ou responsavel do chamado.
    is_support = user.is_staff or ticket.assigned_to_id == user.id
    if not is_support:
        return False

    allowed_transitions = {
        Ticket.Status.OPEN: {Ticket.Status.IN_PROGRESS},
        Ticket.Status.IN_PROGRESS: {Ticket.Status.RESOLVED},
        Ticket.Status.RESOLVED: set(),
    }

    return new_status in allowed_transitions.get(ticket.status, set())


def update_ticket_status(user: User, ticket: Ticket, new_status: str) -> bool:
    valid_status = {choice[0] for choice in Ticket.Status.choices}
    if new_status not in valid_status:
        return False

    if not can_update_ticket_status(user, ticket, new_status):
        return False

    ticket.status = new_status
    ticket.save(update_fields=["status", "updated_at"])
    return True
