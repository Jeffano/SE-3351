Jeffano John, jjohn493@uwo.ca, 251230759

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/l6_XYxi8)
# assignment-1: Refactoring for Clarity and Maintainability

## Objective
To improve an existing piece of software by applying clean code principles, enhancing readability, and ensuring maintainability without altering its functionality.

## Instructions

1. **Provided Code**: bank_system.py is a piece of software that simulates a bank account system. The code works correctly but is written without much consideration for clean code principles.

2. **Your Task**:
    - Refactor the code to make it more readable and maintainable.
    - Rename class and variable names to be more descriptive.
    - Improve the function names.
    - Replace magic numbers with descriptive constants or error messages.
    - Add necessary comments and documentation.
    - Ensure the functionality remains unchanged.
    
3. **Report**: Write a brief report detailing:
    - The changes you made and why.
    - The clean code principles you applied.
    - Challenges faced during the refactoring and how you overcame them.

4. **Code Review (Optional but Recommended)**:
    - Pair up with a classmate and review each other's refactored code.
    - Provide feedback on clarity, organization, and application of clean code principles.

## Submission
- The refactored code.
- Your report on the refactoring process.

## Evaluation Criteria
- Adherence to clean code principles.
- Clarity and readability of the refactored code.
- Quality and relevance of comments and documentation.
- Thoroughness and relevance of the report.

## Report
In the process of refactoring the code, several key changes were made to improve its readability, maintainability, and error-handling capabilities. The original code, which featured a class named 'a' with unclear variable names, was transformed into a more comprehensible and well-documented 'BankAccount' class. Additionally, a custom exception class called `InsufficientBalanceError` was introduced to handle cases where there was not enough balance to withdraw or transfer funds.

Method names and parameters were renamed to be more descriptive and consistent, enhancing the code's overall clarity. This included renaming methods such as `d` to `deposit`, `w` to `withdraw`, `db` to `display_balance`, and `t` to `transfer`. Moreover, the code now follows Python's standard naming conventions and employs meaningful variable names.

A noteworthy change was the replacement of the 'and' operator with the '&' operator when checking conditions. This adjustment was made to ensure proper condition evaluation, as '&' is a bitwise operator that suits this context better.

During the refactoring process, addressing inadequate error handling proved to be a significant challenge. The original code lacked robust error-handling mechanisms and meaningful error messages. Overcoming this challenge involved creating a comprehensive suite of test cases, including edge cases and boundary scenarios. Ensuring that the code remained resilient and didn't break under these conditions was a critical aspect of the refactoring effort. The introduction of the `InsufficientBalanceError` exception and careful validation of error-handling logic were key steps in enhancing the code's reliability.
