from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apilogic.serializers import PlayersSpawnsSerializer,PlayersItemsSerializer, ShopTabDataLazySerializer, ShopTabDataSerializer, DerbyArenasSerializer, HideandseekArenasSerializer, RaceArenasSerializer, TdmArenasSerializer, PlayersSerializer, SettingsSerializer, DmArenasSerializer, HeavyDmArenasSerializer, SniperArenasSerializer, OneShootArenasSerializer
from apilogic.models import Items, PlayersItems, DerbyArenas, ShopEntities, ShopTabData, Ranks, HideandseekArenas, RaceArenas, TdmArenas, DmArenas, HeavyDmArenas, SniperArenas, OneShootArenas, PlayersSpawns, Players, Settings
from rest_framework.response import Response
from rest_framework.decorators import action
from random import randint
from rest_framework import generics, status
class EventsAPI(generics.ListAPIView):     
    def get_queryset(self):
        event_name = self.kwargs['event']
        known_events = {
            'derby': DerbyArenas,
            'hideandseek': HideandseekArenas,
            'race': RaceArenas,
            'tdm': TdmArenas
        }
        if event_name in known_events:
            count = known_events[event_name].objects.count()
            if count > 0:
                random_index = randint(0, count - 1) 
                return [known_events[event_name].objects.all()[random_index]]
        raise Http404()
            
    def get_serializer_class(self):
        event_name = self.kwargs['event']
        known_events = {
            'derby': DerbyArenasSerializer,
            'hideandseek': HideandseekArenasSerializer,
            'race': RaceArenasSerializer,
            'tdm': TdmArenasSerializer
        }
        if event_name in known_events:
            return known_events[event_name]
        raise Http404()

class ArenasAPI(generics.ListAPIView):     
    def get_queryset(self):
        event_name = self.kwargs['arena']
        known_aremas = {
            'dm': DmArenas,
            'heavydm': HeavyDmArenas,
            'sniper': SniperArenas,
            'oneshoot': OneShootArenas
        }
        if event_name in known_aremas:
            actual_arena = known_aremas[event_name].objects.filter(active=1).first()
            if actual_arena is None:
                arena =  known_aremas[event_name].objects.filter().first()
                if arena is None:
                    raise Http404()
                return [arena]
            else:
                return [actual_arena]
        raise Http404()
            
    def get_serializer_class(self):
        event_name = self.kwargs['arena']
        known_aremas = {
            'dm': DmArenasSerializer,
            'heavydm': HeavyDmArenasSerializer,
            'sniper': SniperArenasSerializer,
            'oneshoot': OneShootArenasSerializer
        }
        if event_name in known_aremas:
            return known_aremas[event_name]
        raise Http404()

