# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class ItemsSections(models.Model): 
    name = models.CharField(max_length=64)
    column_size = models.DecimalField(max_digits=2, decimal_places=1, default=1)
    class Meta:
        db_table = 'items_sections'

class Items(models.Model):
    section = models.ForeignKey(ItemsSections, models.DO_NOTHING, null=True, related_name="items")
    title_display_name =  models.CharField(max_length=64)
    sub_section = models.CharField(max_length=32)
    filename = models.CharField(max_length=50)
    description = models.TextField()
    days_to_expire = models.IntegerField(null=True)
    ragemp_item_id = models.IntegerField(null=True)
    class Meta:
        db_table = 'items'

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
    items = models.ManyToManyField(Items, related_name="items", through='PlayersItems')
    login = models.CharField(max_length=35)
    rank = models.ForeignKey(Ranks, models.DO_NOTHING, null=True)
    deaths = models.IntegerField(blank=True, default=0)
    kills = models.IntegerField(blank=True, default=0)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    ped = models.IntegerField()
    money = models.IntegerField()
    diamonds = models.IntegerField()

    class Meta:
        db_table = 'players'

class PlayersItems(models.Model):
    player = models.ForeignKey(Players, on_delete=models.CASCADE, related_name="player_items")
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    equipped = models.BooleanField(null=False, default=True)
    date_expire = models.DateTimeField(null=True)
    class Meta:
        db_table = 'players_items'

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

class ShopTabData(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, null=True, related_name="subcategories")
    display_name = models.CharField(max_length=64)
    title_display_name = models.CharField(max_length=64, null=True)
    description_display_name = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=32)
    money = models.IntegerField()
    diamonds = models.IntegerField()
    column_size = models.DecimalField(max_digits=2, decimal_places=1, default=1)

    class Meta:
        db_table = 'shop_tabs' 
    
class ShopTabFilterData(models.Model):
    tab = models.ForeignKey(ShopTabData, models.DO_NOTHING, related_name="filters") 
    display_name = models.CharField(max_length=64)
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'shop_tabs_filters'

        
class ShopEntities(models.Model):
    filter = models.ForeignKey(ShopTabFilterData, models.DO_NOTHING, null=False, related_name="entities")
    item = models.ForeignKey(Items, models.CASCADE, null=True)
    filename = models.CharField(max_length=50, null=True)
    ragemp_item_id = models.PositiveIntegerField(null=True)
    money = models.IntegerField(null=True)
    diamonds = models.IntegerField(null=True)
    display_name = models.CharField(max_length=64, null=True)

    class Meta:
        db_table = 'shop_entities'