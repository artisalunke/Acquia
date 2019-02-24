.. include:: /common/global.rst

Using New Relic monitoring in a multisite environment
=====================================================

New Relic is a website performance monitoring service that can enable
you to determine where bottlenecks exist in your |acquia-product:ac|
application. After sufficient traffic is requested from that
environment, New Relic will begin to analyze the available data.

If you have a multisite configuration, you can also have New Relic
report data on a per-website basis, which requires that each website
have its own unique New Relic App name. (New Relic's PHP API contains a
`call for setting your app
name <https://docs.newrelic.com/docs/php/the-php-api#api-set-appname>`__.)
This data is available only for the environment as a whole, and you view
it by selecting the appropriate ``sitename.env`` option from the list of
available applications (for example, ``mysite.prod``.)

.. note::  

   Because custom application names that define individual websites are
   initialized later in the Drupal bootstrap process, New Relic cannot
   report on Drupal modules, views, and hooks on a per-domain basis when
   this method is used.

.. _proc:

Procedure
---------

For each Drupal website that you want to monitor with New Relic,
complete the following steps, depending on if you are using
|acquia-product:ac| or |acquia-product:edg|:

|acquia-product:ac|
 Add the following code to the end of the website's ``settings.php`` file:

 .. code-block:: php

    if (extension_loaded('newrelic')) { 
      $exploded_path = explode('/', dirname(__FILE__)); 
      $site_domain = array_pop($exploded_path); 
      newrelic_set_appname("$site_domain;CURRENT_APP_NAME", '', 'true'); 
    }

|acquia-product:edg|
 For a ``post-settings.php`` hook script to use with your websites, see 
 `Altering values in settings.php with hooks </site-factory/extend/hooks/settings-php>`__.

.. _vars:

Code variable descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``$site_domain`` variable is assigned the name of the folder for
this particular ``settings.php`` file. This appears in your list of
applications on New Relic's website. To find this list, go to
https://rpm.newrelic.com.

The ``newrelic_set_appname()`` function uses the following three
parameters:

-  | **APP_NAME(s)** - New Relic allows each trace to be reported to up
     to three app names, but only one is necessary. Multiple app names
     make it possible to have New Relic both monitor the individual
     websites, but still keep monitoring the multisite as a whole to get
     an overview of how the entire application / docroot is performing.
   | In the preceding code, replace ``CURRENT_APP_NAME`` with whatever
     the New Relic App name currently is. You can find this in New Relic
     under **Settings > Environment > Agent initialization**. Look for
     ``newrelic.appname``. It needs to be exactly the same, or New Relic
     will create a new application and the trace history will be broken.
   | The app name displayed in New Relic can be different from the
     actual New Relic app name, since it is possible to manually change
     the displayed name in the New Relic interface.

   .. important:: 

      It is important that the website-specific app name comes before the
      catch-all, because the first app name is the unique identifier. For
      more information, see `New Relic's
      documentation <https://docs.newrelic.com/docs/php/php-agent-phpini-settings#inivar-appname>`__
      on the topic.

-  The **New Relic subscription key** - Leave this value blank to use
   the global key.
-  The **xmit identifier** - If set to ``true``, New Relic will keep the
   trace collected so far. This has a slight performance impact.

For additional documentation regarding New Relic, see their
`documentation website <https://docs.newrelic.com/docs>`__.
