from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'author', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Insert your title"}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert your tab title'}),
            'author': forms.HiddenInput(attrs={'class': 'form-control', 'value': '', 'id': 'user'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert your name'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
