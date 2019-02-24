.. include:: /common/global.rst

Release the Kraken (code)
===========================

.. container:: message-status

   Deploy – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/deploy.html

.. |Previous lesson| replace:: Generating a deployment artifact
.. _Previous lesson: /tutorials/deploy/generating-deployment-artifact

.. |Next lesson| replace:: Post Code Deploy
.. _Next lesson: /tutorials/deploy/post-code-deploy

.. |bltlink| replace:: \ |acquia-product:blt|\ 
.. _bltlink: /devtools/blt


Lesson Goal
-----------

.. container:: message-status

   Deploy a tagged deployment artifact to the production environment.

In order to complete this lesson you will need:

-  A Drupal 8 application deployment artifact
-  Access to an |acquia-product:ac| subscription

In this lesson we will:

#. Backup the production database
#. Deploy a tagged deployment artifact to the production environment

At this stage, you have already quality assured your code and generated
a production-ready deployment artifact. We will now deploy that artifact
to a production environment on |acquia-product:ac|.

Backing up DB
-------------

You should always backup your production database prior to a release,
even if you're entirely confident in the code that you're releasing.
|acquia-product:ac| provides a simple interface for 
`quickly creating environment specific backups </acquia-cloud/manage/back-up#db>`__.

|Backup Databases button on Prod Environment - Cloud UI|

Deploying the codebase
----------------------

Next we'll take your Git tag and deploy it to the production
environment. There are a few ways to do this:

|acquia-product:ac| interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can `use the Acquia Cloud interface to
deploy </acquia-cloud/develop/code/environments#deploy-same>`__ the Git
tag to your production environment:

|Deploying code to Prod on Cloud UI|

CLI based
^^^^^^^^^

|acquia-product:ac| provides a set of Drush commands that allow you to
interact with your application via the CLI. These commands are installed
when you `download your Drush aliases </acquia-cloud/drush/aliases>`__ from
|acquia-product:ac|.

You may use these to deploy your new tag to your production environment.
This can be particularly helpful if you would like to script your
deployments.

.. code-block:: none

   drush @myapp.prod ac-code-path-deploy 1.0.0

Production Mode
^^^^^^^^^^^^^^^

If this is your first release on |acquia-product:ac|, you should take
this opportunity to put your site into `production
mode </acquia-cloud/manage/prod-mode>`__. In
Production mode, you cannot copy your files or database to your
Production environment. This protects you from possibly destroying your
live application by overwriting the live Production files and databases.

|Production Mode in Cloud UI|

Next Lesson > `Post Code Deploy </tutorials/deploy/post-code-deploy>`__
-----------------------------------------------------------------------

Resources
---------

-  `Create environment specific
   backups </acquia-cloud/manage/back-up#db>`__
-  `Download your drush aliases </acquia-cloud/drush/aliases>`__
-  `Using Production Mode </acquia-cloud/manage/prod-mode>`__

.. |Backup Databases button on Prod Environment - Cloud UI| image:: https://cdn2.webdamdb.com/1280_sg7pkCRG4v51.png?1527889013
.. |Deploying code to Prod on Cloud UI| image:: https://cdn3.webdamdb.com/1280_MibSBxYI2eh1.png?1527889012
.. |Production Mode in Cloud UI| image:: https://cdn4.webdamdb.com/1280_E9y1hGYLmMt1.png?1527889016

