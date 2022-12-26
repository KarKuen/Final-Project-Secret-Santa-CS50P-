# SECRET SANTA
#### Video Demo:  <https://youtu.be/4uMrzrkhDd0>
#### Description: Secret Santa is a christmas event where friends and family gather together and exchange gifts. This sounds like your typical christmas however, the catch with Secret Santa is... Instead of gifting multiple people, each person only gift one other person. AND, the biggest twist is, you wouldn't know who is your secret santa, you only know who you're gifting to!

#### Reasoning: I originally thought of making a mobile application with the python library kivy (Because, I wanted to learn mobile development after finishing CS50. Unfortunately, that route has been discontinued and is outdated). However, kivy is not compatible with python 3.11 yet and I faced many issues with installing the library. Therefore, I sought to find a new idea for my final project.

#### Inspiration: I have never celebrated christmas before. This will be my first year celebrating it and I'm participating in a Secret Santa gift exchange. Currently, it's 18/12/2022. Just one week before christmas. Hence, I thought it would be nice to celebrate my first ever christmas gift exchange / secret santa by making my own Secret Santa system!

#### CLASS(): I created a class (Person) which initializes itself with a the person's own name (name), the name of the person they're gifting to (secretsanta) and the gift they are giving them (gift) which is defaulted to coals.

#### PARTICIPANTS(): The first thing the program does is ask for the participants of the secret santa. As the user inputs the participant's names one by one, they are appended into a list. This process can only be stopped when the user input 'E'.

#### SECRETSANTAS(): After collecting all the participant's names, we'll shuffle the list with the python random library to randomize everyone's secret santa. After randomizing the list, as the sequence is in a random order, we can safely assign each participant's secret santa as the person who came before them (within the list), for the first person in the list, his secret santa will be the last person in the list. Therefore, we'll create an object of Person class for each participant, giving them attributes of name and secretsanta.

#### PRESENTS(): Asks users for input of which gifter to select and what to update the gift attribute to for the selected gifter

#### PURCHASE(): Requires parameters of gifter, gift and the list of objects (every participant). This will search through the list of objects (participant) and if the gifter is within that list, update the object's gift attribute to the user's input. If the gifter is not found, no changes are made

#### CHRISTMASSALES(): Repeatedly asks the user if any participants are going to buy gifts. If yes, it'll call the presents() and purchase() functions. If no, end this cycle.

#### CHRISTMASEVE(): Repeatedly prompt user to say 'MERRY CHRISTMAS'

#### CHRISTMASDAY(): Reveal everyone's secret santa and gifts by print them out