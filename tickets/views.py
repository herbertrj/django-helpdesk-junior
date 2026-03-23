from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TicketForm
from .models import Ticket


@login_required
def ticket_list(request):
    tickets = Ticket.objects.select_related("created_by", "assigned_to").order_by("-created_at")

    status = request.GET.get("status")
    if status:
        tickets = tickets.filter(status=status)

    context = {
        "tickets": tickets,
        "selected_status": status,
        "status_choices": Ticket.Status.choices,
    }
    return render(request, "tickets/ticket_list.html", context)


@login_required
def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect("ticket-list")
    else:
        form = TicketForm()
    return render(request, "tickets/ticket_form.html", {"form": form})


@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, "tickets/ticket_detail.html", {"ticket": ticket})


@login_required
def ticket_update_status(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    new_status = request.POST.get("status")
    valid_status = {choice[0] for choice in Ticket.Status.choices}

    if new_status in valid_status:
        ticket.status = new_status
        ticket.save(update_fields=["status", "updated_at"])

    return redirect("ticket-detail", pk=ticket.pk)


@login_required
def dashboard(request):
    status_totals = (
        Ticket.objects.values("status")
        .annotate(total=Count("id"))
        .order_by("status")
    )
    status_map = {item["status"]: item["total"] for item in status_totals}

    context = {
        "total_tickets": Ticket.objects.count(),
        "open_tickets": status_map.get(Ticket.Status.OPEN, 0),
        "in_progress_tickets": status_map.get(Ticket.Status.IN_PROGRESS, 0),
        "resolved_tickets": status_map.get(Ticket.Status.RESOLVED, 0),
    }
    return render(request, "tickets/dashboard.html", context)
