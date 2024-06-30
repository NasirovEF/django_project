from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    login_url = "user:login"

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if (
                user.has_perm("catalog.сan_published")
                and user.has_perm("catalog.сan_edit_description")
                and user.has_perm("catalog.сan_edit_category")
        ) or user.is_superuser:
            queryset = queryset.all()
        else:
            queryset = queryset.filter(is_published=True)
        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.object.pk])

    def form_valid(self, form):
        product = form.save()
        product.created_user = self.request.user
        form.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = "catalog.change_product"

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.created_user or user.is_superuser:
            return ProductForm
        if (
            user.has_perm("catalog.сan_published")
            and user.has_perm("catalog.сan_edit_description")
            and user.has_perm("catalog.сan_edit_category")
        ):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ContactPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "catalog/contacts.html")

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
        return render(request, "catalog/contacts.html")
