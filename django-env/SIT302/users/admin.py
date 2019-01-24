from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]
#
# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Profile)

class ProfileInLine(admin.StackedInline):
    model = Profile
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInLine, )


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(CustomUser, CustomUserAdmin)