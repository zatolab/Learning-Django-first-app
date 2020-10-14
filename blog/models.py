from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Article(models.Model):
    """Статьи"""
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # Поле для заголовока статьи
    title = models.CharField(max_length=250)
    # Поле для изображения
    banner = models.ImageField(upload_to='blog_banners/', blank=True)
    # Поле для формирование URL'ов
    url = models.SlugField(max_length=250, unique_for_date='publish')
    # Поле содержащее внешний ключ (один ко многим) на пользователя
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # Поле для тела статьи
    body = models.TextField()
    # Поле для даты публикации статьи
    publish = models.DateField(default=timezone.now)
    # Поле для даты создания статьи
    created = models.DateField(auto_now_add=True)
    # Поле для даты изменения статьи
    update = models.DateField(auto_now=True)
    # Поле для отображения состояния статьи (опубликовано/черновик)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')



    # Метаданные
    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('-publish',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.url])

    # Метод, отвечающий за отображение объекта в человекочитаемом формате
    def __str__(self):
        return self.title
