from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class blog_category(models.Model):
    blog_cat = models.CharField(max_length=60,unique=True)
    blogcat_img = models.ImageField(upload_to='images/')
    blogcat_description=models.CharField(max_length=200)
    def __str__(self):
        return self.blog_cat
    # (self):
    #     return self.blog_cat
    
class contact_info(models.Model):
    u_email = models.EmailField()
    u_message = models.CharField(max_length=200)
    def _str_(self):
        return self.u_email
class SubscribedUser(models.Model):
    #name = models.CharField(max_length=100)
    u_email = models.EmailField(max_length=100, unique=True)
    # created_date = models.DateTimeField('Date created', default=timezone.now)

    def str(self):
        return self.u_email
    
class blog_post(models.Model):
    blog_name =models.CharField(max_length=100)
    cover_img=models.ImageField(upload_to='images/')
    blog_description=RichTextField(blank=True)
    blog_cat=models.ForeignKey(blog_category, on_delete=models.CASCADE) #foreign key use for filtering
    like_count=models.IntegerField(default=0, null=True)
    view_count=models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.blog_name
    
class blog_comment(models.Model):
    u_comment = models.CharField(max_length=500)
    blog = models.ForeignKey(blog_post, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return f"Comment on '{self.blog.blog_name}': {self.u_comment}"