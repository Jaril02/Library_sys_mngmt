from django.db import models

# Create your models here.
class Member(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    isbn=models.CharField(max_length=13)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Issue(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    issue_date=models.DateField(auto_now_add=True)
    return_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.book.title}-> {self.member.name}"
