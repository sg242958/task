from django.db import models

# Create your models here.
class Category(models.Model):
	course_name = models.CharField(max_length=100)

	def __str__(self):
		return self.course_name

class Subcategory(models.Model):
	subcat = models.ForeignKey(Category, on_delete=models.CASCADE)
	subcatname = models.CharField(max_length=50, default='NULL')

	def __str__(self):
		return self.subcatname

class Subsub(models.Model):
	subsub = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
	subsubname = models.CharField(max_length=50,  default='NULL')

	def __str__(self):
		return self.subsubname



