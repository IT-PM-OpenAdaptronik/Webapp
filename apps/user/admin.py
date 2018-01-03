from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext, gettext_lazy as _
from .models import User
from apps.profile.models import Profile,ProfileImage

#Remove Group
admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    inlines = (ProfileInline, )
    fieldsets = (
        (None, {'fields': ('username', 'email','password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'email', 'is_staff', 'is_superuser')

    def get_company(instance, abc):
        return 'TEST'#instance.profile.company

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
pass