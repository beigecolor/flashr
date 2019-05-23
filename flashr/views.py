from django.shortcuts import render
#deck_create needs to recieve a tag
#deck_create pain level pain_level issue discuss
#deck functions w i p, commented out

# Create your views here:
# Landing
def landing(request):
  return render(request, 'flashr/landing.html')

#Questions
def question_show(request, pk):
  question = Question.objects.get(pk=pk)
  return render(request, 'flashr/card.html', {'question': question})

#Deck
def deck_show(request, tag, idx):
  question = Deck.objects.filter(profile=profile, order_idx=idx)
  return render(request, 'flashr/card_deck.html', {'question': card, 'idx': idx})

def deck_next(request, tag, idx):
  question = Deck.objects.filter(profile=profile, order_idx=(idx+1)) #does this work ?
  return render(request, 'flashr/card_deck.html', {'question': card, 'idx': idx})

def deck_previous(request, tag, idx):
  question = Deck.objects.filter(profile=profile, order_idx=(idx-1)) #does this work ?
  return render(request, 'flashr/card_deck.html', {'question': card, 'idx': idx})


def deck_create(request, profile, tag): #is this correct?
  Deck.objects.filter(profile=profile).delete()

  deck = Question.objects.filter(tags__content=tag) # tags__ or tags. ?
  # user_pain = Pain.objects.filter(profile = user.profile)

  # pain_list = //FIND MATCHES ON Question BETWEEN user_pain AND tagged_cards
  # SELECT * FROM (SELECT question FROM pain_omdel WHERE profile = user.profile) WHERE tags__content=tag 

  # //ORDER pain_list BY pain_level
  # no_pain = //ALL tagged_cards NOT IN pain_list
  # //deck = no_pain + pain_list

  for idx, card in enumerate(deck):
    Deck.objects.create(profile=profile, question=deck[idx], order_idx=(idx+1))
  return redirect('deck_show', profile=profile, order_idx=1)