from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

Tank = 'Tank'
Healing = 'Healing'
Dd = 'Dd'
Trader = 'Trader'
Gildmaster = 'Gildmaster'
Questgiver = 'Questgiver'
Blacksmiths = 'Blacksmiths'
Tanners = 'Tanners'
Potion_Makers = 'Potion_Makers'
Spell_Masters = 'Spell_Masters'

POST_CATEGORY = [
    (Tank, 'Танк'),
    (Healing, 'Хилы'),
    (Dd, 'ДД'),
    (Trader ,'Продавцы'),
    (Gildmaster, 'Гилдмастеры'),
    (Questgiver, 'Квестгиверы'),
    (Blacksmiths, 'Кузнецы'),
    (Tanners, 'Кожевники'),
    (Potion_Makers, 'Зельевары'),
    (Spell_Masters, 'Мастера Заклинаний'),
]

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, choices=POST_CATEGORY, default=Tank)
    headline = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    time_create = models.DateTimeField(auto_now_add=True)
    response = models.ManyToManyField(User)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Category(models.Model):
    category = models.CharField(max_length=24)

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 

