from django.contrib import admin

class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "deleted_at", "is_deleted")

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(
            super().get_readonly_fields(request, obj)
        )

        readonly_fields.extend(
            list(getattr(self, '_readonly_fields', []))
        )

        createonly_fields = list(getattr(self, 'createonly_fields', []))

        if obj:
            readonly_fields.extend(createonly_fields)

        return readonly_fields