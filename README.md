# ExpenseMonitor
ExpenseMonitor
The efficient solution for managing and tracking your expenses on the go

Team:

Oluwasemilogo Owolabi: Front End Designer

Owolabi Oluwadamilola: UI Designer

Yusuf Muibi: Back End Designer

Technologies

To complete the ExpenseTracker project, the following technologies will be necessary:
Python
Flask (Python web framework)
HTML
CSS
JavaScript
SQLite (lightweight database)
Git (version control)
A code editor (e.g., Visual Studio Code, Sublime Text)
Web browser for testing and debugging
Backend:

Flask: Flask is a lightweight, flexible Python web framework that is easy to learn and well-suited for building small to medium-sized web applications. An alternative option could have been Django, another popular Python web framework. However, Django is more opinionated, comes with more built-in features, and has a steeper learning curve compared to Flask. Since ExpenseTracker is a relatively simple app, Flask's minimalistic approach and ease of use made it a better choice for this project.




Frontend:

JavaScript: JavaScript is the standard language for building interactive web applications and will be used for handling user interactions and making API calls in ExpenseTracker. An alternative could have been using a JavaScript framework or library like React or Vue.js. While these frameworks offer more advanced features and better organization for larger-scale applications, they also introduce additional complexity and a steeper learning curve. For a relatively simple app like ExpenseTracker, using plain JavaScript might be a more straightforward approach, especially for developers new to web development.
Challenge
The ExpenseTracker project aims to solve the problem of efficiently and conveniently tracking and managing personal expenses. Whether managing daily expenses, planning a budget, or analyzing spending habits, having an easy-to-use expense tracker app can be incredibly helpful.
However, it's important to note that the ExpenseTracker project will not solve more complex financial management tasks like investment tracking or advanced budgeting features. It is primarily designed as a straightforward tool for basic expense tracking.
The primary users and beneficiaries of the ExpenseTracker app will be:
Individuals: People who want to track their daily expenses and better understand their spending habits.
Families: Households looking to manage and track family expenses and budgets.
Students: Individuals who need to manage limited budgets and track spending during their studies.
While the ExpenseTracker app itself is not dependent on a specific locale, the usefulness and accuracy of the app will depend on the user diligently recording their expenses.




