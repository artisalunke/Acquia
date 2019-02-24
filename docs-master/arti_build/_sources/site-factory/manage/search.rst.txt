.. include:: /common/global.rst

|acquia-product:as| and |acquia-product:edg|
============================================

.. container:: message-status

   **ADVANCED** - Incorrect use of this webpage's content can share 
   search data between websites in your cluster.

For your |acquia-product:edg| websites to be able to use
|acquia-product:as|, you must install the suite of search modules for
your version of Drupal. Because all websites in an environment share a
single search index, it is important to configure your websites to
provide website-specific hashes for |acquia-product:as| to return search
results for only a single website in your cluster.

To learn more about the currently-supported versions of search modules
on |acquia-product:ac|, see 
`Modules for Acquia Search </acquia-search/modules>`__.


Configuring |acquia-product:as| and |acquia-product:edg|
--------------------------------------------------------

To configure |acquia-product:as| for multisite use with
|acquia-product:edg|, complete the following steps:

#. `Contact Acquia Support </support#contact>`__ to request that search
   cores be provisioned for each environment in your
   |acquia-product:edg| subscription.
#. Install and configure the `recommended search
   modules </acquia-search/modules>`__ for your version of Drupal.
#. Enable multisite search support using the following steps appropriate
   for your installed version of Drupal:

   -  *Drupal 8* - Apply the `patch from issue
      #2873443 <https://www.drupal.org/node/2873443>`__ on Drupal.org to
      the
      `|acquia-product:anc| <https://www.drupal.org/project/acquia_connector>`__
      module.
   -  *Drupal 7* - Install and enable the `Acquia Search Multiple
      Indexes <https://www.drupal.org/project/acquia_search_multi_subs>`__
      module

#. Verify that your search installation is configured to switch search
   cores when necessary, as described in the `Configuring automated core
   switching <#autoswitch>`__ section on this page.
#. To prevent searches from returning results for multiple websites,
   configure unique hash values for each website, as described in
   `Ensure correct implementation of Solr
   hashes </acquia-search/multiple-cores/sharing>`__.

If, after completing these steps, your websites still cannot connect to
|acquia-product:as|, see `Troubleshooting multiple search
cores </acquia-search/multiple-cores/troubleshoot>`__ for instructions
about how to resolve common problems with multisite search.


Configuring automated core switching
------------------------------------

After you enable multisite support for |acquia-product:as|, confirm that
|acquia-product:as| is configured to switch search cores when necessary
by performing the steps for your chosen search modules.

.. note::  

   The 
   `Acquia Search Multiple Indexes <https://www.drupal.org/project/acquia_search_multi_subs>`__ 
   must be enabled, or these pages will be inaccessible.


Drupal 7 websites using the Search API module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Ensure that your website is not using any of the code overrides
   included in the `Overriding Solr core automatic connection
   switching </acquia-search/multiple-cores/override>`__ documentation
   page.
#. Sign in to your Drupal website as an administrator.
#. In the top menu, click **Configuration**.
#. In the **Search and metadata** section, click **Search API**.
#. Click **Edit** next to the **Server** that you want to modify.
#. Click the **|acquia-product:as|** section to display its available
   options.
#. Click the **Configure |acquia-product:as|** section to display its
   available options.
#. Select the **Automatically switch when an Acquia Environment is
   detected** check box.


Drupal 7 websites using the Apache Solr module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Ensure that your website is not using any of the code overrides
   included in the `Overriding Solr core automatic connection
   switching </acquia-search/multiple-cores/override>`__ documentation
   page.
#. Sign in to your Drupal website as an administrator.
#. In the top menu, click **Configuration**.
#. In the **Search and metadata** section, click **Apache Solr search**.
#. Click the **Settings** tab, and then click **Edit** for the desired
   search environment.
#. Click the **Configure |acquia-product:as|** section to display its
   available options.
#. Select the **Automatically switch when an Acquia Environment is
   detected** check box.
