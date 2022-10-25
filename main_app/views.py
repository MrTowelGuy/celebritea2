from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟﾉ</h1>')

def about(request):
    return render(request, 'about.html')


# Add new view
def teas_index(request):
  return render(request, 'teas/index.html', { 'teas': teas })


class Tea:
    def __init__(self, title, type, description, witnesses):
        self.title = title
        self.type =  type
        self.description = description
        self.witnesses = witnesses


teas = [
    Tea('Elon Public Intoxication','Embarassing Loser Status!','A disoriented Elon Musk was sited in Helen, GA tripping on peyote. Eye witnesses claim to have seen him in nothing but an Adventure Time bathrobe and a Batman mask. He was allegedly trying to administer cpr to a dead goldfish crying his stupid little eyes out like a loser', 7),
    Tea('Mickey Mouse Adultery House','Adultery??','Minnie, walking into the clubhouse with the camera crew from cheaters, found Mickey naked in the pantry with a naked Courtney Love. The camera crew witnesses described seeing Courtney Love naked as something similar to "visual terrorism". Sources say that Mickey could be responsible for having a hand in Courtney Love thinking it was okay for her to make music', 10),
    Tea('Living InCyde', 'Unexpected!', 'Leaked emails spill content showing that the frontman of Living In Fear, Curtis, had been emailing mid 2010s crunk-core group "BrokeNcyde" to express his passion and love for their band and their music. When said emails leaked, BC-13 went on record to say that they loved the passion Curtis has for them and would very much like to set up a tour with them and Living in Fear. Curtis has since denied all allegations of writing such an email, going on record to say that "BrokeNcyde is straight Dog water ass clown music". Recent chilling developments had eye witnesses claiming that they had seen Curtis listening to "Bree Bree" by BC-13 on their spotify friend activity, Curtis forgetting to put his spotify on a private listening session', 4569),
]