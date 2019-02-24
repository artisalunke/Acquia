.. include:: /common/global.rst

Importing multiple entities at once
===================================

As a content creator, you may need to import many of your publishing
website's entities to your |acquia-product:ch| at once, without manually
saving each of your nodes again individually in Drupal. Mass imports are
possible with the creation of a custom import script. When used with the
|acquia-product:ch| Import Queue feature, the imported entities are
processed using Drupal's batch API, which reduces the risk of resource
exhaustion on your websites.

.. note::  

   -  The example scripts included in the following procedure work only
      with the Drupal 8 version of |acquia-product:ch|.
   -  For information about batch exports (instead of imports) of entities,
      see `Exporting multiple entities at
      once </content-hub/sharing/export>`__.

To use one of the provided import scripts, complete the following steps:

#. Create a file named ``import.php`` with the code from one of the
   following gists on Github, based on your needs:

   -  `Manual configuration of content to
      import <https://gist.github.com/acquialibrary/294d03689e082bba00f42ad6d00ecce0>`__
   -  `Importing all content matching a filter created on a subscribing
      website <https://gist.github.com/acquialibrary/21fce5c42e791ad76d96816fd38a8d8d>`__

#. Add the ``import.php`` file to your codebase.
#. Enable the |acquia-product:ch| Import Queue feature.
#. Connect to your subscribing website's server using SSH. For more
   information about SSH, see `Managing applications using the command
   line </acquia-cloud/ssh>`__.
#. Navigate to the folder containing your ``import.php`` file, and then
   execute the following Drush command (where ``[site-uri]`` is your
   website's URI):

   ``drush -l  scr import.php``

.. important:: 

   Acquia recommends that you use these scripts to import only independent
   entity types, such as nodes and taxonomy terms.

   Attempting to import dependent entities, such as paragraphs, will fail
   due to the lack of parent entities. The example scripts specifically
   exclude dependent entities.
