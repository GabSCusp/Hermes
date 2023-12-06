from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Produto, Review, List
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import ReviewForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def detail_produto(request, produto_id):
    if request.user.is_authenticated:        
        produto = get_object_or_404(Produto, pk=produto_id)
        if 'last_viewed' not in request.session:
            request.session['last_viewed'] = []
        request.session['last_viewed'] = [produto_id] + request.session['last_viewed']
        if len(request.session['last_viewed']) > 5:
            request.session['last_viewed'] = request.session['last_viewed'][:-1]
        context = {'produto': produto}
        return render(request, 'produtos/detail.html', context)
    return redirect('login')


def list_produtos(request):
    if request.user.is_authenticated:
        produto_list = Produto.objects.all()
        context = {"produto_list": produto_list}
        return render(request, 'produtos/Produtos.html', context)
    return redirect('login')

def search_produtos(request):
    if request.user.is_authenticated:
        context = {}
        if request.GET.get('query', False):
            search_term = request.GET['query'].lower()
            produto_list = Produto.objects.filter(name__icontains=search_term)
            context = {"produto_list": produto_list}
        return render(request, 'produtos/search.html', context)
    return redirect('login')

def create_produto(request):
   if request.user.is_authenticated: 
    if request.method == 'POST':
        produto_name = request.POST['name']
        produto_preço = request.POST['preço']
        produto_Local = request.POST['Local']
        produto_poster_url = request.POST['poster_url']
        produto = Produto(name=produto_name,
                      preço=produto_preço,
                      Local=produto_Local,
                      poster_url=produto_poster_url)
        produto.save()
        return HttpResponseRedirect(
            reverse('produtos:detail', args=(produto.id, )))
    else:
        return render(request, 'produtos/create.html', {})
   return redirect('login')

@login_required
def create_review(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    
    if request.method == 'POST':
        # Atribuir o usuário autenticado como autor
        form = ReviewForm(request.POST, initial={'author': request.user.username})
        if form.is_valid():
            review_text = form.cleaned_data['text']
            review = Review(author=request.user,  # Usuário autenticado
                            text=review_text,
                            produto=produto)
            review.save()
            return HttpResponseRedirect(
                reverse('produtos:detail', args=(produto_id, )))
    else:
        # Atribuir o usuário autenticado como autor (caso não seja um POST)
        form = ReviewForm(initial={'author': request.user.username})
        
    context = {'form': form, 'produto': produto}
    return render(request, 'produtos/review.html', context)

class ListListView(generic.ListView, LoginRequiredMixin):
    login_url = 'login'
    model = List
    template_name = 'produtos/lists.html'


class ListCreateView(LoginRequiredMixin, generic.CreateView):
    model = List
    template_name = 'produtos/create_list.html'
    fields = ['name', 'author', 'produtos']
    success_url = reverse_lazy('produtos:lists')
    login_url = 'login'

class ListDetailView(LoginRequiredMixin, DetailView):
    model = List
    template_name = 'produtos/list_detail.html'  
    login_url = 'login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProdutoListView(LoginRequiredMixin, generic.ListView):
    model = Produto
    login_url = 'login'
    template_name = 'produtos/Produtos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'last_viewed' in self.request.session:
            unique_produto_ids = set(self.request.session['last_viewed'])
            context['last_produtos'] = [get_object_or_404(Produto, pk=produto_id) for produto_id in unique_produto_ids]
        return context

class LastViewedProdutosView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'produtos/last_viewed.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'last_viewed' in self.request.session:
            unique_produto_ids = set(self.request.session['last_viewed'])
            context['last_produtos'] = [get_object_or_404(Produto, pk=produto_id) for produto_id in unique_produto_ids]
        return context
