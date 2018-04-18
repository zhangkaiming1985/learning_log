from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import logout


def logout_view(request):
	"""注销用户"""

	logout(request)
	return redirect('learning_logs:index')


def register(request):
	"""注册新用户"""

	# 初次显示空表单
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# 让用户自动登录，再重新定向到主页
			authenticated_user = authenticate(username=new_user.username,
											  password=request.POST['password1'])
			login(request, authenticated_user)
			return redirect('learning_logs:index')

	context = {'form': form}
	return render(request, 'users/register.html', context)
