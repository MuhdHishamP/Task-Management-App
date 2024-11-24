from django.contrib import admin
from .models import Task
from django.contrib import messages
from .models import UserInvitation

# Register your models here.

admin.site.register(Task)


@admin.register(UserInvitation)
class UserInvitationAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    fields = ("email",)

    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
            obj.send_invitation()
            messages.success(request, f"Invitation sent to {obj.email}")
        except Exception as e:
            messages.error(request, f"Failed to send invitation: {str(e)}")
