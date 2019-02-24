.. include:: /common/global.rst

Generating a deployment artifact
======================================

.. container:: message-status

   Deploy – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/deploy.html

.. |Previous lesson| replace:: Preparing for Production
.. _Previous lesson: /tutorials/deploy/preparing-production

.. |Next lesson| replace:: Release the Kraken
.. _Next lesson: /tutorials/deploy/release-kraken-code

.. |bltlink| replace:: \ |acquia-product:blt|\ 
.. _bltlink: /devtools/blt

Lesson Goal
-----------

.. container:: message-status

   Generate a production-ready deployment artifact for a Drupal 8 application.

In order to complete this lesson you will need:

-  A Drupal 8 application that is ready for deployment
-  Access to an |acquia-product:ac| subscription
-  Composer
-  PHP 5.6+
-  Git

The following tools are not required, but are recommended:

-  |bltlink|_

In this lesson we will:

#. Generate a deployment artifact
#. Push the artifact to |acquia-product:ac|

As discussed in lesson 1, deploying a Drupal 8 application to production
requires producing a "deployment artifact". This lesson will walk you
through creating that artifact.

Using |acquia-product:blt| (recommended)
----------------------------------------

If you are using |acquia-product:blt|, you can simply run its
'`deploy <http://blt.readthedocs.io/en/8.x/readme/deploy/>`__' command.
It will generate a production-ready artifact automatically.

.. raw:: html

   <iframe src="https://asciinema.org/a/126914/embed?size=medium&amp;speed=1&amp;autoplay=1&amp;loop=1&amp;theme=asciinema&amp;t=0&amp;preload=1" id="asciicast-iframe-126914" name="asciicast-iframe-126914" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 885px; float: none; visibility: visible; height: 521px;"></iframe>

Specifically, the command will:

-  Remove development dependencies
-  Optimize your composer autoload files
-  Remove extraneous files from the application
-  Execute frontend compilation tasks
-  Cut a git tag for you
-  Push that tag to your hosting environment

Manual approach
---------------

For those not using |acquia-product:blt|, you should at a minimum use
Composer to remove development dependencies and optimize your
application's autoloader:

.. code-block:: none

   composer install --no-dev --optimize-autoloader

This will install only the dependencies in your composer.json's
"require" array (not in the "require-dev" array) and will `optimize
Composer's
autoloader <https://getcomposer.org/doc/articles/autoloader-optimization.md>`__,
which significantly improves application performance.

You should also consider performing the following manual steps:

-  Remove Drupal core text files, like CHANGELOG.txt, from your docroot.
   These can inadvertently reveal your exact Drupal core version to
   malicious site visitors.
-  Change/Restrict any reachable path for security purposes (i.e.
   node\_modules or similar).
-  Compile front end source code (like SASS) into front end assets (like
   CSS).

After you've manually prepared your codebase for production, you will
need to create a new Git tag.

Cutting Tags
^^^^^^^^^^^^

Using a git tag for deployment is a best practice because tags are
immutable. In other words, after it has been created a tag cannot be
changed. For instance, using a tag will prevent someone from
accidentally pushing a new commit to a branch that is deployed to your
production environment. This cannot happen with a tag.

.. code-block:: none

   git tag 1.0.0 -m ‘This is the first major release!’

Now that your tag is cut, you can simply push it to |acquia-product:ac|:

.. code-block:: none

   git push origin 1.0.0

Naming your releases
^^^^^^^^^^^^^^^^^^^^

You should use a naming convention for your tags that works well for
your team. The most popular (and recommended option) is `Semantic
Versioning <http://semver.org/>`__ (semver). In short, semver provides a
set of rules for naming tags. The rules help you track:

-  The order in which releases are made
-  Releases that introduce backwards incompatible changes (major)
-  Releases that introduce new, backwards compatible functionality
   (minor)
-  Releases that provide backwards compatible bug fixes (patch)

Tags using semver take the form MAJOR.MINOR.PATCH. For more information,
see `semver.org <http://semver.org>`__.

In combination with Composer version constraints, you can use semver to
ensure that your application's dependencies are never accidentally
updated to a backwards incompatible version.

Now that you have a deployment artifact, you're ready to deploy it on
your |acquia-product:ac| production environment!

Next Lesson > `Release the Kraken (code) </tutorials/deploy/release-kraken-code>`__
-----------------------------------------------------------------------------------

In this next lesson we will deploy a production-ready deployment
artifact to |acquia-product:ac|.

Resources
---------

-  `Deploying to cloud - |acquia-product:blt|
   Documentation <http://blt.readthedocs.io/en/8.x/readme/deploy/>`__
-  `Semantic Versioning <http://semver.org>`__
