# Generated by Django 4.1.3 on 2022-11-23 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_coupon_id', models.CharField(max_length=250, verbose_name='stripe coupon id')),
                ('percent_off', models.IntegerField(verbose_name='discount in percents')),
                ('amount_off', models.IntegerField(verbose_name='discount in amount')),
            ],
            options={
                'verbose_name': 'discount',
                'verbose_name_plural': 'discounts',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('discount', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app_payment.discount', verbose_name='discount')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_tax_id', models.CharField(max_length=250, verbose_name='stripe tax id')),
                ('tax_name', models.CharField(max_length=50, verbose_name='tax name')),
                ('percentage', models.FloatField(verbose_name='tax percentage')),
                ('inclusive', models.BooleanField(verbose_name='is inclusive')),
            ],
            options={
                'verbose_name': 'tax',
                'verbose_name_plural': 'taxes',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(verbose_name='price'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='app_payment.item', verbose_name='item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app_payment.order', verbose_name='order')),
            ],
            options={
                'verbose_name': 'position',
                'verbose_name_plural': 'positions',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxes', to='app_payment.tax', verbose_name='tax'),
        ),
    ]