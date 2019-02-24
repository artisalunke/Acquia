.. include:: /common/global.rst

Integrating GitHub
===================

Tutorial Goal
---------------

.. container:: message-status

   Implement continuous integration for a Drupal application on Acquia Cloud.

Lesson Goal
--------------

.. container:: message-status

   Integrate GitHub with your Acquia Cloud application so that when you create a new pull request on GitHub, a new pipelines build is automatically started.


**Note:** GitHub is not a requirement for Acquia Cloud CD.

In this lesson, we will integrate GitHub with the Acquia Cloud
application such that, when a new pull request is created, a new CD
pipelines build starts. `GitHub <https://github.com/>`__ is a popular
SaaS tool that allows developers to write software collaboratively. It
facilitates code review, discussion, and integration with Continuous
Integration and Continuous Delivery tools.

A GitHub “pull request” allows a developer to propose code changes to a
project. The changes in the pull request can be tested, reviewed, and
discussed prior to merging those changes into a project.

In order to complete this lesson you will need:

-  `A CD pipelines client installed and configured
   locally </tutorials/1-installing-pipelines-client-locally>`__
   (Lesson #1 of Tutorial)
-  `A defined build </tutorials/2-defining-build>`__ (Lesson #2 of
   Tutorial)
-  A GitHub account with a SSH key added
-  SSH access to an Acquia Cloud Subscription
-  A local copy of your Acquia Cloud Subscription’s git repository
-  A \*NIX terminal

In this lesson we will:

#. Create a GitHub repository
#. Connect Acquia Cloud CD to GitHub
#. Submit a pull request on GitHub
#. View the log for the triggered build
#. Merge & manually deploy a build artifact to Acquia Cloud

1. Create a GitHub repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already have a GitHub repository, skip this step. Otherwise, sign
into your GitHub account and navigate to https://github.com/new to
create one.

Add GitHub as a new remote by modifying your project repository’s local
clone. Then, push your code to GitHub:

::

    git remote add github 
    git@github.com:[org-or-username]/[project-name].git
    git push github master

2. Connect Acquia Cloud CD to GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways to connect Acqiua Cloud CD with GitHub:

#. Use the Acquia Cloud UI in your web browser
#. Use the Pipelines client on your command line

Use the Acquia Cloud UI in your web browser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To connect Acquia Cloud CD to GitHub using the Acquia Cloud UI, open a
web browser and follow these steps:

#. Visit cloud.acquia.com and login.
#. Select your Drupal application.
#. Click the "Pipelines" link in the left-hand sidebar.
#. Click "More links" and then click "View application info".
#. Under "Connected repository information" click "Configure".
#. Under "Configure Pipelines with your GitHub repository" click
   "Configure".
#. Click "Connect to GitHub".
#. Grant Pipelines access to GitHub.
#. Click "Select GitHub repository".
#. Choose a repository to connect. Note that you may filter the list by
   entering a string into the "Filter repositories" field.

Use the Pipelines client on your command line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**If you have already connected Acquia Cloud CD to GitHub via the Acquia
Cloud UI, skip ahead to the next section.**

To connect Acquia Cloud CD to GitHub using the command line, we will
generate a new access key on GitHub.

Navigate to https://github.com/settings/tokens, click the gray "Generate
new token" button, choose “repo” as the scope, then click the green
“Generate token” button. Leave this tab open--we will need the token
soon.

|github_generate_token.gif|

.. |github_generate_token.gif| image:: https://lh3.googleusercontent.com/7UzX6MadrR4q1oofZu036uf0NyN0bESZF3ZbJJ86FSw51kGa17SLdeiurn4Duv4AJ4POLMlfQNJx5MQfjg_q6u13ht4bp5PBoPzF4fgdow8BU1shf_X1_kg5TWMNnKMQonQeP7vz

| The application ID is needed for the Acquia application. To find this,
  execute:
|  

::

    pipelines list-applications

| A list of accessible applications appears. Find the correlating
  application and copy the ID to your clipboard. then run the following
  command:
|  

::

    pipelines github-connect --application-id=[Application ID from list-applications] GITHUB_USER/GITHUB_REPO GITHUB_PERSONAL_ACCESS_TOKEN

.. raw:: html

   <iframe src="https://asciinema.org/a/105430/embed?size=medium&amp;speed=1&amp;autoplay=1&amp;loop=1&amp;theme=asciinema&amp;t=0&amp;preload=1" id="asciicast-iframe-105430" name="asciicast-iframe-105430" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 810px; float: none; visibility: visible; height: 521px;"></iframe>

Congratulations, GitHub is now integrated with Acquia Cloud CD
pipelines!

3. Submit a pull request on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Introduce a simple change to the repository and propose that change by
submitting a pull request.

Use GitHub’s user interface to complete the following:

-  Delete the default README.acquia file
-  Create a new git branch named remove-default-readme
-  Create a pull request from remove-default-readme to master

|Triggering a pull request|

.. |Triggering a pull request| image:: /sites/docs.acquia.com/files/inline-images/github_pull_request_triggerBRS_0.gif

**Optional:** If you prefer not to use the GitHub UI to make changes,
you may perform these same actions using the command line and *then*
submit the pull request via the GitHub UI.

::

    git checkout -b remove-default-readme
    rm README.acquia
    git add README.acquia
    git commit -m 'Removing default README.acquia.'
    git push github remove-default-readme

4. View the log for the triggered build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The pull request displays information about the CD pipelines job,
  including the ID, and the status (i.e. in progress, successful, or
  failed).

|image2|

.. |image2| image:: https://lh4.googleusercontent.com/s7-LjrTbEreI1ffcCfM9vEH9hIyaeXZWYpX3bTpTu224FLpb2KGgQQVRhJHYdEzNqMv9HuIKArWPs3c7ZS8RrnOyf-nZfghW1_9mySbg_db4TYN0A5nykFi1OZRj_Yvu3DsoZFBy

You may click on the yellow circle icon next to the build in order to
view the log output for the job in the Pipelines UI. You may also view
the log output on the command line by executing:

::

    pipelines logs --job-id=[job-id]

5. Merge & manually deploy a build artifact to Acquia Cloud
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the build is successful, a green check mark will be displayed in
the GitHub UI. This indicates all of the commands in the
acquia-pipelines.yml file executed successfully.

You may confidently click the “Merge” button in the GitHub UI to merge
the remove-default-readme branch into the master branch.

CD pipelines will automatically start another job for the newly merged
commit(s) on the master branch. When finished, CD pipelines will create
or update the pipelines-master-build branch on the Acquia Cloud with
changes.

Deploy the pipelines-master-build branch to one of your Acquia
environments to test your changes.

|Deploying on Acquia Cloud|

**Optional:** If you prefer not to use Acquia Cloud’s UI to deploy this
branch, you may perform the following action on the command line using
Acquia Cloud API’s drush commands:

::

    drush ac-code-path-deploy @mysite.dev pipelines-master-build

However, this requires that you `locally install drush aliases for your
site <https://docs.acquia.com/cloud/drush-aliases>`__.

Next Lesson
-----------

-  `4: Continuous Delivery
   Environments </tutorials/continuous-delivery-environments>`__

   -  Create a new Continuous Delivery Environment in the Acquia Cloud
      whenever your CD pipelines build is executed




.. |Deploying on Acquia Cloud| image:: /sites/docs.acquia.com/files/inline-images/acquia_deploy_0.gif

