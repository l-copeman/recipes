from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe
from .forms import CommentForm

class RecipeList(generic.ListView):
    model = Recipe
    template_name = "recipe/index.html"
    paginate_by = 3

def recipe_feature(request, slug):
    """
    Display an individual :model:`recipe.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.

    **Template:**

    :template:`recipe/recipe_feature.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.recipe = recipe
        comment.save()


    return render(
        request,
        "recipe/recipe_feature.html",
        {"recipe": recipe,
        "comments": comments,
        "comment_form": comment_form,
        },
    )