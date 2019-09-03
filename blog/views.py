from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .form import *
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from django.views.generic.edit import CreateView, FormView
from django.views.generic import ListView, View
from .models import Event
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-Date')
    serializer_class = BlogSerializer

def register(request):
    return render(request, 'blog/signup.html')

def login(request):
    return render(request, 'blog/login.html')

def BlogViews(request):
    posts = Blog.objects.all()
    return render(request, 'blog/index.html', { 'post': posts })

def Success(request):
    return render(request, 'blog/success.html')

    

def comment(request):
    return render(request, 'blog/blogdetail.html')

def SignUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
    else:
        form = UserRegisterForm()
    return render(request, "signup1.html", {'form': form})


def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_surname = request.POST.get('contact_surname')
            contact_email = request.POST.get('contact_email')
            contact_subject = request.POST.get('contact_subject')
            contact_content = request.POST.get('content')

            template = get_template('blog/contact_form.txt')
            
            context = {
                'contact_name' : contact_name,
                'contact_surname': contact_surname,
                'contact_email' : contact_email,
                'contact_subject': contact_subject,
                'contact_content' : contact_content,
            }
            
            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                "To Waves" + '',
                ['emka6451@gmail.com'],
                headers = { 'Reply To': contact_email }
            )

            email.send()

            return redirect('blog:success')
    return render(request, 'blog/contact1.html', {'form':Contact_Form })

def contact_us(request):
    return render(request, 'blog/contact1.html')

def commentuser(request):
    return render(request, 'blog/comment_users.html')

def user_panel(request):
    return render(request, 'blog/profile.html')

def join(request):
    return render(request, 'blog/join_events.html')

def homepage(request):
    categories = Category.objects.all()
    return render(request, 'blog/homepage.html',{'categories':categories})



def login(request):
    return render(request, 'blog/login1.html')

def logout(request):
    return render(request, 'blog/homepage.html')

def eventcreate(request):
    return render(request, 'blog/create.html')

def event_user_page(request):
    return render(request, 'blog/event_user_page.html')

def signup(request):
    return render(request, 'blog/signup1.html')

def categories(request):
    events = Event.objects.all()
    return render(request, 'blog/categories.html',{'events':events})

class JoinAjaxView(View):
    def get(self,request):
        if self.request.is_ajax():
            event_id = self.request.GET.get('event_id',False)
            if event_id:
                current_event = Event.objects.get(pk=event_id)
                current_event.user.add(self.request.user)
                return JsonResponse({
                    'message':'Success',
                    'joined_user_count': current_event.user.count()
                },status=200)
            return JsonResponse({
                'message':'Not found'
            },status=404)

class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    # fields = ['name','description','start_time','img','category','appointment_time']
    template_name = 'blog/create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def description(request):
    context = {}
    event = Event.objects.filter(user=request.user).last()
    return render(request, 'blog/description.html', {'event':event})


        
