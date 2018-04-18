from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
	"""学习笔记主页"""
	return render(request, 'learning_logs/index.html')


def topics(request):
	"""显示所有主题"""
	topics = Topic.objects.order_by("date_added")
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
	"""显示特定主题"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by("-date_added")
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
	"""增加新的主题"""
	if request.method != 'POST':
		# 若未提交数据，则提供一个新表单
		form = TopicForm()
	else:
		# POST提交数据，对其进行处理
		form = TopicForm(request.POST)
		if form.is_valid():  # 验证表单合法性
			form.save()  # 保存在数据库中
			return HttpResponseRedirect(reverse('learning_logs:topics'))  # 重新定向，前往reverse解析的网址

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
	"""增加新条目"""
	# 获取当前topic
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)  # 若new_entry = form 不能保存增加的entry，改成form.topic = topic, form.save()亦是如此
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
	"""编辑条目"""

	# 获取当前主题和条目
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method != 'POST':
		# 初次请求，使用当前条目填充
		form = EntryForm(instance=entry, data=None)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

	context = {'topic': topic, 'entry': entry, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)


