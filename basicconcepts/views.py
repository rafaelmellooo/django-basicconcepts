from django.http import HttpResponse


class User:
    def index(request):
        return HttpResponse(['Rafael', 'Rodrigo'])

    def show(request, id):
        user_list = {
            1: {
                'id': 1,
                'name': 'Rafael de Mello e Sousa'
            }
        }

        return HttpResponse(str(user_list[id]['id']) + ' - ' + user_list[id]['name'])
