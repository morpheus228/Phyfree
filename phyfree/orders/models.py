from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=30, default='', null=False)
    last_name = models.CharField(max_length=30, default='', null=False)
    image = models.ImageField(null=True)

    employer_rating = models.FloatField(null=True)
    employee_rating = models.FloatField(null=True)
    employer_resume = models.TextField(null=True)
    employee_resume = models.TextField(null=True)

    active = models.BooleanField(default=False, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'users'


class Order(models.Model):
    id = models.AutoField(primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)
    activated_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)

    employer = models.ForeignKey('User', related_name='created_orders', null=False, on_delete=models.CASCADE)
    employee = models.ForeignKey('User', related_name='executed_orders', default='', null=True, on_delete=models.CASCADE)

    title = models.CharField(max_length=30, null=False)
    description = models.TextField(default='', null=True)
    location = models.CharField(max_length=15, default='', null=True)

    PRICE_CHOICES = zip(range(50, 10001, 50), range(50, 10001, 50))
    price = models.IntegerField(choices=PRICE_CHOICES, null=False)

    STATUS_CHOICES = enumerate(["CREATED", "AVAILABLE", "ACTIVE", "COMPLETED", "ERROR"])
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        db_table = "orders"

    def __str__(self):
        return str(self.id)
