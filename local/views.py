from django.views import generic
from local.models import Local

class LocalListView(generic.ListView):
    template_name = "local/local.html"
    model = Local
