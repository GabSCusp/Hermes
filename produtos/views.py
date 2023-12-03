from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Produto, Review, List
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import ReviewForm
from django.shortcuts import render, get_object_or_404

def detail_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    context = {'produto': produto}
    return render(request, 'produtos/detail.html', context)

def list_produtos(request):
    produto_list = Produto.objects.all()
    context = {"produto_list": produto_list}
    return render(request, 'produtos/Produtos.html', context)

def detail_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    context = {'produto': produto}
    return render(request, 'produtos/detail.html', context)

def search_produtos(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        produto_list = Produto.objects.filter(name__icontains=search_term)
        context = {"produto_list": produto_list}
    return render(request, 'produtos/search.html', context)

def create_produto(request):
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

def create_review(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_author = form.cleaned_data['author']
            review_text = form.cleaned_data['text']
            review = Review(author=review_author,
                            text=review_text,
                            produto=produto)
            review.save()
            return HttpResponseRedirect(
                reverse('produtos:detail', args=(produto_id, )))
    else:
        form = ReviewForm()
    context = {'form': form, 'produto': produto}
    return render(request, 'produtos/review.html', context)

class ListListView(generic.ListView):
    model = List
    template_name = 'produtos/lists.html'


class ListCreateView(generic.CreateView):
    model = List
    template_name = 'produtos/create_list.html'
    fields = ['name', 'author', 'produtos']
    success_url = reverse_lazy('produtos:lists')

