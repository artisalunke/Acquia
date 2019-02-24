.. include:: /common/global.rst

Defining a Build
===================

Tutorial Goal
--------------

.. container:: message-status

   Implement continuous integration for a Drupal application on Acquia Cloud.

Lesson Goal
-----------

.. container:: message-status

   Create a custom Acquia CD pipelines build definition that downloads a third-party package required by your application.

Continuous integration typically requires that some build process occurs
each time that a change is introduced (or proposed via Pull Request) to
the “master” branch of a git repository. That process performs
various operations on the code base.

In this lesson, we have provided a hypothetical scenario and an
accompanying hypothetical build process.

**Note:** Your Drupal application will likely require a different,
custom build. After completing this tutorial, customize this lesson to
suit your application’s specific needs.

Scenario
^^^^^^^^

We would like to use the
`league/csv <https://packagist.org/packages/league/csv>`__ PHP library
in a custom module in our Drupal Application.

Build plan
^^^^^^^^^^

The following build process will occur each time a change is pushed to
our application via git:

#. Composer will be used to download the ``league/csv`` package

   -  In keeping with best practices, we will not commit this third
      party package directly to the repository’s master branch. Instead,
      CD pipelines will download this package each time a pipelines
      build is executed (see `Production is an artifact of
      development <https://events.drupal.org/neworleans2016/sessions/production-artifact-developmenthttp://craychee.io/blog/2015/10/04/production-is-an-artifact/>`__ in
      Resources for more information).

#. Acquia CD pipelines will then commit the modified code base, along
   with the downloaded ``league/csv`` package, to a new
   pipelines-master-build branch (known as the build artifact).
#. The build artifact will then deployed to an Acquia Cloud Environment,
   where a user may interact with the website.

In order to complete this lesson you will need:

-  `The CD pipelines client installed and configured
   locally </tutorials/1-installing-pipelines-client-locally>`__ (Lesson #1
   of Tutorial)
-  SSH access to an Acquia Cloud Subscription
-  A local copy of your Acquia Cloud Subscription’s git repository
-  A \*NIX terminal
-  The following locally installed tools:

   -  PHP
   -  `Composer <https://getcomposer.org/>`__
   -  `Git <https://git-scm.com/downloads>`__

In this lesson we will:

#. Add a Composer dependency to our project
#. Create a pipelines build definition file (acquia-pipelines.yml)
#. Execute the Acquia Cloud pipelines build
#. Deploy the build artifact to an Acquia Cloud environment

1. Add a Composer dependency to your project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Note:** If you are not familiar with Composer, please see `Using
  Composer with
  Drupal <https://www.drupal.org/docs/develop/using-composer/using-composer-with-drupal>`__. 
| Please skip the referenced `special steps required to manage
  Drupal-specific dependencies via
  Composer <https://www.drupal.org/docs/develop/using-composer/using-composer-to-manage-drupal-site-dependencies#managing-existing-site>`__
  as they are not applicable in this lesson.

| Use Composer to add ``league/csv`` as a new site dependency:
|  

::

    cd my/project/directory
    composer require league/csv

Once this command is executed, `Composer <https://getcomposer.org/>`__
will add ``league/csv`` to the ``require`` array within the
``composer.json`` file and download the latest stable version of
``league/csv`` to the ``vendor`` directory. Composer will also update
the
`composer.lock <https://getcomposer.org/doc/01-basic-usage.md#composer-lock-the-lock-file>`__
file.

| Commit the changes to the ``composer.json`` and ``composer.lock``
  files.
|  

**Note:** `Best
practices <https://getcomposer.org/doc/faqs/should-i-commit-the-dependencies-in-my-vendor-directory.md>`__
dictate that you should not commit the dependency directly.

Add a new line to the ``.gitignore`` file, instructing git to ignore the
``vendor`` directory. CD pipelines will be responsible for downloading
and committing this directory later during the build process.

::

    echo "/vendor" >> .gitignore
    git add .gitignore composer.json composer.lock
    git commit -m "Requiring league/csv package."

.. raw:: html

   <iframe src="https://asciinema.org/a/105455/embed?size=medium&amp;speed=1&amp;autoplay=1&amp;loop=1&amp;theme=asciinema&amp;t=0&amp;preload=1" id="asciicast-iframe-105455" name="asciicast-iframe-105455" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 810px; float: none; visibility: visible; height: 521px;"></iframe>

2. Create a pipelines build definition file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The build definition file, named ``acquia-pipelines.yml``, will instruct
CD pipelines to install the Composer requirements defined in your
``composer.lock`` file.

::

    touch acquia-pipelines.yml

| Add the following text to acquia-pipelines.yml file:
|  

.. code-block:: yaml

    version: 1.0.0
    services:
      - mysql
    events:
      build:
        steps:
            - setup-project:
                type: script
                script:
                  - composer install

This build file defines a single “setup-project” step which runs a
single command: ``composer install``.

| Commit the new build definition file and push all local changes to
  your Acquia Cloud git remote (we assume this is “origin”).
|  

::

    git add acquia-pipelines.yml
    git commit -m 'Adding acquia-pipelines.yml file.'
    git push origin

.. raw:: html

   <iframe src="https://asciinema.org/a/105426/embed?size=medium&amp;speed=1&amp;autoplay=1&amp;loop=1&amp;theme=asciinema&amp;t=0&amp;preload=1" id="asciicast-iframe-105426" name="asciicast-iframe-105426" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 810px; float: none; visibility: visible; height: 521px;"></iframe>

3. Execute the pipelines build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Acquia CD pipelines can now start a build using our custom build
definition file. What does this mean? In detail, CD pipelines will:

-  Provision a temporary machine
-  Use the temporary machine to clone the repository
-  Check out the git branch for which the job was triggered
-  Use the temporary machine to execute the custom build instructions
-  If successful, commit all files (even .gitignored ones) to a new
   "build branch"
-  Push the build branch to the Acquia Cloud subscription

**Note:** If you did not clone your repository from Acquia Cloud, you
may need to set the default Application ID for your local repository.
Use ``pipelines list-applications`` to find the ID for your Acquia Cloud
application. Then, execute pipelines
``set-application-id --application-id=[application-id]``

| Use the locally installed CD pipelines client to trigger a new build
  for the current branch.
|  

::

    pipelines start

| The robots are working! Check the status of the build using the local
  CD pipelines client for updates at any time by executing:
|  

::

    pipelines status
    pipelines log

.. raw:: html

   <iframe src="https://asciinema.org/a/105423/embed?size=medium&amp;speed=1&amp;autoplay=1&amp;loop=1&amp;theme=asciinema&amp;t=0&amp;preload=1" id="asciicast-iframe-105423" name="asciicast-iframe-105423" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 810px; float: none; visibility: visible; height: 521px;"></iframe>

4. Deploy the build artifact to an Acquia Cloud environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the build is complete (assuming it does not fail), the new build
branch will be available in the Acquia Cloud subscription user
interface.

Next Lesson(s)
--------------

Acquia Cloud CD does not require the use of GitHub or Continuous
Delivery Environments. Therefore, please choose your adventure
accordingly:

-  `3: Integrating GitHub </tutorials/3-integrating-github>`__

   -  Learn how to execute your pipelines build automatically whenever a
      Pull Request or commit is created on GitHub

-  `4: Continuous Delivery
   Environments </tutorials/continuous-delivery-environments>`__

   -  Learn how to create a new On Demand Environment in the Acquia
      Cloud whenever your pipelines build is executed
