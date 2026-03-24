from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TicketCommentForm, TicketForm
from .models import Ticket
from .services import update_ticket_status


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
    ticket = get_object_or_404(Ticket.objects.select_related("created_by", "assigned_to"), pk=pk)
    comments = ticket.comments.select_related("author").all()

    if request.method == "POST":
        form = TicketCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.author = request.user
            comment.save()
            return redirect("ticket-detail", pk=ticket.pk)
    else:
        form = TicketCommentForm()

    context = {
        "ticket": ticket,
        "comments": comments,
        "comment_form": form,
    }
    return render(request, "tickets/ticket_detail.html", context)


@login_required
def ticket_update_status(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    new_status = request.POST.get("status")
    update_ticket_status(ticket, new_status)

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
