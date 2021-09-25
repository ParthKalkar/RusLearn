# [RusLearn](http://ruslearn-dev.us-west-2.elasticbeanstalk.com/)
[![Pylint](https://github.com/ParthKalkar/RusLearn/actions/workflows/pylint.yml/badge.svg)](https://github.com/ParthKalkar/RusLearn/actions/workflows/pylint.yml)
[![Deployment](https://github.com/ParthKalkar/RusLearn/actions/workflows/deploy.yml/badge.svg)](https://github.com/ParthKalkar/RusLearn/actions/workflows/deploy.yml)

With RusLearn, we want to provide a large platform built on the idea and learning philosophy of flashcards: Simple and atomic units of knowledge, that have been 
scientifically proven to be one of the most effective learning methods, especially when used in combination with techniques such as spaced repetition. RusLearn saves you the time and 
effort of understanding these learning techniques by implementing everything internally and guiding you completely through your learning experience, with no extra effort on your side except the small bursts 
of focus in the short learning sessions. RusLearn also offers premium tier subscriptions, which offer you further high quality content with the flashcards, such as video, audio, and external links. 
Moreover, you should know that RusLearn offers more than just flashcards for you to review. If you have confidence in your knowledge of a certain subject or language, you can contribute to the platform with your own flashcards and earn money with them! 
A user can select the “tutor” subscription tier, which instead of taking your money, gives you money (depending on how well your flashcard packs are doing, and how popular they are).

## Description:
In its current stage, RusLearn is a web-application that accompanies users on the journey of learning the Russian language by:
- Applying flashcards memorizing technique
  
- Offering both standard and community-based flashcard packs.
  
- Offering premium subscriptions besides the free plans.
  
The initial idea of RusLearn stems from the following problems:
- The shortage of similar applications on the market
  
- The similar applications don't offer the same set of features
- Costly subscription that can't be afforded by students.

In the long-term, RusLearn might extend into a multi-platform learning application, with support for many languages.

## Link to the project's artifacts:
[Descriptions](https://docs.google.com/document/d/1xzDPuQek72qCGHcejrLsAYMtsXDgOepC/edit?usp=sharing&ouid=110717885064894218528&rtpof=true&sd=true)

## Developer's guide
RusLearn is open-source. Anyone is welcome to contribute given that they follow our [code of conduct](./CODE_OF_CONDUCT.md).
### Technical stack
The platform is mainly built around a *Django* backend server, that connects the frontend *React.js*
server to a *PostgreSQL* database using a RESTful JSON API. 


The platform also uses other 3rd party services such as:
- *The PayPal API*: used for payouts to tutors on the platform.
- *The Stripe API*: used to receive student monthly subscription payments.
- *Google Firebase Authentication*: Used to integrate with Google accounts.

### Installation guide (*Debian Linux environment*)
First, clone the GitHub repository in your directory of choice:
```commandline
git clone git@github.com:ParthKalkar/RusLearn.git
```
Make sure you have Python installed:
```commandline
sudo apt-get install python3 python3-pip virtualenv
```
In the project's directory, create a Python virtual environment and activate it:
```commandline
virtualenv venv && source venv/bin/activate
```
Now install all the Python dependencies:
```commandline
pip3 install -r requirements.txt
```
To migrate the database and create the database tables:
```commandline
python3 manage.py makemigrations && python3 manage.py migrate
```
Once the migrations are done, you will be able to run the server locally using:
```commandline
python3 manage.py runserver
```
---
## Authors:
*[Rafik Hachana](https://github.com/RafikHachana)*, *[Parth Kalkar](https://github.com/ParthKalkar)*, *[Danil Shalagin](https://github.com/danilXX2000)*, *[Truong Nguyen](https://github.com/enestydarealmc)*

## Copyrights:
This is a student project done during the course of SSAD *(Software Systems Analysis and Design)* in *Innopolis University*, *Fall semester 2021*. Therefore, we claim the authority of all source code being used here.
In addition, fair use of this source code can be done within the MIT copyright license
