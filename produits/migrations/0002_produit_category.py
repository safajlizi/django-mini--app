# Generated by Django 4.0.2 on 2022-03-02 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0001_initial'),
        ('produits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='categorys.category'),
        ),
    ]