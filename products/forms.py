from django import forms

from .models import Category, Product, Comment
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


class CommentForm(forms.ModelForm):
    """
    Review form for user to edit review
    """
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': 'Your review:'
        }


class AddToWishlistForm(forms.Form):
    pass
