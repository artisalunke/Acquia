.. include:: /common/global.rst

CD Environments
===================

Tutorial Goal
---------------

.. container:: message-status

   Implement continuous integration for a Drupal application on Acquia Cloud.

Lesson Goal
-------------

.. container:: message-status

   Configure your build file to create a new CD environment (CDE) for each GitHub pull request and to destroy that CDE upon merge.

In this lesson, we will modify a build file so that Acquia CD pipelines
will automatically create a new CD environment for each pull
request. This environment can then be visited by team members using a
web browser to manually test for quality and stability. Once this
feature branch is merged, Acquia CD pipelines will destroy the CD
environment automatically.

In order to complete this lesson you will need:

-  `The CD pipelines client installed and configured
   locally </tutorials/1-installing-pipelines-client-locally>`__
   (Lesson #1 of Tutorial)
-  `A defined build </tutorials/2-defining-build>`__ (Lesson #2 of
   Tutorial)
-  SSH access to an Acquia Cloud Subscription
-  A local copy of your Acquia Cloud Subscription’s git repository
-  A \*NIX terminal

| **Note:** GitHub is not a requirement for Acquia Cloud CD.
|  

In this lesson we will:

#. Modify your build file

   -  Create a new local feature branch
   -  Add a new build step
   -  Add new pr-merged and pr-closed steps

#. Submit a Pull Request on GitHub
#. Visit the new CD environment
#. Merge the pull request

2. Modify your build file
~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new local feature branch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use git to create a new feature branch.

::

    git checkout -b pipelines-ode-deploy

Add a new build step
^^^^^^^^^^^^^^^^^^^^

Next, we will modify your ``acquia-pipelines.yml`` file such that a new
CDE will be created when a new Pull Request is opened. To accomplish
this, we use the `Pipelines Deploy
tool <https://github.com/acquia/pipelines-examples/tree/master/tutorial-701#how-it-works>`__.

Add the following build step to your build definition file:

::

         - deploy:
              script:
                - pipelines-deploy

**Note:** Nest this step under events.build.steps. Please see the
`acquia-pipelines.yml <https://github.com/acquia/pipelines-examples/blob/master/tutorial-701/acquia-pipelines.yaml>`__
example.

Add new pr-merged and pr-closed steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These steps will destroy the CD environment after a pull request is
merged or closed:

::

      pr-merged:
        steps:
          - deploy:
              script:
                - pipelines-deploy

      # When a GitHub pull request is closed, this deletes the coresponding ODE.
      pr-closed:
        steps:
          - deploy:
              script:
                - pipelines-deploy

**Note:** Nest this step under the events key. Please see the
`acquia-pipelines.yml <https://github.com/acquia/pipelines-examples/blob/master/tutorial-701/acquia-pipelines.yaml>`__
example.

Commit the changes and push the feature branch to github remote:

::

    git add acquia-pipelines.yml
    git commit -m 'Adding ODE deployment step to acquia-pipelines.yml.'
    git push github pipelines-ode-deploy

.. raw:: html

   <iframe src="https://asciinema.org/a/105425/embed?size=medium&amp;speed=1&amp;autoplay=1&amp;loop=1&amp;theme=asciinema&amp;t=0&amp;preload=1" id="asciicast-iframe-105425" name="asciicast-iframe-105425" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 810px; float: none; visibility: visible; height: 521px;"></iframe>

3. Submit a Pull Request on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the GitHub UI to create a new Pull Request:

|Creating a new pull request|

A pipelines build is automatically triggered.  Wait for the build to
finish and use GitHub to review proposed code changes. 

Once the build completes successfully, a green checkbox appears next to
the commit ID. This indicates that all steps were successful, including
the step that created the CD environment.

4. Visit the new CD environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the Acquia Cloud UI to find and visit that environment.

Feel free to interact with the application to manually inspect the
environment as a user. 

5. Merge the pull request
~~~~~~~~~~~~~~~~~~~~~~~~~

At this point, you can confidently merge the pull request.

Click the merge button in the GitHub UI. This destroys the CD
environment and triggers a pipelines build for the “master” branch,
which the feature branch was merged into.

The ``pipelines-master-build`` will update on the Acquia Cloud.

You may deploy the ``pipelines-master-build`` to a development
environment and visit it! 

**Congratulations, you’ve successfully implemented a basic continuous integration process with Acquia Cloud!**
--------------------------------------------------------------------------------------------------------------

 

Getting Started with Acquia Cloud CD
------------------------------------

#. `Installing CD pipelines client
   Locally </tutorials/getting-started-acquia-cloud-cd/installing-pipelines-client-locally>`__
#. `Defining a
   Build </tutorials/getting-started-acquia-cloud-cd/defining-build>`__
#. `Integrating
   GitHub </tutorials/getting-started-acquia-cloud-cd/integrating-github>`__
#. `CD Environments </tutorials/getting-started-acquia-cloud-cd/continuous-delivery-environments>`__

.. |Creating a new pull request| image:: /sites/docs.acquia.com/files/inline-images/ode_pr.gif

