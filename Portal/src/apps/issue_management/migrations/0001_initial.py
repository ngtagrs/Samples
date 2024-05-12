# Generated by Django 5.0.6 on 2024-05-11 07:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueCategory',
            fields=[
                ('category', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='分類')),
            ],
        ),
        migrations.CreateModel(
            name='IssueStatus',
            fields=[
                ('status', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='ステータス')),
            ],
        ),
        migrations.CreateModel(
            name='IssueComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='タイトル')),
                ('description', models.TextField(verbose_name='説明')),
                ('registered_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('pic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='in_charge_issue', to=settings.AUTH_USER_MODEL, verbose_name='担当者')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='registered_issue', to=settings.AUTH_USER_MODEL, verbose_name='登録者')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_issue', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
                ('category', models.ForeignKey(default='未選択', on_delete=django.db.models.deletion.SET_DEFAULT, to='issue_management.issuecategory', verbose_name='案件分類')),
                ('status', models.ForeignKey(default='未選択', on_delete=django.db.models.deletion.SET_DEFAULT, to='issue_management.issuestatus', verbose_name='ステータス')),
            ],
        ),
    ]
