from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import HttpResponse
from .models import Tag, Question, Deck

#deck_create needs to receive a tag
#deck_create pain level pain_level issue discuss
#deck functions w i p, commented out

# Create your views here:
# Landing
def index(request):
      return HttpResponse("hello, world you are at card question")

def landing(request):
  all_tags = Tag.objects.all().annotate(num_questions=Count('question')).order_by('-num_questions')
  top_tags = all_tags[0:3]
  return render(request, 'flashr/landing.html', {'all_tags': all_tags, 'top_tags': top_tags})

#Questions
def question_show(request, pk):
  question = Question.objects.get(pk=pk)
  return render(request, 'flashr/card.html', {'question': question})

#Deck
##show one deck item
def deck_show(request, tag, idx):
  print('deck show. Request: ', request)
  if idx <= 0: idx = 1
  # Next
  ## Will need to know how many questions there are in total for this tag
  ## Add if statement for stopping going past that max tag id
  user = request.user
  question = Deck.objects.get(profile=user.profile, order_idx=idx).question
  return render(request, 'flashr/card_deck.html', {'question': question, 'tag': tag, 'idx': idx})

# def deck_next(request, tag, idx):
#   question = Deck.objects.filter(profile=profile, order_idx=(idx+1)) #does this work ?
#   return render(request, 'flashr/card_deck.html', {'question': card, 'idx': idx})

# def deck_previous(request, tag, idx):
#   question = Deck.objects.filter(profile=profile, order_idx=(idx-1)) #does this work ?
#   return render(request, 'flashr/card_deck.html', {'question': card, 'idx': idx})

def deck_create(request, tag): #is this correct?
  user = request.user 
  Deck.objects.filter(profile=user.profile).delete()
  tag.lower()
  # print(tag)
  deck = Question.objects.filter(tags__content=tag) # tags__ or tags. ?
  # user_pain = Pain.objects.filter(profile = user.profile)

  # pain_list = //FIND MATCHES ON Question BETWEEN user_pain AND tagged_cards
  # SELECT * FROM (SELECT question FROM pain_omdel WHERE profile = user.profile) WHERE tags__content=tag 

  # //ORDER pain_list BY pain_level
  # no_pain = //ALL tagged_cards NOT IN pain_list
  # //deck = no_pain + pain_list
  for idx, card in enumerate(deck):
    Deck.objects.create(profile=user.profile, question=deck[idx], order_idx=(idx+1))
  return redirect('deck_show', tag=tag, idx=1)