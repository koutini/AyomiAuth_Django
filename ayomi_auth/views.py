from django.shortcuts import render, redirect
from ayomi_auth.forms import SignUpForm, UpdateProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


def RegisterView(request):
    """Definition of register view method"""
    if request.user.is_authenticated:
        return redirect('profile')
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            messages.success(request, 'Your account was created you can login now ! ')
            return redirect('login')
        else:
            messages.error(request, 'Your account was  not created')
    return render(request, 'register.html', {'form': form})


def LoginView(request):
    """Definition of login view method"""
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def LogoutView(request):
    """Definition of logout view method"""
    logout(request)
    return redirect('login')


class ProfileView(LoginRequiredMixin, TemplateView):
    """Definition of profile view class"""
    user_form = UpdateProfileForm
    template_name = 'profile.html'

    def post(self, request):

        post_data = request.POST or None
        user_form = UpdateProfileForm(post_data, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.info(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)