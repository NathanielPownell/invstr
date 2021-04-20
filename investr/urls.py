from django.urls import path, include
from django.conf.urls.static import static
from . import views




urlpatterns = [
    path('', views.dash, name='investr' ),
    path('trade/', views.trade, name='trade' ),
    path('trade/<slug:slug>', views.tradedetail, name='tradedetail'),
    # path('history/', views.history, name='history' ),
    # path('watchlist/', views.watchlist.as_view(), name='watchlist' ),
    
    path('watchlist/', views.watchlist, name='watchlist' ),

    path('watchlistedit/', views.watchlist_edit.as_view(), name='watchlistedit' ),
    path('watchlistdelete/', views.resetwatchlist, name='watchlistdelete' ),

    path('buy/',views.buy.as_view(), name="buy"),


    path('news/', views.news, name='news' ),
    path('test/', views.test.as_view(), name='history'),
    # path('test-api', views.get_data),
    path('api/', views.history.as_view()),
    path('buy/', views.buy.as_view()),
]