.. include:: /common/global.rst

Troubleshooting multiple search cores
=====================================

Multiple |acquia-product:as| cores

-  `Use </acquia-search/multiple-cores>`__
-  Override
-  `Share </acquia-search/multiple-cores/sharing>`__
-  Troubleshoot

Under some conditions, a website administrator might see information
like the following in the Solr connection status:

    To protect your data, the [Acquia Search / Search API Acquia] module
    is enforcing read-only mode on the indexes, because it could not
    figure out what Acquia-hosted Solr core to connect to. This helps
    you avoid writing to a production index if you copy your site to a
    development or other environment(s). These index IDs would have
    worked, but could not be found on your Acquia subscription:

    -  ABCD-12345.qa.mysiteXYZXYZ12345
    -  ABCD-12345.qa.default

This message indicates one of the following situations:

-  Your current subscription does not contain a Solr core that belongs
   to the current environment (for example, ``dev``, ``stage``, or
   ``prod``) or to the current Drupal multisite instance.
-  The modules have forced the Solr connection into `read-only
   mode </acquia-search/multiple-cores/sharing>`__ to prevent operations
   that could cause index corruption.

If you receive a message like this, refresh your Acquia subscription on
your Drupal website by using the following steps:

#. As an administrator on your Drupal website, go **Reports > Status
   Report**.
#. To the right of **Acquia subscription status**, click **Manually
   refresh the subscription status**.

.. _continue:

If you continue to see the error
--------------------------------

If your website continues to display the message, you can take further
corrective steps based on your website's environment and subscription
level:

*If you have an Enterprise/Elite subscription...*

-  *…and the website is hosted on |acquia-product:ac|*, take one of the
   following actions:

   -  `contact Acquia Support </support#contact>`__ to request any
      additional or missing Solr cores. Be sure to attach the status
      messages and website URL(s) from the problem website.
   -  Configure the connection by `overriding the Drupal
      variables </acquia-search/multiple-cores/override>`__.
   -  Take no action, which will cause the website or environment to use
      your production Solr core in read-only mode, allowing you to test
      search using the production website’s Solr core.

-  *…and the website is not hosted within |acquia-product:ac|*, take one
   of the following actions:

   -  Configure the connection by `overriding the Drupal
      variables. </acquia-search/multiple-cores/override>`__
   -  Take no action, which will cause the website or environment to use
      your production Solr core in read-only mode, allowing you to test
      search using the production website’s Solr core.

*If you have a different subscription level* (in which case you are
entitled only to a single Solr search core for your entire
subscription), take one of the following actions:

-  Configure the connection by `overriding the Drupal
   variables. </acquia-search/multiple-cores/override>`__
-  Take no action, which will cause the website or environment to use
   your production Solr core in read-only mode, allowing you to test
   search using the production website’s Solr core.
