from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import UserPackStatus, UserCardStatus,CardPack, FlashCard, UserCardStatus
import datetime
from django.http.response import JsonResponse

# Create your views here.
from django.urls import reverse


@login_required
def home(request):
    user_profile = request.user
    packs = CardPack.objects.filter(createBy=request.user)
    return render(request, 'home.html', context={
        'user_profile': user_profile,
        'packs': packs
    })
    # return HttpResponse('Hello, World!')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("form received")
        if form.is_valid():
            print("the form is valid")
            form.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        messages.error(request, "not valid")
    form = CustomUserCreationForm(request.POST)
    context = {
        'register_form': form,
        'form': AuthenticationForm()
    }
    return render(request, 'registration/login.html', context)


def logout_request(request):
    logout(request)
    return redirect('login')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('home'))
        else:
            messages.error(request, 'username or password not correct')
            return redirect(reverse('login'))


    else:
        form = AuthenticationForm(request.POST)
        register_form = CustomUserCreationForm()
    return render(request, 'registration/login.html', {'form': form, 'register_form': register_form})


@login_required
def get_next_card(request):
    user_id = request.user.UserID
    pack_id = request.form.PackID

    pack_status_id = UserPackStatus.objects.get(UserID = user_id,PackID = pack_id).PackStatusID
    status_for_card = UserCardStatus.objects.filter(PackStatusIP = pack_status_id).order_by('lastReviewedTime')[0]
    status_for_card.lastReviewedTime =  datetime.datetime.today()

    card = status_for_card.CardID
    print(f"found card: {[card.sourceText,card.targetText]}")
    card = {'sourceText':card.sourceText,'targetText':card.targetText}
    json_dump = JsonResponse.dumps(card)
    return json_dump

@login_required
def add_new_pack(request):
    pack = CardPack(createBy=request.user,
                    )


@login_required
def create_pack(request):
    user = request.user
    pack_name = request.form.PackName
    pack_source_language = request.form.SourceLanguage
    pack_target_language = request.form.TargetLanguage
    number_of_words = request.form.NumberOfWords

    if number_of_words==None:
        number_of_words = 0
    p = CardPack(Name = pack_name,createBy = user,public = False,
            approved = False,sourceLanguage = pack_source_language,targetLanguage = pack_target_language,numberOfCards = number_of_words)
    pack_status = UserPackStatus(UserID = user,PackID = p)
    return redirect('home')

@login_required
def add_card(request):
    user = request.user
    pack_name = request.form.PackName
    pack_source_language = request.form.SourceLanguage
    pack_target_language = request.form.TargetLanguage
    number_of_words = request.form.NumberOfWords

    '''FlashCard(models.Model):
    FlashCardID = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,
                                   editable=False)  # integer PRIMARY KEY,
    pack = models.ForeignKey(CardPack, on_delete=models.CASCADE)  # integer = # REFERENCES CardPack(PackID),
    sourceText = models.TextField(max_length=100)  # text NOT NULL,
    ImageID = models.TextField(max_length=50)  # text,
    targetText = models.TextField(max_length=100)  # text NOT NULL,
    sourceAudio = models.TextField(max_length=50)  # text,
    targetAudio = models.TextField(max_length=50)  # text
    
    UserCardStatus(models.Model):
    CardStatusID = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,
                                    editable=False)  # integer PRIMARY KEY,
    PackStatusIP = models.ForeignKey(UserPackStatus,
                                     on_delete=models.CASCADE)  # integer REFERENCES UserPackCard (PackStatusID),
    CardID = models.ForeignKey(FlashCard, on_delete=models.CASCADE)  # integer REFERENCES FlashCard (FlashCardID),
    cardStrength = models.FloatField(default=0)  # numeric NOT NULL,
    lastReviewedTime = models.DateTimeField()  # date NOT NULL,
    firstReviewedTime = models.DateField()
    '''

    p = FlashCard()
    pack_status = UserCardStatus()
    return redirect('home')