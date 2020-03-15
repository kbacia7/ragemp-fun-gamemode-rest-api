from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apilogic.serializers import PlayersSpawnsSerializer, DerbyArenasSerializer, HideandseekArenasSerializer, RaceArenasSerializer, TdmArenasSerializer, PlayersSerializer, SettingsSerializer, DmArenasSerializer, HeavyDmArenasSerializer, SniperArenasSerializer, OneShootArenasSerializer
from apilogic.models import DerbyArenas, HideandseekArenas, RaceArenas, TdmArenas, DmArenas, HeavyDmArenas, SniperArenas, OneShootArenas, PlayersSpawns, Players, Settings
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
        if action == 'play_as_guest':
            if 'login' in data:
                player_with_this_login = Players.objects.filter(login=data['login']).first()
                print(player_with_this_login)
                if player_with_this_login is not None:
                    return Response(1)
                return Response(0)

        if action == 'login':
            if 'password' in data and 'login' in data:
                player = Players.objects.filter(password=data['password'], login=data['login']).first()
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
                Players(
                    login=data['login'],
                    password=data['password'],
                    email=data['email'],
                    deaths=0,
                    kills=0,
                    ped=0,
                    rank="Player"
                ).save()
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