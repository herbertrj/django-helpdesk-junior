from .models import Ticket


def update_ticket_status(ticket: Ticket, new_status: str) -> bool:
    valid_status = {choice[0] for choice in Ticket.Status.choices}
    if new_status not in valid_status:
        return False

    ticket.status = new_status
    ticket.save(update_fields=["status", "updated_at"])
    return True
