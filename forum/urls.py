from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('add_question/', add_question, name='add_question'),
    path('add_question_ajax/<str:id>/', add_question_ajax, name='add_question_ajax'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json_question, name='show_json_question'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]