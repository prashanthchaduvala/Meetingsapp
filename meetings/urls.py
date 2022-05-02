from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.detail, name = 'detail'),
    path('rooms',views.rooms_list,name='rooms'),
    path('new',views.new,name='new'),
    path('create_room/',views.create_room,name='create_room'),
    path("record/",views.record, name="record"),
    path("get_record/",views.get_records, name="get_record"),
]
