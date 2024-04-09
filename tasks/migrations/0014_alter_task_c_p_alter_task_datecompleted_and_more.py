# Generated by Django 5.0.3 on 2024-03-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_task_edad_alter_task_estado_alter_task_municipio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='c_p',
            field=models.CharField(max_length=250, verbose_name='C.P'),
        ),
        migrations.AlterField(
            model_name='task',
            name='datecompleted',
            field=models.DateTimeField(help_text='Ejemplo: /dd/mm/yyyy/', null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default='Ingrese sus Comentarios (Opcional)', verbose_name='Comentarios'),
        ),
        migrations.AlterField(
            model_name='task',
            name='edad',
            field=models.IntegerField(choices=[('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75')], default=[('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75')], help_text='Selecciona tu Edad'),
        ),
        migrations.AlterField(
            model_name='task',
            name='nombre_enlace',
            field=models.IntegerField(choices=[('vasti_arana', 'Vasti Arana'), ('israel_y_profe', 'Israel y Profe'), ('omar_castellanos', 'Omar Castellanos'), ('esther_castellanos', 'Esther Castellanos'), ('cesar', 'Cesar'), ('bere', 'Bere'), ('caleb_lupian', 'Caleb Lupian'), ('alonso', 'Alonso'), ('abner_lopez', 'Abner Lopez'), ('edgar', 'Edgar'), ('isai', 'Isai'), ('peter', 'Don Peter'), ('adin', 'Adin')], help_text='Selecciona tu Coordinador'),
        ),
        migrations.AlterField(
            model_name='task',
            name='num_casilla',
            field=models.CharField(help_text='Ingresa Num de Casilla', max_length=250, verbose_name='Nº de Casilla'),
        ),
        migrations.AlterField(
            model_name='task',
            name='num_seccion',
            field=models.IntegerField(choices=[('1218', '1218'), ('1219', '1219'), ('1220', '1220'), ('1221', '1221'), ('1213', '1213'), ('1214', '1214'), ('1215', '1215'), ('1208', '1208'), ('1207', '1207'), ('1206', '1206'), ('1204', '1204'), ('1205', '1205'), ('1192', '1192'), ('1216', '1216'), ('1217', '1217'), ('1252', '1252'), ('1250', '1250'), ('1251', '1251'), ('1249', '1249'), ('1255', '1255'), ('0709', '0709'), ('0710', '0710'), ('0711', '0711'), ('0712', '0712'), ('0713', '0713'), ('0714', '0714'), ('0715', '0715'), ('0716', '0716'), ('0717', '0717'), ('0718', '0718'), ('0719', '0719'), ('0720', '0720'), ('0653', '0653'), ('0641', '0641'), ('0642', '0642'), ('0643', '0643'), ('0644', '0644'), ('0645', '0645'), ('0646', '0646'), ('0647', '0647'), ('0648', '0648'), ('0649', '0649'), ('0650', '0650'), ('0651', '0651'), ('0652', '0652'), ('0653', '0653'), ('0654', '0654'), ('0655', '0655'), ('0656', '0656'), ('1334', '1334'), ('1335', '1335'), ('1331', '1331'), ('1332', '1332')], help_text='Selecciona una Seccion', verbose_name='Nº de Seccion'),
        ),
        migrations.AlterField(
            model_name='task',
            name='participacion',
            field=models.CharField(choices=[('RC', 'Representante de Casilla'), ('RG', 'Representante General'), ('MV', 'Movilizador'), ('SP', 'Simpatizante')], help_text='Selecciona una Opcion', max_length=100),
        ),
    ]
