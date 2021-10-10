[![Pylint](https://github.com/ParthKalkar/RusLearn/actions/workflows/pylint.yml/badge.svg)](https://github.com/ParthKalkar/RusLearn/actions/workflows/pylint.yml)
[![Django Tests](https://github.com/ParthKalkar/RusLearn/actions/workflows/django.yml/badge.svg)](https://github.com/ParthKalkar/RusLearn/actions/workflows/django.yml)
[![Deployment](https://github.com/ParthKalkar/RusLearn/actions/workflows/deploy.yml/badge.svg)](https://github.com/ParthKalkar/RusLearn/actions/workflows/deploy.yml)
[![GitHub stars](https://img.shields.io/github/stars/ParthKalkar/RusLearn)](https://github.com/ParthKalkar/RusLearn)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/yegor256/takes/blob/master/LICENSE.txt)
# [RusLearn](http://ruslearn-dev.us-west-2.elasticbeanstalk.com/)

> With RusLearn, we want to provide a large platform built on the idea and learning philosophy of flashcards: Simple and atomic units of knowledge, that have been 
scientifically proven to be one of the most effective learning methods, especially when used in combination with techniques such as spaced repetition. RusLearn saves you the time and 
effort of understanding these learning techniques by implementing everything internally and guiding you completely through your learning experience, with no extra effort on your side except the small bursts 
of focus in the short learning sessions. RusLearn also offers premium tier subscriptions, which offer you further high quality content with the flashcards, such as video, audio, and external links. 
Moreover, you should know that RusLearn offers more than just flashcards for you to review. If you have confidence in your knowledge of a certain subject or language, you can contribute to the platform with your own flashcards and earn money with them! 
A user can select the “tutor” subscription tier, which instead of taking your money, gives you money (depending on how well your flashcard packs are doing, and how popular they are).

In code section you can see more examples and video demo.

![main_ex](./Docs/Demo/MainEx.png)

![main_ex](./Docs/Demo/Main_page.png)
Main page

---
## Table of contents
- Project description
    - [Glossary](https://github.com/ParthKalkar/RusLearn#glossary)
    - [Progress](https://github.com/ParthKalkar/RusLearn#what-we-have-so-far)
    - [Developer's guide](https://github.com/ParthKalkar/RusLearn#developers-guide)
	    - Technical stack
	    - Installation guide
	    - Deployment guide
    - [Authors & Copyright](https://github.com/ParthKalkar/RusLearn#authors)
- [Business Goals and Objectives](Readme_content/README_buisiness_goals.md)
- [Requirements](Readme_content/README_req.md) 
- [Design](Readme_content/README_design.md)
- [Architecture](Readme_content/README_arch.md)
- [Code](Readme_content/README_code.md)

---
## Glossary
- Flashcard: 2 faced cards (represented as cards in the user interface) with one side containing a hint or question about a piece of information and the other side contains the information itself.
- Spaced repetition: Is a memorization technique that uses regular practice of the least memorized content in a certain subject or knowledge area.
- Modification right: The ability to edit/delete the flashcards collection
Sharing functionality: The ability to share the collection of cards among users
- Django: framework sitting between database and front end
REACT: front end framework
- Money-making functionality: Users with packs satisfying certain criteria can enable this functionality to earn money from the subscriptors of these packs.
- Queries: database querying code to retrieve information
- Benchmark: environment to measure performance of testing version/unit of product


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
Make sure you have Node.JS installed:
```commandline
sudo apt-get install npm
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
Once the migrations are done, you will be able to run the backend server locally using:
```commandline
python3 manage.py runserver
```
To run the frontend React server, open the terminal in the `react-app` directory and run:
```
npm start
```

### Deployment guide
You can deploy the website on Amazon Web Services Elastic Beanstalk, by executing the next steps:
1. Make 2 `.zip` files from the source code, the first file should contain the `react-app` directory, the second file should contain all the files except the directory of the first file.
2. Deploy the files to separate Elastic Beanstalk environments.
3. In the React App environment, specify the environment URL of your backend server in main.js.
4. In the Django environment, add the current environment URL in the `ALLOWED_HOSTS` in the `settings.py` file.
---
## Authors:
*[Rafik Hachana](https://github.com/RafikHachana)*, *[Parth Kalkar](https://github.com/ParthKalkar)*, *[Danil Shalagin](https://github.com/danilXX2000)*, *[Truong Nguyen](https://github.com/enestydarealmc)*

## Copyrights:
This is a student project done during the course of SSAD *(Software Systems Analysis and Design)* in *Innopolis University*, *Fall semester 2021*. Therefore, we claim the authority of all source code being used here.
In addition, fair use of this source code can be done within the MIT copyright license
