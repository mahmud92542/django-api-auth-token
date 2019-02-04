from django.urls import path
from django.conf.urls import url
from .views import *
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [

path('friends',FriendViewset.as_view(), name='friend'),
path('belonging',BelongingViewset.as_view(),name='belonging'),
path('borrowed',BorrowedViewset.as_view(),name='borrowed'),
path('belong',BelongViewset.as_view(),name='belong'),
path('friend',FriendsViewset.as_view(),name='friends'),
path('borrow',BorrowViewset.as_view(),name='borrow'),
#url('borrow/update/(?P<pk>\d)',BorrowUpdate.as_view(),name='borrow-update')
path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]