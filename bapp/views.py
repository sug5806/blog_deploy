from .models import Write
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Write

# Create your views here.
class Bloglist(ListView):
    model = Write

class Blogcreate(CreateView):
    model = Write
    fields = ['title', 'content']
    template_name_suffix = '_create'
    success_url = '/'


class Blogupdate(UpdateView):
    model = Write
    fields = ['title', 'content']
    template_name_suffix = '_update'
    success_url = '/'

class Blogdelete(DeleteView):
    model = Write
    template_name_suffix = '_delete'
    success_url = '/'

class Blogdetail(DetailView):
    model = Write
    template_name_suffix = '_detail'
