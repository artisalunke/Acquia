.. include:: /common/global.rst

Connecting CD environments to your Bitbucket repo
=================================================

The |acquia-product:ac| pipelines feature enables you to integrate
applications on your |acquia-product:ccd| environments with version
control repositories hosted on Bitbucket.

To connect your regular |acquia-product:ac| environments with Bitbucket,
see  Using |acquia-product:ac|  `with a remote
repository </acquia-cloud/develop/github#bitbucket>`__.

Important

-  You can connect pipelines only to repositories that are owned by the
   current Bitbucket user. For more information, see `Known issues in </acquia-cloud/cd/known-issues>`__  |acquia-product:ccd|.
-  This feature only works with Bitbucket Cloud, not Bitbucket Server.

.. _repo:

Requirements
------------

Before you connect a CD environment to your repository, ensure that you
meet the requirements for your repository, based on the following:

-  *If you do not have a Bitbucket repository*, `sign in to your
   Bitbucket account <https://bitbucket.org>`__, and then visit
   `bitbucket.org/repo/create <https://bitbucket.org/repo/create>`__ to
   create a new repository from the Bitbucket UI.
-  *If you have an existing repository,* add Bitbucket as a new remote
   by modifying your project repository’s local clone with the following
   code (where ``[username]`` is your Bitbucket username and
   ``[project]`` is the name of your project):

   ``git remote add bitbucket git@bitbucket.org:[username]/[project].git git push bitbucket master``

.. _connect:

Procedure
---------

To use the |acquia-product:ac| interface to connect an application on a
CD environment with your Bitbucket repository, complete the following
steps:

#. Sign in to your |acquia-product:ac|
   `account <https://cloud.acquia.com>`__.
#. Click the name of the application that you want to connect to
   Bitbucket.
#. In the left menu, click **Pipelines**. If your application does not
   display a **Pipelines** link, `contact Acquia
   Support </support#contact>`__.
#. Click the **More links** icon |cd-pipelines_more-links.png| and then
   click **View application info**.
#. In the **Connected repository information** section, click the
   **Configure** link. A configured Git email address is required. If
   the email address is invalid, Pipelines jobs will not start when
   changes are pushed, and webhooks will fail with HTTP 500 errors.

   |Click the Configure link|

#. In the **Select Source** section, click the **Choose source** link.

   |Configure Pipelines with your GitHub repository|

#. Click the **Configure** link for the **Configure Pipelines with your
   Bitbucket repository** section.

   |Choose Bitbucket|

#. Click **Connect to Bitbucket**.
   Pipelines will connect to Bitbucket and display a confirmation page.
#. Click the **Grant access** button in the Bitbucket interface to grant
   your application access to your Bitbucket repository.
   The |acquia-product:ac| interface for your environment's pipelines
   information will be displayed.
#. Click **Select Bitbucket repository**.
#. Select the repository to which you want to connect, and then click
   **Continue**.

Each time that you use Bitbucket to create or reopen a pull request or
push a commit, |acquia-product:ac| executes the ``pipelines start``
command using the build definition file in the Bitbucket repository, and
commits the resulting build artifact to your |acquia-product:ac|
repository.

.. _next:

Next step
---------

To operate, the pipelines feature expects a file in YAML format named
``acquia-pipelines.yml`` to exist in the root directory of your code
repository. This build definition file contains all of the information
that is required for pipelines to perform the build, including any
variables that are required and the instructions used to perform the
build. Pipelines can build from both forked and non-forked repositories.

For information about how to structure this file and what it should
contain, see `Creating and managing your build definition
file </acquia-cloud/develop/pipelines/yaml>`__.

.. |cd-pipelines_more-links.png| image:: https://cdn3.webdamdb.com/100th_sm_MQqKwPrIX611.png?1526475680
   :width: 30px
   :alt: More links
.. |Click the Configure link| image:: https://cdn4.webdamdb.com/md_AErzBRq81aS7.png?1526475476
   :alt: Click the configure link
.. |Configure Pipelines with your external repository| image:: https://cdn2.webdamdb.com/310th_sm_I6SyfTGlqL86.png?1526475469
   :alt: Configure Pipelines with your external repository
.. |Choose Bitbucket| image:: https://cdn3.webdamdb.com/310th_sm_sQnPqvyuZT78.png?1526475505
   :alt: Choose Bitbucket
