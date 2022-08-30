"""Defines URL pattern for my_app"""

from django.urls import path

from . import views

app_name = "learning_log"
urlpatterns = [
    # Home page
    path('',views.index,name = 'index'),
    # Page that shows all the topics
    path('topics/',views.topics,name='topics'),
    # Detail page for sigle topic
    path('topics/<int:topic_id>/',views.individual_topic,name='individual_topic'),
    # Page for adding a new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    # Add a new entry
    path('new_entry/<int:topic_id>',views.new_entry,name='new_entry'),
    # Page for editing entries
    path('edit_entry/<int:entry_id>/',views.edit_entry, name='edit_entry'),
    # delete a topic
    path('delete_topic/<int:topic_id>',views.delete_topic,name='delete_topic'),
    # delete an entry
    path('delete_entry/<int:entry_id>',views.delete_entry,name='delete_entry'),
]

