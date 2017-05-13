from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FormParser
from models import *
from serializers import *

@api_view(['GET'])
def index(request):
        return JsonResponse({'User': 'Quim'})

@api_view(['GET'])
def prova(request):
    qdata = FormParser().parse(request)
    data = qdata.dict()
    # hour = Hour.create(value=1)
    # hour.save()
    # hour = Hour.create(value=1)
    # hour.save()
    #hours = Hour.objects.all()
    #print hours
    #hour = Hour.objects.all().filter(value=1)
    #hour = Hour.objects.get(value=1)
    #print hour
    projects = Project.objects.all()
    print projects[0].name
    t_ch = TypeChallenge.objects.all()
    print t_ch[0].name
    return HttpResponse('Bingo!')


# Instance creators

@api_view(['POST'])
def NewUser(request):
    """
    Creates a new user
    POST form field requirements:
        num_contract = (int)
        password = (string)
    """
    if request.method == 'POST':
        # Parsing uses application/x-www-form-urlencoded format
        qdata = FormParser().parse(request)
        data = qdata.dict()
        print data
        num_contract =  int(data['num_contract'])
        password = data['password']
        print num_contract, password

        u = User.objects.all().filter(username=num_contract).exists()
        if not u:
            user = User.objects.create_user(num_contract,password)
            user.save()
            print 'User is'
            print user
            du = DropUser(user=user)
            print 'Drop user is'
            print du
            print 'And his user is'
            print du.user
            du.save()
            print 'Saved drop user is'
            print du
            return JsonResponse({'Succes': 'All OK'})
        else:
            return JsonResponse({'Error': 'User already exists'})
    else:
        return JsonResponse({'Error': 'Not POST method'})

@api_view(['POST'])
def NewProject(request):
    """
    Creates a new project
    POST form field requirements:
        num_contract = (int)
        name = (string)
        description = (string)
        location = (string)
        goal = (int)
    """
    if request.method == 'POST':
        # Parsing data
        qdata = FormParser().parse(request)
        data = qdata.dict()
        num_contract =  data['num_contract']

        u = User.objects.all().filter(username=num_contract).exists()
        if u:
            #user = User.objects.get(username=num_contract)
            #if user.is_staff:
                name_proj =  data['name']
                n = Project.objects.all().filter(name=name_proj).exists()
                if not n:
                    description = data['description']
                    location = data['location']
                    goal = data['goal']
                    proj = Project.create(name_proj,description,location,goal)
                    proj.save()
                    print 'Project saved!'
                    return JsonResponse({'Succes': 'All OK'})
                else:
                    return JsonResponse({'Error': 'Project already exists'})
            #else:
                #return JsonResponse({'Error': 'User is not admin'})
        else:
            return JsonResponse({'Error': 'User does not exist'})
    else:
        return JsonResponse({'Error': 'Not POST method'})

@api_view(['POST'])
def NewTypeChallenge(request):
    """
    Creates a new Type of Challenge.
    POST form field requirements:
        name = (string)
        description = (string)
        multiplier = (int) [1-inf]
        obj = (int) [0-100]

        hours = (int) [1-24] ** Needs revision (for multiple inputs)
        days = (int) [1-7] ** Needs revision (for multiple inputs)
        months = (int) [1-12] ** Needs revision (for multiple inputs)
    """
    if request.method == 'POST':
        # Parsing data from POST application/x-www-form-urlencoded
        qdata = FormParser().parse(request)
        data = qdata.dict()
        print data
        name = data['name']
        description = data['description']
        multiplier = data['multiplier']
        obj = data['obj']

        hours = data['hours']
        days = data['days']
        months = data['months']

        #create models
        hour = Hour.create(hours)
        hour.save()
        day = Day.create(days)
        day.save()
        month = Month.create(months)
        month.save()

        tc = TypeChallenge.create(name=name, description=description, multiplier=multiplier, obj=obj)
        tc.save()

        tc.hours.add(hour)
        tc.days.add(day)
        tc.months.add(month)

        print 'Success! Challenge created'

        return JsonResponse({'Challenge': name})
    else:
        return JsonResponse({'Error': 'Not POST method'})

