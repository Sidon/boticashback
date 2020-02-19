from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions, mixins, status
from rest_framework.viewsets import GenericViewSet
from .serializers import ResellerSerializer
from django_tables2 import RequestConfig
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.http import HttpResponseRedirect
from apps.reseller.models import Reseller
from apps.reseller.tables import ResellerTable
from apps.reseller.forms import ResellerForm, ResellerFilter

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


class ResellerViewSet(GenericViewSet, mixins.CreateModelMixin):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)

    # permission_classes = (IsAuthenticated,)
    serializer_class = ResellerSerializer
    queryset = Reseller.objects.all()


class ResellerListView(ListView):
    model = Reseller
    template_name = 'reseller/reseller_list.html'
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
    template_name = 'reseller/reseller-create.html'
    form_class = ResellerForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class ReadMeView(TemplateView):
    template_name = "reseller/readme.html"

    def get_context_data(self, **kwargs):
        rst_file = kwargs['rst_file']
        with open(rst_file, 'r') as f:
            text = f.read()

        print(kwargs)

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['text'] = text

        return context


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated', 'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'reseller/login.html', {'form': form})