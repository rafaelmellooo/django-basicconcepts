from django.shortcuts import render


class User:
    def index(request):
        return render(request, 'index.html')

    def show(request, id):
        user_list = {
            1: {
                'id': 1,
                'name': 'Rafael de Mello e Sousa'
            },

            2: {
                'id': 2,
                'name': 'Fernando Geraldo Oliveira'
            }
        }

        user = {}

        try:
            user = {
                'id': user_list[id]['id'],
                'name': user_list[id]['name']
            }
        except:
            user = {
                'error': 'User not found'
            }

        return render(request, 'user.html', user)
