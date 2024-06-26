from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from blog.models import Blog
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ("heading", "slag_blog", "text", "image", "published")

    def form_valid(self, form):
        new_blog = form.save()
        new_blog.slag_blog = slugify(new_blog.heading)
        new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.object.pk])


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ("heading", "slag_blog", "text", "image", "published")
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slag_blog = slugify(new_blog.heading)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.object.pk])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
