from django.contrib import messages
from django.shortcuts import render, redirect

from .models import  Comments

def dashboard(request):
    # On traite ici les requetes POST
    if request.method == 'POST':

        #Récupérer les données des champs qui proviennent de la page html.
        comments = request.POST.get('comments')
        name = request.POST.get('name')

        # On vérifie si tout est remplie ici et on renvoie un message d'erreur
        if not comments:
            messages.error(request, 'Ajoutez un message ')
            return redirect('dashboard')
        if not name:
            messages.error(request, 'Ajoutez un nom')
            return redirect('dashboard')
        # On enregistre dans la base de donnée

        Comments.objects.create(name=name, comments=comments).save()
        messages.success(request, 'Message ajoutée')
        return redirect('dashboard')

    # On récupere tout les commentaires ici
    all_comments = Comments.objects.all().order_by('-created_at')
    # On renvoie ici tout sur le front-end
    context = {'all_comments': all_comments}
    return render(request, 'index.html', context)