import django_filters

from .models import Task


class TaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name="status", lookup_expr="iexact")
    priority = django_filters.CharFilter(field_name="priority", lookup_expr="iexact")
    due_date_before = django_filters.DateTimeFilter(
        field_name="due_date", lookup_expr="lte"
    )
    due_date_after = django_filters.DateTimeFilter(
        field_name="due_date", lookup_expr="gte"
    )

    class Meta:
        model = Task
        fields = ["status", "priority", "due_date_before", "due_date_after"]
