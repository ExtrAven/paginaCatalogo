from django.db import models
from django.utils.html import format_html


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category_images/", blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def show_image(self):
        if self.image:
            return format_html(
                f'<img src="{self.image.url}" width="100" height="100" />'
            )
        else:
            return "No Hay Imagen"

    show_image.short_description = "Imagen"


class Product(models.Model):
    image = models.ImageField(upload_to="product_images", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"pertenece a la categoría {self.category}"

    def show_image(self):
        return format_html(f'<img src="{self.image.url}" width="200" height="200" />')

    show_image.short_description = "Imagen"
