from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=100)
    # author = models.ForeignKey(Author, on_delete='models.Cascade')
    author = models.ManyToManyField(Author, through='Book_Author')


class Book_Author(models.Model):
    book = models.ForeignKey(Book)
    author = models.ForeignKey(Author)
    user = models.CharField(max_length=100)

    class Meta:
        # чтобы пары id не повторялись
        unique_together = (('book', 'author'),)
        # ordering = ['-user']
        # db_table = ''




"""
class TaggedItem(models.Model):
    content_type = models.ForeignKey(ContentType)
    tag = models.SlugField()
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

u = User()

t = TaggedItem(content_object=u, tag='')
"""