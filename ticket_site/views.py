from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import ProjectSerializer
from .models import Project
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

@permission_classes((permissions.AllowAny,))
class Ticketing(APIView):
    serializer_class = ProjectSerializer

    def get(self,request):
        data = Project.objects.values('project_name').distinct()
        return render(request,'ticket_site/ticketing.html',{'data':data})

    def post(self,request):
        ticket_details = request.POST.get('ticket_details')
        ticket_data = Project.objects.filter(project_name=ticket_details)
        return render(request, 'ticket_site/list_ticketing.html', {'data': ticket_data })


class CreateTicket(SuccessMessageMixin,CreateView):
    model = Project
    fields = ('project_name', 'issue_type', 'description', 'label')
    success_url = '.'
    success_message = "Ticket Successfully created!"

@permission_classes((permissions.AllowAny,))
class TicketSearchList(APIView):
    serializer_class = ProjectSerializer

    def post(self,request):
        project_name = request.POST.get('search')
        queryset = Project.objects.all()
        if project_name is not None:
            queryset = queryset.filter(project_name=project_name).values('project_name').distinct()
        return render(request, 'ticket_site/ticketing.html', {'data': queryset})



# class TicketSearchList(generics.ListAPIView):
#     print('here')
#     queryset = Project.objects.all()
#     serializer_class = TicketSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('project_name', 'label')



