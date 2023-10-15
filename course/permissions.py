from rest_framework.permissions import BasePermission, IsAuthenticated



class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        return request.user == view.get_object().author


class IsModer(BasePermission):
    def has_permission(self, request, view):
        return request.user.group == 'moder'

class CoursePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'DELETE']:
            return IsModer().has_permission(request, view)
        return IsAuthenticated().has_permission(request, view)