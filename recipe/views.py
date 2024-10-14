from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Recipe, Comment
from .forms import CommentForm


class RecipeList(generic.ListView):
    """Recipe List View"""
    model = Recipe
    template_name = "recipe/index.html"
    paginate_by = 3


def recipe_feature(request, slug):
    """
    Display an individual recipe:model:`recipe.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.

    **Template:**

    :template:`recipe/recipe_feature.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error submitting comment!')

    comment_form = CommentForm()

    return render(
        request,
        "recipe/recipe_feature.html",
        {"recipe": recipe,
         "comments": comments,
         "comment_form": comment_form,
         },
    )


def comment_edit(request, slug, comment_id):
    """
    Edit a comment from user :model:`recipe.Comment`.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.
    ``comment``
        An instance of :model:`recipe.Comment`.

    **Template:**

    :template:`recipe/recipe_feature.html`
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_feature', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete a comment from user :model:`recipe.Comment`.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.
    ``comment``
        An instance of :model:`recipe.Comment`.

    **Template:**

    :template:`recipe/recipe_feature.html`
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_feature', args=[slug]))


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500 )
