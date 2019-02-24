.. include:: /common/global.rst

Installing |acquia-product:acm| and components
==============================================

.. toctree::
   :hidden:
   :glob:

   /commerce/install/modules/
   /commerce/install/magento/   

Installing |acquia-product:acm|

-  Start
-  `Modules </commerce/install/modules>`__
-  `Magento </commerce/install/magento>`__

Use the following instructions to install |acquia-product:acm| and
connect your Drupal website to your commerce solution.

Requirements
------------

Before installing |acquia-product:acm|, be sure to plan for the
following requirements:

-  Contact your Acquia Account Manager to obtain the Drupal modules for
   |acquia-product:acm|.
-  Understand your PCI DSS compliance needs.
   To be PCI DSS compliant, your main website must be in Acquia's shared
   virtual private cloud (VPC). Because your website connects to your
   payment gateway, it is considered to be in scope for PCI DSS
   compliance. For information about Acquia's PCI DSS compliance, see
   `Compliance with standards and
   regulations </acquia-cloud/arch/compliance-standards-and-regulations#pci-dss>`__.

Getting started
---------------

To install and use |acquia-product:acm|, complete the following steps to
connect your Drupal website with your commerce solution:

#. On your Drupal website, `install the |acquia-product:acm| Drupal
   modules </commerce/install/modules>`__.
#. Work with Acquia to configure the |acquia-product:ccs| to communicate
   between Drupal and your commerce solution.
#. If you are using Magento as your commerce solution, `configure the
   Magento-to-|acquia-product:acm|
   connection </commerce/install/magento>`__.
