from django.shortcuts import render, get_object_or_404, redirect

from .form import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BirthdayMixin:
    model = Birthday
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list')


class BirthdayCreateView(BirthdayMixin, CreateView):
    pass


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayDeleteView(DeleteView):
    model = Birthday
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list')


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    pass
