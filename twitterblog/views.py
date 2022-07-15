from django.shortcuts import render,redirect
from twitterblog.forms import UserRegistrationForm,User,LogInForm,UserProfileForm,PostForm
from django.views.generic import View,CreateView,FormView,TemplateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from twitterblog.models import UserProfile,Blogs
from django.utils.decorators import method_decorator


# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"you must login")
            return redirect("log-in")
    return wrapper



class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration.html"
    model = User
    success_url = reverse_lazy("log-in")


class LogInView(FormView):
    form_class = LogInForm
    template_name = "login.html"
    model = User
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("success")
                login(request,user)
                return redirect("home")
            else:
                messages.error(request,"login failed")
                return render(request,self.template_name,{"form":form})

@method_decorator(signin_required,name="dispatch")
class IndexView(CreateView):
    model = Blogs
    form_class = PostForm
    template_name = "home.html"
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        form.instance.author=self.request.user
        messages.success(self.request,"post has been saved")
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        blogs=Blogs.objects.all().order_by("-posted_date")
        context["blogs"]=blogs
        return context




@method_decorator(signin_required,name="dispatch")
class UserCreationView(CreateView):
    form_class = UserProfileForm
    template_name = "profile-creation.html"
    model = UserProfile
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"profile has been created")
        self.object = form.save()
        return super().form_valid(form)


@method_decorator(signin_required,name="dispatch")
class ProfileView(TemplateView):
    template_name = "myprofile.html"

@method_decorator(signin_required,name="dispatch")
class UserUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "user-update.html"
    success_url = reverse_lazy("my-profile")
    pk_url_kwarg = "user_id"

@signin_required
def log_out(request,*args,**kwargs):
    logout(request)
    return redirect("log-in")