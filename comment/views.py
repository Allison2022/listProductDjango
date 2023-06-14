from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm, ContactForm

def index(request):
    comments = Comment.objects.all()
    return render(request, 'index.html', context={'comments':comments})

# function to add a comment
def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CommentForm()

    context = {
        "form":form
    }
    return render(request, 'add.html', context)

# function to update a comment
def update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        print(form.errors.as_json())
        if form.is_valid():
            form.save(commit=True, text="Hola mundo")
            return redirect('update', pk=comment.id)
    else:
        form = CommentForm(instance=comment)

    context = {
        "form":form,
        "comment": comment,
    }
    return render(request, 'update.html', context)

# contact function
def contact(request):
    form = ContactForm()
    context = {
        "form":form,
    }
    return render(request, 'contact.html', context)