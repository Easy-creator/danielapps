from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
    
class Products(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    image = models .ImageField(null=False, upload_to="products_images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=00, null=False)
    
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    objects = models.Manager() #default manager 

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-date',)
