from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from money.forms import CategoryForm, BillForm
from money.models import Bill, Category
from money.views import BillCreateView, StatsView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r"^category/$", login_required(ListView.as_view(
        model=Category,
        template_name="list_category.html"
    )), name="category"),
    url(r"^category/add/$", login_required(CreateView.as_view(
        model=Category,
        template_name="form_category.html",
        form_class=CategoryForm,
        success_url="/category/",
    )), name="category_add"),
    url(r"^category/rm/(?P<pk>\d+)/$", login_required(DeleteView.as_view(
        queryset=Category.objects.order_by("name"),
        template_name="confirm_category.html",
        success_url="/category/",
    )), name="category_remove"),
    url(r"^category/update/(?P<pk>\d+)/$", login_required(UpdateView.as_view(
        model=Category,
        template_name="form_category.html",
        form_class=CategoryForm,
        success_url="/category/",
    )), name="category_update"),
    url(r"^bill/add/$", login_required(BillCreateView.as_view(
        template_name="form_bill.html",
        form_class=BillForm,
        success_url="/",
    )), name="bill_add"),
    url(r"^bill/rm/(?P<pk>\d+)/$", login_required(DeleteView.as_view(
        model=Bill,
        template_name="confirm_bill.html",
        success_url="/",
    )), name="bill_remove"),
    url(r"^bill/update/(?P<pk>\d+)/$", login_required(UpdateView.as_view(
        model=Bill,
        template_name="form_bill.html",
        form_class=BillForm,
        success_url="/",
    )), name="bill_update"),
    url(r"^stats/$", login_required(StatsView.as_view()), name="stats"),
    url(r"^mobile/$", login_required(TemplateView.as_view(
        template_name="mobile.html",
    )), name="mobile"),
    url(r"^", login_required(ListView.as_view(
        queryset=Bill.objects.order_by("date").reverse(),
        template_name="list_bill.html",
        paginate_by=20,
    )), name="home"),
)