Risks
Technical Risks:
Database Availability and Reliability: The ExpenseTracker app relies on SQLite for storing user expense data. If the database encounters issues such as data corruption or connectivity problems, it could directly impact the app's functionality and reliability.
Safeguards: Implement error handling and backup mechanisms in case of database failures, such as regular backups and data validation.
Alternative: Explore using other lightweight databases like PostgreSQL or MySQL for more robust data handling.
Cross-Browser Compatibility: Since the app will be web-based, ensuring consistent behavior and rendering across different web browsers and devices is essential.
Safeguards: Thoroughly test the app on various popular browsers and devices during development and implement cross-browser compatibility techniques (e.g., vendor prefixes, feature detection, polyfills).
Alternative: Consider building a native mobile app instead of a web app to ensure a more consistent experience across devices, but at the cost of increased development complexity and platform-specific implementations.
Non-Technical Risks:
Competitive Market: Expense tracker apps are relatively common, and numerous alternatives already exist in the market.
Strategies: Conduct market research to identify unique selling points and differentiate ExpenseTracker from competitors (e.g., better user experience, additional features, targeted marketing).
**Explore potential partnerships or integrations with other financial management services to increase visibility and reach.
Data Privacy and Security: As a financial app handling expense data, it's crucial to ensure user data privacy and security.
Strategies: Implement robust security measures (e.g., encryption, secure communication protocols, access controls) and follow best practices for data privacy and protection.
**Clearly communicate data handling policies and obtain necessary user consents.
By proactively identifying and addressing these risks, the ExpenseTracker project can better mitigate potential issues and increase its chances of success.
Infrastructure
Branching and Merging Strategy
For the ExpenseTracker project, our team will follow the Git Flow branching model, which is a popular and effective strategy for managing code changes and releases. Here's how it will work:
Main Branch: The main branch will always represent the latest production-ready code.
Development Branch: A long-lived develop branch will be used for ongoing development and integration of new features.
Feature Branches: Whenever a new feature needs to be implemented, a new branch will be created from the develop branch with a descriptive name (e.g., feature/expense-tracker). Development work for that feature will happen on this branch.
Merging Feature Branches: Once a feature is completed and tested, a pull request will be created to merge the feature branch into the develop branch. This will trigger a code review process, and after approval, the changes will be merged into develop.
Release Branches: When it's time for a new release, a release branch will be created from develop. This branch will be used for final testing, documentation updates, and any last-minute fixes.
Merging Release Branches: After thorough testing and approval, the release branch will be merged into both main and develop branches, representing the new production release and the starting point for future development, respectively.
This branching strategy promotes code stability, allows for parallel development, and facilitates code reviews and testing before merging into the main codebase.
Deployment Strategy
For deployment, we will utilize a continuous integration and deployment (CI/CD) pipeline. Here's an overview of the process:
Continuous Integration: Every code change (pull request) will trigger an automated build and testing process. This will ensure that the codebase is always in a deployable state and catch any issues early.
Staging Environment: A staging environment will be set up to mirror the production environment as closely as possible. Successful builds from the develop branch will be automatically deployed to the staging environment for further testing and verification.
Production Deployment: Once the staging environment is thoroughly tested and approved, the deployment process will be triggered to push the code changes to the production environment. This can be done automatically or manually, depending on the project's requirements and risk tolerance.
Data Population
The ExpenseTracker app will rely on user input to record and manage expense data. The app will store this data in an SQLite database, allowing users to view, edit, and analyze their expenses.
For testing and development purposes, we may consider implementing a seeding or mocking mechanism to populate the app with sample expense data. This will allow for consistent testing scenarios and ensure that the app's functionality can be verified without relying on live user data during the development phase.
Testing Strategy
To ensure the quality and reliability of the ExpenseTracker app, we will implement a comprehensive testing strategy that includes the following components:
Unit Tests: Unit tests will be written for individual components and functions of the app, both on the backend (Python/Flask) and the frontend (JavaScript). These tests will verify the correctness of isolated code units and facilitate easier debugging and refactoring.
Integration Tests: Integration tests will be used to verify the correct interaction and data flow between different components of the app, such as the frontend communicating with the backend API or the backend managing data in the SQLite database.
End-to-End (E2E) Tests: E2E tests will simulate real user scenarios and test the app from a holistic perspective, ensuring that all components work together as expected and the overall user experience is satisfactory.
Continuous Integration (CI): As mentioned earlier, every code change will trigger an automated build and testing process in our CI pipeline. This will ensure that all unit, integration, and E2E tests are executed, and any failures are caught before the code is merged or deployed.
Test Automation: We will leverage test automation tools and frameworks like pytest (for Python), Jest (for JavaScript), and Selenium (for E2E testing) to streamline the testing process and enable efficient regression testing with every code change.
Manual Testing: While automated testing will be the primary focus, manual testing will also be conducted, especially for critical user scenarios and edge cases that may be difficult to automate effectively.
This comprehensive testing strategy will help ensure the quality, reliability, and stability of the ExpenseTracker app throughout its development lifecycle and enable us to catch and address issues early in the process.
Existing Solutions
There are several existing solutions in the market that offer expense tracking functionality. Here are some notable examples:
Mint: A popular expense tracking and budgeting app that offers a comprehensive set of features including account synchronization, budgeting tools, and financial insights.
Similarities: Like ExpenseTracker, Mint allows users to track their expenses and manage budgets.
Differences: Mint has a more extensive feature set, including automatic expense categorization, bill reminders, and credit score monitoring. ExpenseTracker aims to be a simpler and more focused solution for basic expense tracking.
Expensify: A well-known expense management app used primarily by businesses for expense reporting and reimbursement.
Similarities: Both solutions offer expense tracking capabilities.
Differences: Expensify focuses on business expense management with features like receipt scanning, report generation, and corporate card reconciliation. ExpenseTracker is designed for individual and family use with a focus on simplicity.
By understanding the landscape of existing solutions, ExpenseTracker can identify areas for improvement and differentiation to offer a unique and valuable user experience.

