from .models import Setting
def data_pass(request):
    data = {
        'title':"News Portal",
        "settingData":Setting.objects.first(),
    }
    return data