from django.db import models


class Firm(models.Model):
    """Class for firm"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "#{id} {name}".format(id=self.id, name=self.name)

    class Meta:
        ordering = ['name']


class Product(models.Model):
    """Class for product. it has one to many relation with Firm on firm column."""
    name = models.CharField(max_length=200)
    firm = models.ForeignKey(Firm)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ['name']


class Comment(models.Model):
    """Class for comment. This object holds the user comments, ratings and product photos.
    product column has a relation with Product object.  """
    title = models.CharField(max_length=100)
    product = models.ForeignKey(Product)
    message = models.TextField()
    photo = models.ImageField()
    rate = models.PositiveSmallIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    #user - will be added
    #is_published - models.BooleanField(default=False) - comments that approved by admin will be published

    def __str__(self):
        return "{} {}".format(self.title, self.product)

    class Meta:
        get_latest_by = "creation_date"
        ordering = ['title']

