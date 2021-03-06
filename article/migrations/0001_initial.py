# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-11 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('content', models.TextField(default=b'', verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('count', models.IntegerField(default=0, verbose_name='\u6587\u7ae0\u70b9\u51fb\u6570')),
                ('editor', models.SmallIntegerField(choices=[(1, '\u5bcc\u6587\u672c\u7f16\u8f91\u5668'), (2, 'Markdown\u7f16\u8f91\u5668')], default=1, verbose_name='\u7f16\u8f91\u5668\u7c7b\u578b')),
                ('status', models.SmallIntegerField(choices=[(1, '\u8349\u7a3f'), (2, '\u5df2\u53d1\u5e03')], default=2, verbose_name='\u72b6\u6001')),
            ],
            options={
                'ordering': ['-publish_time'],
                'verbose_name_plural': '\u535a\u6587\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='ArticleManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='\u90ae\u4ef6')),
                ('website', models.URLField(blank=True, verbose_name='\u4e2a\u4eba\u7f51\u7ad9')),
            ],
            options={
                'verbose_name_plural': '\u6587\u7ae0\u4f5c\u8005',
            },
        ),
        migrations.CreateModel(
            name='CarouselImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.CharField(max_length=50, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('description', models.CharField(max_length=100, verbose_name='\u56fe\u7247\u63cf\u8ff0')),
                ('path', models.CharField(max_length=100, verbose_name='\u56fe\u7247\u5730\u5740')),
                ('link', models.CharField(blank=True, default=b'', max_length=200, null=True, verbose_name='\u56fe\u7247\u5916\u94fe')),
                ('weights', models.SmallIntegerField(blank=True, default=10, null=True, verbose_name='\u56fe\u7247\u6743\u91cd')),
                ('img_type', models.SmallIntegerField(choices=[(1, 'banner'), (2, 'ads')], default=1, verbose_name='\u7c7b\u578b')),
            ],
            options={
                'verbose_name_plural': '\u8f6e\u64ad\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': '\u6587\u7ae0\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('content', models.TextField()),
                ('target', models.CharField(blank=True, max_length=100, null=True)),
                ('anchor', models.CharField(blank=True, max_length=20, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('province', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='article.Comments')),
            ],
            options={
                'verbose_name_plural': '\u8bc4\u8bba\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u7f51\u7ad9\u540d\u79f0')),
                ('link', models.CharField(max_length=100, verbose_name='\u7f51\u7ad9\u5730\u5740')),
                ('avatar', models.CharField(blank=True, default=b'', max_length=100, verbose_name='\u7f51\u7ad9\u56fe\u6807')),
                ('desc', models.CharField(blank=True, default=b'', max_length=200, verbose_name='\u7f51\u7ad9\u63cf\u8ff0')),
                ('weights', models.SmallIntegerField(blank=True, default=10, null=True, verbose_name='\u6743\u91cd')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='\u8054\u7cfb\u90ae\u7bb1')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.CharField(max_length=50, verbose_name='\u97f3\u4e50\u540d\u79f0')),
                ('url', models.CharField(max_length=100, verbose_name='\u97f3\u4e50\u5730\u5740')),
                ('cover', models.CharField(max_length=100, verbose_name='\u97f3\u4e50\u5c01\u9762')),
                ('artist', models.CharField(blank=True, default=b'', max_length=100, null=True, verbose_name='\u827a\u672f\u5bb6')),
                ('lrc', models.CharField(blank=True, default=b'', max_length=100, null=True, verbose_name='\u97f3\u4e50\u6b4c\u8bcd')),
            ],
            options={
                'verbose_name_plural': '\u80cc\u666f\u97f3\u4e50',
            },
        ),
        migrations.CreateModel(
            name='OwnerMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u7b80\u4ecb')),
                ('message', models.TextField(default=b'', verbose_name='\u5bc4\u8bed')),
                ('editor', models.SmallIntegerField(choices=[(1, '\u5bcc\u6587\u672c\u7f16\u8f91\u5668'), (2, 'Markdown\u7f16\u8f91\u5668')], default=1, verbose_name='\u7f16\u8f91\u5668\u7c7b\u578b')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u4e3b\u4eba\u5bc4\u8bed',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('email', models.EmailField(max_length=254, verbose_name='\u8ba2\u9605\u90ae\u7bb1')),
            ],
            options={
                'verbose_name_plural': '\u90ae\u4ef6\u8ba2\u9605',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='\u6807\u7b7e\u540d')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u6587\u7ae0\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('nickname', models.CharField(max_length=50)),
                ('avatar', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('blogger', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '\u8bbf\u5ba2\u7ba1\u7406',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replyers', to='article.Visitor'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='article.Visitor'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Author', verbose_name='\u4f5c\u8005'),
        ),
        migrations.AddField(
            model_name='article',
            name='classification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Classification', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='article.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]
