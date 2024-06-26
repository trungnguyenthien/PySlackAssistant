# Generated by Django 4.2.11 on 2024-05-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_channeltsrecord_name_jp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemMessageRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cid_jp', models.CharField(default='', max_length=12)),
                ('cid_vn', models.CharField(default='', max_length=12)),
                ('message', models.TextField(default='')),
            ],
        ),
    ]
