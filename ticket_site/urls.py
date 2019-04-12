from django.conf.urls import url
from .views import Ticketing,CreateTicket,TicketSearchList


urlpatterns = [
    # url(r'', Ticketing.as_view(), name='ticket'),
    url(r'^$', Ticketing.as_view(), name='ticket'),
    url(r'^create_ticket/$', CreateTicket.as_view(), name='create_ticket'),
    url(r'^search/$', TicketSearchList.as_view(), name='search'),

]