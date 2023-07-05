from django.contrib.auth.models import User
from django.db import models
from django.conf import settings as app_settings
from django.db.models import Manager, QuerySet
from django.utils import timezone


class AppQuerySet(QuerySet):
    def delete(self):
        self.update(is_deleted=True)


class AppManager(Manager):
    def get_queryset(self):
        return AppQuerySet(self.model, using=self._db).exclude(is_deleted=True)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text="creation datetime")
    updated_at = models.DateTimeField(auto_now=True, help_text="updated datetime")
    deleted_at = models.DateTimeField(
        null=True, blank=True, help_text="deleted datetime"
    )
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="%(class)s_created_by",
        help_text="user performing create action",
    )
    status = models.CharField(max_length=20, choices=app_settings.STATUS_OPTIONS, help_text="status of data availability")
    is_deleted = models.BooleanField(default=False, help_text="delete data status")

    objects = AppManager()

    class Meta:
        abstract = True

    @classmethod
    def get_fields(cls, excludes=[], extras=[]):
        fields = [
            field.name for field in cls._meta.get_fields() if field.name not in excludes
        ]

        if extras:
            fields.extend(extras)

        return list(dict.fromkeys(fields))

    def delete(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()


class ExtraBaseModel(BaseModel):
    approved_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="%(class)s_approved_by",
        help_text="user performing approve action",
    )
    cancelled_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="%(class)s_cancelled_by",
        help_text="user performing cancell action",
    )
    deleted_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="%(class)s_deleted_by",
        help_text="user performing delete action",
    )

    class Meta:
        abstract = True
