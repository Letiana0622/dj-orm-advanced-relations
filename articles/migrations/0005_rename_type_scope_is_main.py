# Generated by Django 4.1.5 on 2023-01-15 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='type',
            new_name='is_main',
        ),
    ]
