# Create your views here.
from django.shortcuts import HttpResponse, render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from creators.models import Creator


def creator_record(request, creator_id):
    request.breadcrumbs('Creators', reverse('creators_list'))
    creator_id = int(creator_id)
    creator = None
    creator = Creator.objects.get(id=creator_id)
    return render_to_response('creators.html',
                              {"creator": creator}, context_instance=RequestContext(request))
    
    
def creators_list(request):
    orderby = None
    creator_list = None       
    orderby = request.GET.get('orderby', None)
    if orderby is None:
        orderby = 'name'            
    if orderby == 'activity_start_year':
        creator_list = Creator.objects.order_by('activity_start_year', 'activity_end_year')
    else:
        creator_list = Creator.objects.order_by(orderby)
    paginator = Paginator(creator_list, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    creators = paginator.page(page)
    return render_to_response('creators_list.html',
                              {"creators": creators, "order": orderby}, context_instance=RequestContext(request))