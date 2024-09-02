from django.shortcuts import get_object_or_404, render

from .models import Category, Product


# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories})


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category_id=id)
    return render(
        request, "category_detail.html", {"category": category, "products": products}
    )


def terms(request):
    return render(request, "terms.html")


def privacy(request):
    return render(request, "privacy.html")
