from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import models


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
            # instance
            if isinstance(attr, models.ForeignKey):
                foreign_model = attr.rel.to  # Model class
                v = foreign_model.objects.get(pk=v)
            setattr(instance, k, v)
        instance.save()

        data = self._to_json([instance])
        return self._json_response(data)
