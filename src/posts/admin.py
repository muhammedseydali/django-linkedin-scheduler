from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["updated_at", "share_on_linkedin"]
    search_fields = ["content", "user__username"]
    ordering = ["-updated_at"]

    def get_list_display(self, request):
        """Dynamically display columns based on user type."""
        base_fields = ["content", "updated_at"]
        if request.user.is_superuser:
            return ["content", "user", "share_on_linkedin", "shared_at_linkedin", "updated_at"]
        return base_fields

    def get_queryset(self, request):
        """Filter posts so normal users see only their own."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_delete_permission(self, request, obj=None):
        """Allow delete only if post not shared yet."""
        if request.user.is_superuser:
            return True
        if obj is None:
            return False
        return obj.user == request.user and not obj.shared_at_linkedin

    def get_readonly_fields(self, request, obj=None):
        """Prevent editing of shared posts."""
        if obj and obj.shared_at_linkedin:
            return ["user", "content", "shared_at_linkedin", "share_on_linkedin"]
        if request.user.is_superuser:
            return ["shared_at_linkedin"]
        return ["user", "shared_at_linkedin"]

    def save_model(self, request, obj, form, change):
        """Automatically assign user to post when created."""
        if not change and not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)
