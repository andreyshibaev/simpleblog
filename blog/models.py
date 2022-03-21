from django.db import models
from django.urls import reverse


class CategoryPost(models.Model):
    name_category = models.CharField(verbose_name='name category', max_length=90, db_index=True)
    slug = models.SlugField(verbose_name='slug', db_index=True, unique=True, null=True)
    content = models.TextField(verbose_name='content', blank=True)

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self): 
        return self.name_category

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})
    


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='name post', db_index=True)
    slug = models.SlugField(verbose_name='slug', db_index=True, unique=True, null=True)
    content = models.TextField(verbose_name='text post')
    publish = models.BooleanField(default=True)
    datearticle = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(verbose_name='photo', upload_to='blog/', blank=True)
    category = models.ForeignKey(CategoryPost, verbose_name='category', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'New post'
        verbose_name_plural = 'All posts'
 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
              