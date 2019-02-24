.. include:: /common/global.rst

Managing your code with other tools
===================================

As a website developer in |acquia-product:ac|, be default you have
access to three hosted environments for your development and deployment:
Development, Staging, and Production. You also have access to a fourth,
additional environment: the local development environment on your
computer. Having a local development environment allows you to obtain
quick feedback regarding changes that you make to your website, all
before you commit code to the |acquia-product:ac| code repository.

.. _devdesktop:

Using |acquia-product:add| for local development
------------------------------------------------

||acquia-product:add| logo|\ The best way to develop and run your
website locally is with |acquia-product:add|, Acquia's free all-in-one
Drupal stack, which is integrated with |acquia-product:ac|. You can
export websites created in |acquia-product:add| into your
|acquia-product:ac| subscription or make a local clone of your
|acquia-product:ac| websites with a couple of clicks. You can then
easily sync the local and |acquia-product:ac| versions of your websites,
pushing changes up to the cloud and pulling them down to your local
version.

For more information, see the `|acquia-product:add|
documentation </dev-desktop>`__.

.. _drush:

Using Drush when developing locally
-----------------------------------

If you're not using |acquia-product:add|, when you use
`Drush <http://docs.drush.org/en/master/>`__ during website development,
use the following argument with Drush commands to direct Drush to use
the ``settings.php`` in the ``[docroot]/sites/localhost`` directory:

``-l http://localhost/example``

where ``http://localhost/example`` is the address of your website.

As an example, the following Drush command downloads the currently
recommended version of the |acquia-product:cha| module, while using the
``localhost`` version of ``settings.php``:

``drush dl acquia_lift -l http://localhost/example``

.. _deploy:

Developing locally using other tools
------------------------------------

If you do not want to use the code management workflow tool included
with |acquia-product:ac|, you can use the tool of your choice to manage
your |acquia-product:ac| code repositories.

To deploy code across environments using the command line, complete the
following steps:

#. `Connect to the target environment using SSH </acquia-cloud/ssh>`__.
#. In the command prompt window, enter a command similar to the
   following:

   ``git clone trunk tags/2011-03-18 git commit -a -m "Created new tag"``

.. ||acquia-product:add| logo| image:: https://www.acquia.com/sites/default/files/product/header/aquiadrupal_icon_80.png
   :class: no-sb logo-pp

