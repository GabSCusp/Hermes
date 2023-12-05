from django.views import generic
from local.models import Local
from local.forms import AddLocalForm
from django.shortcuts import redirect, render

class LocalListView(generic.ListView):
    template_name = "local/local.html"
    model = Local

def adicionar_local(request):
    if request.method == "POST":
        form = AddLocalForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('home') #TODO: considerar adicionar uma página de confirmação 
        else:
            print(form.errors)
    form = AddLocalForm()
    return render(request, 'local/adicionar_local.html', {'form':form})