# Get methods

@api_view(['GET'])
def view_profile(request):
    """
    Allows a user to see his user info.
    USER PROJECTS AND PRIORITIES NEED TO BE ADDED.
    """
    #username =  request.GET.get('username','')
    username = 42 ################################################3
    if(User.objects.filter(username=username).exists()):
        user = User.objects.get(username=username)
        if(DropUser.objects.filter(user=user).exists()):
            du = DropUser.objects.get(user=user)
            serializer = DropUserSerializer(du)
            json = JSONRenderer().render(serializer.data)
            return JsonResponse(json, safe=False)
        else:
            return JsonResponse({'Error': "User does not exist"})
    else:
        return JsonResponse({'Error': "User doesn't exist"})

@api_view(['GET'])
def view_proj(request):
    """ Renders project info."""
    name = "proj guay" ###################################################
    if(Project.objects.filter(name=name).exists()):
        proj = Project.objects.get(name=name)
        serializer = ProjectSerializer(proj)
        json = JSONRenderer().render(serializer.data)
        return JsonResponse(json, safe=False)
    else:
        return JsonResponse({'Error': "Project does not exist"})

@api_view(['GET'])
def view_t_ch(request):
    """ Renders challenge info."""
    name = "no lavadoras" ############################################
    if(TypeChallenge.objects.filter(name=name).exists()):
        t_ch = TypeChallenge.objects.get(name=name)
        serializer = TypeChallengeSerializer(t_ch)
        json = JSONRenderer().render(serializer.data)
        return JsonResponse(json, safe=False)
    else:
        return JsonResponse({'Error': "Project does not exist"})

# @api_view(['GET'])
# def view_ch(request):
#     """ Renders customized challenge info."""
#     ch = "I'm a customized ch"
#     #username =  request.GET.get('username','')
#     username = 42 ######################################3
#     if(User.objects.filter(username=username).exists()):
#         user = User.objects.get(username=username)
#         #du = DropUser.objects.get(user=user)
#         return JsonResponse({'Name': user.username})
#     else:
#         return JsonResponse({'Error': "User doesn't exist"})
#     if(Challenge.objects.filter(name=ch).exists()): #Temporal
#         return JsonResponse({'T_Ch': t_ch})
#     else:
#         return JsonResponse({'Error': "User not exists"})


# Load methods

@api_view(['GET'])
def load_t_ch(request):
    """Loads all challenge names from DB."""
    t_chs = TypeChallenge.objects.all()
    serializer = TypeChallengeSerializer(t_chs, many=True)
    json = JSONRenderer().render(serializer.data)
    return JsonResponse(json, safe=False)

@api_view(['GET'])
def load_proj(request):
    """Loads all projects from DB."""
    projs = Project.objects.all()
    serializer = ProjectSerializer(projs, many=True)
    json = JSONRenderer().render(serializer.data)
    return JsonResponse(json, safe=False)

def config_proj(request):
    """ This function will change the priorities of the projects that the user has. """
    pass

@api_view(['POST'])
def join_ch(request):
    """
    This function assigns a new challenge to a user.
    POST form fields requirements:
        typechallenge = (name of the challenge)
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
        tc = TypeChallenge.objects.get(name=data['typechallenge'])
        user = User.objects.get(name=data["user"])
        d_user = DropUser.objects.get(user=user)

        # Create new challenge instance for the user
        ## Funcionn de Irene( inputs = typechallenge, user; output = goal)
        goal = 7 # Dumb variable
        challenge = Challenge.create(tc, goal)

        # Make and save changes
        d_user.save()
        d_user.challenges.add(challenge)

        return HttpResponse("User joined (rock'n'roll music fading)")

    else:
        return HttpResponse("WTF! Man, you have to do post for this, man!")
