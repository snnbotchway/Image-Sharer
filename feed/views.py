from django.views.generic import TemplateView, FormView, DetailView
from .forms import AddNewImage
from .models import Post
from django.contrib import messages

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['img_obj'] = Post.objects.all().order_by('-id')
        return context

class NewImageView(FormView):
    template_name= 'new-image.html'
    form_class= AddNewImage
    success_url= '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        Post.objects.create(
            description = form.cleaned_data['description'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'Image uploaded successfully!')
        return super().form_valid(form)
    


class ImageDetail(DetailView):
    template_name= 'detail.html'
    model = Post

