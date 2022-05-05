# How to contribute to py-ISPyB

Before submitting the code to this repository please read these contributing guidelines. These guidelines aim to help the developer community to maintain the code stable and reusable.

This is a contribution guide for [py-ISPyB](https://github.com/ispyb/py-ispyb). If you would like to learn more about the project, please start with the [README](https://github.com/ispyb/py-ispyb/blob/master/README.md).

This guide is intended for members of the ISPyB collaboration with contributor access to the repository. If you are not a member but would like to contribute, please contact us.

-   [Reporting Bugs](#reporting-bugs)
-   [Submiting code to the repository](#submiting-code-to-the-repository)
-   [Reviewing process](#reviewing-process)
-   [Coding style guidelines](#coding-style-guidelines)

### Reporting bugs

Before submitting a new bug check if the bug is not already reported in the [bug issues](https://github.com/ispyb/py-ispyb/issues?q=is%3Aopen+is%3Aissue+label%3Abug).
If the corresponding issue does not exist then:

-   [Open a new issue](https://github.com/ispyb/py-ispyb/issues/new) with a short description in the title.
-   In the description describe the bug:
    -   Conditions when the bug appears;
    -   How it can be reproduced;
    -   Possible cause of the bug and source code where it occurs;
    -   If possible add an error log.
-   Assign the `bug` label to the issue.

### Submitting code to the repository

To submit code to the repository, please follow these steps:

1. All code contribution has to be done from an issue. If there is no existing issue for the submission you wish to make, start by [creating a new one](https://github.com/ispyb/py-ispyb/issues/new), and describe what should be done for it to be considered as fulfilled;

2. Once you have identified your contribution issue, [assign it to yourself](https://docs.github.com/en/issues/tracking-your-work-with-issues/assigning-issues-and-pull-requests-to-other-github-users) so that everyone can keep track of what is in progress;

3. Create a branch for the contribution. You should create a branch from the GitHub issue page, by clicking the `Create a branch` button under the `Development` section on the right;

4. Start implementing your changes and [commit](https://github.com/git-guides/git-commit) them;

5. Once the changes are mature enough to be discussed, create a `draft` [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) in the repository;

6. When you feel like your changes are ready for production, mark the pull request as `ready for review`;

7. Wait for [review](#reviewing-process);

8. Once a reviewer has approved your pull request, you are in charge of [merging](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request). We use `squash and merge` to keep history clear and simple.

### Reviewing process

Pull requests marked as ready have to be reviewed before they can be merged.

**The reviewer must be, if possible, from a different facility than the author.**

The reviewer is in charge of verifying the following conditions:

-   the contribution matches the issue requirements
-   no breaking change has been introduced without proper discussion
-   sufficient testing has been implemented
-   CI checks are green
-   the coding style is respected

If necessary, make comments on the code with clear hints on what to do for the author.

When the code is ready for production, mark the pull request as ready.

**When the reviewer validates the pull request, its author is in charge of merging.**

### Coding style guidelines

It is very important to write clean and readable code. Therefore we use `Flake8` linting and `black` formatting as a style standard. This standard is enforced in CI.

**In addition to this, it was decided to name variables that refer to database columns, such as `sessionId` named the same way as they are in the schema. This is not enforced by CI linting and should be verified by reviewers.**
