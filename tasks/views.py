def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed  # toggle True/False
    task.save()
    return redirect('/')

