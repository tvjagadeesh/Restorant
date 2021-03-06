from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView,CreateView
from .models import RestaurantLocation
from .forms import RestaurantCreateView,RestaurantLocationCreateForm

# Create your views herd
def restaurants_createview(request):
    form=RestaurantLocationCreateForm(request.POST or None)
    errors=None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/restaurants/')

    if form.errors:
        errors=form.errors

    template_name='restaurants/form.html'
    context={'form':form,'errors':errors}
    return render(request,template_name,context)





class HomeTemplateview(TemplateView):
    #template_name='restaurants_list.html'
    queryset=RestaurantLocation.objects.all()
    extra_context={
    'object_list':queryset
    }
    print(queryset)
    def get(self, request, *args, **kwargs):
        queryset=RestaurantLocation.objects.all()
        context ={
        'object_list':queryset
        }
        return self.render_to_response(context)



class Restaurant_ListView(ListView):
      queryset=RestaurantLocation.objects.all()
      def get_queryset(self):
          print(self.kwargs)
          slug=self.kwargs.get('slug')
          if slug:
              queryset=RestaurantLocation.objects.filter(
              Q(category__icontains=slug) |
              Q(category__iexact=slug))
          else:
              queryset=RestaurantLocation.objects.all()
          return queryset
class RestaurantDetailView(DetailView):
      queryset=RestaurantLocation.objects.all()
'''      def get_object(self,*args,**kwargs):
          rest_id=self.kwargs.get('rest_id')
          obj=get_object_or_404(RestaurantLocation,id=rest_id)
          slug_field=super(RestaurantDetailView,self).get_slug_field()
          print(str(obj)+'this is the object'+str(slug_field))
          return obj'''


class RestaurantCreateView(CreateView):
    form_class=RestaurantLocationCreateForm
    template_name='restaurants/form.html'
    success_url = "/restaurants/"
