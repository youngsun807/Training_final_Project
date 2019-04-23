from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('intro/', views.intro, name='intro'),
    path('index/', views.index, name='index'),
    path('personal/', views.personal, name='personal'),
    path('age/', views.age, name='age'),
    path('habit/', views.habit, name='habit'),

    
    # path('other/', views.OtherList.as_view(), name='other_list'),
    # path('chart/', views.chart, name='chart'),
    # path('chart/roadChart/', views.roadChart, name='roadChart'),
    # path('chart/reviewTop10Chart/', views.reviewTop10Chart, name='reviewTop10Chart'),

    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('ajaxreq/', views.ajaxRes, name='ajaxRes'),
    # path('ajaxReqRes/', views.myReqRes, name='ajaxReqRes')
]