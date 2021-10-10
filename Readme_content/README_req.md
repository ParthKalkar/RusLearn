# Requirements

## Table of contents
- [Project description](../README.md)
- [Business Goals and Objectives](../README_buisiness_goals.md)
- Requirements
    - Requirement Analysis and Specifications
        - Features
        - User Stories
    - Quality attributes (non-functional requirements)

- [Design](Readme_content/README_design.md)
- [Architecture](Readme_content/README_arch.md)
- [Code](Readme_content/README_code.md)
---

## Requirement Analysis and Specifications

### Features

| **ID #** | **User Story Title** | **Priority** |
| ----- | ----- | ------ |
| 1.1 | Registration | Must
| 1.2 | Login/Logout | Must
| 1.3 | Change Personal & Privacy Information| Must
| 1.4 | Change Personal & Privacy Information| Must
|1.5 | Tutor subscription tier | Must
| 1.6 | Dashboard |Must
| 1.9 | Word input | Must
| 1.11 | Cards with words | Must
| 1.8 | Share mode/Peer learning | Normal
| 1.10 | Translate mode | Normal
| 1.7 | Subscription |Low
| 2.1 | Flashcard packs Quality Assurance |Low


### User Stories

| **User Type** | **User Story Title** | **User stories** |
| ---- | ---- | ---- |
|Web User | Registration | <ul><li> As a user, I enter my username, password, and email, then I click on the register button and my account is created (stored on database), with which I will be able to login later. </li><li> As a user, I choose a picture from either my local files or a link, then click on submit. Then the picture is set to be my profile picture. </li><li> As a user, I click on “register with Google”, then an authentication page pops up and if I click agree on all terms, I will have my linked account to Google created.</li></ul>
||Login/Logout| As a user, I click on login or logout buttons, then I will arrive at the homepage of my account or log out of it.
||Change Personal & Privacy Information| As a user, I want to have an editing page where I can re-enter my password, name, email, photo,... so that when I click submit, the information is renewed.
||Teacher mode |As a user, I want to have different levels of accessibility so that I can add new words and phrases in order to work as a content creator/teacher
||Dashboard | As a user, I want my dashboard to display: <ol> <li>Profile status: name, subscription type, expire date, change subscription type. </li> <li>Pack names, edit/review buttons.</li><li> Logout button.</li> <li>Learning progress on each pack.</li> </ol>
||Subscription| As a user, I buy premium subscription then I have unlimited access to all packs and cards 
||Share mode/Peer learning| As a user, I click on invite button, and I can specify whom I can have as a co-learner of a pack
||Word input| As a user, I enter either line-by-line or batch inputs of words, then click submit/create then my new words are added to the existing pack or a new pack is created.
||Translate mode| As a user, I click on the “flip” button and the flashcard changes its side, revealing to me the answer/translation of my word.
||Cards with words|<ul><li> As a user I want the app to create cards (Russian word on one side and English word on another side) from my list of worlds </li> <li> As a user, I click on “shuffle” check-box, then the cards are randomly showed when I click “review”</li> <li> As a user I want the app to pronounce words on the card </li></ul>
|Admin| Flashcard packs Quality Assurance|<ul><li> As an Admin, I want to have access to all the flashcard packs and their content for content moderation.</li> <li> As an Admin, I want to be able to flag and delete inappropriate/low-quality public flashcard packs. </li> <li> As an Admin, I want to be able to block users from the platform in case they indulge in in behaviour against the community guidelines (e.g. spam, publication of inappropriate/shocking content…)</li><ul>



## Quality attributes (non-functional requirements)

Quality Attributes
|Characteristics|Sub-Characteristics|Definition
|---|---|---|
|Usability|Accessibility|<ul> <li> Users are divided into creators and subscribers to a pack with their privileges <ul> <li> Owners can review/edit their packs (add/delete words)</li> <li> Subscribers can only review the pack and their progress of learning </li></ul> <li>Premium users can access unlimited packs and words</li></ul>|
|Reliability|Availability|Uptime: 4 nines (99.99%) 
|Reliability|Recoverability | In case of error or bugs, the application should be able to save the user’s profile data and cards with words at the nearest save.
|Performance Efficiency|Time-behavior|<ul><li> Average response time: 0.4s</li> <li>Limit response time: 1s</li></ul>
|Maintainability|Testability|<ul><li> A bug if detected can be fixed within 1 day </li> <li>Code should follow industrial standard specified here: https://www.it-cisq.org/coding-rules/index.htm </li></ul>

