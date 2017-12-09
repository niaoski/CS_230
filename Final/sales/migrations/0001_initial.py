# Generated by Django 2.0 on 2017-12-09 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('company', models.CharField(max_length=100, unique=True)),
                ('contact_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_number', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date_ordered', models.DateField()),
                ('ship_date', models.DateField()),
                ('emp_init', models.CharField(max_length=3)),
                ('po_number', models.CharField(blank=True, max_length=50, null=True)),
                ('branch', models.IntegerField(default=1)),
                ('ship_method', models.CharField(blank=True, max_length=50, null=True)),
                ('courier', models.CharField(blank=True, max_length=50, null=True)),
                ('order_type', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('QUEUED', 'Queued'), ('SHIPPED', 'Shipped')], default='QUEUED', max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='QueuedBottle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fill', models.CharField(choices=[('AC', 'Acetylene'), ('AR', 'Argon'), ('BG', 'Beer Gas'), ('CD', 'Carbon Dioxide'), ('GS', 'Guinness Gas'), ('HE', 'Helium'), ('C2', 'Mix C2'), ('C10', 'Mix C10'), ('C25', 'Mix C25'), ('NI', 'Nitrogen'), ('OX', 'Oxygen'), ('ST', 'Stargon'), ('SY', 'Syphon')], max_length=13)),
                ('size', models.CharField(choices=[('T', 'T'), ('K', 'K'), ('S', 'S'), ('D', 'D'), ('Q', 'Q'), ('R', 'R'), ('50', '50'), ('40', '40'), ('20', '20'), ('15', '15'), ('10', '10'), ('5', '5'), ('2.5', '2.5')], max_length=3)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Order')),
            ],
        ),
        migrations.CreateModel(
            name='QueuedTub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fill', models.CharField(choices=[('ICE_3', '3 Mill'), ('ICE_16', '16 Mill'), ('ICE_BLOCK', 'Ice Block'), ('BAGGED_ICE_3', '3 Mill Bagged'), ('BAGGED_ICE_16', '16 Mill Bagged')], max_length=13)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Order')),
            ],
        ),
    ]
