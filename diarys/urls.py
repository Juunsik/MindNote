from django.urls import path
from . import views


urlpatterns = [
    path("diary/", views.page_list),
    # path("diary/info/", views.info),
    # path("diary/write/", views.page_create),
    # path("diary/page/<int:page_di>/", views.page_detail),
    # path("diary/page/<int:page_di>/edit/", views.page_update),
    # path("diary/page/<int:page_di>/delete/", views.page_delete),
]
