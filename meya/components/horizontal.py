# Write or paste code here. You can also use the blueprints as a starting pointfrom meya import Component
from meya.cards import Image
import requests
from meya.cards import Card, Cards, Button

class Giphy(Component):
    
    def start(self):
        buttons = [
            Button(
                text='See Wikipedia page',
                url='https://en.wikipedia.org/wiki/African_elephant'
                ),
            Button(
                text='See more',
                action='next'
                ),
            Button(
                text='Vote',low='vote_result',
                data={'vote': 'african'}
                )
                ]
        element1 = Card(
            title='African Elephant',
            text='One species of African elephant is the largest living terrestrial animal.',
            item_url='https://en.wikipedia.org/wiki/African_elephant',
            image_url='http://i.imgur.com/7Z9IX5W.jpg',
            buttons=buttons)
        buttons = [
            Button(
                text='See Wikipedia page',
                url='https://en.wikipedia.org/wiki/Asian_elephant'
                ),
            Button(
                text='See more',
                action='next'
                ),
            Button(
                text='Vote',
                flow='vote_result',
                data={'vote': 'asian'}
                )
                ]
        element2 = Card(
            title='African Elephant',
            text='In general, the Asian elephant is smaller than the African elephant.',
            item_url='https://en.wikipedia.org/wiki/Asian_elephant',
            image_url='http://i.imgur.com/w5qzZ7I.jpg',
            buttons=buttons)

        card = Cards(elements=[element1, element2])
        message = self.create_message(card=card)

        
        return self.respond(message=message, action="next")
