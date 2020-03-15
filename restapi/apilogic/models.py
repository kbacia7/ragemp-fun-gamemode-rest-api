# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DerbyArenas(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    vehicle_model = models.IntegerField(db_column='vehicle_model', default=0)  # Field name made lowercase.
    height_limit = models.DecimalField(db_column='height_limit', max_digits=35, decimal_places=25, default=0)  # Field name made lowercase.
    class Meta:
        db_table = 'derby_arenas'


class DerbyArenasSpawns(models.Model):
    arena = models.ForeignKey('DerbyArenas', models.DO_NOTHING, null=True, related_name="spawns")  # Field name made lowercase.
    x = models.DecimalField(max_digits=35, decimal_places=25)
    y = models.DecimalField(max_digits=35, decimal_places=25)
    z = models.DecimalField(max_digits=35, decimal_places=25)
    rotation = models.DecimalField(max_digits=35, decimal_places=25)

    class Meta:
        db_table = 'derby_arenas_spawns'


class DmArenas(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    active = models.IntegerField()

    class Meta:
        db_table = 'dm_arenas'


class DmArenasSpawns(models.Model):
    arena = models.ForeignKey(DmArenas, models.DO_NOTHING, null=True, related_name="spawns")  # Field name made lowercase.
    x = models.DecimalField(max_digits=35, decimal_places=25)
    y = models.DecimalField(max_digits=35, decimal_places=25)
    z = models.DecimalField(max_digits=35, decimal_places=25)

    class Meta:
        db_table = 'dm_arenas_spawns'


class DmArenasWeapons(models.Model):
    arena = models.ForeignKey(DmArenas, models.DO_NOTHING, null=True, related_name="weapons")  # Field name made lowercase.
    weapon_id = models.PositiveIntegerField()  # Field name made lowercase.
    ammo = models.PositiveIntegerField()

    class Meta:
        db_table = 'dm_arenas_weapons'


class HeavyDmArenas(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    active = models.IntegerField()

    class Meta:
        db_table = 'heavy_dm_arenas'


class HeavyDmArenasSpawns(models.Model):
    arena = models.ForeignKey(HeavyDmArenas, models.DO_NOTHING, null=True, related_name="spawns")  # Field name made lowercase.
    x = models.DecimalField(max_digits=35, decimal_places=25)
    y = models.DecimalField(max_digits=35, decimal_places=25)
    z = models.DecimalField(max_digits=35, decimal_places=25)

    class Meta:
        db_table = 'heavy_dm_arenas_spawns'


class HeavyDmArenasWeapons(models.Model):
    arena = models.ForeignKey(HeavyDmArenas, models.DO_NOTHING, null=True, related_name="weapons")  # Field name made lowercase.
    weapon_id = models.PositiveIntegerField()  # Field name made lowercase.
    ammo = models.PositiveIntegerField()

    class Meta:
        db_table = 'heavy_dm_arenas_weapons'


class HideandseekArenas(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    looking_x = models.DecimalField(db_column='looking_x', max_digits=35, decimal_places=25)  # Field name made lowercase.
    looking_y = models.DecimalField(db_column='looking_y', max_digits=35, decimal_places=25)  # Field name made lowercase.
    looking_z = models.DecimalField(db_column='looking_z', max_digits=35, decimal_places=25)  # Field name made lowercase.

    class Meta:
        db_table = 'hideandseek_arenas'


class HideandseekArenasSpawns(models.Model):
    arena = models.ForeignKey(HideandseekArenas, models.DO_NOTHING, null=True, related_name="spawns")  # Field name made lowercase.
    x = models.DecimalField(max_digits=35, decimal_places=25)
    y = models.DecimalField(max_digits=35, decimal_places=25)
    z = models.DecimalField(max_digits=35, decimal_places=25)

    class Meta:
        db_table = 'hideandseek_arenas_spawns'


class OneShootArenas(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    active = models.IntegerField()

    class Meta:
        db_table = 'one_shoot_arenas'


class OneShootArenasSpawns(models.Model):
    arena = models.ForeignKey(OneShootArenas, models.DO_NOTHING, null=True, related_name="spawns")  # Field name made lowercase.
    x = models.DecimalField(max_digits=35, decimal_places=25)
    y = models.DecimalField(max_digits=35, decimal_places=25)
    z = models.DecimalField(max_digits=35, decimal_places=25)

    class Meta:
        db_table = 'one_shoot_arenas_spawns'


class OneShootArenasWeapons(models.Model):
    arena = models.ForeignKey(OneShootArenas, models.DO_NOTHING, null=True, related_name="weapons")  # Field name made lowercase.
    weapon_id = models.PositiveIntegerField()  # Field name made lowercase.
    ammo = models.PositiveIntegerField()

    class Meta:
        db_table = 'one_shoot_arenas_weapons'


class Ranks(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = 'ranks'

class Players(models.Model):
    login = models.CharField(max_length=35)
    rank = models.ForeignKey(Ranks, models.DO_NOTHING, null=True)
    deaths = models.IntegerField(blank=True, default=0)
    kills = models.IntegerField(blank=True, default=0)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    ped = models.IntegerField()

    class Meta:
        db_table = 'players'

class PlayersSpawns(models.Model):
    x = models.DecimalField(max_digits=35, decimal_places=25)
    y = models.DecimalField(max_digits=35, decimal_places=25)
    z = models.DecimalField(max_digits=35, decimal_places=25)

    class Meta:
        db_table = 'players_spawns'


class RaceArenas(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    class Meta:
        db_table = 'races_arenas'


class RaceArenasCheckpoints(models.Model):
    arena = models.ForeignKey(RaceArenas, models.DO_NOTHING, null=True, related_name="checkpoints")  # Field name made lowercase.
    x = models.DecimalField(max_digits=35, decimal_places=25)
    y = models.DecimalField(max_digits=35, decimal_places=25)
    z = models.DecimalField(max_digits=35, decimal_places=25)

    class Meta:
        db_table = 'races_arenas_checkpoints'


class RaceArenasSpawns(models.Model):
    arena = models.ForeignKey(RaceArenas, models.DO_NOTHING, null=True, related_name="spawns")  # Field name made lowercase.
    x = models.DecimalField(max_digits=35, decimal_places=25)
    y = models.DecimalField(max_digits=35, decimal_places=25)
    z = models.DecimalField(max_digits=35, decimal_places=25)
    vehicle_model = models.IntegerField()  # Field name made lowercase.
    rotation = models.DecimalField(max_digits=35, decimal_places=25)

    class Meta:
        db_table = 'races_arenas_spawns'


class Settings(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'settings'


class SniperArenas(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    active = models.IntegerField()

    class Meta:
        db_table = 'sniper_arenas'


class SniperArenasSpawns(models.Model):
    arena = models.ForeignKey(SniperArenas, models.DO_NOTHING, null=True, related_name="spawns")  # Field name made lowercase.
    x = models.DecimalField(max_digits=35, decimal_places=25)
    y = models.DecimalField(max_digits=35, decimal_places=25)
    z = models.DecimalField(max_digits=35, decimal_places=25)

    class Meta:
        db_table = 'sniper_arenas_spawns'


class SniperArenasWeapons(models.Model):
    arena = models.ForeignKey(SniperArenas, models.DO_NOTHING, null=True, related_name="weapons")  # Field name made lowercase.
    weapon_id = models.PositiveIntegerField()  # Field name made lowercase.
    ammo = models.PositiveIntegerField()

    class Meta:
        db_table = 'sniper_arenas_weapons'


class TdmArenas(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    class Meta:
        db_table = 'tdm_arenas'


class TdmArenasSpawns(models.Model):
    arena = models.ForeignKey(TdmArenas, models.DO_NOTHING, null=True, related_name="spawns")  # Field name made lowercase.
    x = models.DecimalField(max_digits=35, decimal_places=25)
    y = models.DecimalField(max_digits=35, decimal_places=25)
    z = models.DecimalField(max_digits=35, decimal_places=25)
    team = models.PositiveIntegerField()

    class Meta:
        db_table = 'tdm_arenas_spawns'


class TdmArenasWeapons(models.Model):
    arena = models.ForeignKey(TdmArenas, models.DO_NOTHING, null=True, related_name="weapons")  # Field name made lowercase.
    weapon_id = models.PositiveIntegerField()  # Field name made lowercase.
    ammo = models.PositiveIntegerField()

    class Meta:
        db_table = 'tdm_arenas_weapons'
