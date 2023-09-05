from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import escape
from django.utils.text import slugify
from django.urls import reverse

from todo.models import Collection, Task


def index(request):
    context = {}

    collection_slug = request.GET.get("collection")
    try:
        collection = get_object_or_404(Collection, slug=collection_slug)
    except Http404:
        collection = Collection.get_default_collection()

    context["collections"] = Collection.objects.order_by("slug")
    context["collection"] = collection
    context["tasks"] = collection.task_set.order_by("description")

    return render(request, 'todo/todo.html', context=context)


def add_collection(request):
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(
        name=collection_name,
        slug=slugify(collection_name))
    if created:
        HttpResponse("La collection existe déjà ", status=409)

    return render(request, 'todo/collection.html', context={"collection": collection})


def delete_collection(request):
    collection = Collection.objects.get(slug=escape(request.POST.get("collection")))
    collection.delete()
    response = HttpResponse("")
    response["HX-Redirect"] = reverse("todo")
    return response


def add_task(request):
    collection = Collection.objects.get(slug=escape(request.POST.get("collection")))
    description = escape(request.POST.get("task-description"))
    task = Task.objects.create(description=description, collection=collection)

    return render(request, 'todo/task.html', context={"task": task})


def delete_task(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.delete()

    return HttpResponse("")


def get_tasks(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    tasks = collection.task_set.order_by('description')

    return render(request, 'todo/tasks.html', context={"tasks": tasks})


def get_collection_detail(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    tasks = collection.task_set.order_by('description')

    return render(request, 'todo/collection_detail.html', context={"collection": collection, "tasks": tasks})