from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser
from models import *

def index(request):
    return HttpResponse("Hello, dear user. This is our page. You gotta love it. Feel the groove...    Isn't it yellow mellow?")

# User experience functions

def config_proj(request):
    """This function will change the priorities of the projects that the user has."""
    pass

def load_ch(request):
    """This function makes estimations of the goals for the current user, based on his historical data from the database."""
    pass

@api_view(['POST'])
def join_ch(request):
    """
    This function assigns a new challenge to a user.
    POST form fields requirements:
        challenge = (name of the challenge)
        user = (user contract)
    """
    if request.method == 'POST':
        # Get data from POST method
        qdata = FormParser().parse(request)
        #print qdata
        data = qdata.dict()
        #print data
        #print data['challenge']

        # Process data
        challenge = Challenge.objects.get( name=data['challenge'] )
        user = User.objects.get( name=data["user"] )
        d_user = DropUser.objects.get( user=user )

        # Make and save changes
        d_user.challenges.add(challenge)
        d_user.save()

    return HttpResponse("User joined (rock'n'roll music fading)")

@api_view(['GET'])
def view_profile(request):
    """Allows a user to see his user info."""
    pass

def load_proj(request):
    """Loads all projects from DB."""
    pass

def see_proj(request):
    """Renders project info."""
    pass


