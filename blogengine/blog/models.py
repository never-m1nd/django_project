from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Post(models.Model):
    body = models.TextField(db_index=True)
    title = models.CharField(max_length=40, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, max_length=50)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'pk': self.pk,
                                                  'slug': self.slug
                                                  })

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
            'slug': self.slug
        }
        return reverse('post_detail_url', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']


class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']