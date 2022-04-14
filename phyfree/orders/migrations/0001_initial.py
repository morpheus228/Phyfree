# Generated by Django 4.0.4 on 2022-04-13 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('employer_rating', models.FloatField(null=True)),
                ('employee_rating', models.FloatField(null=True)),
                ('employer_resume', models.TextField(null=True)),
                ('employee_resume', models.TextField(null=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activated_at', models.DateTimeField(null=True)),
                ('completed_at', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(default='', null=True)),
                ('location', models.CharField(default='', max_length=15, null=True)),
                ('price', models.IntegerField(choices=[(50, 50), (100, 100), (150, 150), (200, 200), (250, 250), (300, 300), (350, 350), (400, 400), (450, 450), (500, 500), (550, 550), (600, 600), (650, 650), (700, 700), (750, 750), (800, 800), (850, 850), (900, 900), (950, 950), (1000, 1000), (1050, 1050), (1100, 1100), (1150, 1150), (1200, 1200), (1250, 1250), (1300, 1300), (1350, 1350), (1400, 1400), (1450, 1450), (1500, 1500), (1550, 1550), (1600, 1600), (1650, 1650), (1700, 1700), (1750, 1750), (1800, 1800), (1850, 1850), (1900, 1900), (1950, 1950), (2000, 2000), (2050, 2050), (2100, 2100), (2150, 2150), (2200, 2200), (2250, 2250), (2300, 2300), (2350, 2350), (2400, 2400), (2450, 2450), (2500, 2500), (2550, 2550), (2600, 2600), (2650, 2650), (2700, 2700), (2750, 2750), (2800, 2800), (2850, 2850), (2900, 2900), (2950, 2950), (3000, 3000), (3050, 3050), (3100, 3100), (3150, 3150), (3200, 3200), (3250, 3250), (3300, 3300), (3350, 3350), (3400, 3400), (3450, 3450), (3500, 3500), (3550, 3550), (3600, 3600), (3650, 3650), (3700, 3700), (3750, 3750), (3800, 3800), (3850, 3850), (3900, 3900), (3950, 3950), (4000, 4000), (4050, 4050), (4100, 4100), (4150, 4150), (4200, 4200), (4250, 4250), (4300, 4300), (4350, 4350), (4400, 4400), (4450, 4450), (4500, 4500), (4550, 4550), (4600, 4600), (4650, 4650), (4700, 4700), (4750, 4750), (4800, 4800), (4850, 4850), (4900, 4900), (4950, 4950), (5000, 5000), (5050, 5050), (5100, 5100), (5150, 5150), (5200, 5200), (5250, 5250), (5300, 5300), (5350, 5350), (5400, 5400), (5450, 5450), (5500, 5500), (5550, 5550), (5600, 5600), (5650, 5650), (5700, 5700), (5750, 5750), (5800, 5800), (5850, 5850), (5900, 5900), (5950, 5950), (6000, 6000), (6050, 6050), (6100, 6100), (6150, 6150), (6200, 6200), (6250, 6250), (6300, 6300), (6350, 6350), (6400, 6400), (6450, 6450), (6500, 6500), (6550, 6550), (6600, 6600), (6650, 6650), (6700, 6700), (6750, 6750), (6800, 6800), (6850, 6850), (6900, 6900), (6950, 6950), (7000, 7000), (7050, 7050), (7100, 7100), (7150, 7150), (7200, 7200), (7250, 7250), (7300, 7300), (7350, 7350), (7400, 7400), (7450, 7450), (7500, 7500), (7550, 7550), (7600, 7600), (7650, 7650), (7700, 7700), (7750, 7750), (7800, 7800), (7850, 7850), (7900, 7900), (7950, 7950), (8000, 8000), (8050, 8050), (8100, 8100), (8150, 8150), (8200, 8200), (8250, 8250), (8300, 8300), (8350, 8350), (8400, 8400), (8450, 8450), (8500, 8500), (8550, 8550), (8600, 8600), (8650, 8650), (8700, 8700), (8750, 8750), (8800, 8800), (8850, 8850), (8900, 8900), (8950, 8950), (9000, 9000), (9050, 9050), (9100, 9100), (9150, 9150), (9200, 9200), (9250, 9250), (9300, 9300), (9350, 9350), (9400, 9400), (9450, 9450), (9500, 9500), (9550, 9550), (9600, 9600), (9650, 9650), (9700, 9700), (9750, 9750), (9800, 9800), (9850, 9850), (9900, 9900), (9950, 9950), (10000, 10000)])),
                ('status', models.IntegerField(choices=[(0, 'CREATED'), (1, 'AVAILABLE'), (2, 'ACTIVE'), (3, 'COMPLETED'), (4, 'ERROR')], default=0)),
                ('employee', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executed_orders', to='orders.user')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_orders', to='orders.user')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
