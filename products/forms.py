from django import forms
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email       = forms.EmailField()
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "Your description",
                                "class": "new-class-name two",
                                "id": "my-id-for-text-area",
                                "rows":10,
                                "cols":80
                            }
                        ))
    price       = forms.DecimalField(initial=599.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    
    def clean_title(self):
        title = self.cleaned_data["title"]
        if not "resource" in title:
            raise forms.ValidationError("Title is not valid")
        elif not "item" in title:
            raise forms.ValidationError("Title is not valid")

        return title

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email.endswith("net"):
            raise forms.ValidationError("email is not valid")
        return email
    
class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "Your description",
                                "class": "new-class-name two",
                                "id": "my-id-for-text-area",
                                "rows":10,
                                "cols":80
                            }
                        ))
    price       = forms.DecimalField(initial=599.99)
