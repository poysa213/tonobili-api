# Generated by Django 4.0 on 2023-02-26 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField(default=5, null=True)),
                ('vitess', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('is_verify', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('state', models.CharField(blank=True, choices=[('NEW', 'New'), ('OLD', 'Old')], default='OLD', max_length=255)),
                ('transmission', models.CharField(choices=[('AUTO', 'Auto'), ('MANUAL', 'Manual'), ('AUTOMANUAL', 'Auto Manual')], default='MANUAL', max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarMarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='store.carmarket')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, null=True)),
                ('is_verify', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('state', models.CharField(blank=True, choices=[('NEW', 'New'), ('OLD', 'Old')], default='NEW', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PartCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PartImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='store/images/parts')),
                ('part', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='store.part')),
            ],
        ),
        migrations.AddField(
            model_name='part',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='store.partcategory'),
        ),
        migrations.AddField(
            model_name='part',
            name='market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='store.carmarket'),
        ),
        migrations.AddField(
            model_name='part',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='store.carmodel'),
        ),
        migrations.AddField(
            model_name='part',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='users.user'),
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='store/images/cars')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='store.carmarket'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='store.carmodel'),
        ),
        migrations.AddField(
            model_name='car',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='users.user'),
        ),
    ]
