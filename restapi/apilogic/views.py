from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apilogic.serializers import DerbyArenasSerializer, HideandseekArenasSerializer, RaceArenasSerializer, TdmArenasSerializer, DmArenasSerializer, HeavyDmArenasSerializer, SniperArenasSerializer, OneShootArenasSerializer
from apilogic.models import DerbyArenas, HideandseekArenas, RaceArenas, TdmArenas, DmArenas, HeavyDmArenas, SniperArenas, OneShootArenas
from rest_framework.response import Response
from rest_framework.decorators import action
from random import randint
from rest_framework import generics

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