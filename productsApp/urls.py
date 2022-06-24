from django.urls import path
from .views import home, shop, signup, related

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('signup/', signup, name='signup'),
    path('related/', related, name='related')
]


handler404 = 'productsApp.views.custom_page_not_found_view'