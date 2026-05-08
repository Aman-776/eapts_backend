from django.contrib import admin
from .models import Person, PersonName, Patient, User, Role, Privilege, UserRole, RolePrivilege

admin.site.register(Person)
admin.site.register(PersonName)
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Privilege)
admin.site.register(UserRole)
admin.site.register(RolePrivilege)
