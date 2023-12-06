from django.views import generic
from local.models import Local
from local.forms import AddLocalForm
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

class LocalListView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    template_name = "local/local.html"
    model = Local

class LocalDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'login'
    model = Local
    template_name = 'local/detalhe_local.html'
    context_object_name = 'local'

def adicionar_local(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddLocalForm(request.POST, request.FILES) 
            if form.is_valid():
                form.save()
                return redirect('home') #TODO: considerar adicionar uma página de confirmação 
            else:
                print(form.errors)
        form = AddLocalForm()
        return render(request, 'local/adicionar_local.html', {'form':form})
    return redirect('login')
