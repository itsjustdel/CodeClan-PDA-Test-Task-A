### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # should be == instead of =
    if card.value = 1:
      return True
      # missing colon : after else
    else
      return False
   
  # dif should be def
  # missing comma between card1 and card2
  dif highest_card(self, card1 card2):
  #not indented, if and else should be tabbed in
  if card1.value > card2.value:
    # should be return card1
    return card
  else:
    return card2
  

# whole method needs indented to be inside CardGame
def cards_total(self, cards):
  # unfinished variable declaration - should be "total = 0"
  total
  for card in cards:
    total += card.value
    # return is embedded and shouldn't be
    # total needs to cast to a string
    return "You have a total of" + total
  
```
