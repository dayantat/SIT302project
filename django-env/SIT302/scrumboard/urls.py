# from django.urls import path, re_path
# # from django.conf.urls import url
# from .api import ListApi, CardApi
# from django.views.generic import TemplateView
# #  This is only going to work if the code is added to the SIT302 urls file
# #  The entry for this page is directly commented in the SIT302/urls.py file
#
# urlpatterns = [
#     # as_view() converts the lists to functions
#     re_path(r'^lists$', ListApi.as_view()),  # If you get a request for lists this view is displayed
#     re_path(r'^cards$', CardApi.as_view()),  # re_path has replaced url
#     re_path(r'^home', TemplateView.as_view(template_name="scrumboard/home.html")),
# ]

from .api import ListViewSet, CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  # Anything handled by the router class attaches a / on the end
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = router.urls