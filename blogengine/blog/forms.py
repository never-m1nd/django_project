from django import forms
from .models import Post, Tag
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError


class CreatePostForm(forms.Form):

    title = forms.CharField(label='Title')
    body = forms.CharField(label='What you think')
    tags = forms.CharField(label='Tags', required=False)

    def save(self):
        new_post = Post.objects.create(title=self.cleaned_data['title'],
                                       body=self.cleaned_data['body'],)
        for tag in self.cleaned_data['tags'].split(','):
            if tag:
                try:
                    new_tag = Tag.objects.get(title=tag)
                except ObjectDoesNotExist:
                    new_tag = Tag.objects.create(title=tag)
                    new_post.tags.add(new_tag)
                else:
                    new_post.tags.add(new_tag)
        return new_post

#
# class CreatePostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'body', 'tags']

    # widgets = {
    #     'tags': forms.SelectMultiple()
    # }

    # def clean_slug(self):
    #     new_slug = self.cleaned_data['slug']
    #     return new_slug

    # def save(self):
    #     new_post = Post.objects.create(title=self.cleaned_data['title'],
    #                                    body=self.cleaned_data['body'],)
    #     for tag in self.cleaned_data['tags'].split(','):
    #         if tag:
    #             try:
    #                 new_tag = Tag.objects.get(title=tag)
    #             except ObjectDoesNotExist:
    #                 new_tag = Tag.objects.create(title=tag)
    #                 new_post.tags.add(new_tag)
    #             else:
    #                 new_post.tags.add(new_tag)
    #     return new_post
