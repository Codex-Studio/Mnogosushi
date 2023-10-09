from django.urls import path 

from apps.tables.views import menu, add_to_order, clear_order, remove_from_order, order


urlpatterns = [
    path('<int:table_uuid>/', menu, name='menu'),
    path('order/', order, name="order"),
    path('add_to_order/', add_to_order, name='add_to_order'),
    path('clear_order/', clear_order, name='clear_order'),
    path('remove_from_order/<int:id>/', remove_from_order, name='remove_from_order'),
]