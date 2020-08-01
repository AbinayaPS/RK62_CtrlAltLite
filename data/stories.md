## welcome
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## crime list path
* greet
  - utter_greet
* deny
  - utter_crimelist
* affirm
  - utter_iamabot

## crime reg path
* greet
  - utter_greet
* affirm
  - utter_ask_crime_type
* say_crime_type{"type_of_crime":"Content related to online sexual abuse"}
  - slot{"type_of_crime":"Content related to online sexual abuse"}
  - action_confirm_type

## content crime reg path
* affirm_content_crime{"content_crime_confirmation":"True"}
 - content_crime_form  
 - form{"name":"content_crime_form"}
 - form{"name":null}
 - utter_thanks

## other crime reg path
* affirm_other_crime{"other_crime_confirmation":"True"}
  - slot{"other_crime_confirmation":"True"}
  - utter_ask_other_crime_type
* choose_other_crime_type{"other_crime_type":"loss of money"}
  - slot{"other_crime_type":"loss of money"}
  - ask_other_crime_sub_category
* choose_sub_category{"other_crime_sub_category":"Matrimonial fraud"}
  - other_crime_form
  - form{"name":"other_crime_form"}
  - form{"name":null}
  - utter_thanks
