from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView  # added TemplateView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import (PermissionRequiredMixin)
from django.core.paginator import Paginator

class MapView(TemplateView):
    template_name = "map.html"

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse_lazy('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        paginator = Paginator(self.object_list, 5)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)

        context["cat_menu"] = cat_menu
        context['page_obj'] = page_obj
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class UserAccessMixin(PermissionRequiredMixin):
    def __init__(self):
        self.request = None

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('home')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class AddPostView(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = ('post.add_post', '')
    permission_denied_message = "We are sorry, you cannot do this action..."
    login_url = 'home'
    redirect_field_name = 'next'

    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class AddCategoryView(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = ('category.add_category', '')
    permission_denied_message = "We are sorry, you cannot do this action..."
    login_url = 'home'
    redirect_field_name = 'next'

    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
