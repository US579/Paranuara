from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'employees',
                views.EmployeesViewSet,
                basename='employees')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/samefriends/<int:pk1>/<int:pk2>/',
         views.SameFriendsView.as_view(), name='samefriends'),
    path('api/fruit_and_vegetable/<int:pk1>/',
         views.FriutVegetableView.as_view(), name='fruit_and_vegatable'),
]
