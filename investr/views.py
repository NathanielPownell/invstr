from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import CreateView, ListView, DeleteView  
from users.models import Position, Wlist
from .forms import EnterPositionForm, wlist_form
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.

@login_required
def dash(request):
    return render(request, 'invstr/index.html')

@login_required
def trade(request):

    if request.method == "POST": #checking if the request method is a POST

        if "buy" in request.POST: #checking if there is a request to delete a todo
            

            context = {
                'message' : "Buy order placed!"
            }
            return render(request, "invstr/trade.html", context)


        if "sell" in request.POST:


            context = {
                'message' : "Buy order placed!"
            }
            return render(request, "invstr/trade.html", context)


    else:
        return render(request, "invstr/trade.html")




    return render(request, 'invstr/trade.html')







@login_required
def tradedetail(request, slug):
    return render(request, 'invstr/trade.html')

# class history(request):
#     return render(request, 'invstr/history.html')

class test(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'invstr/history.html')

class history(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        labels = [
            'January',
            'February', 
            'March', 
            'April', 
            'May', 
            'June', 
            'July'
            ]

        chartdata = [100000, 90000, 105000, 110000, 98000, 104000, 120000]
        data ={
                     "labels":labels,
                     "chartdata":chartdata,
             }
        return Response(data)


# class watchlist(ListView):
#     model = Wlist

#         # Begin testing
#     if request.method == "POST": #checking if the request method is a POST
        
#         if "taskDelete" in request.POST: #checking if there is a request to delete a todo
#             checkedlist = request.POST["checkedbox"] #checked todos to be deleted
#             for todo_id in checkedlist:
#                 todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
#                 todo.delete() #deleting todo

#     else:
#         def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             return context
#         template_name = "invstr/watchlist.html"







from django.shortcuts import render,redirect
# from .models import TodoList, Category

def watchlist(request): #the index view
    todos = Wlist.objects.all() #quering all todos with the object manager
    
    if request.method == "POST": #checking if the request method is a POST

        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = int(request.POST["checkedbox"]) #checked todos to be deleted
            # typeof = checkedlist.type()
            # for check in checkedlist:

            stock = Wlist.objects.get(id=int(checkedlist)) #getting todo id
            stock.delete() #deleting todo
        return render(request, "invstr/watchlist.html", {"object_list": todos})

    else:
        return render(request, "invstr/watchlist.html", {"object_list": todos})



def resetwatchlist(request):
    stocks = Wlist.objects.all()

    if request.method == "POST":
        for x in stocks:
            x.delete()

        context = {
            'message' : "Your watchlist has been reset"
        }

        return render(request, "invstr/watchlist_delete.html", context)

    else:
        return render(request, "invstr/watchlist_delete.html")

            











# def watchlist_edit(request):
    
#     if request.method == 'POST': # If the form has been submitted...
#         form = wlist_form(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#             # Process the data in form.cleaned_data
#             # ...
#             form.save()

#             print(form.cleaned_data['my_form_field_name'])

#             return HttpResponseRedirect('/invstr/watchlist.edit.html') # Redirect after POST
#     else:
#         form = wlist_form() # An unbound form
#         fields = {symbol : 'symbol', user : 'user'}

#     return render(request, fields, template_name='invstr/watchlist_edit.html')

class watchlist_edit(CreateView):
    model = Wlist
    template_name = "invstr/watchlist_edit.html"
    form_class = wlist_form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# class watchlist_delete(DeleteView):
    # model = Wlist
    # success_url = reverse_lazy('watchlist')
    # if request.method == 'POST':
    #     return render(request, 'invstr/watchlist_edit.html')
    # def get_object(self):
    #     symbol_ = self.kwargs.get("symbol")
    #     return get_object_or_404(Wlist, symbol = symbol_)
    # else :
    #     return render(request, 'invstr/watchlist_edit.html')

   
    
  
    # def get_object(self):
    #     symbol_ = self.kwargs.get("symbol")
    #     return get_object_or_404(Wlist, symbol = symbol_)







@login_required
def news(request):
    return render(request, 'invstr/news.html')

class buy(CreateView):
    model = Position
    template_name = 'invstr/trade.html'
    form_class = EnterPositionForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.entryprice = self.object.getprice(self.object.user)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())