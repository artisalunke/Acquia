.. include:: /common/global.rst

Managing applications with |acquia-product:ac|
==============================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/*

|acquia-product:ac| applications run on a Drupal-optimized platform. The
core of the platform is an open-source LAMP server stack, combining the
Linux (Ubuntu) operating system, Apache web server, MySQL (Percona)
database, and PHP programming language with Drupal. The default
|acquia-product:ac| configuration works as-is for most web experiences
and other applications. |acquia-product:ac| provides you with a suite of
tools you can use to manage your applications and the domains and
environments they run on.

.. _app:

What's an application?
----------------------

In |acquia-product:ac|, an
`*application* </acquia-cloud/glossary#application>`__ is a software
product that implements a web service, such as a Drupal-based web site
or a web-accessible API. Application specifically refers to the software
product as an entity in itself, separate from the potentially many
installations of the application in different environments, such as
production, or development, that may use specific domain names, with
specific content. Applications have a lifecycle and typically have
multiple versions. An application is primarily made up of its program
code, such as Drupal core plus contributed and custom modules, along
with static assets such as images and stylesheets for its visual theme.

Here are some of the tasks you can perform using the |acquia-product:ui|
and other tools:

-  `Managing domains </acquia-cloud/manage/domains>`__
-  `Managing |acquia-product:ac|
   servers </acquia-cloud/manage/servers>`__
-  `Configuring your environments </acquia-cloud/manage/configure>`__
-  `Managing applications using the command line </acquia-cloud/ssh>`__
