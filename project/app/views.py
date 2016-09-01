from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView
from django.http import HttpResponse
from django.core import serializers
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import models
from models import Productos, Compras, Sedes, Clientes
from django import forms
from django.forms import modelformset_factory
from django.contrib import messages



class APIListCreate(View):
    model = None

    @method_decorator(csrf_exempt)  # CRSF exempt to POST, PUT
    def dispatch(self, request, *args, **kwargs):
        return super(APIListCreate, self).dispatch(request, *args, **kwargs)

    def get_model(self):
        return self.model

    def _to_json(self, queryset):
        """Serializes a queryset into json format"""
        return serializers.serialize('json', queryset)

    def _json_response(self, data):
        return HttpResponse(data, content_type="application/json")

    def get(self, *args, **kwargs):
        """Gets list of instances or detail of one instance
        if pk is provided in URL"""
        model = self.get_model()

        # Determine if we're getting a particular instance or a list of
        # instances
        if 'pk' in kwargs:
            try:
                data = self._to_json([model.objects.get(pk=kwargs['pk'])])
            except:
                raise Http404("Object %s doesn't exist." % (kwargs['pk']))
        else:
            data = self._to_json(model.objects.all())

        return self._json_response(data)

    def post(self, *args, **kwargs):
        post_data = self.request.POST
        model = self.get_model()

        for k, v in post_data.iteritems():
            instance = model()
            attr = model._meta.get_field(k)

            # If field is a foreignkey we need to get the related model
            # instance first.
            if isinstance(attr, models.ForeignKey):
                foreign_model = attr.rel.to  # Model class
                v = foreign_model.objects.get(pk=v)
            setattr(instance, k, v)
        instance.save()

        data = self._to_json([instance])
        return self._json_response(data)



class FormCompra(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ('producto',)

class ComprasView(FormView):
    template_name = 'compras.html'
    form_class = modelformset_factory(Compras, fields=('producto', 'sede', 'precio'),min_num=0, extra=0)
    success_url='/compras'

    def get_form(self):
        data = self.request.POST if self.request.method =='POST' else None
        return self.form_class(data, queryset=Compras.objects.none())

    def form_valid(self, form):
        # Set client from cliente input to all instances.
        client = Clientes.objects.get(pk=self.request.POST['cliente'])

        instances = form.save()
        for i in instances:
            i.cliente = client
            i.save()

        messages.add_message(self.request, messages.SUCCESS,"Se han agregado las siguientes compras <ul>%s</ul>"%(
            ''.join(["<li>%s</li>"%(i) for i in instances])))
        return super(ComprasView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context= super(ComprasView, self).get_context_data(**kwargs)
        context['products'] = Productos.objects.all()
        context['sedes'] = Sedes.objects.all()
        context['clientes'] = Clientes.objects.all()
        return context
