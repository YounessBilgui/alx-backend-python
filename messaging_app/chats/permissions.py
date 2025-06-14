from rest_framework import permissions
from rest_framework.permissions import BasePermission

from chats.models import Conversation


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return obj.sender.id == request.user.id
        return True


class IsParticipant(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()


class IsAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


