.. include:: /common/global.rst

Configuring and enabling Lift Inspector
=======================================

.. toctree::
   :hidden:
   :glob:

   /lift/drupal/inspector/*

|acquia-product:cha| Inspector

-  Intro
-  `Using </lift/drupal/inspector/using>`__

|acquia-product:alt| includes |acquia-product:cha| Inspector, a
debugging tool that you can use to examine the way your website is
working with |acquia-product:cha| and troubleshoot any issues that you
may be having.

Note

|acquia-product:cha| Inspector requires jQuery 1.7 or newer.

Use |acquia-product:cha| Inspector to gather information about the
following issues:

-  The `data captures <#profile>`__ that your website is sending to the
   |acquia-product:alw| service
-  The `website content <#preview>`__ that users in different segments
   are being shown
-  The `events <#event>`__ that your website's data captures are
   triggering in |acquia-product:alw| and |acquia-product:alt|

Known Issues

The following are known issues in |acquia-product:cha| Inspector:

-  When you log in as an administrator, |acquia-product:cha| Inspector
   can be launched from the |acquia-product:cha| menu bar, but the
   **Site preview** tab does not function.
-  |acquia-product:cha| Inspector works on iOS and Android devices, but
   the user experience has not been optimized.
-  |acquia-product:cha| Inspector does not work with desktop Internet
   Explorer or Windows Phone.

 

.. _reqs:

Requirements
------------

Before using |acquia-product:cha| Inspector, ensure that your website
meets the following requirements:

Note

Turning on **Debug mode** allows |acquia-product:cha| Inspector to load.
However, to optimize website performance, **Debug mode** should be
turned off after you have finished using |acquia-product:cha| Inspector.

-  Complete the `Adding the Acquia Lift
   keys </lift/drupal/install/enable#keys>`__ section on the `Enabling
   Acquia Lift Drupal on your site </lift/drupal/install/enable>`__
   documentation page.
-  Ensure that jQuery 1.7 or greater is installed on your website.
-  On the **General** tab, select the **Debug mode** check box.

.. _enable:

Enabling |acquia-product:cha| Inspector
---------------------------------------

Use one of the following options to enable |acquia-product:cha|
Inspector:

-  When visiting your website as an anonymous (not signed in) user, add
   the following text to the end of your website's URL:

    

   ``?acquia_lift_inspect_mode=1``

   For example, if your website URL is ``http://www.example.com``,
   append the parameter in the following manner:

   ``http://www.example.com/?acquia_lift_inspect_mode=1``

-  When signed in to your website as an administrator, in the
   |acquia-product:cha| menu bar, click **Start |acquia-product:cha|
   Inspector session**.

You have now enabled |acquia-product:cha| Inspector. For information
about how to use this tool to debug your website's personalizations, see
`Using |acquia-product:cha| Inspector </lift/drupal/inspector/using>`__.
