from django import forms

from .models import Ticket, TicketComment


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "priority", "assigned_to"]


class TicketCommentForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "Escreva um comentario..."}),
        }
