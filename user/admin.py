from django.contrib import admin
from user.models import MyUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class MyUserAdmin(UserAdmin):
	list_display = ('name','email','phone','balance', 'last_login', 'is_admin','is_staff')
	search_fields = ('pk', 'email',)
	readonly_fields=('pk', 'date_joined', 'last_login',)

	ordering = ['email',]	
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
            #              🖞 without username
        }),
    )

admin.site.register(MyUser,MyUserAdmin)
