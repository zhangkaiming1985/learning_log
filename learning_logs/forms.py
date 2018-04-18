from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
	"""基于Topic建立的表单"""

	class Meta:
		model = Topic
		# 表单包含的字段
		fields = ['text']
		# 指定了一个空标签
		labels = {'text': ''}


class EntryForm(forms.ModelForm):
	"""基于Entry建立的表单"""

	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		# 小部件属性，使文本区域的宽度由默认的40列增加到80列
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
