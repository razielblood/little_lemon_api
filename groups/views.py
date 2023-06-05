from django.contrib.auth.models import Group, User
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from groups.permissions import GroupPermissions
from rest_framework.views import APIView

from groups.serializers import AssignedUserSerializer


class ManageGroupView(APIView):
    permission_classes = [GroupPermissions]

    def post(self, request: HttpRequest, group: str):
        username = request.data["username"]
        if not username:
            return Response({"message": "error, username is required"}, status=status.HTTP_400_BAD_REQUEST)

        group = group.replace("-", " ").title()

        user = get_object_or_404(User, username=username)
        desired_group = get_object_or_404(Group, name=group)

        desired_group.user_set.add(user)

        return Response({"message": "ok"})

    def get(self, request: HttpRequest, group):
        group = group.replace("-", " ").title()
        assigned_users = User.objects.filter(groups__name=group)
        serialized_data = AssignedUserSerializer(assigned_users, many=True)
        return Response(serialized_data.data)


class RemoveUserFromGroupView(APIView):
    permission_classes = [GroupPermissions]

    def delete(self, request: HttpRequest, group, user_id):
        group = group.replace("-", " ").title()
        user = get_object_or_404(User, id=user_id)
        desired_group = get_object_or_404(Group, name=group)

        desired_group.user_set.remove(user)

        return Response({"message": "ok"})
