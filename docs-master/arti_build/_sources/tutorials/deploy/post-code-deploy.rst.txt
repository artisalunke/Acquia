.. include:: /common/global.rst

Post Code Deploy
===================

.. container:: message-status

   Deploy – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/deploy.html

.. |Previous lesson| replace:: Release the Kraken
.. _Previous lesson: /tutorials/deploy/release-kraken-code

.. |bltlink| replace:: \ |acquia-product:blt|\ 
.. _bltlink: /devtools/blt

Lesson Goal
-----------

Perform application updates after new code has been deployed.

In order to complete this lesson you will need:

-  Command line access to an |acquia-product:ac| subscription
-  Drupal 8 application that is deployed to |acquia-product:ac|

The following tools are not required, but recommended:

-  |bltlink|_

In this lesson we will:

-  Update production database to reflect code changes

Config and database updates
---------------------------

At this point, the code for your new release is on your production
server(s). However, your database has not been updated in any way.

Database updates
^^^^^^^^^^^^^^^^

A typical code release will require the following database-related
actions to be performed:

-  Update hooks provided by contributed module should be executed. This
   is easily accomplished with ``drush updatedb``.
-  Changes to exported configuration files should be imported. Depending
   on your configuration management strategy, this may require
   ``drush config-import`` or ``drush features-revert-all``.

-  Your caches should be rebuilt. This will allow changes to Twig
   templates, CSS, Javascript, and various other cached data to be
   registered. This can be accomplished with ``drush cache-rebuild``.

Depending on the changes that your release contains, these commands may
need to be run in a specific order or even multiple times. The
consequences of running these commands incorrectly can be subtle and
complex.

If you are using |acquia-product:blt|, this is handled for you via the
``blt deploy:update`` command, which will run all aforementioned
commands in the correct order.

|acquia-product:ac| Hooks
-------------------------

|acquia-product:ac| Hooks provide a mechanism for automatically
executing a script when a particular action is performed. For releases,
the ``post-code-update`` and ``post-code-deploy`` cloud hooks are
relevant. These will allow a custom script to be executed each time that
a new tag is deployed to your production environment.

To implement a cloud hook, `you must create an executable bash script
and place it in a specific location in your
codebase </acquia-cloud/api/cloud-hooks>`__.

If you are using |acquia-product:blt|, you can generate a set of default
cloud hooks automatically by executing ``blt setup:cloud-hooks``. This
will place default bash scripts into the appropriate directories and set
the correct permissions on them. These scripts will implement the
aforementioned ``blt deploy:update`` command to automatically execute
the suggested database updates each time that you make a deployment.

**Congratulations, you've successfully deployed a Drupal application to a production environment following Drupal 8 best practices!**
-------------------------------------------------------------------------------------------------------------------------------------

Resources
---------

-  `Automating with Cloud Hooks </acquia-cloud/api/cloud-hooks>`__
