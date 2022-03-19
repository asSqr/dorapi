# Generated by Django 4.0.1 on 2022-03-16 04:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dorapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GadgetLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('begin_index', models.IntegerField()),
                ('end_index', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='mgadget',
            name='linked_gadgets',
            field=models.ManyToManyField(related_name='linked_mgadgets', related_query_name='linked_mgadget', through='dorapi.GadgetLink', to='dorapi.MGadget'),
        ),
        migrations.AddField(
            model_name='gadgetlink',
            name='from_mgadget',
            field=models.ForeignKey(db_column='from_mgadget_id', on_delete=django.db.models.deletion.CASCADE, related_name='to_gadgetlinks', related_query_name='to_gadgetlink', to='dorapi.mgadget'),
        ),
        migrations.AddField(
            model_name='gadgetlink',
            name='to_mgadget',
            field=models.ForeignKey(db_column='to_mgadget_id', on_delete=django.db.models.deletion.CASCADE, related_name='from_gadgetlinks', related_query_name='from_gadgetlink', to='dorapi.mgadget'),
        ),
    ]