# learning_logs/urls

from django.urls import path

from . import views

# 命名空间
app_name = 'learning_logs'

urlpatterns = [
	# URL请求模式

	# 主页
	path('', views.index, name='index'),

	# 显示所有主题
	path('topics/', views.topics, name='topics'),

	# 显示特定主题
	# 当请求网址模式与下面相同时，捕获int值，存储在topic_id中，连同request一同发给view
	path('topics/<int:topic_id>/', views.topic, name='topic'),

	# 增加新的主题
	path('new_topic/', views.new_topic, name='new_topic'),

	# 增加新的条目
	path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),

	# 编辑条目
	path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
