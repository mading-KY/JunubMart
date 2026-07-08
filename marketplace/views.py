from django.shortcuts import render


def add_product(request):
    return render(request, "marketplace/add_product.html")

def product_list(request):
    return render(request, "marketplace/product_list.html")

def product_detail(request, pk):
    return render(request, "marketplace/product_detail.html")


