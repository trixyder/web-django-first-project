from django.db import models

# Create your models here.
class CrmStatus(models.Model):
    status_name = models.CharField(max_length=100, verbose_name='Название статуса')
    
    def __str__(self):
        return self.status_name 
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = "Статусы"




class Order(models.Model):
    order_date = models.DateField(auto_now=True)
    order_name = models.CharField(max_length=50, verbose_name="Имя")
    order_phonenumber = models.CharField(max_length=50, verbose_name= "Номер телефона")
    order_status = models.ForeignKey(CrmStatus, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.order_name
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"


class CrmComment(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete = models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name="Текст комментария")
    comment_dt = models.DateField(auto_now=True, verbose_name="Дата создания")
    
    
    def __str__(self):
        return self.comment_text
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"

            
        

    
    
    
