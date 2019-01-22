from django.shortcuts import render

from mymusic.models import Label, Songs


def label(request):
    # data = {}
    object_lists = Label.objects.all()
    for object_list in object_lists:
        # print(object_list.id)
        songs_list = Songs.objects.filter(songs_id=object_list.id)

    return render(request, 'label.html',locals())
