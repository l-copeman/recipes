# Recipes At Home

## Features

- Each page has a navbar and a footer

### Navbar 

![Navbar](documentation/features/screenshots/header-bg.png)

Navbar has the following links:
- Home page
- Register
- Login
- Logo links to home page 

![Logo](documentation/features/screenshots/logo.png) ![Hover](documentation/features/screenshots/hover.png)

Links that are hovered over are highlighted with black text.

The simplistic design of the navbar is based on the decision to make the use of the webapp easy for the user.

When the app is viewed on smaller screens, the 'Home', 'Register', and 'Log In' links are all hidden within a toggle button. This helps to maintain a clean navbar that is not overcrowded.

- ![Mobile View](documentation/features/screenshots/header-sm.png)

Whichever page is currently active, it is displayed by the relevant link being in black text as opposed to white.

- ![Home Active](documentation/features/screenshots/active-home.png)
- ![Register Active](documentation/features/screenshots/active-register.png)
- ![Login Active](documentation/features/screenshots/active-log-in.png)

When the user is logged in, the navbar looks as follows:

![Navbar User logged in](documentation/features/screenshots/logged-in.png)


### Footer

- Footer for larger screens
  - ![Footer](documentation/features/screenshots/footer-bg.png)
- Footer for smaller screens
  - ![Footer](documentation/features/screenshots/footer-sm.png)

Footer has the following sections:

- About section, with a brief description of the app:
    - ![About](documentation/features/screenshots/about.png)
- Social Links, links to social media platforms:
    - ![Social Links](documentation/features/screenshots/social-links.png)
    - All links are underlined when hovered over
    - All links open the relevant social page in a new window
- Developer:
    - ![Developer](documentation/features/screenshots/developer.png) 
    - The GitHub logo has hover properties and links to the developers GitHub page
    - The link opens GitHub in a new window    


### Home Page

![Home Page](documentation/features/screenshots/home-page.png)

- When the home page is loaded, the user is able to view a list of the recipes.
- 3 recipes cards can be viewed per page.
- Each recipe card shows:
  - Title
  - Excerpt
  - Image
  - Author
  - Servings per recipe
  - ![Recipe Home Page](documentation/features/screenshots/home-recipe.png)
  - When the recipe is hovered over, the text is underlined and the opacity changes
  - The recipe can be clicked anywhere on the card to open the recipe

- If the user has logged in, a message displays which user is signed in, in the top-right corner of the page.
  - ![User logged in](documentation/features/screenshots/signed-in-as.png)

- At the bottom of the page there is a 'NEXT' button, to navigate to the next page of listings
  - ![Next Button](documentation/features/screenshots/next.png)
- After you have left the first page, a 'PREV' button shows, allowing the user to return to the previous page 
  - ![Prev Button](documentation/features/screenshots/prev.png)
- If there are more than two pages to navigate through, both 'NEXT' and 'PREV' buttons are displayed
  - ![Next and Prev Buttons](documentation/features/screenshots/prev-next.png)  
- Both 'NEXT' and 'PREV' buttons have hover properties; background changes to a lighter color and text becomes black  

- For smaller screens, the recipe cards are displayed on top of one another, in a single column
  - ![Mobile Home Page](documentation/features/screenshots/home-sm.png)

- If an image is not uploaded for a recipe, a default placeholder image is shown instead
  - ![Default Image](documentation/features/screenshots/default-image.png)


### Recipe Feature Page

After the user has clicked on a particular recipe card, the recipe opens with a more detailed view. The list of ingredients is shown as well as the method. Below this is the comment section.
![Recipe Feature Page](documentation/features/screenshots/recipe-feature-bg.png)
  - The title is shown in the top-left of the page. 
  - The recipe author and servings per recipe stated below title. 
  - The excerpt is shown below this inside enlarged quotation marks to make the text stand out. 
  - An image is displayed in the top-right of the page. 
  - The ingredients are displayed within a card, next to the method so they can be easily cross-refereneced.
  - The method is written in easy to follow steps. 

For smaller screens, there is no image displayed. This is to stop the screen being overcrowded and allows for easy navigation around the page.
![Recipe feature mobile](documentation/features/screenshots/recipe-feature-sm.png) 

### Comments 

Below each featured recipe there is a comments section. This allows users to leave a comment about the recipe, if they have signed in. Only comments that have been approved by admin will be displayed to all users. The user is able to edit and delete their own comments. 

