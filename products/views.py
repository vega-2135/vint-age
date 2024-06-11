from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import AddToWishlistForm, ProductForm, ReviewForm
from .models import Category, Product, Review, Wishlist

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

    # Display only approved reviews
    reviews = product.reviews.order_by("-created_on")

    # Display a form to users, so they can add review
    skip_shopping_bag = False

    req_context = request.session.get("context", None)
    if req_context:
        del request.session["context"]
        skip_shopping_bag = req_context["skip_shopping_bag"]

    if request.user.is_authenticated:
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            messages.success(
                request,
                "Thank you for taking \
                the time to leave a review of this product",
            )
            skip_shopping_bag = True

    context = {
        "product": product,
        "reviews": reviews,
        "review_form": ReviewForm(),
        "skip_shopping_bag": skip_shopping_bag,
    }

    return render(request, "products/product_detail.html", context)


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
    return redirect(request.build_absolute_uri())


@login_required
def edit_review(request, product_id, review_id):
    """
    View to edit reviews
    """
    # Display only approved reviews
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.order_by("-created_on")

    if request.method == "POST":
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        # If the form is invalid or someone other than the author tries to edit
        # the review then that's not allowed an a error message is shown
        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.product = product
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, "Review Updated!")
        else:
            messages.add_message(
                request, messages.ERROR, "Error updating review!"
            )

        context = {
            "product": product,
            "reviews": reviews,
            "review_form": ReviewForm(),
            "skip_shopping_bag": True,
        }

    return redirect(reverse("product_detail", args=[product_id]))


@login_required
def delete_review(request, product_id, review_id):
    """
    view to delete reviews
    """
    review = get_object_or_404(Review, pk=review_id)
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.order_by("-created_on")

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, "Review deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own reviews!"
        )

    context = {"skip_shopping_bag": True }
    request.session['context'] = context
    return redirect(reverse("product_detail", args=[product_id]))


@login_required
def wishlist(request):
    try:
        # Attempt to get the existing Wishlist instance for the user
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        # If no Wishlist exists, create one
        wishlist = Wishlist.objects.create(user=request.user)

    wishlist_items = wishlist.items.all()

    # Get the context in case it comes from remove_from_wishlist
    req_context = request.session.get("context", None)
    skip_shopping_bag = False
    # Delete the context from the request in case it keeps getting redirected
    if req_context:
        del request.session["context"]
        skip_shopping_bag = req_context["skip_shopping_bag"]
    context = {
        "products": wishlist_items,
        "is_wishlist": True,
        "skip_shopping_bag": skip_shopping_bag,
    }
    return render(
        request,
        "products/wish_list.html",
        context,
    )


@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(pk=product_id)
    reviews = product.reviews.order_by("-created_on")
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

    context = {
        "form": form,
        "product": product,
        "reviews": reviews,
        "review_form": ReviewForm(),
        "skip_shopping_bag": True,
    }
    return render(
        request,
        "products/product_detail.html",
        context,
    )


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist = request.user.wishlist
    wishlist.items.remove(product)
    messages.success(request, "Product deleted from Wishlist!")
    # Because I want to show the message but not the shopping bag
    # I'm using Django session framework to skip it in the templates ("base.html")
    context = {'skip_shopping_bag': True}
    request.session['context'] = context
    return redirect(reverse("wishlist"))
