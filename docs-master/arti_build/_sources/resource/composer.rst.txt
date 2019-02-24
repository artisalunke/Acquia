.. include:: /common/global.rst

Using Composer with Drupal 8 sites
==================================

.. toctree::
   :hidden:
   :glob:

   /resource/composer/*

`Composer <https://getcomposer.org/>`__ is a tool for managing PHP
dependencies for your website or application. It allows you to declare
the libraries your project depends on, and it will install and update
them for you.

For full instructions about downloading and installing Composer for your
operating system, see `Composer's Getting Started
guide <https://getcomposer.org/doc/00-intro.md>`__.

Using Composer with Acquia Cloud
--------------------------------

Because Composer is not installed on |acquia-product:ac|, we recommend
that you install Composer locally and use it with your local copy to
perform updates and manage dependencies. You can then deploy your build
artifact to your |acquia-product:ac| environments using the
`|acquia-product:ac| pipelines
feature </acquia-cloud/develop/pipelines>`__.

To follow best practices with Composer, you should maintain a source
code (*source*) repository for your project that is separate from your
|acquia-product:ac| (*build*) repository. Your *source* repository
should contain only the minimum amount of code required to build your
project, such as a ``composer.json`` file, ``composer.lock`` file, and
any custom modules or settings. The *source* repository should not
contain copies of your Composer dependencies. Your *build* repository
(hosted on |acquia-product:ac|) should contain static snapshots, called
*build artifacts*, of your entire codebase (including Composer
dependencies) that are ready for deployment to |acquia-product:ac|.

To move code between your *source* and *build* repositories, you can use
one of the following methods:

-  Copy the necessary files locally
-  Use a continuous integration service, such as the
   `|acquia-product:ac| pipelines
   feature </acquia-cloud/develop/pipelines>`__
-  Use a tool that automates this process (such as |acquia-product:blt|)

It is possible, but not recommended, to use a Composer-based workflow
with only a single repository. Using a single repository creates a
brittle development workflow, which can make it difficult to maintain
code consistency. For instance, with a single repository, the versions
of dependencies in ``composer.json`` and the versions of dependencies
actually committed to the repository must be kept in sync, which
introduces a high risk of human error.

If you are unable to use the `|acquia-product:ac| pipelines
feature </acquia-cloud/develop/pipelines>`__, you can use Composer based
on the following methods:

-  *Using |acquia-product:blt| ``deploy`` commands*, as described in the
   |acquia-product:blt| `Deployment
   workflow <http://blt.readthedocs.io/en/latest/readme/deploy/>`__
-  *Installing Composer through Live Development (not recommended)*
   It is also possible to install Composer in |acquia-product:ac|, but
   to do so you will need to both enable `Live
   Development </acquia-cloud/develop/livedev>`__ and follow normal Git
   workflow for checking out the code (including adding the changed
   flags, committing the changes, and pushing to origin).
   After installing Composer, using Composer on |acquia-product:ac|
   requires Live Development mode to be enabled. For more information
   about working with Live Development, see `Live Development
   workflow </acquia-cloud/develop/livedev-workflow>`__.
   By default the ``.gitignore`` file ignores the ``Vendor`` directory,
   which makes sense if you are using Composer on |acquia-product:ac|
   directly.

Using Composer with Drupal
--------------------------

In Drupal versions 8.1 and greater, Drupal core uses Composer to manage
dependencies, which can include Drupal modules. For more information,
see the following Drupal.org resources:

-  `Using Composer in a Drupal
   project <https://www.drupal.org/node/2404989>`__
-  `Using Composer to install Drupal packages through
   Drupal.org <https://www.drupal.org/node/2718229>`__

Starting with Drupal 8.4, a minimum version of Drush 8.1.12 is required
if installed globally, and Drush 8.1.15 if required at the project level
using Composer.

-  `Drupal Core issue describing Drupal 8 and Drush compatibility
   scenarios <https://www.drupal.org/node/2874827>`__
-  `Drush Github project <https://github.com/drush-ops/drush>`__
-  `Drush documentation <http://docs.drush.org/en/master/>`__

Migrating into a Composer-managed build
---------------------------------------

Migrating an existing Drupal 8 website into a Composer-managed build
requires building a ``composer.json`` file that includes all of the
required packages for your existing website. For more information about
the migration process, see the `Composer: Migrate an existing D8 site
into a Composer-managed
build <%5Bkb%5Darticle/composer-migrate-existing-d8-site-composer-managed-build>`__
knowledgebase article.
