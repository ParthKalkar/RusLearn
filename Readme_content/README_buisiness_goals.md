# Business goals

## Table of contents
- [Project description](../README.md)
- Business Goals and Objectives 
    - [Business Relevance](https://github.com/ParthKalkar/RusLearn/blob/main/Readme_content/README_buisiness_goals.md#business-relevance)
    - [Roles and responsibilities](https://github.com/ParthKalkar/RusLearn/blob/main/Readme_content/README_buisiness_goals.md#stakeholders)
    - [Architectural drivers](https://github.com/ParthKalkar/RusLearn/blob/main/Readme_content/README_buisiness_goals.md#architectural-drivers)
        - Business goals
        - Constraints

- [Requirements](./README_req.md) 
- [Design](./README_design.md)
- [Architecture](./README_arch.md)
- [Code](./README_code.md)
---

## Business relevance:
#### Competitors
Flashcards app (like Anki, Quizlet, Memrise,...), and platforms for earning through making flashcards (like Stuvia, ProProfs, …).
#### Challenge
- Many similar apps on the market, but none of them provide tutor roles, or features like batch input when creating flashcards (input with multiple lines of words)
- Most of the learning packs created serve the community for free, the owner gains nothing but popularity
#### How we solve
- Provide batch input for users
- Enable money-making functionality for users who reach certain criteria (similar to Spotify, Youtube...)
#### What make us unique
- Financial-driven motivation: there will be two types of users: those who learn and those who create to not just share but earn money.
- Since people actually pay to subscribe to a pack, the community review of a pack is improved as well as the quality of it.
#### Objectives
- Create a marketed version of quizlet
- Solve some tiny user experience details the apps on market is having 

## Stakeholders:
| **Stakeholder’s Name** | **Roles** | **Responsibilities** |
| ----- | ----- | ------ |
| **Tester** | - Testing functionalities of the application - Set up the benchmark environment - Run the functionality | Note down the results and report bugs 
| **Developers** | Develop the application | Be aware of all user stories, FR (functional requirement), and NFR (non-functional requirement) - Apply the proper technology to develop each submodule - Test, debug repeat, comment the code - Define and document requirements - Provide information, estimates and feedback to the Project manager
|**Project Manager**|Planning, executing, monitoring, controlling, and closing out the project.|Accountable for the entire project scope - The project resource and budget - The success or failure of the project
|**Product Owner** | Set deadlines, financial management, propose requirements, validate project | Schedule delivery deadline (hard/soft) - Describe what customers expect - Present the deliveries to the customer - Handle the budget/bargaining - Validate if each delivery matches customer’s needs: validation goals
|**Investor / Client** |Pay, experience, require |State out core ideas of the product, how it should look, how it should function. - Be on time on payment - Confirm if each delivery satisfies them.
---

## Architectural drivers
### Business goals:

- Minimum Viable Product - the earliest version of the built product. Getting the first iteration done. 

- Private Beta Launch - Once the MVP is done, we’ll need to get some feedback and this can be done by offering a limited amount of users access to the products via a private beta. 

- Redesign/Iteration - The design, feedback, iterate cycle is one that should be ongoing throughout the development process. However, when it comes to business goals, the first redesign and iteration need to happen immediately after the feedback from the private beta users.

- Public Beta Launch - Releasing the app for a more wide range of users after confirming that the database and server can handle the load 

- Major Milestone - After the public beta launch, it would be important to continue the redesign/feedback/iteration cycle for a while as you figure out how to best refine your product. Within some time of launching, one of the business goals is to hit at least one major milestone. That milestone is to focus on traction and monetize the app

- Attract Investment - The first investment round should be done after checking all the previous business goals 

### Constraints:

- Schedule mandates:

    Finish within 2 months, before the deadline of SSD
Weekly meeting to check the progress

- Budget limitations:

    - Server renting
    - License registration fees

- Cost of Ownership:

    Expenditure of capital must be returned within 1 year from revenue of subscription

- Database constraints:

    Enough to serve, for now, 1000 users and scalable to 5000 if needed without spending more

- Dataset constraints: 

    Need for collecting a handsome amount of words and phrases to be translated and used 

- Team experience: 

    The team lacks some prior working experience together 

- Technology Stack: 

    Not enough experience in the tech stack that will be used for the development 

