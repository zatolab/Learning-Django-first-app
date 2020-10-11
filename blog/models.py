from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # Поле для заголовока статьи
    title = models.CharField(max_length=250)
    # Поле для формирование URL'ов
    slug = models.SlugField(max_length=250, unique_for_date='publish')
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

    # Метод, отвечающий за отображение объекта в человекочитаемом формате
    def __str__(self):
        return self.title
