from django.db import models

# Create your models here.

class Topic(models.Model):
	"""用户学习主题"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text


class Entry(models.Model):
	"""学到的关于某个主题的具体知识"""
	# 外键级联Topic，在建立entry标签时，显示topic的下拉菜单选项
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		"""若entry为复数，则显示entries而非entrys"""
		verbose_name_plural = 'entries'

	def __str__(self):
		"""返回模型的字符串表示"""
		return (self.text[::10]+'...')
