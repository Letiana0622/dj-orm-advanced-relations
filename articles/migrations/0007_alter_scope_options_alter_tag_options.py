# Generated by Django 4.1.5 on 2023-01-16 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_tag_scope_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-title'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
