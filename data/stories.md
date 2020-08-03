## welcome
* greet
  - utter_greet

## story 2
* goodbye
  - utter_goodbye

## story 3
* bot_challenge
  - utter_iamabot

## story 4
* greet
  - utter_greet
* deny
  - utter_crimelist
* affirm
  - utter_iamabot

## story 5
* greet
  - utter_greet
* affirm
  - utter_ask_crime_type
* say_crime_type{"type_of_crime":"Content related to online sexual abuse"}
  - slot{"type_of_crime":"Content related to online sexual abuse"}
  - action_confirm_type

## story 6
* affirm_content_crime{"content_crime_confirmation":"True"}
  - content_crime_form  
  - form{"name":"content_crime_form"}
  - form{"name":null}
  - utter_thanks

## story 7
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

## sexualexplicit path
* sexualexplicit
   - utter_sexualexplicitawar

## definition_sexualexplicit path
* defsexualexplicit
   - utter_definesexualexplicit

##sexualobscenity path
* sexualobscenity
   - utter_sexualobscenityawar

## threatmeasures path
* threatmeasures
  - utter_threatmeasures

## hatredandthreat path
* hatredandthreat
  - utter_hatredandthreat

## onlinegambling path
* onlinegambling
  - utter_onlinegambling

## onlineprostitution path
* onlineprostitution
  - utter_onlineprostitution

## rape
* rape
  - utter_rape

## rape_meaning
* rape_meaning
  - utter_rape_meaning

# childponography
* childponography
  - utter_childponography

## defonlineharassment path
* defonlineharassment
  - utter_desconlineharss

## typesonlineharass path
* typesonlineharass
  - utter_typesonlineharass

## hatespeech path
* hatespeech
  - utter_hatespeech

## Cyberbullying path
* Cyberbullying
  - utter_Cyberbullying

## RevengePorn path
* RevengePorn
  - utter_RevengePorn

## Dogpiling path
* Dogpiling
  - utter_Dogpiling

## Trolling path
* Trolling
  - utter_Trolling

## Catfishing path
* Catfishing
  - utter_Catfishing

## Swatting path
* Swatting
  - utter_Swatting

## Doxing
* Doxing
  - utter_Doxing

## Impersonation path
* Impersonation
  - utter_Impersonation

## Cyberstalking path
* Cyberstalking
  - utter_Cyberstalking

## reporthatespeech path
* reporthatespeech
  - utter_reporthatespeech

## reportcyberbullying path
* reportcyberbullying
  - utter_reportcyberbullying

## helpbulled path
* helpbulled
  - utter_helpbulled

## parentssupport path
* parentssupport
  - utter_parentssupport

## punishments path
* punishments
  - utter_punishments

## security path
* security
  - utter_security

## reportrevenge path
* reportrevenge
  -utter_reportrevenge

## hacking path
* hacking
  - utter_hacking

## hackedphone path
* hackedphone
  - utter_hackedphone

## ifhacked path
* ifhacked
  - utter_ifhacked

##  wayshacked path
* wayshacked
  - utter_wayshacked

## preventhack path
* preventhack
  - utter_preventhack

## reporthacked path
* reporthacked
  - utter_reporthacked

## internet banking path 1
* internetbankingfraud 
  - utter_internetbankingfraud

## internet banking path 2
* internetbanking_safely 
  - utter_internetbanking_safely 

## e wallet 1
* Ewallet_fraud
  - utter_Ewallet_fraud

## e wallet 2
* ewallet_precautions 
  - utter_ewallet_precaution 

## e wallet 3 
* ewallet_report 
  - utter_ewallet_report

## atm path 1
* ATM_Creditcard_report
  - utter_ATM_Creditcard_report

## atm path 2
* ATM_Creditcard_precautions
  - utter_ATM_Creditcard_precautions 

## job fraud 1
* jobfraud_precautions 
  - utter_jobfraud_precautions

## job fraud 2
* jobfraud_report 
  - utter_jobfraud_report 

## matrimonial 1 
* matrimonialfraud_precautions 
  - utter_matrimonialfraud_precautions 

## matrimonial 2
* matrimonialfraud_report
  - utter_matrimonialfraud_report 

## fraud call 1
* fraudcall_precautions 
  - utter_fraudcall_precuations 

## fraud call 2
* fraudcall_report 
  - utter_fraudcall_report 

## story 86
* desc_cryptocurrency 
  - utter_crypto_desc

## story 87
* help_cryptocurrency 
  - utter_crypto_help
  - utter_crypto_safety

## story 88 
* email_hacking 
  - utter_email_hacking
  - utter_email_safety 

## story 89
* email_safety 
  - utter_email_safety

## interactive_story_1
* onlinegambling
    - utter_onlinegambling
* reportcyberbullying
    - utter_reportcyberbullying
* ifhacked
    - utter_ifhacked

## interactive_story_2
* reportcyberbullying
    - utter_reportcyberbullying
* Ewallet_fraud
    - utter_Ewallet_fraud

## interactive_story_3
* email_phishing
    - utter_email_phishing
* security
    - utter_security
* sexualobscenity
    - utter_sexualobscenityawar
* reportcyberbullying
    - utter_reportcyberbullying

## interactive_story_4
* ATM_Creditcard_precautions
    - utter_ATM_Creditcard_precautions
* ATM_Creditcard_report
    - utter_ATM_Creditcard_report
* stop
