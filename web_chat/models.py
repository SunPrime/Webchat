from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=10)


class Person(models.Model):
    name = models.CharField(max_length=30)
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)


class Message(models.Model):
    body = models.CharField(max_length=100)
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(Person, on_delete=models.CASCADE)


class Ban(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)