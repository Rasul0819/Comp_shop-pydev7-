from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255,verbose_name='Категория')
    slug = models.CharField(max_length=255,verbose_name='Слаг для категрий')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self) :
        return self.category_name

class Company(models.Model):
    company_name = models.CharField(max_length=255,verbose_name='Компания')
    slug = models.CharField(max_length=255,verbose_name='Слаг для компаний')
    class Meta:
        verbose_name = 'Комания'
        verbose_name_plural = 'Компании'
    def __str__(self) :
        return self.company_name
    

    
class Product(models.Model):
    price = models.DecimalField(max_digits=20,verbose_name='Цена',decimal_places=3)
    model_name = models.CharField(max_length = 255,verbose_name='Имя товара')
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE,
                                      verbose_name='Название категорий')
    company_name = models.ForeignKey(Company,on_delete=models.CASCADE,
                                     verbose_name='Название Компаний')
    description = models.TextField(verbose_name='Описание')
    image1 = models.ImageField(verbose_name='Главная картинка',upload_to='images')
    image2 = models.ImageField(verbose_name='Вторая картинка',upload_to='images',blank=True)
    image3 = models.ImageField(verbose_name='Третья картинка',upload_to='images',blank=True)
    count = models.IntegerField(verbose_name='Количество товара',)
    characteristcs = models.TextField(verbose_name='Характеристики товара',)
    sale_off = models.DecimalField(max_digits=20,verbose_name='Скидка',
                                   decimal_places=3,blank=True,null=True)
    date=models.DateTimeField(verbose_name='Дата',auto_now_add=True)
    likes = models.BooleanField(blank=True,verbose_name='Избранные')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    def __str__(self):
        return self.model_name



# class Comments(models.Model):
#     comment_text = models.TextField(verbose_name='Комментарий к продукту')
#     date = models.DateTimeField(auto_now_add=True,verbose_name='Дата коммента')
#     author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Автор коммента')
#     product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Имя продукта')
#     rating = models.IntegerField(verbose_name='Рейтинг продукта')

