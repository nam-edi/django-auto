from django.contrib import admin

from todo.models import Collection, Task

admin.site.register(Collection)
admin.site.register(Task)
