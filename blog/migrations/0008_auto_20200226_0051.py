# Generated by Django 2.2.6 on 2020-02-25 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200226_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment'),
        ),
    ]
