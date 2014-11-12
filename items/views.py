#from django.shortcuts import render

from django.views.generic import base, list, DetailView
from models import Item, Photo

# Create your views here.

class IndexView(base.TemplateView):

    template_name = "Index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['item_list'] = lambda: Item.objects.all()
        return context
        
class Item_List_View(list.ListView): 
    template_name = 'items_list.html'
     
    def get_context_data(self, **kwargs):
        context = super(Item_List_View, self).get_context_data(**kwargs)
        context['item_list'] = self.queryset
        return context
    
    def get_queryset(self):
        return Item.objects.all()
        
class Item_Detail_View(DetailView):
    template_name = 'items_detail.html'
    model = Item
       
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Item.objects.all())
        return super(Item_Detail_View, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Item_Detail_View, self).get_context_data(**kwargs)
        context['item_detail'] = self.object
        return context

class Photo_Detail_View(DetailView):
    template_name = 'photos_detail.html'
    model = Photo
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Photo.objects.all())
        return super(Photo_Detail_View, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Photo_Detail_View, self).get_context_data(**kwargs)
        context['photo_detail'] = self.object
        return context
    