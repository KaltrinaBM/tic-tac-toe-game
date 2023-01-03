<h1 align="center">Tic Tac Toe Game</h1>

This is a Tic Tac Toe game, where the player can play against the computer. Player will have to enter a name to play the game. Computer will play random moves to beat the player. The player will have the symbol 'X' and the computer will have the symbol 'O'. The scores will be updated, so the player can track the scores.

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to play easily with the computer and enter my name.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the game and use simple options of the game.
        3. As a First Time Visitor, I want to see scores if I win any games.

    -   #### Frequent User Goals
        1. As a Frequent User, I want to check to see if the game is updated with different options.

*   ### Flowcharts

    -   Flowchart below explains how the game functions and has been made using [Lucid Charts](https://www.lucidchart.com/pages/)

    ![Flowchart](/images/flowchart.png)

## Technologies Used

### Languages Used

Python

### Frameworks, Libraries & Programs Used

1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
2. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
3. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
4. [Heroku](https://www.heroku.com/) 
    - To deploy the program to public
5  [Lucid Charts](https://www.lucidchart.com/pages/)
    - To create the flowchart
    
## Features

-   Responsive on all device sizes

### Existing Features

- __The instructions to play the game__

  - The heading and the logo are easy to see when user enter the page.

![Instructions](/images/instructions.PNG)

- __Play or Quit the game__

  - This section has the question if player wants to continue and play by selecting 'Y' or quit the game by selecting 'N'.

![Play or Quit](/images/playorquit.PNG)

- __Displaying the board__

  - The game and a reference board will be displayed once the player selected yes, so the player can start.

![Board](/images/board.PNG)

- __Playing the game__
   - Playing the game against cumputer where the player can type any blank spots and computer will select spots randomly.

![Playing](/images/playing.PNG)

- __Displaying the Winner__
   - Displaying the winner of the game after each game won.

![Winner](/images/win.PNG)

- __Displaying the Tie__
   - Displaying when the game is Tie.

![Tie](/images/tie.PNG)

### Features Left to Implement

- To have an option so user can select which symbol wants to have and to refactor the code.

## Testing

The following cases were carried out to ensure that the program is functioning as expected: ALL PASSED

[PEP8 CI Python Linter](https://pep8ci.herokuapp.com/#)

#Results:
All clear, no errors found

The code has been pasted and came back with no errors.

Features

All features have been tested manually to see if all the inputs work as expected.

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to play easily with the computer and enter my name.

        Upon entering the site, the user will see the instructuons and has to enter the name, then select 'Y' to play, so the board will be displayed game starts.

    2. As a First Time Visitor, I want to be able to easily navigate throughout the game and use simple options of the game.

        It is easy to navigate throughout the site, there reference board makes it easy to play the game with the NumLock keyboard.

    3. As a First Time Visitor, I want to see scores if I win any games.

        The scores will be incremented for each player once a game is won.

-   #### Returning Visitor Goals

    1. As a Frequent User, I want to check to see if the game is updated with different options.
       
       In the future, game should have more options for the player to select.

### Further Testing

-   The Website was tested on Google Chrome and Internet Explorer.
-   The website was viewed on a variety of devices such as Desktop, Laptop, Andorid phones.
-   A large amount of testing was done to ensure that all functions are working as intended.
-   Family members were asked to review and play the game to point out any bugs and/or user experience issues.

### Known Bugs

-   There were bugs where scores were not updated accordingly, but that is fixed by calling the function when the game is won. Also, the code to check if there are 3 same symbols vertically, horizontally and diagonally, didn't work properly, and it is now fixed by updating keyboard keys accordingly. However, the code for checking possible wins has to be refactored. 

### Unfixed Bugs

-   There are features that could not be implemented due to the deadline.

## Deployment

There is just one branch of this project and the deployed version of this site is the most current version in the repository. The live site can be accessed via this link here - [Tic Tac Toe Game]()

### How to deploy

### Heroku
To deploy this page to Heroku from its [GitHub repository](https://github.com/KaltrinaBM/tic-tac-toe-game) the following steps were taken:

- Log into or register new account at [Heroku](https://www.heroku.com/).
- Click the button **New** in top right corner of the dashboard.
- From the drop-down menu select **Create new app**.
- Enter your apps name in the first field and select your region.
- Click on **Create App** if you are happy with your choices.
- Once you the app is made you will see yourself within **Deploy** tab. Press on **Settings** tab.
- Once you are in the **Settings** tab scroll down till you find **Config Vars**.
- Press the button **Reveal Config Vars** and for 'KEY' field, type in PORT and for the value field type in '8000'.
Press the **Add** button.
- Scroll down to **Buildpacks**. Click the button **Add buildpack** and select 'python'. Do the same step and add 'node.js'.
**PYTHON MUST BE ON TOP OF THE BUILDPACKS. IF IN YOUR CASE NODE.JS IS FIRST, CLICK AND DRAG PYTHON TO TOP AND SAVE.**
- Return back to the **Deploy** tab. From the deployment method, select 'Github' as the deployment.
- You will be asked to connect your github account. Confirm and proceed.
- Search for your repository name and connect.
- Once that is done and successfully connected, select how you want to push updates from the following options.

  _Clicking **Enable Automatic Deploys**. This will update once you push updates to your Github._

  _Selecting the correct branch for deployment from drop-down menu and pressing **Deploy Branch** button. This will have to be done everytime manually._

- You will see a message "The app was successfully deployed" when the app is built with python and all the depencencies
- Click on view and you will see the deployed site

## Credits

- [Google](https://www.google.com/)- Different articles.
- [W3 Schools](https://www.w3schools.com/) - Learned additional things regarding the questions or errors.
- [Stack Overflow](https://stackoverflow.com/) - The first webpage displaying when Googling errors or questions.


### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.