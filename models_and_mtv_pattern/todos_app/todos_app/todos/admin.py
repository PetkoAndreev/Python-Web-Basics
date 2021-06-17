from django.contrib import admin

from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person, Category


# Option 2 with decorator
# @admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    sortable_by = ['title']
    list_filter = ['owner']

    # def has_change_permission(self, request, obj=None):
    #     return False


# Option 1
admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)
