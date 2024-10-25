from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from apps.user.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Registrar tus modelos en el admin
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('alias', 'avatar')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'alias', 'avatar', 'password1', 'password2'),
        }),
    )

    # Verificar si el usuario pertenece a un grupo específico
    def is_registered(self, obj):
        return obj.groups.filter(name='Registered').exists()
    is_registered.short_description = 'Es Usuario Registrado'
    is_registered.boolean = True

    def is_collaborator(self, obj):
        return obj.groups.filter(name='Collaborators').exists()
    is_collaborator.short_description = 'Es Colaborador'
    is_collaborator.boolean = True

    def is_admin(self, obj):
        return obj.groups.filter(name='Admins').exists()
    is_admin.short_description = 'Es Administrador'
    is_admin.boolean = True

    # Acciones para agregar usuarios a los grupos
    def add_to_registered(self, request, queryset):
        registered_group = Group.objects.get(name='Registered')
        for user in queryset:
            user.groups.add(registered_group)
        self.message_user(request, "Los usuarios seleccionados fueron añadidos al grupo 'Registered'.")
    add_to_registered.short_description = 'Agregar a Usuarios Registrados'

    def add_to_collaborators(self, request, queryset):
        collaborators_group = Group.objects.get(name='Collaborators')
        for user in queryset:
            user.groups.add(collaborators_group)
        self.message_user(request, "Los usuarios seleccionados fueron añadidos al grupo 'Collaborators'.")
    add_to_collaborators.short_description = 'Agregar a Colaboradores'

    def add_to_admins(self, request, queryset):
        admins_group = Group.objects.get(name='Admins')
        for user in queryset:
            user.groups.add(admins_group)
        self.message_user(request, "Los usuarios seleccionados fueron añadidos al grupo 'Admins'.")
    add_to_admins.short_description = 'Agregar a Administradores'

    # Acciones para remover usuarios de los grupos
    def remove_from_registered(self, request, queryset):
        registered_group = Group.objects.get(name='Registered')
        for user in queryset:
            user.groups.remove(registered_group)
        self.message_user(request, "Los usuarios seleccionados fueron removidos del grupo 'Registered'.")
    remove_from_registered.short_description = 'Remover de Usuarios Registrados'

    def remove_from_collaborators(self, request, queryset):
        collaborators_group = Group.objects.get(name='Collaborators')
        for user in queryset:
            user.groups.remove(collaborators_group)
        self.message_user(request, "Los usuarios seleccionados fueron removidos del grupo 'Collaborators'.")
    remove_from_collaborators.short_description = 'Remover de Colaboradores'

    def remove_from_admins(self, request, queryset):
        admins_group = Group.objects.get(name='Admins')
        for user in queryset:
            user.groups.remove(admins_group)
        self.message_user(request, "Los usuarios seleccionados fueron removidos del grupo 'Admins'.")
    remove_from_admins.short_description = 'Remover de Administradores'

    # Acciones disponibles en el admin
    actions = [add_to_registered, add_to_collaborators, add_to_admins,
               remove_from_registered, remove_from_collaborators, remove_from_admins]

    # Modificar el list_display para incluir los nuevos campos
    list_display = ('username', 'email', 'alias', 'is_staff', 'is_superuser', 'is_registered', 'is_collaborator', 'is_admin')
    search_fields = ('username', 'email', 'alias', 'id')
    ordering = ('-date_joined',)

# Registrar el modelo personalizado de usuario
admin.site.register(User, CustomUserAdmin)

# Crear automáticamente los grupos cuando se migra la base de datos
@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    Group.objects.get_or_create(name='Registered')
    Group.objects.get_or_create(name='Collaborators')
    Group.objects.get_or_create(name='Admins')
