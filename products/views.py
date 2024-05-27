from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.core.exceptions import SuspiciousOperation

from .forms import AddToWishlistForm, ProductForm
from .models import Category, Product, Wishlist

# Create your views here.


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
    #raise SuspiciousOperation("Title and ingredients are required.")


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


@login_required
def wishlist(request):
    try:
        # Attempt to get the existing Wishlist instance for the user
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        # If no Wishlist exists, create one
        wishlist = Wishlist.objects.create(user=request.user)

    wishlist_items = wishlist.items.all()
    return render(
        request,
        "products/wish_list.html",
        {"products": wishlist_items, "is_wishlist": True},
    )


@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == "POST":
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
            if Wishlist.objects.filter(
                user=request.user, items__pk=product.pk
            ).exists():
                messages.warning(
                    request,
                    f"{product.name} is already added to your Wishlist.",
                )
            else:
                wishlist = Wishlist.objects.get(user=request.user)
                wishlist.items.add(product)
                messages.success(
                    request, f"Added {product.name} to your Wishlist"
                )
    else:
        form = AddToWishlistForm()  # Initialize the form for GET requests

    return render(
        request,
        "products/product_detail.html",
        {"form": form, "product": product},
    )


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist = request.user.wishlist
    wishlist.items.remove(product)
    messages.success(request, "Product deleted from Wishlist!")
    return redirect(reverse("wishlist"))
