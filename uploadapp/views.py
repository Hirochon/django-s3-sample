from django.views import generic
from .forms import PhotoForm
from .models import PhotoModel

class Photo(generic.CreateView):
    model = PhotoModel
    form_class = PhotoForm
    template_name = 'uploadapp/uploadapp.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Photo, self).get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["photos"] = PhotoModel.objects.all()
        return context
