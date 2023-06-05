from django.urls import path
from groups.views import ManageGroupView, RemoveUserFromGroupView

urlpatterns = [
    path("groups/<str:group>/users/", ManageGroupView.as_view()),
    path("groups/<str:group>/users/<int:userid>", RemoveUserFromGroupView.as_view()),
]
