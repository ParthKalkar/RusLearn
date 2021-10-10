from django.contrib.auth.decorators import login_required
from django.db import reset_queries
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import UserPackStatus, UserCardStatus, CardPack, FlashCard, UserCardStatus, language_list
import datetime
from django.http.response import JsonResponse

# Create your views here.
from django.urls import reverse
import regex
from random_word import RandomWords
import googletrans

def get_last_card(request, pack):
    pack_status_id = UserPackStatus.objects.get(UserID=request.user, PackID=pack).PackStatusID
    status_for_card = UserCardStatus.objects.filter(PackStatusIP=pack_status_id).order_by('lastReviewedTime')[0]
    # status_for_card.lastReviewedTime = datetime.datetime.today()
    return status_for_card.CardID

@login_required
def home(request):
    user_profile = request.user
    packs = CardPack.objects.filter(createBy=request.user)
    flash_cards = []
    empty_packs = []
    next_card = []
    for i in packs:
        tmp = FlashCard.objects.filter(pack=i)
        flash_cards.append([i.PackID, tmp])
        if len(list(tmp))==0:
            empty_packs.append(i.PackID)
        else:
            next_card.append([i.PackID, get_last_card(request, i)])
            # pass


    print(flash_cards)
    return render(request, 'home.html', context={
        'user_profile': user_profile,
        'packs': packs,
        'flash_cards': flash_cards,
        'empty_packs': empty_packs, 
        'next_card': next_card, 
        'language_list': language_list()
    })
    # return HttpResponse('Hello, World!')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = None
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
    if form is None:
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
    form = None
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
            print(form.error_messages)    
            print(form.errors)
    else:
        form = AuthenticationForm()
    register_form = CustomUserCreationForm()
    print(form.errors)
    return render(request, 'registration/login.html', {'form': form, 'register_form': register_form})


@login_required
def get_next_card(request):
    user_id = request.user
    pack_id = request.POST['pack_id']

    pack_status_id = UserPackStatus.objects.get(UserID=user_id, PackID=pack_id).PackStatusID
    status_for_card = UserCardStatus.objects.filter(PackStatusIP=pack_status_id).order_by('lastReviewedTime')[0]
    # status_for_card.lastReviewedTime = datetime.datetime.today()

    card = status_for_card.CardID
    print(f"found card: {[card.sourceText, card.targetText]}")
    card = {'source_text': card.sourceText, 'target_text': card.targetText, 'card_id': card.FlashCardID}
    json_dump = JsonResponse(card)
    return json_dump


# @login_required
# def add_new_pack(request):
#     pack = CardPack(createBy=request.user,
#                     )


@login_required
def create_pack(request):
    if request.method == 'POST':
        user = request.user
        pack_name = request.POST['name']
        pack_source_language = request.POST['source']
        pack_target_language = request.POST['target']
        number_of_words = request.POST['number_of_words']

        if number_of_words is None:
            number_of_words = 0
        p = CardPack(Name=pack_name, createBy=user, public=False,
                     approved=False, sourceLanguage=pack_source_language, targetLanguage=pack_target_language,
                     numberOfCards=number_of_words)
        pack_status = UserPackStatus(UserID=user, PackID=p)
        p.save()
        pack_status.save()

        for i in range(int(number_of_words)):
            word = RandomWords().get_random_word()
            print(word)
            source_translation = word
            target_translation = word
            translator = googletrans.Translator()
            if pack_source_language != 'en':
                # use re-attempts
                attempts = 10
                while True:
                    try:
                        attempts -= 1
                        source_translation = translator.translate(word, dest=pack_source_language, src='en').text
                        break
                    except Exception as e:
                        print(e)
                        if attempts==0:
                            source_translation = word
                            break
            if pack_target_language != 'en':
                # use re-attempts
                attempts = 10
                while True:
                    try:
                        attempts -= 1
                        target_translation = translator.translate(word, dest=pack_target_language, src='en').text
                        break
                    except Exception as e:
                        print(e)
                        if attempts==0:
                            target_translation = word
                            break

            card = FlashCard(pack=p, sourceText=source_translation, targetText=target_translation)
            card_status = UserCardStatus(PackStatusIP=UserPackStatus.objects.filter(PackID=p, UserID=user)[0],
                                     CardID=card
                                     )
            card.save()
            card_status.save()

    return redirect('home')


@login_required
def add_card(request):
    if request.method == 'POST':
        user = request.user
        pack = CardPack.objects.filter(PackID=request.POST['pack_id'])[0]
        source_text = request.POST['source_text']
        target_text = request.POST['target_text']

        # print(request.POST['batch_input'])
        #re = regex.match(r"(\p{L}|\d)+(?: )*-(?: )*(\p{L}|\d)+", request.POST['batch_input'])
        #print(re)

        for match in request.POST['batch_input'].split("\n"):
            print(f"Found batch input item : {match}")
            tmp = match.split(" - ")
            if len(tmp) != 2:
                continue
            card = FlashCard(pack=pack, sourceText=tmp[0], targetText=tmp[1])
            card_status = UserCardStatus(PackStatusIP=UserPackStatus.objects.filter(PackID=pack, UserID=user)[0],
                                     CardID=card
                                     )
            card.save()
            card_status.save()
        card = FlashCard(pack=pack, sourceText=source_text, targetText=target_text)
        card_status = UserCardStatus(PackStatusIP=UserPackStatus.objects.filter(PackID=pack, UserID=user)[0],
                                     CardID=card, 
                                     # lastReviewedTime=datetime.datetime.today(),
                                     # firstReviewedTime=datetime.datetime.today()
                                     )
        card.save()
        card_status.save()

    # p = FlashCard()
    # pack_status = UserCardStatus()
    return redirect('home')


@login_required
def delete_pack(request):
    if request.method == 'POST':
        pack_id = request.POST['pack_id']
        CardPack.objects.filter(PackID=pack_id).delete()
    return redirect('home')


@login_required
def delete_card(request):
    if request.method == 'POST':
        card_id = request.POST['card_id']
        FlashCard.objects.filter(FlashCardID=card_id).delete()
    return redirect('home')

@login_required
def view_card(request):
    print(request.POST)
    print(dict(request.POST))
    user = request.user
    user.XP_points += 1
    user.save()
    card = FlashCard.objects.filter(FlashCardID=request.POST.get('card_id'))[0]
    user_card_status = UserCardStatus.objects.filter(CardID=card)[0]
    user_card_status.save()
    return JsonResponse({'status': 'success.'})

@login_required
def subscription_page(request):
    return render(request, 'subscriptions.html')