class PlayersAPI(generics.GenericAPIView):    
    def get(self, request, action):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, action):
        data = request.data
        if action == 'give_item':
            print(data)
            if 'item_id' in data and 'player_id' in data and len(data['item_id']) > 0 and len(data['player_id']) > 0:
                new_player_item = PlayersItems(item=Items.objects.get(pk=int(data['item_id'])), player=Players.objects.get(pk=int(data['player_id'])), equipped=False)
                new_player_item.save()
                player_items = PlayersItems.objects.filter(player=int(data['player_id'])).all()
                return Response(PlayersItemsSerializer(player_items, many=True).data)

        if action == 'equip':
            if 'item_id' in data and 'player_id' in data and len(data['item_id']) > 0 and len(data['player_id']) > 0:
                player_item = PlayersItems.objects.filter(item=int(data['item_id']), player=int(data['player_id'])).first()
                if player_item is not None:
                    player_item.equipped = player_item.equipped is not True
                    player_item.save()
                    player_items = PlayersItems.objects.filter(player=int(data['player_id'])).all()
                    if player_item.item.sub_section is not None and player_item.equipped is True:
                        PlayersItems.objects.filter(player=int(data['player_id']), item__section__name=player_item.item.section.name).exclude(pk=player_item.id).update(equipped=False)
                    return Response(PlayersItemsSerializer(player_items, many=True).data)
                return Response(0)
        if action == 'play_as_guest':
            if 'login' in data:
                player_with_this_login = Players.objects.filter(login=data['login']).first()
                if player_with_this_login is not None:
                    return Response().all()
                return Response(0)

        if action == 'login':
            if 'login' in data:
                print(data)
                player = Players.objects.filter(login=data['login']).first()
                if player is not None:
                    return Response(PlayersSerializer(player).data)            

        if action == 'register':
            if 'password' in data and 'login' in data and 'email' in data:
                player_with_this_login = Players.objects.filter(login=data['login']).first()
                if player_with_this_login is not None:
                    return Response(1)
                player_with_this_email = Players.objects.filter(email=data['email']).first()
                if player_with_this_email is not None:
                    return Response(2)
                default_rank_setting = Settings.objects.filter(name='default_rank_id').first()
                rank = Ranks.objects.filter(pk=int(default_rank_setting.value)).first()
                player = Players(
                    login=data['login'],
                    password=data['password'],
                    email=data['email'],
                    deaths=0,
                    kills=0,
                    rank=rank,
                    money=1000,
                    diamonds=5
                )
                player.save()
                item_skin = Items.objects.filter(section__name="skin_spawn").first()
                new_player_item = PlayersItems(item=item_skin, player=player, equipped=True)
                new_player_item.save()
                return Response(0)

        if action == 'save':
            if 'id' in data or 'login' in data:
                player = None
                if 'id' in data:
                    player = Players.objects.filter(pk=data['id']).first()
                if 'login' in data and player is None:
                    player = Players.objects.filter(login=data['login']).first()
                if player is not None:
                    for field in data.keys():
                        if field == 'id':
                            continue
                    setattr(player, field, data[field])
                    player.save()
                    return Response()
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)



    def get_queryset(self):
        action_name = self.kwargs['action']
        if action_name == 'spawns':
            return PlayersSpawns.objects.all()
        raise Http404()
            
    def get_serializer_class(self):
        action_name = self.kwargs['action']
        if action_name == 'spawns':
            return PlayersSpawnsSerializer
        raise Http404()

class SettingsAPI(generics.ListAPIView):    
    def get_queryset(self):
        return Settings.objects.filter(name__contains='{}_'.format(self.kwargs['name'] )).all()
            
    def get_serializer_class(self):
        return SettingsSerializer


class ShopAPI(generics.ListAPIView):    
    def get_queryset(self):
        tab_name = self.kwargs['tab']
        if tab_name != 'all':
            return ShopTabData.objects.filter(name=tab_name).all()
        else:
            return ShopTabData.objects.exclude(parent__isnull=False).all()
        
    def get_serializer_class(self):
        if self.kwargs['tab'] != 'all':
            return ShopTabDataSerializer
        else:
            return ShopTabDataLazySerializer

class BuyAPI(generics.GenericAPIView):    
    def post(self, request):
        data = request.data
        print(data)
        is_guest = data['player_id'] == "0"
        print(is_guest)
        if data['buy_in'] is not None and len(data['buy_in']) > 0:
            if int(data['item_id']) is not None and int(data['item_id']) > 0 and data['currency'] is not None and len(data['currency']) > 0:
                if data['buy_in'] == 'shop':
                    response = {}
                    player = Players.objects.filter(pk=int(data['player_id'])).first()
                    shop_entity = ShopEntities.objects.filter(pk=int(data['item_id'])).first()
                    response_code = 1
                    cost = 0
                    if (player is not None or is_guest is True) and shop_entity is not None:
                        if is_guest is True:
                            if data['currency'] == 'MONEY':
                                cost = shop_entity.money
                            else:
                                cost = shop_entity.diamonds
                            response_code = 2
                        else:
                            if data['currency'] == 'MONEY':
                                if player.money >= shop_entity.money:
                                    player.money -= shop_entity.money
                                    cost = shop_entity.money
                                    response_code = 0
                            elif data['currency'] == 'DIAMONDS':
                                if player.diamonds >= shop_entity.diamonds:
                                    player.diamonds -= shop_entity.diamonds
                                    cost = shop_entity.diamonds
                                    response_code = 0
                        item = shop_entity.item
                        item_id = None
                        if item is not None:
                            item_id = item.id
                        if item_id is not None:
                            player_item = PlayersItems.objects.filter(item=int(item_id), player=int(data['player_id'])).first()
                            if player_item is not None:
                                response_code = 3
                        if response_code == 0:
                            player.save()
                        return Response({
                            'code': response_code,
                            'tab_name': shop_entity.filter.tab.name,
                            'cost': cost,
                            'ragemp_item_id': shop_entity.ragemp_item_id,
                            'item_id': item_id
                        })
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

