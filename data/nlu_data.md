<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/rasa-starter-pack/704 --> 

## intent:goodbye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon
- good day mate
- bye bud!
- bye sister
- peace out
- hasta la vista
- nice talking to you!


## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot
- hey pal
- hey buddy!
- hi buddy!
- hi dude
- hey dude!
- hola
- hi sisters
- hey man
- hey girl
- hey you
- hello

## intent:thanks
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you
- thanks so much bro
- thanks so much dude
- I just wanted to say thanks
- I just wanted to thank you
- Thank you from the bottom of my heart

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely
- of course
- certainly
- obviously
- okay
- ok
- cool
- oh true

## intent:name
- My name is [Juste](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [Josh](name)
- I'm [Lucy](name)
- People call me [Greg](name)
- It's [David](name)
- Usually people call me [Amy](name)
- My name is [John](name)
- You can call me [Sam](name)
- Please call me [Linda](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
- I am [Charlie](name)
- I am [Charlie](name)
- I am [Ben](name)
- Call me [Susan](name)
- [Lucy](name)
- [Peter](name)
- [Mark](name)
- [Joseph](name)
- [Tan](name)
- [Pete](name)
- [Elon](name)
- [Penny](name)
- name is [Andrew](name)
- I [Lora](name)
- [Stan](name) is my name
- [Susan](name) is the name
- [Ross](name) is my first name
- [Bing](name) is my last name
- Few call me as [Angelina](name)
- Some call me [Julia](name)
- Everyone calls me [Laura](name)
- I am [Ganesh](name)
- My name is [Mike](name)
- just call me [Monika](name)
- Few call [Dan](name)
- You can always call me [Suraj](name)
- Some will call me [Andrew](name)
- My name is [Ajay](name)
- I call [Ding](name)
- I'm [Partia](name)
- Please call me [Leo](name)
- name is [Pari](name)
- name [Sanjay](name)
- My name is [Bhoomika](name)
- My name is [Analilia](name)
- My name is [Tyler](name)
- My name [Jeff](name)

## intent:joke
- Can you tell me a joke?
- I would like to hear a joke
- Tell me a joke
- A joke please
- Tell me a joke please
- I would like to hear a joke
- I would like to hear a joke, please
- Can you tell jokes?
- Please tell me a joke
- I need to hear a joke
- I'd like a joke please
- Tell me something funny that will make me laugh

## intent:tweet_subject
- Find me a tweet on [puppies](subject)
- Get me a tweet on [horses](subject)
- I want a tweet on [Cancun](subject)
- Find a twitter on [Coachella](subject)
- Display a tweet about [avengers](subject)
- Show me [computer science](subject) tweets
- Show me tweets about [harry styles](subject)
- Show me [makeup tutorial](subject) tweets
- Show me [funny dogs](subject) tweets
- Find me a tweet on [puppies](subject)
- Get me a tweet on [horses](subject)
- I want a tweet on [Cancun](subject)
- Find a twitter on [Coachella](subject)
- Display a tweet about [avengers](subject)
- Show me [computer science](subject) tweets
- Show me tweets about [harry styles](subject)
- Show me [makeup tutorial](subject) tweets
- Show me [funny dogs](subject) tweets


## intent:tweet_context
- Find me a [funny](mood) tweet on [puppies](subject)
- Get me a [cool](mood) tweet on [horses](subject)
- I want a [beautiful](mood) tweet on [Cancun](subject)
- Find an [awesome](mood) twitter on [Coachella](subject)
- Display a [non-spoiler](mood) tweet about [avengers](subject)
- Show me [informative](mood) [computer science](subject) tweets
- Show me an [interesting](mood) tweets about [harry styles](subject)
- Show me a [hilarious](mood) [makeup tutorial](subject) tweets
- Show me a [funny](mood) [dogs](subject) tweets
- Find me a [cute](mood) tweet on [puppies](subject)
- Get me a [nice](mood) tweet on [horses](subject)
- I want a [cool](mood) tweet on [Cancun](subject)
- Find a [popular](mood) twitter on [Coachella](subject)
- Display a [fun](mood) tweet about [avengers](subject)
- Show me a [cool](mood) [computer science](subject) tweets
- Show me some [funny](mood) tweets about [harry styles](subject)
- Show me a [nice](mood) [makeup tutorial](subject) tweets
- Show me [funny](mood) [dogs](subject) tweets

## intent:search_company
- Show me what [Best Buy](ORG)/[Shoppers](ORG)/[BP](ORG) is talking about on twitter.
- Show me what [Amazon](ORG) is talking about on twitter.
- Hey, find me a tweet on [Google](ORG) and [Kmart](ORG)
- Find me a tweet by [Google](ORG)
- Find me a tweet by [Google](ORG)/[Yahoo](ORG)
- Find me a tweet from [Best Buy](ORG)/[Shoppers](ORG)/[BP](ORG)
- Find me a tweet from [BP](ORG)
- Get a tweet on [Sears](ORG)
- Get a tweet on [Sears](ORG) and [Nestle](ORG)
- Search for a tweet on [Burger King](ORG)
- Give me a tweet on [Samsung](ORG)
- Get tweet on [Nintendo](ORG)
- Get me a tweet on [Torrid](ORG)
- Find a tweet on [Exxon](ORG)
- Find a tweet on [Amazon](ORG)
- Find a tweeet by [CBS](ORG)
- Find a tweet by [NBC](ORG)
- Find a tweet by [CNN](ORG)
- Find me a tweet by [Apple](ORG)
- Find me a tweet by [Twitter](ORG)
- Find me a tweet by [Towson University](ORG)
- Find a tweet by [Reddit](ORG)
- Find a tweet by [Comcast](ORG)

## intent:search_hash
- Find me a tweet with hashtag [#TowsonU](hashtag)
- Find me a tweet with hashtag [#HarryStyles](hashtag)
- Fine me a tweet with the hashtag [#Coachella](hashtag)
- Find me a tweet with the hashtag [#Motivation](hashtag)
- Find me a tweet about [#Starbucks](hashtag)
- Find me a tweet about [#JamesCharles](hashtag)
- Find me a tweet about [#DavidDobrik](hashtag)


## lookup:ORG
- Gap
- Footlocker
- Payless Shoes
- Giant
- Safeway
- Cheeasecake Factory
- PF Chang's
- Shell
- Athletica
- Lululemon
- Wish
- CBS
- NBC
- Amazon
- Google
- BP
- Sears
- Burger King
- Samsung 
- Nintendo
- Torrid
- Exxon
- Amazon
- CBS
- NBC
- CNN
- Apple
- Twitter
- Towson University
- Reddit


##lookup:hashtag
- #gogreen
- #environment
- #savetheearth
- #cleanenergy