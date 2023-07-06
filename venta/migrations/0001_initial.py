# Generated by Django 4.1.7 on 2023-07-05 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.modelo')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.producto')),
                ('stocktienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stocktienda')),
            ],
        ),
    ]