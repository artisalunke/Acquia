.. include:: /common/global.rst

Connecting pipelines to your Github repo
========================================

The pipelines feature included with |acquia-product:ac| enables you to integrate your Acquia-hosted application with version control repositories hosted on GitHub.

.. container:: message-status

   |Learning Services logo|\   For a step-by-step video tutorial of this process, see `Getting Started with Acquia Cloud CD </tutorials/getting-started-acquia-cloud-cd>`__.*

Requirements
------------

Before you connect |acquia-product:ac| to your repository, ensure that you meet the requirements for your repository, based on the following:

- *If you do not already have a GitHub repository,* `sign in to your GitHub account <https://github.com>`__, and then visit `github.com/new <https://github.com/new>`__ to create a new repository from the GitHub interface.
- *If you have an existing repository,* add GitHub as a new remote by modifying your project repository’s local clone with the following code (where ``[username]`` is your GitHub username and ``[project]`` is the name of your project):

  .. code-block:: none

      git remote add github git@github.com:[username]/[project].git git push github master

Procedure
---------

To use the |acquia-product:ac| interface to connect |acquia-product:ac| with your GitHub repository, complete the following steps:

.. note::

   If you prefer to connect to your GitHub repository by using the command-line client, see `Installing the pipelines client </acquia-cloud/develop/pipelines/cli>`__.

#. `Sign in to your |acquia-product:ac| account <https://cloud.acquia.com>`__.
#. Click the name of the application that you want to connect to GitHub.
#. In the left menu, click **Pipelines**. If your application does not display a **Pipelines** link, `contact Acquia Support </support#contact>`__.
#. Click the **More links** icon |cd-pipelines_more-links.png| and then click **View application info**.
#. In the **Connected repository information** section, click the **Configure** link.

   |Click the Configure link|

#. In the **Select Source** section, click the **Choose source** link.

   |Configure Pipelines with your GitHub repository|

#. Click the **Configure** link for the **Configure Pipelines with your GitHub repository** section.

   |Select GitHub|

#. Click **Connect to GitHub**. |acquia-product:ac| will connect to GitHub and display a confirmation page.
#. Click the **Authorize** button in the GitHub interface to grant |acquia-product:ac| access to your GitHub repository. |acquia-product:ac| will display a page that contains your environment's pipelines information.
#. Click **Select GitHub repository**.
#. Select the repository to which you want to connect, and then click **Continue**.

Changing your webhook
---------------------

If you want to change the webhook in use by your repository, complete the following steps:

.. note::

   You can use this process to also remove the webhook from your repo. In that case, skip the final step in the following procedure.

#. Sign in to GitHub.
#. Go to the following URL:

   ``https://github.com/[your_namespace]/[your_repo]/settings/hooks``

#. Delete the webhook associated with your application.
#. Complete the steps in the previous `connection procedure <#connect>`__ to reinitialize your repository with the new Acquia application ID and GitHub repository name.

Next step
---------

To operate, the pipelines feature expects a file in YAML format named ``acquia-pipelines.yml`` to exist in the root directory of your code repository. This build definition file contains all of the information that is required for pipelines to perform the build, including any variables that are required and the instructions used to perform the build.

For information about how to structure this file and what it should contain, see `Creating and managing your build definition file </acquia-cloud/develop/pipelines/yaml>`__.

.. |Learning Services logo| image:: https://cdn3.webdamdb.com/1280_w1WjsvuWixS1.png?-62169955200
   :class: no-sb float-left logo-sm-lift
   :width: 36px
.. |cd-pipelines_more-links.png| image:: https://cdn2.webdamdb.com/100th_sm_MQqKwPrIX611.png?1526475680
   :width: 30px
.. |Click the Configure link| image:: https://cdn4.webdamdb.com/1280_AErzBRq81aS7.png?1526475476
   :width: 562px
   :height: 270px
.. |Configure Pipelines with your GitHub repository| image:: https://cdn3.webdamdb.com/md_I6SyfTGlqL86.png?1526475469
   :width: 278px
   :height: 216px
.. |Select GitHub| image:: https://cdn3.webdamdb.com/md_UB3KdobwqkT5.png?1527199918
   :width: 365px
   :height: 296px
