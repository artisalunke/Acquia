.. include:: /common/global.rst

Exporting an application from Acquia Cloud
==========================================

|acquia-product:ac| is an open SaaS platform that doesn't lock in your
application. You can export the whole application — code, themes,
database, and files — at any time to a site archive file, which you can
then use to host your application locally, or use another hosting
service.

One easy way to make a local, running copy of your website is with
|acquia-product:add|. Read the |dd-docs|_, especially |startwithcloud|_, 
for information about how to do this.

.. |dd-docs| replace:: \ |acquia-product:add|\  documentation
.. _dd-docs: /dev-desktop

.. |startwithcloud| replace:: Starting with an \ |acquia-product:ac|\  site
.. _startwithcloud: /dev-desktop/start/cloud

You can also use the `Drush <http://www.drush.org/>`__ command line tool
to create a portable site archive file, which you can then install on a
different hosting platform if you desire. The site archive file created
during the export process includes your databases, themes, content,
modules, website and module configuration settings, and users. To create
a site archive file:

#. `Connect to your server with SSH </acquia-cloud/ssh>`__.
#. Run a command like the following:

   .. code-block:: none

      drush @site.env archive-dump --destination=../mysite.tar.gz

   where ``[site]`` is the name of your application on
   |acquia-product:ac|, ``[env]`` is the |acquia-product:ac| environment
   (one of ``prod``, ``test``, or ``dev``), and the ``--destination``
   argument is the location where you want the site archive file
   created.

You can then use ``scp`` or another similar tool to download the site
archive file.

.. important:: 

   Acquia does not recommend using the `Backup and
   Migrate <https://drupal.org/project/backup_migrate>`__ module with
   |acquia-product:ac|. `Learn
   more </articles/backup-and-migrate-module-acquia-hosted-sites>`__.
