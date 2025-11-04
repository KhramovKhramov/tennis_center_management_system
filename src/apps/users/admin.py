from apps.users.models import User
from django.contrib import admin


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        'get_full_name',
        'username',
        'email',
        'phone_number',
        'date_of_birth',
        'gender',
    )

    def get_full_name(self, obj):
        return obj.full_name

    get_full_name.short_description = 'ФИО'
