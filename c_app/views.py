from django.shortcuts import render,get_object_or_404,redirect
from .models import Contact
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def  home(request):
    context={
        'contacts':Contact.objects.all()
    }
    return render(request,"index.html",context)

def detail(request,id):
    context={
        'Contact':get_object_or_404(Contact, pk=id)
    }
    return render(request,"detail.html",context)

def search(request):
    if request.GET:
        search_term = request.GET['search_term'] 
        search_result =Contact.objects.filter(
            Q(Name__icontains=search_term) |
            Q(information__icontains=search_term)

        )

        context={
            'search_term': search_term,
            'contacts': search_result
        }
        return render(request,'search.html',context)
    else:
        return redirect('home')

class ContactCreateView(CreateView):
    model = Contact
    template_name = "create.html"
    fields=['Name','email','phone','gender','information','image']
    success_url='/'

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = "update.html"
    fields=['Name','email','phone','gender','information','image']
    def form_valid(self,form):
        instance = form.save()
        return redirect('detail',instance.pk)

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = "delete.html"
    success_url='/'

class SingUpView(CreateView):
    from_class= UserCreationForm
    template_name ='registration/signup.html'
    success_url='home'
