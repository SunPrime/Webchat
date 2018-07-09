import json

from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from web_chat.models import Person, Ban


@api_view(['GET'])
def get_users(request):
    if request.session.get('role') != 'admin':
        return HttpResponse('Forbidden', status=403)
    all_users = Person.objects.filter(role__role_name='user')
    json_user = {'users':[]}

    for user in all_users:
        temp = {}
        ban = Ban.objects.filter(user=user).first()
        temp['login'] = user.login
        temp['links'] = []
        link = {}

        if ban == None:
            link['rel'] = 'add'
            link['href'] = reverse('add_to_ban')
        else:
            link['rel'] = 'delete'
            link['href'] = reverse('delete_from_ban', args=[ban.id])

        temp['links'].append(link)
        json_user['users'].append(temp)

    return HttpResponse(json.dumps(json_user), content_type='application/json', status=200)


@csrf_exempt
@api_view(['POST'])
def add_to_ban(request):
    if request.session.get('role') != 'admin':
        return HttpResponse('Forbidden', status=403)
    json_data = JSONParser().parse(request)
    login = json_data['login']
    person = Person.objects.filter(login=login).first()
    if person != None:
        ban = Ban(user=person)
        ban.save()
        return HttpResponse('ok', status=200)
    else:
        return HttpResponse('Not Found', status=404)


@api_view(['DELETE'])
def delete_from_ban(request, ban_id):
    if request.session.get('role') != 'admin':
        return HttpResponse('Forbidden', status=403)
    ban = Ban.objects.filter(id=ban_id).first()
    if ban != None:
        ban.delete()
        return HttpResponse('ok', status=200)
    else:
        return  HttpResponse('Not Found', status=404)