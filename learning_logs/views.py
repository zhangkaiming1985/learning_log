from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
	"""学习笔记主页"""
	return render(request, 'learning_logs/index.html')

def topics(request):
	"""显示所有主题"""
	topics = Topic.objects.order_by("date_added")
	context = {'topics':topics}
	return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
	"""显示特定主题"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by("-date_added")
	context = {'topic':topic, 'entries':entries}
	return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
	"""增加新的主题"""
	if request.method != 'POST':
		# 若未提交数据，则提供一个新表单
		form = TopicForm()
	else:
		# POST提交数据，对其进行处理
		form = TopicForm(request.POST)
		if form.is_valid():# 验证表单合法性
			form.save()# 保存在数据库中
			return HttpResponseRedirect(reverse('learning_logs:topics'))# 重新定向，前往reverse解析的网址

	context = {'form':form}
	return render(request, 'learning_logs/new_topic.html', context)

