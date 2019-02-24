.. include:: /common/global.rst

|acquia-product:ais|
====================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/insight/*

Using |acquia-product:ais|

-  Intro
-  `Using </acquia-cloud/insight/using>`__
-  `Alerts </acquia-cloud/insight/alerts>`__
-  `Modules </acquia-cloud/insight/code>`__
-  `Connector </acquia-cloud/insight/install>`__
-  `Configure </acquia-cloud/insight/config>`__

|acquia-product:ais| is a set of tools that evaluates your website's
performance, security, and search engine optimization to help you
monitor and optimize your websites. Insight uses the
`|acquia-product:anc| <https://www.drupal.org/project/acquia_connector>`__
module on your website to connect to the |acquia-product:ais| service on
a regular schedule, sending up-to-date information about the website's
code and configuration.

.. _about:

About the |acquia-product:anc|
------------------------------

Before you can use |acquia-product:ais|, you must install and enable the
latest stable release of |acquia-product:anc|. The
`|acquia-product:anc| <https://www.drupal.org/project/acquia_connector>`__
is a Drupal module package that enables your sites based on Drupal 8 or
7 to exchange information with the |acquia-product:ais| service. It
consists of the following modules:

-  *|acquia-product:anc|* - Enables secure communication between your
   Drupal website and Acquia to monitor up-time, check for updates, and
   collect site information. For details about what information the
   |acquia-product:anc| sends, see `Sending information to
   Acquia </acquia-cloud/insight/config>`__.
-  *|acquia-product:as|* - (Drupal 7) Gets you started with
   `|acquia-product:as| </acquia-search>`__, Acquia's plug-and-play
   search service.

In the 7.x versions, the |acquia-product:ais| module is divided into
separate Acquia Agent and Acquia Site Profile Information modules.

Acquia's `|acquia-product:ld| </lightning>`__ distrubution begins with
the |acquia-product:anc| modules already installed. This enables you to
connect your site to |acquia-product:ais| without installing any
additional modules.

For more information about installing the |acquia-product:anc| and how
it works, see:

-  `Installing the
   |acquia-product:anc| </acquia-cloud/insight/install>`__
-  `Sending information to Acquia </acquia-cloud/insight/config>`__
