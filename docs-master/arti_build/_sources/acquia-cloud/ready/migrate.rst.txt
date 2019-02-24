.. include:: /common/global.rst

Assessing your Drupal site for migration onto Acquia Cloud
==========================================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/ready/migrate/*

Migrating your Drupal website to |acquia-product:ac|

-  Assess
-  `Checklist </acquia-cloud/migrate/checklist>`__

If you are migrating your current Drupal website to `Acquia Cloud <https://www.acquia.com/products-services/acquia-cloud>`__ and your migration primarily involves moving content into a new website, the following best practices will ensure the smoothest possible transition from your current website to your new one:

-  `Assess your content <#assessing-your-content>`__
-  `Consider assisted migration <#considering-assisted-migration>`__
-  `Use the Migrate module <#using-the-migrate-module>`__
-  `Import your content <#importing-your-content>`__

Assessing your content
----------------------

Evaluating the content on your current website will help you to determine the scope of your migration. It will also allow you to assess whether you can perform the migration yourself, or whether you need assistance.

-  Determine how many content types are to be moved, how many fields each content type contains, and what those fields are. If there are comments on a particular content type, determine approximately how many there are. How many items of each content type are to be switched over?

-  Determine how many users are to be switched to Drupal, and how many profile fields associated with users are to be switched. How will these users be authenticated in the new website? Will the website use Drupal native authentication, or something else?

-  Is there a free-tagging vocabulary to be moved to Drupal? If so, how many vocabularies (sets of categories), besides tags, are to be moved?

-  Determine if there are other kinds of data that need to be transitioned to Drupal. If applicable, include subscriptions, user points and badges, content ratings, private messages, user relationships (some examples can include: following, friends), statistics, page views, and workflow. How many items of each type are there? Are there other types not mentioned here?

Considering assisted migration
------------------------------

Having a clear picture of your current website's content helps you decide if you can perform the migration yourself, or if you will need guidance. Acquia can assist you with your migration, either guiding you through the entire process, or assisting you with certain tasks while your team handles others. In a `full migration engagement </acquia-cloud/ready/migration>`__, Acquia handles all stages of content migration, from analysis of data through launch. A migration jumpstart proceeds in the following manner:

#. Acquia will work onsite with the customer to analyze and map the data to be migrated.
#. Offsite, Acquia will develop a framework for the migration process.
#. Your website-building team will handle the iteration and launch.

To schedule an assisted migration, `contact Acquia <https://www.acquia.com/about-us/contact>`__.

Using the Migrate module
------------------------

The `Migrate <https://www.drupal.org/migrate>`__ module is a flexible framework that allows you to migrate content into Drupal from other sources. This is an advanced module which is best suited for developers with object-oriented programming skills in PHP. It provides the infrastructure to manage large-scale, complex website migrations. If you aren't comfortable using command-line tools, there are some modules that you can install along with Migrate that will allow you to perform simple migrations — one example is the `WordPress Migrate <https://www.drupal.org/project/wordpress_migrate>`__ module for importing Wordpress content into Drupal 7.

.. admonition:: Wordpress unsupported

   While you can use modules to import a Wordpress export file, Wordpress is unsupported on Acquia's hosting.

Importing your content
----------------------

After you have decided upon a suitable method of content migration from your existing website, pick a date a few days before your website will launch, and run a full import of your content into the to-be-production website. Ideally, your last migration before launch will only contain new, updated information. At the designated time, set your old website to read-only.

As you prepare to launch your new website, be sure to perform the tasks on the `prelaunch checklist for Drupal websites </acquia-cloud/migrate/checklist>`__. For more information about how to prepare your new website for use with |acquia-product:ac|, see `Preparing your website for Acquia Cloud <%5Bacquia-product:kb%5Darticles/preparing-your-site-acquia-cloud>`__.

Additional information
----------------------

For detailed information on content migration from analysis to launch, watch the Acquia webinar `Ensuring success when migrating your content to Drupal <https://www.acquia.com/resources/acquia-tv/conference/ensuring-success-when-migrating-your-content-drupal>`__.
