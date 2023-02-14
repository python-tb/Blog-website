from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name 

    @property
    def cat_count(self):
        blogs = self.blog_set.all()
        num = blogs.count()
        return num

   
class Blog(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=35)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # category = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try: 
            url = self.image.url 
        except:
            url = ""

        return url 