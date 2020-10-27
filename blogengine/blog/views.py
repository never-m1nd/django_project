from django.shortcuts import render, reverse, redirect
from django.views import generic
from .forms import *
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.


class TagDetail(generic.DetailView):
    model = Tag
    template_name = 'blog/tag.html'


class Index(generic.ListView):
    paginate_by = 5
    model = Post
    template_name = 'blog/base_blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search != '':
            object_list = self.model.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
        else:
            object_list = self.model.objects.all()
        return object_list


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
    query_pk_and_slug = True


class DeletePost(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'is_staff'
    model = Post
    success_url = '/'


class CreatePost(LoginRequiredMixin, generic.View):

    def get(self, request):
        form = CreatePostForm()
        return render(request, 'blog/test_post_create.html', {'form': form})

    def post(self, request):
        print(request)
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return redirect(new_post)
        return render(request, 'blog/test_post_create.html', context={'form': form})


class UpdatePost(LoginRequiredMixin,PermissionRequiredMixin, generic.View):
    permission_required = 'is_stuff'

    def get(self, request, pk, slug):
        post = Post.objects.get(pk=pk)
        form = CreatePostForm()
        return render(request, 'blog/post_update_form.html', {'form': form, 'post': post})

    def post(self, request, pk, slug):
        post = Post.objects.get(pk=pk)
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.tags.all().delete()
            for tag in form.cleaned_data['tags'].split(','):
                if tag:
                    try:
                        new_tag = Tag.objects.get(title=tag)
                    except ObjectDoesNotExist:
                        new_tag = Tag.objects.create(title=tag)
                        post.tags.add(new_tag)
                    else:
                        post.tags.add(new_tag)
            post.save()
            return redirect(post)
        return render(request, 'blog/post_update_form.html', context={'form': form, 'post': post})
