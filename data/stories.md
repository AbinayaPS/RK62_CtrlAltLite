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

## online bullying path
* online_bullying
  - utter_onlinebullying

## cyber criminal path
* cybercriminal
  - utter_cybercrimetypes

## crime type path
* crime_type
  - utter_typedesc

## personal crime path
* personal_crime
  - utter_personaldesc

## personal crime path
* personal_crime
  - utter_personaldesc

## property desc path
* property_crime
  - utter_propertydesc

## Inchoate crime path
* Inchoate_crime
  - utter_Inchoatedesc

## Statutory crime path
* Statutory_crime
  - utter_Statutorydesc

## financial_crime path
* financial_crime
  - utter_financialdesc

## financial type path
* financial_type
  - utter_financialtypecrime

## deposit path
* deposit
  - utter_deposit

## deposit path 2
* fraud_types
  - utter_fraudtypes

## cyberexamples path
* cyberexamples
  - utter_cyberex

## mobile hackings path
* mobile_hacking
  - utter_mobilehacking

## matrimonial fraudsafety path
* matrimonial_fraudsafety
  - utter_matrimonialfraudsafety

## employment fraud path
* employment_fraud
  - utter_employmentfraud

## social media path
* social_media
  - utter_socialmedia

## protect yourself cybercrime path
* protect_yourself_cybercrime
  - utter_protectyourself_cybercrimes

## protect yourself cybercrime path
* protect_yourself_cybercrime
  - utter_protectyourself_cybercrimes

## child pornography path
* childpornography
  - utter_childpronography

## financial safety path
* financialsafety
  - utter_financialfraud

## report youtube path
* reportyoutube
  - utter_report_youtube

## report facebook path
* reportfacebook
  - utter_report_facebook

## report insta path
* reportinsta
  - utter_report_instagram

## report twitter path
* reporttwitter
  - utter_report_twitter

## report linkedln path
* reportlinkedIn
  - utter_report_LinkedIn

## report whatsapp path
* report_whatsapp
  - utter_report_whatsapp

## sexual explicit path
* sexualexplicit
   - utter_sexualexplicitawar

## definition sexualexplicit path
* defsexualexplicit
   - utter_definesexualexplicit

## sexual obscenity path
* sexualobscenity
   - utter_sexualobscenityawar

## threatmeasures path
* threatmeasures
  - utter_threatmeasures

## hatred and threat path
* hatredandthreat
  - utter_hatredandthreat

## online gambling path
* onlinegambling
  - utter_onlinegambling

## online prostitution path
* onlineprostitution
  - utter_onlineprostitution

## rape path 
* rape
  - utter_rape

## rape meaning path
* rape_meaning
  - utter_rape_meaning

## child pornography
* childponography
  - utter_childponography
  
## def online harassment path
* defonlineharassment
  - utter_desconlineharss

## types onlineharass path
* typesonlineharass
  - utter_typesonlineharass

## hate speech path
* hatespeech
  - utter_hatespeech

## Cyber bullying path
* Cyberbullying
  - utter_Cyberbullying

## Revenge Porn path
* RevengePorn
  - utter_RevengePorn

## Dog piling path
* Dogpiling
  - utter_Dogpiling

## Troling path
* Trolling
  - utter_Trolling

## Cat fishing path
* Catfishing
  - utter_Catfishing

## crime swatting path
* Swatting
  - utter_Swatting

## crime Doxing path 
* Doxing
  - utter_Doxing

## crime impersonation path
* Impersonation
  - utter_Impersonation

## Crime cyberstalking path
* Cyberstalking
  - utter_Cyberstalking

## report hate speech path
* reporthatespeech
  - utter_reporthatespeech

## report cyber bullying path
* reportcyberbullying
  - utter_reportcyberbullying

## helping bulled path
* helpbulled
  - utter_helpbulled

## parents support path
* parentssupport
  - utter_parentssupport

## punishment path
* punishments
  - utter_punishments

## crime security path
* security
  - utter_security

## report revenge path
* reportrevenge
  -utter_reportrevenge

## crime hacking path
* hacking
  - utter_hacking

## crime hackedphone path
* hackedphone
  - utter_hackedphone

## if hacked path
* ifhacked
  - utter_ifhacked

## crime way shacked path
* wayshacked
  - utter_wayshacked

## prevent hack path
* preventhack
  - preventhack

## report hacked path
* reporthacked
  - utter_reporthacked  

## crime internet banking
* internetbankingfraud
  - utter_internetbankingfraud

## internet banking safely
* internetbanking_safely
  - utter_internetbanking_safely

## e wallet fraud
* Ewallet_fraud
  - utter_Ewallet_fraud

## e wallet examples
* Ewallet_example
  - utter_Ewalletloot_example

## e wallet precautions
* ewallet_precautions
  - utter_ewallet_precaution

## e wallet report
* ewallet_report
  - utter_ewallet_report

## ATM Credit card precautions
* ATM/Creditcard_precautions
  - utter_ATM/Creditcard_precautions

## ATM Credit card report
* ATM/Creditcard_report
  - utter_ATM/Creditcard_report

## job fraud precautions
* jobfraud_precautions
  - utter_jobfraud_precautions

## job fraud report path
* jobfraud_report
  - utter_jobfraud_report

## matrimonial fraud precautions
* matrimonialfraud_precautions
  - utter_matrimonialfraud_precautions
  
## matrimonial report 
* matrimonialfraud_report 
  - utter_matrimonialfraud_report
  
## fraud call precaution path 
* fraudcall_precautions
  - utter_fraudcall_precuations

## fraud call report
* fraudcall_report
  - utter_fraudcall_report

## crypto currency path 
* desc_cryptocurrency 
  - utter_crypto_desc

## crypto path 2
* help_cryptocurrency 
  - utter_crypto_help
  - utter_crypto_safety

## email path 
* email_hacking 
  - utter_email_hacking
  - utter_email_safety 

## email 2 
* email_safety 
  - utter_email_safety
