from django.shortcuts import render,get_object_or_404
from systermmsg.models import SystermMsg

# Create your views here.
def ListAll(request):
    allmsgs = SystermMsg.objects.all()
    return render(request, 'message/system_msg_list.html', {'allmsgs': allmsgs})

def sys_msg_detail(request, id):
    sys_msg = get_object_or_404(SystermMsg, id=id)
    return render(request, 'message/systerm_msg_detail.html', {'sys_msg':sys_msg})

