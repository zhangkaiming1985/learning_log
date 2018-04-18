from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
	"""基于Topic建立的表单"""
	class Meta:
		model = Topic
		# 表单包含的字段
		fields = ['text']
		# 不要为text生成标签
		labels = {'text': ''}