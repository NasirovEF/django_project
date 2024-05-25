from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "contacts.html")


def one_product(request, pk):
    product = Product.objects.get(pk=pk)
    # next_prod = Product.objects.get(pk=pk + 1)
    products = Product.objects.all()
    context = {"product": product,
               "products": products,
               }
    return render(request, "product.html", context)


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "add_prod.html")