from django.urls import path
from app import views
urlpatterns=[
    path('messages/',views.MessageListView.as_view(),name='message-list'),
    path('messages/create/',views.MessageCreateViews.as_view(),name='messages-create'),
]