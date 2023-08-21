from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(models.BaseUser, CustomUserAdmin)
