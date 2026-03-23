from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Ticket(models.Model):
    class Status(models.TextChoices):
        OPEN = "open", "Aberto"
        IN_PROGRESS = "in_progress", "Em andamento"
        RESOLVED = "resolved", "Resolvido"

    class Priority(models.TextChoices):
        LOW = "low", "Baixa"
        MEDIUM = "medium", "Media"
        HIGH = "high", "Alta"

    title = models.CharField("Titulo", max_length=120)
    description = models.TextField("Descricao")
    status = models.CharField(
        "Status",
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
    )
    priority = models.CharField(
        "Prioridade",
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    created_by = models.ForeignKey(
        User,
        related_name="created_tickets",
        on_delete=models.CASCADE,
        verbose_name="Criado por",
    )
    assigned_to = models.ForeignKey(
        User,
        related_name="assigned_tickets",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Responsavel",
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return f"#{self.id} - {self.title}"
