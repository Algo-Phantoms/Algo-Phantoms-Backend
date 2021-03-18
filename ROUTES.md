# Routes

-   The `admin/` path takes you to the admin console

-   The default path includes the urls for the core app

-   The `quiz/` path contains urls for the quiz app. It lets you view the quiz/quizzes.

    -   The `quiz/random/<str:topic>/` path shows a random question from the provided `topic` in the url

    -   The `quiz/question/<str:topic>/` path shows a question from the particular quiz for the provided `topic` in the url

-   `accounts` has urls for Django all-auth

-   `rest-auth/` contains the urls for Django Rest Framework

    -   `rest-auth/login/` is DRF's login view

    -   `rest-auth/registration/` is DRF's registration view

    -   `rest-auth/account-confirm-email/` is DRF's verification email view
