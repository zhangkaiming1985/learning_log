# learning_logs/urls

from django.urls import path
from django.contrib.auth.views import login

from . import views

# 命名空间
app_name = 'users'

urlpatterns = [
	# URL请求模式

	# 登录
	# 因为未定义自己的视图函数，传递了一个字典来告诉Django到哪里去找我们编写的模板
	path('login/', login, {'template_name': 'users/login.html'}, name='login'),

	# 注销
	path('logout/', views.logout_view, name='logout'),

	# 注册新用户
	path('register/', views.register, name='register')


]
