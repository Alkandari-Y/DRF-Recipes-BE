from rest_framework.permissions import AllowAny, IsAdminUser


class AdminOrReadOnlyMixin:
    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAdminUser()]
