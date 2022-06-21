from django.views.generic import TemplateView, FormView
from .forms import AddNewImage
from .models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['img_obj'] = Post.objects.all()
        return context
    

class NewImageView(FormView):
    template_name= 'new-image.html'
    form_class= AddNewImage
    success_url= '/'

    def form_valid(self, form):
        Post.objects.create(
            description = form.cleaned_data['description'],
            image = form.cleaned_data['image']
        )
        return super().form_valid(form)