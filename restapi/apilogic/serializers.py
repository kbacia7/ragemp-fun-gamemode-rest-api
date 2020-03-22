from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apilogic.models import DerbyArenas, DerbyArenasSpawns, DmArenas, DmArenasSpawns, DmArenasWeapons, HeavyDmArenas, HeavyDmArenasSpawns, HeavyDmArenasWeapons, HideandseekArenas, HideandseekArenasSpawns
from apilogic.models import Ranks, OneShootArenas, OneShootArenasSpawns, OneShootArenasWeapons, Players, PlayersSpawns, RaceArenas, RaceArenasCheckpoints, RaceArenasSpawns, Settings, SniperArenas, TdmArenas, TdmArenasSpawns, TdmArenasWeapons
from apilogic.models import ShopEntity, ShopTabFilterData, ShopTabData


class DerbyArenasSpawnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DerbyArenasSpawns
        fields = ['x', 'y', 'z', 'rotation']

class DerbyArenasSerializer(serializers.ModelSerializer):
    spawns = DerbyArenasSpawnsSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = DerbyArenas
        fields = '__all__'

class DmArenasWeaponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DmArenasWeapons
        fields = ['weapon_id', 'ammo']

class DmArenasSpawnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DmArenasSpawns
        fields = ['x', 'y', 'z']

class DmArenasSerializer(serializers.ModelSerializer):
    spawns = DmArenasSpawnsSerializer(
        many=True,
        read_only=True,
    )
    weapons = DmArenasWeaponsSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = DmArenas
        fields = '__all__'
    
class HeavyDmArenasWeaponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeavyDmArenasWeapons
        fields = ['weapon_id', 'ammo']

class HeavyDmArenasSpawnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeavyDmArenasSpawns
        fields = ['x', 'y', 'z']

class HeavyDmArenasSerializer(serializers.ModelSerializer):
    spawns = HeavyDmArenasSpawnsSerializer(
        many=True,
        read_only=True,
    )
    weapons = HeavyDmArenasWeaponsSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = HeavyDmArenas
        fields = '__all__'

class HideandseekArenasSpawnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HideandseekArenasSpawns
        fields = ['x', 'y', 'z']

class HideandseekArenasSerializer(serializers.ModelSerializer):
    spawns = HideandseekArenasSpawnsSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = HideandseekArenas
        fields = '__all__'

class OneShootArenasWeaponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneShootArenasWeapons
        fields = ['weapon_id', 'ammo']

class OneShootArenasSpawnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneShootArenasSpawns
        fields = ['x', 'y', 'z']

class OneShootArenasSerializer(serializers.ModelSerializer):
    spawns = OneShootArenasSpawnsSerializer(
        many=True,
        read_only=True,
    )
    weapons = OneShootArenasWeaponsSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = OneShootArenas
        fields = '__all__'
        
class RanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranks
        fields = '__all__'

class PlayersSerializer(serializers.ModelSerializer):
    rank = RanksSerializer(
        many=False,
        read_only=True,
    )
    class Meta:
        model = Players
        fields = '__all__'

class PlayersSpawnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersSpawns
        fields = '__all__'

class RaceArenasSpawnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceArenasSpawns
        fields = ['x', 'y', 'z', 'rotation', 'vehicle_model']

class RaceArenasCheckpointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceArenasCheckpoints
        fields = ['x', 'y', 'z']

class RaceArenasSerializer(serializers.ModelSerializer):
    spawns = RaceArenasSpawnsSerializer(
        many=True,
        read_only=True,
    )
    checkpoints = RaceArenasCheckpointsSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = RaceArenas
        fields = '__all__'

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'

class SniperArenasWeaponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneShootArenasWeapons
        fields = ['weapon_id', 'ammo']

class SniperArenasSpawnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneShootArenasSpawns
        fields = ['x', 'y', 'z']

class SniperArenasSerializer(serializers.ModelSerializer):
    spawns = SniperArenasSpawnsSerializer(
        many=True,
        read_only=True,
    )
    weapons = SniperArenasWeaponsSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = SniperArenas
        fields = '__all__'

class TdmArenasWeaponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TdmArenasWeapons
        fields = ['weapon_id', 'ammo']

class TdmArenasSpawnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TdmArenasSpawns
        fields = ['x', 'y', 'z', 'team']

class TdmArenasSerializer(serializers.ModelSerializer):
    spawns = TdmArenasSpawnsSerializer(
        many=True,
        read_only=True,
    )
    weapons = TdmArenasWeaponsSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = TdmArenas
        fields = '__all__'

class TdmArenasSerializer(serializers.ModelSerializer):
    spawns = TdmArenasSpawnsSerializer(
        many=True,
        read_only=True,
    )
    weapons = TdmArenasWeaponsSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = TdmArenas
        fields = '__all__'

class ShopEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopEntity
        fields = '__all__'

class ShopTabFilterDataSerializer(serializers.ModelSerializer):
    entities = ShopEntitySerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = ShopTabFilterData
        fields = '__all__'


class ShopTabDataSerializer(serializers.ModelSerializer):
    filters = ShopTabFilterDataSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = ShopTabData
        fields = '__all__'
    
    def get_fields(self):
        fields = super(ShopTabDataSerializer, self).get_fields()
        fields['subcategories'] = ShopTabDataSerializer(many=True)
        return fields

class ShopTabDataLazySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopTabData
        fields = '__all__'