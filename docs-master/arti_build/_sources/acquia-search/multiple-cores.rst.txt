.. include:: /common/global.rst

Using multiple search cores
===========================

.. toctree::
   :hidden:
   :glob:

   /acquia-search/multiple-cores/override/
   /acquia-search/multiple-cores/sharing/
   /acquia-search/multiple-cores/troubleshoot/

.. container:: internal-navigation

   **Multiple Acquia Search cores**

   * Use
   * :doc:`Override </acquia-search/multiple-cores/override>`
   * :doc:`Share </acquia-search/multiple-cores/sharing>`
   * :doc:`Troubleshoot </acquia-search/multiple-cores/troubleshoot>`

|acquia-product:as| supports the use of separate search cores, both by |acquia-product:ac| environment or multisite instance. This allows each environment (Development, Staging, and Production) to have its own separate search core, enabling development and testing using independent Solr configuration and data.

.. note::

    -  Only `Enterprise and Elite subscriptions 
       </support/guide#overview_subscriptions>`__ on |acquia-product:ac| are 
       entitled to multiple Solr cores for a subscription. Other customers can 
       choose to share their single Solr core across websites and environments.
    -  Although this feature requires at least |acquia-product:anc| version
       8.x-1.9 or 7.x-3.1, Acquia recommends that you use `specific versions
       of Drupal modules </acquia-search/modules>`__ for |acquia-product:as|
       with your |acquia-product:as| subscription.
    -  For information about using |acquia-product:as| with
       |acquia-product:edg|, see |acsf-search|_.

Per-environment connection behavior
-----------------------------------

The `Drupal modules </acquia-search/modules>`__  for |acquia-product:as| 
detect the current application's environment and then connect to the
ideal Acquia-hosted Solr core. This default can be overridden.

.. note::

   This functionality was previously provided in the `Acquia Search Multiple Indexes <https://www.drupal.org/project/acquia_search_multi_subs>`__ module, which is now deprecated and should be disabled.

As an example, if your current Acquia subscription (named in this
example ``ABCD-12345``) has three Solr cores:

- ``ABCD-12345.dev.default`` (Development)
- ``ABCD-12345.test.default`` (Staging)
- ``ABCD-12345.prod.default`` (Production)

and you attempt to copy a website between environments, one of following
actions will occur:

- *A valid core is found* |br| 
   An Acquia-hosted website running in the development environment in
   the ``sites/default`` directory will use the
   ``ABCD-12345.dev.default`` core. If you then copy this website to the
   Acquia test environment, the Solr connection will switch to the
   ``ABCD-12345.test.default`` core.
- *No valid core is found* |br| 
   If you do not have a valid Solr core defined for an environment,
   automatic switching will not take place, and the connection will
   switch to read-only mode on the production core. This protects your
   Solr data from being modified by other websites. Without this
   protection, several scenarios could result in data
   corruption/pollution, or even pose security issues (such as
   accidentally exposing privileged information on unwanted websites).
   As an example, if you copy your Acquia-hosted production website to
   an Acquia-hosted environment named ``QA`` and if there is no
   currently-defined ``QA`` Solr core in your subscription, the modules
   will connect in read-only mode to the production core at
   ``ABCD-12345.prod.default``. |br| 
   When the |acquia-product:as| modules enable read-only mode on a
   connection, your website can still run searches against an
   |acquia-product:as| Solr core, even though operations that include
   changing, adding, or deleting content will not work. Without this
   protection, the website copy may delete or otherwise corrupt your
   production Solr core as you edit and delete content, run indexing, or
   run cron. Your visitors will begin to see nonsensical results on
   search pages on your production website, for which the only fix is to
   completely
   `reindex </acquia-search/multiple-cores/sharing#reindex>`__ Solr for
   the production website.

Reviewing the current Acquia Search connection status
-----------------------------------------------------

To determine the current connection status of your website's connection, you can use the Drupal administrative interface and examine the Connection status dialog box.

As a Drupal administrator, use one of the following methods to determine the connection status:

-  Navigate to **Reports > Status report** for a summary of your connections.
-  *Search API module* - 
   Navigate to **Configuration > Search API**, and then click each server name.
-  *Apache Solr Search Integration module* - Navigate to **Configuration > Apache Solr search**, and then click **Edit** for each displayed environment.

Additional troubleshooting may be required if there is a problem
connecting to the core.

.. |acsf-search| replace:: \ |acquia-product:as|\  and \ |acquia-product:edg|\ 
.. _acsf-search: /site-factory/manage/search

