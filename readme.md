# AI Email Manager

SI 568 project documentation

Charles Song

## Introduction

The overwhelming amount of emails is one of the main sources of stress for many students in the university. 
While some emails contain important notifications and interesting events, others are less significant. 
It can be time-consuming for students to open each email individually, 
but students also do not want to miss important information. 
The purpose of this project is to build an application that utilizes the ChatGPT API to manage inbox emails efficiently. 
The application will read the email in the gmail inbox using Gmail API, then
categorize them into different categories: To-dos, events, notifications, and others. 

## How to use

### Get Gmail API

Please refer to [Using OAuth 2.0 to Access Google APIs | Authorization](https://developers.google.com/identity/protocols/oauth2) for how to get a Gmail OAuth 2.0 API.

You can follow this guide to run a sample to test Gmail API is successfully implemented: [Python quickstart | Gmail | Google Developers](https://developers.google.com/gmail/api/quickstart/python). 
If you run the sample, there should be a “token.json” file generated, 
put the AI_Email_Manager.py in the same directory.

### Modify the code and run it

In the function `get_emails`, 
change `max_results` to how many emails you want the AI email manager to read. 
Note: Don’t put a big number, or it will be out of the ChatGPT capacity.

Run the code. 
If successful, you should get a “Success” prompt and a file “email debrief.txt” will be generated. 
Read the debrief, now we have a debrief of our inbox emails!


## Output example

Subject: SEAS & PitE Students: Please Do Not Scab

To-Do. This email is asking SEAS and PitE students to refuse the offer of taking on GSI responsibilities or any labor withheld by GEO during the ongoing strike. The email defines what scabbing is and encourages students to support their fellow SEAS community members by not scabbing. The email also suggests ways in which students can show solidarity such as joining fellow students on the picket line or signing the open letter.

&nbsp;

Subject: [GEO] Reminder: GMM tonight at 7pm in Angell

Category: Event

Summary: This is a reminder email for the GEO general membership meeting happening tonight at 7 pm in Angell Hall Auditorium A. The email contains a link to RSVP for Zoom details, and a FAQ document is attached for new members.

&nbsp;

Subject: ✅ Annual UMSI Student Survey - Win a $50 UMSI Store Gift Card

Category: Other

Summary: The email is from the Office of Academic and Student Affairs (OASA) about the Annual UMSI Student Survey which takes only 10 minutes to complete. The students who complete the survey will be eligible to win a $50 UMSI Store gift card.

&nbsp;

Subject: SEAS Current Student Survey - Chance to Win $100!

To-Do: SEAS Current Student Survey - Chance to Win $100!

&nbsp;

Subject: Minutes from Masters Caucus 4/3 meeting

Category: Other

Summary: The email provides the minutes from the Masters Caucus meeting and highlights the Masters Caucus Compensation Survey. The email also discusses relevant topics for Masters students, such as compensation and hiring practices. Additionally, the email mentions some recent bargaining wins and encourages involvement in the Masters Caucus.

&nbsp;

Subject: Re: GHGRP Vulcan 0403

To-Do: Finalizing a report and scheduling a meeting on Wednesday.
