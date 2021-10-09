from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

import uuid

'''class Questions(models.Model):
	question_text=models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Questions,on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default=0)'''


class SubscriptionTier(models.Model):
    TierID = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)  # integer PRIMARY KEY,
    monthlyPrice = models.IntegerField()  # integer NOT NULL,
    # yearlyPrice = models.IntegerField()  # integer NOT NULL,
    maxReviewsPerDay = models.IntegerField()  # integer NOT NULL,
    communityPacksAvailable = models.BooleanField()  # boolean NOT NULL,
    maxLanguages = models.IntegerField()  # integer NOT NULL,
    pictures = models.BooleanField()  # boolean NOT NULL,
    discountWithPackContribution = models.BooleanField()  # boolean NOT NULL


# CREATE TYPE payment AS ENUM ('cash', 'card');

class Subscription(models.Model):
    PAYMENT_METHOD = [
        ('cash', 'Cash'),
        ('card', 'Card')
    ]

    SubscriptionID = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,
                                      editable=False)  # integer PRIMARY KEY,
    Tier = models.ForeignKey(SubscriptionTier, on_delete=models.CASCADE)  # integer REFERENCES SubscriptonTier(TierID),
    expiration = models.DateField()  # date NOT NULL,
    started = models.DateField()  # date NOT NULL,
    paymentMethod = models.CharField(max_length=4, choices=PAYMENT_METHOD)  # payment NOT NULL,
    paymentInfo = models.TextField()  # text NOT NULL


# class Users(models.Model):
#     # CREATE TYPE regService AS ENUM ('Google');
#     REGISTATION_SERVICE = [
#         ("go", "Google"),
#         ("no", "No")
#     ]
#     UserID = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,
#                               editable=False)  # integer NOT NULL Primary,
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     Username = models.CharField(max_length=40, unique=True)  # text UNIQUE,
#     registrationDate = models.DateField(auto_now=True)  # date NOT NULL,
#     registrationService = models.CharField(max_length=2, choices=REGISTATION_SERVICE)  # regService,
#     email = models.EmailField(unique=True, blank=True, null=True)  # text UNIQUE NULL,
#     # paswordHash = models.CharField(max_length=40, null=True)  # text NULL,
#     # subscriptionID = models.ForeignKey(Subscription, on_delete=models.CASCADE,
#     #                                    blank=True)  # integer REFERENCES Subsciption (SubscriptionID ) onDelete = ?


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    XP_points = models.PositiveIntegerField(default=0)  # integer,
    registrationDate = models.DateField(auto_now=True)  # date NOT NULL,

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Users.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class CardPack(models.Model):
    # CREATE TYPE language AS ENUM ('English', 'Russian');
    LANGUAGE = [
        ('EN', 'English'),
        ('RU', 'Russian')
    ]

    PackID = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)  # integer PRIMARY KEY,
    Name = models.CharField(max_length=20, unique=True)  # text NOT NULL UNIQUE,
    createBy = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # integer REFERENCES Users(UserID),
    creationDate = models.DateField(auto_now=True)  # date NOT NULL,
    public = models.BooleanField()  # boolean NOT NULL,
    approved = models.BooleanField()  # boolean NOT NULL,
    rating = models.IntegerField(blank=True, default=0)  # numeric NULL,
    numberOfCards = models.IntegerField(default=0)  # integer NOT NULL,
    sourceLanguage = models.CharField(max_length=2, choices=LANGUAGE)  # language NOT NULL,
    targetLanguage = models.CharField(max_length=2, choices=LANGUAGE)  # language NOT NULL,


class FlashCard(models.Model):
    FlashCardID = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,
                                   editable=False)  # integer PRIMARY KEY,
    pack = models.ForeignKey(CardPack, on_delete=models.CASCADE)  # integer = # REFERENCES CardPack(PackID),
    sourceText = models.TextField(max_length=100)  # text NOT NULL,
    ImageID = models.TextField(max_length=50)  # text,
    targetText = models.TextField(max_length=100)  # text NOT NULL,
    sourceAudio = models.TextField(max_length=50)  # text,
    targetAudio = models.TextField(max_length=50)  # text


class UserPackStatus(models.Model):
    PackStatusID = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,
                                    editable=False)  # integer PRIMARY KEY,
    UserID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # integer REFERENCES Users (UserID),
    PackID = models.ForeignKey(CardPack, on_delete=models.CASCADE)  # integer REFERENCES CardPack(PackID),
    progress = models.IntegerField(blank=True, default=0)  # numeric NOT NULL,
    startDate = models.DateField(auto_now=True)  # date NOT NULL


class UserCardStatus(models.Model):
    CardStatusID = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,
                                    editable=False)  # integer PRIMARY KEY,
    PackStatusIP = models.ForeignKey(UserPackStatus,
                                     on_delete=models.CASCADE)  # integer REFERENCES UserPackCard (PackStatusID),
    CardID = models.ForeignKey(FlashCard, on_delete=models.CASCADE)  # integer REFERENCES FlashCard (FlashCardID),
    cardStrength = models.FloatField(default=0)  # numeric NOT NULL,
    lastReviewedTime = models.DateTimeField(auto_now=True)  # date NOT NULL,
    firstReviewedTime = models.DateField(auto_now_add=True)  # date NOT NULL




