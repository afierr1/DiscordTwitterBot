## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* name{"name":"Sam"}
 - utter_greet
 

## story_joke_01
* joke
 - action_joke
 
## story_joke_02
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* joke
 - action_joke
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
 
 
## story_first
* first
 - action_first
 
## story_tweet_01
* tweet
 - action_twitter
 
## story_tweet_02
 
 * greet
 - utter_name
 * name{"name":"Bhoomika"} 
 - utter_greet
 *tweet
 - action_search_tweet
 *thanks
 - utter_thanks
 *goodbye
 - utter_goodbye
 
 ## story_hashtag_01
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* tweet
 - search_hashtag
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
 
 
## story_search_tweet
 * tweet_subject
  - action_search_tweet
  
## story_search_company
  * search_company
  - action_search_company
