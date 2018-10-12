import logging

from django.db import models

log = logging.getLogger(__name__)


class Demo(models.Model):
    user_id = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'todo_demo'