- If no comments have been left, a message stating this is shown:
![No Comments](documentation/features/screenshots/no-comments.png)
- If messages have been left that are yet to be approved, a message stating this is shown:
![Awaiting approval](documentation/features/screenshots/approval-comments.png)
- If a user is not signed in, they are asked to do so to be able to leave a comment:
![Please sign in](documentation/features/screenshots/please-log-in.png)
- The text `log in` is a link to the sign in page. This text is blue and has hover properties
- When a user is logged in, a personalised form is shown where a comment can be left:
![Comment Form](documentation/features/screenshots/leave-comment.png)
  - A message showing that the maximum characters allowed is 900 is shown
  - The users name is shown in the "Leave a comment, from `user`:" message
  - The submit button can be clicked to send the comment
  - The submit button has hover properties
- A message is displayed at the top of the page when a message has been left:
  ![Comment Submitted](documentation/features/screenshots/comment-submitted.png)
- If the form is submitted empty, a validation message is shown:
  ![Form Validation](documentation/features/screenshots/comment-validation.png)
- When a comment has been left, only the user is able to view the comment until it is approved by admin
![Display comment](documentation/features/screenshots/display-comment-wait.png)
  - The author of the comment is shown:
  ![Author](documentation/features/screenshots/user-wrote.png)
  - The time and date that the comment was left is shown:
  ![Time and Date](documentation/features/screenshots/date-time.png)
  - A message showing the comment is awaiting approval is shown:
  ![Awaiting approval](documentation/features/screenshots/awaiting-approval.png)
- The edit and delete buttons only show if the comment is from the user
- Both buttons have hover properties
- If the user clicks the edit button, the comment can be edited
- The message to be edited populates the comment form ready to be edited
- The cursor is focused on the comment form, for good UX practice
- What was the `Submit` button on the comment form, is changed to `Update`:![Update](documentation/features/screenshots/update.png)
- When the message is updated, a message is displayed at the top of the page:
![Comment Updated](documentation/features/screenshots/comment-updated.png)
- The user is able to delete one of their comments, with the delete button
- After the initial click, a modal is shown asking for confirmation that the comment should be deleted:
![Delete Modal](documentation/features/screenshots/delete-comment.png)
- If the user clicks delete, the message is deleted and a message is displayed at the top of the page:
![Delete Message](documentation/features/screenshots/comment-deleted.png)
- If the user clicks cancel, they are taken to the home page.
- When a comment has been approved by the admin, this is how it will be displayed to other users:
![Displayed Message](documentation/features/screenshots/approved-comment.png)


### Accounts

To be able to utilise the comment section, users are required to have an account.

#### Log In Page

![Log In](documentation/features/screenshots/sign-in.png)

The log in page allows users who already have an account to log in with their username and password.
  - If a user doesnt have an account yet, there is a link to register:![Register Link](documentation/features/screenshots/no-account-sign-up.png)
  - This `Sign Up` text is in blue and has hover properties.
  - If the `Username` field is left empty, a validation message is shown:![Validation Username](documentation/features/screenshots/username-validation.png)
  - If the `Password` field is left empty, a validation message is shown:![Validation Password](documentation/features/screenshots/password-validation.png)
  - If the username and password have been entered incorrectly, a message is shown:![Incorrect Details](documentation/features/screenshots/incorrect-details.png)
  - After successfully logging in, the user is taking to the home page, where a message is displayed:
  ![Sign In Message](documentation/features/screenshots/success-sign-in.png)

#### Register Page

![Register Page](documentation/features/screenshots/sign-up.png)

The sign up page allows users to register an account.
  - If the user already has an account, they can navigate to the sign in page:![Sign In](documentation/features/screenshots/already-account.png)
  - This `Sign In` text is in blue and has hover properties.
  - If the user leaves the username blank, a validation message is shown:![Username Validation](documentation/features/screenshots/username-valid-up.png)
  - If the user enters a username that already exists, a message is shown:![Username Exists](documentation/features/screenshots/user-exists.png)
  - If the password doesn't match the criteria shown, messages are shown:
    -![Password Validation](documentation/features/screenshots/password-short.png)
    -![Password Validation](documentation/features/screenshots/entirely-numeric.png)
  - After successfully creating an account, the user is logged in and shown a message:![Success Sign In](documentation/features/screenshots/sign-register.png)


#### Log Out Page


![Log Out Page](documentation/features/screenshots/sign-out.png)

When a user is logged in, they are able to log out via the log out page. The Log Out page ask for confirmation that the user wishes to log out.
 - Both buttons have hover properties. 
 - If they select `Sign Out`, they are signed out, returned to the home page and shown a successful log out message:
 ![Success Log Out](documentation/features/screenshots/success-sign-out.png)
 - If they select `Cancel`, they are returned to the home page.
