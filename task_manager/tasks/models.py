
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Task(models.Model):
    PRIORITY_LOW = "low"
    PRIORITY_MEDIUM = "medium"
    PRIORITY_HIGH = "high"

    PRIORITY_CHOICES = [
        (PRIORITY_LOW, "Low"),
        (PRIORITY_MEDIUM, "Medium"),
        (PRIORITY_HIGH, "High"),
    ]

    STATUS_PENDING = "pending"
    STATUS_COMPLETED = "completed"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_COMPLETED, "Completed"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["due_date", "-priority"]

    def clean(self):
        if self.due_date <= timezone.now():
            raise ValidationError({"due_date": "Due date must be in the future."})

    def save(self, *args, **kwargs):
        if self.status == self.STATUS_COMPLETED and self.completed_at is None:
            self.completed_at = timezone.now()
        if self.status == self.STATUS_PENDING and self.completed_at is not None:
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.owner.username})"
