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

## crime path
* cybercrime
  - utter_cybercrimedesc

## frauddetech path
* online_fraud
  - utter_frauddetect

## onlinebullying path
* online_bullying
  - utter_onlinebullying

## cybercriminal path
* cybercriminal
  - utter_cybercrimetypes

## crime_type path
* crime_type
  -utter_typedesc

## personalcrime path
* personal_crime
  - utter_personaldesc

## personalcrime path
* personal_crime
  - utter_personaldesc

## propertydesc path
* property_crime
  - utter_propertydesc

## Inchoatecrime path
* Inchoate_crime
  - utter_Inchoatedesc

## Statutory_crime path
* Statutory_crime
  - utter_Statutorydesc

## financial_crime path
* financial_crime
  - utter_financialdesc

## financial_type path
* financial_type
  - utter_financialtypecrime

## deposit path
* deposit
  - utter_deposit

## deposit path
* fraud_types
  - utter_fraudtypes

## cyberexamples path
* cyberexamples
  - utter_cyberex

## mobile_hackings path
* mobile_hacking
  - utter_mobilehacking

## matrimonial_fraudsafety path
* matrimonial_fraudsafety
  - utter_matrimonialfraudsafety

## employment_fraud path
* employment_fraud
  - utter_employmentfraud

## social_media path
* social_media
  - utter_socialmedia

## protect_yourself_cybercrime path
* protect_yourself_cybercrime
  - utter_protectyourself_cybercrimes

## protect_yourself_cybercrime path
* protect_yourself_cybercrime
  - utter_protectyourself_cybercrimes

## childpornography path
* childpornography
  - utter_childpronography

## financialsafety path
* financialsafety
  - utter_financialfraud

## reportyoutube path
* reportyoutube
  - utter_report_youtube

## reportfacebook path
* reportfacebook
  - utter_report_facebook

## reportinsta path
* reportinsta
  - utter_report_instagram

## reporttwitter path
* reporttwitter
  - utter_report_twitter

## reportlinkedln path
* reportlinkedIn
  - utter_report_LinkedIn

## report_whatsapp path
* report_whatsapp
  - utter_report_whatsapp
