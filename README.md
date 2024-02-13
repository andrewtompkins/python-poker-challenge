# Poker Hand Project

## Part 1
You have decided that you would like to make your own digital version of 5 card poker.

After a lot of thought, you have decided to do this by simulating a deck of standard playing cards.
Your deck of cards consist of a group of card objects, with each card having a ranking (Ace - King) and a suite (Diamonds, hearts, clubs and spades)

You should be able to construct a hand, which can contain any number of cards, less than 52.
With a hand of 5 cards, you should be able to retrieve a hand rank and also be able to compare two hands of 5 cards using comparators.
Details for the hand rankings can be found here: http://www.wsop.com/poker-hands/

Thankfully, a lot of the groundwork has been completed by someone before you and only a few functions require completion.
These functions are:
* The hand comparison and describe functions in `pokerhands.handrank.Hand`)
* The deck picking function: `pokerhands.Deck.pick`

Provide a solution to this problem function which satisfies all the test cases provided and any new tests you add.
Note that your solution will be evaluated against a more exhaustive list of tests, so think about missing test coverage and add tests you think are necessary.

## Part 2: Stretch goal
Once you've completed Part 1 of the project, you decide that you'd like to see the best single 5-card hand you can create out of N-cards (limited by the deck size of 52).
Add this alternative option into the project with appropriate tests.

## Requirements
* Python 3

## Running tests
Run: `python3 -m unittest discover tests -p '*_test.py'`

When all the tests pass and you are happy with the state of the code, return the code to SprintHive.

## Notes
* If you find a bug or design issue with the existing code, fix it or change it as required and document this change.
* State any assumptions you make
