import random
suits=['hearts','spade','clubs','diamonds']
ranks=['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'ace':14}
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def printcard(self):
        print(f'{self.rank} "of"  {self.suit}')

# two=Card('hearts','seven')
# print(two.value)

class Deck():
    def __init__(self):
        self.allcards=[]
        
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.allcards.append(created_card)


class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        pass
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        print(f'player {self.name} has {len(self.len_cards)} cards')

gaddi=Deck()
# first_card=gaddi.allcards[0]
# first_card.printcard()
random.shuffle(gaddi.allcards)
# for i in gaddi.all_cards:
#     print(i)
ashu=Player("ashu")
shivank=Player("shivank")
# for i in range(0,52):
#     print(gaddi.allcards[i].printcard())





ashu.all_cards=gaddi.allcards[26:]
shivank.all_cards=gaddi.allcards[:26]
new_list=[]
while len(ashu.all_cards)!=0 and len(shivank.all_cards)!=0:
    card1 = ashu.remove_one()
    card2 = shivank.remove_one()
    if card1.value > card2.value:
       
        new_list.append(card1)
        new_list.append(card2)
        # ashu.add_cards.pop(0)
        # shivank.add_cards.pop(0)
        ashu.all_cards.extend(new_list)
        new_list=[]

    elif card1.value < card2.value:
        
        new_list.append(card1)
        new_list.append(card2)
        # ashu.add_cards.pop(0)
        # shivank.add_cards.pop(0)
        shivank.all_cards.extend(new_list)
        new_list=[]

    else:
        if len(ashu.all_cards)<5:
            print("shivank won")
            break
        elif len(shivank.all_cards)<5:
            print("ashu won")
            break
        for i in range(0,5):
             new_list.append(card1)
             new_list.append(card2)
             card1 = ashu.remove_one()
             card2 = shivank.remove_one()
if ashu.all_cards==[]:
    print("shivank won")

elif shivank.all_cards==[]:
    print("ashu won")


        
