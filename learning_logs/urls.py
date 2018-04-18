# learning_logs/urls

from django.urls import path

from . import views

# 命名空间
app_name = 'learning_logs'

urlpatterns = [
	# 主页
	path('', views.index, name='index'),

	# 显示所有主题
	path('topics/', views.topics, name='topics'),

	# 显示特定主题
	path('topics/<int:topic_id>/', views.topic, name='topic'),

	# 增加新的主题
	path('new_topic/', views.new_topic, name='new_topic')
]