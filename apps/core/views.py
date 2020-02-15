from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import permissions, mixins, status
from rest_framework.viewsets import GenericViewSet
from .serializers import ResellerSerializer
from django_tables2 import RequestConfig
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.http import HttpResponseRedirect
from apps.core.models import Reseller
from apps.core.tables import ResellerTable
from apps.core.forms import ResellerForm, ResellerFilter


class ResellerViewSet(GenericViewSet, mixins.CreateModelMixin):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = ResellerSerializer
    queryset = Reseller.objects.all()


class ResellerListView(ListView):
    model = Reseller
    template_name = 'core/reseller_list.html'
    context_object_name = 'Reseller'
    filterset_class = ResellerFilter

    def get_context_data(self, **kwargs):
        context = super(ResellerListView, self).get_context_data(**kwargs)
        table = ResellerTable(Reseller.objects.all().order_by('full_name'))
        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        context['table'] = table
        return context


class ResellerCreateView(CreateView):
    model = Reseller
    template_name = 'core/reseller-create.html'
    form_class = ResellerForm
    success_url = '/home'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class ReadMeView(TemplateView):
    template_name = "core/readme.html"

    def get_context_data(self, **kwargs):
        rst_file = kwargs['rst_file']
        with open(rst_file, 'r') as f:
            text = f.read()

        print(kwargs)

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['text'] = text

        return context
