import pymssql


from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Server, Domain, Property, Application


def ServerDetail(request, pk):
    qs_server = Server.objects.filter(pk=pk)

    server = str(qs_server[0])
    database = 'STOF_DBA'
    try:
        conn = pymssql.connect(server=server, database=database, as_dict=True)
        cursor = conn.cursor()
        cursor.execute('SELECT @@VERSION as version;')
        results = cursor.fetchall()
        return render(request, 'server/server_detail.html', context={'pk': pk, 'server': server, 'results': results},)
    except Exception as err:
        messages.error(request, str(err), extra_tags='error')
        # messages.error(request, 'server not found!!!')
        return render(request, 'server/server_detail.html', context={'pk': pk, 'server': server},)


class ServerViewAll(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        return Server.objects.all()


class ServerViewByDomain(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        self.domain = get_object_or_404(Domain, id=self.kwargs['pk'])
        print(self.domain)
        return Server.objects.filter(domain=self.domain)


class ServerViewByProperty(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        self.property = get_object_or_404(Property, id=self.kwargs['pk'])
        return Server.objects.filter(property=self.property).order_by('name')


class ServerViewByApplication(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        self.application = get_object_or_404(Application, id=self.kwargs['pk'])
        return Server.objects.filter(application=self.application).order_by('name')


class ServerDetailView(DetailView):
    model = Server
    # template_name = 'server/server_detail.html'
    # context_object_name = 'server_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['server'] = Server.objects.filter(pk=self.object.pk)

        server = 'SG10-DBAOPS-01'
        database = 'STOF_DBA'
        conn = pymssql.connect(server=server, database=database, as_dict=True)

        cursor = conn.cursor()
        cursor.execute(
            'SELECT [Log_ID], [Log_Date], [Log_Source], [Log_Status], [Log_Message] FROM [log].[VDS_Archive_Log];')

        results = cursor.fetchall()
        # return render(request, 'server/server_detail.html', context={'results': results},)
        return results


class ApplicationViewAll(ListView):
    template_name = 'server/application.html'
    context_object_name = 'application_list'

    def get_queryset(self):
        return Application.objects.all()


class DomainViewAll(ListView):
    template_name = 'server/domain.html'
    context_object_name = 'domain_list'

    def get_queryset(self):
        return Domain.objects.all()


class PropertyViewAll(ListView):
    template_name = 'server/property.html'
    context_object_name = 'property_list'

    def get_queryset(self):
        return Property.objects.all()
