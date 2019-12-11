import pymssql
import json

# from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Server, Domain, Property, Application


def ServerLogs(request, server_id, log_type, group_type=None, group_id=None):

    server_selected = Server.manager.filter(pk=server_id)

    server_list = GetServerList(group_type=group_type, group_id=group_id)

    server = str(server_selected[0])

    database = 'STOF_DBA'

    if log_type == 'server':
        query = '''
        DECLARE 
            @ErrorLog TABLE(LogID int identity(1, 1) not null primary key, 
            LogDate datetime null, 
            ProcessInfo NVARCHAR(100) null, 
            LogText NVARCHAR(4000) null); 
        INSERT INTO @ErrorLog(LogDate, ProcessInfo, LogText)  EXEC master..xp_readerrorlog 1, 1; 
        INSERT INTO @ErrorLog(LogDate, ProcessInfo, LogText)  EXEC master..xp_readerrorlog 2, 1; 
        INSERT INTO @ErrorLog(LogDate, ProcessInfo, LogText)  EXEC master..xp_readerrorlog 3, 1; 
        INSERT INTO @ErrorLog(LogDate, ProcessInfo, LogText)  EXEC master..xp_readerrorlog 4, 1; 
        SELECT 
            CONVERT(varchar, LogDate, 126)  as date, 
            ProcessInfo as process, 
            LogText as log 
        FROM @ErrorLog 
        WHERE ProcessInfo != \'Backup\' 
        AND  DATEDIFF(HOUR,LogDate, GETDATE()) < 48
        ORDER BY LogDate DESC;'''
    elif log_type == 'agent':
        query = '''
        DECLARE 
            @ErrorLog TABLE(LogID int identity(1, 1) not null primary key, 
            LogDate datetime null, 
            ErrorLevel NVARCHAR(100) null, 
            Text NVARCHAR(4000) null); 
        INSERT INTO @ErrorLog(LogDate, ErrorLevel, Text)  EXEC master..xp_readerrorlog 1, 2; 
        INSERT INTO @ErrorLog(LogDate, ErrorLevel, Text)  EXEC master..xp_readerrorlog 2, 2; 
        INSERT INTO @ErrorLog(LogDate, ErrorLevel, Text)  EXEC master..xp_readerrorlog 3, 2; 
        INSERT INTO @ErrorLog(LogDate, ErrorLevel, Text)  EXEC master..xp_readerrorlog 4, 2; 
        SELECT 
            CONVERT(varchar, LogDate, 126)  as date, 
            ErrorLevel as process, 
            Text as log 
        FROM @ErrorLog 
        WHERE DATEDIFF(HOUR,LogDate, GETDATE()) < 96
        ORDER BY LogDate DESC;'''
    else:
        query = ''

    try:
        conn = pymssql.connect(server=server, database=database, as_dict=True)
        cursor = conn.cursor()
        cursor.execute(query)

        logs = json.dumps(cursor.fetchall())

        return render(request, 'server/server_logs.html', context={
            'group_type': group_type,
            'group_id': group_id,
            'server_selected': server_selected,
            'server_list': server_list,
            'logs': logs},)
    except Exception as err:
        messages.error(request, str(err), extra_tags='error')
        return render(request, 'server/server_logs.html', context={
            'group_type': group_type,
            'group_id': group_id,
            'server_selected': server_selected,
            'server_list': server_list},)


def ServerDetail(request, server_id, group_type=None, group_id=None):

    server_selected = Server.manager.filter(pk=server_id)

    server_list = GetServerList(group_type=group_type, group_id=group_id)

    return render(request, 'server/server_detail.html', context={
        'group_type': group_type,
        'group_id': group_id,
        'server_selected': server_selected,
        'server_list': server_list},)


class ServerViewAll(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        return Server.manager.all()


class ServerViewByDomain(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        self.domain = get_object_or_404(Domain, id=self.kwargs['pk'])
        return Server.manager.filter(domain=self.domain).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ServerViewByDomain, self).get_context_data(**kwargs)
        context['server_list'] = Server.manager.filter(domain=self.domain).order_by('name')
        context['group_type'] = 'domain'
        context['group_id'] = self.kwargs['pk']
        return context


class ServerViewByProperty(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        self.property = get_object_or_404(Property, id=self.kwargs['pk'])
        return Server.manager.filter(property=self.property).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ServerViewByProperty, self).get_context_data(**kwargs)
        context['server_list'] = Server.manager.filter(property=self.property).order_by('name')
        context['group_type'] = 'property'
        context['group_id'] = self.kwargs['pk']
        return context


class ServerViewByApplication(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        self.application = get_object_or_404(Application, id=self.kwargs['pk'])
        # return Server.manager.filter(application=self.application).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ServerViewByApplication, self).get_context_data(**kwargs)
        context['server_list'] = Server.manager.filter(application=self.application).order_by('name')
        context['group_type'] = 'application'
        context['group_id'] = self.kwargs['pk']
        return context


class ApplicationViewAll(ListView):
    template_name = 'server/application.html'
    context_object_name = 'application_list'

    def get_queryset(self):
        return Application.manager.all()


class DomainViewAll(ListView):
    template_name = 'server/domain.html'
    context_object_name = 'domain_list'

    def get_queryset(self):
        return Domain.manager.all()


class PropertyViewAll(ListView):
    template_name = 'server/property.html'
    context_object_name = 'property_list'

    def get_queryset(self):
        return Property.manager.all()


def GetServerList(group_type=None, group_id=None):
    if group_type == 'domain':
        server_list = Server.manager.filter(domain=group_id).order_by('name')
    elif group_type == 'property':
        server_list = Server.manager.filter(property=group_id).order_by('name')
    elif group_type == 'application':
        server_list = Server.manager.filter(application=group_id).order_by('name')
    else:
        server_list = Server.manager.all().order_by('name')
    return server_list
