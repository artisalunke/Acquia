.. include:: /common/global.rst

Preventing data reporting in |acquia-product:ais|
=================================================

While |acquia-product:ais| provides data that can help you manage your
website performance and security, you may not want all of your websites
to report data. Extraneous websites can skew your real statistics, and
mask true problems you need to address.

Extra websites may be displayed in |acquia-product:ais| because you
have:

-  Old websites that haven't been fully decommissioned
-  Local development websites cloned from websites that were reporting
   to |acquia-product:ais|
-  Websites that were configured to report, but should not have been

You can disable websites from reporting data to |acquia-product:ais|
through:

-  `The Acquia Cloud user interface <#cloud>`__
-  `Drupal's user interface <#drupal>`__

.. _cloud:

Disabling reporting from the |acquia-product:ac| user interface
---------------------------------------------------------------

The fastest way to prevent data reporting is through the
|acquia-product:ac| user interface. Disabling reporting here stops
|acquia-product:ais| from accepting additional data from an application,
but does not delete already reported data or prevent the application
from attempting to report. To disable reporting from the
|acquia-product:ac| user interface, perform the following steps:

#. Sign in to your |acquia-product:ac| account.
#. Select a subscription, then an environment, and then click
   **Insight**.
#. Next to the word **Insight**, you will see a switch. Toggle this
   switch to turn data reporting off. It is on by default, when switched
   to the right side. |Toggle to pause or resume data collection|
#. A confirmation dialog will appear. To disable data collection, click
   **Pause**.

After revoking reporting permissions for an application, the module will
detect the revoked permissions the next time it attempts to send data or
when cron is run, and it will disable itself in Drupal.

.. _drupal:

Disabling reporting from Drupal's user interface
------------------------------------------------

Drupal sends data to |acquia-product:ais| through the
|acquia-product:anc|. You can turn off data reporting at any time,
preventing the application from attempting to connect to
|acquia-product:ais| at all. If you have revoked reporting permissions
in the |acquia-product:ac| user interface, the module will automatically
be disabled when it attempts to report.

.. _local:

Disabling reporting when creating a local environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you create a local copy of an application hosted on
|acquia-product:ac| for development, you can perform the following steps
to prevent this local copy from reporting information back to
|acquia-product:ais|:

#. Sign into your local Drupal application as an administrator.
#. In the administrative menu for Drupal, click **Reports > Status
   report**.
#. You may see a message such as:

   ``Acquia Insight returned the following messages, Further information may be in the logs. A change has been detected in your site environment. Please check the Acquia SPI status on your Status Report page for more information.``

   In the table following the message, under **Acquia Insight, click**
   click the **confirm the action you wish to take** link.

#. On the **Acquia SPI Environment Change Actions** page, select the
   appropriate action:

   -  *Disable this site from sending profile data to Acquia Insight.* -
      Prevents this application from sending any data
   -  *Update existing site with these changes.* - Start reporting from
      the current application, discontinue reporting from the previous
      application
   -  *Track this as a new site on Acquia Insight.* - Continue tracking
      the previous application, and also track this application

#. Click **Submit** to save your preference.

.. _post-install:

Disabling reporting for an existing application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you no longer want an application to report data, you can turn off
data transfer to |acquia-product:ais| by performing the following steps:

#. Sign into your Drupal application as an administrator.
#. Go to your `Acquia Network configuration
   page </acquia-cloud/insight/config#configure>`__.
#. Under **Acquia subscription settings**, deselect the appropriate
   check boxes. If you still want to collect data, but not send it,
   deselect **Send via Drupal cron**.
#. Click **Save configuration**.

Your application will no longer send data to |acquia-product:ais|.

.. _enable:

Re-enabling data collection
---------------------------

To re-enable reporting for an application, you must re-enable the the
application from the |acquia-product:ac| user interface before
re-enabling the module in Drupal.

#. Sign in to your |acquia-product:ac| account.
#. Select a subscription, then an environment, and then click
   **Insight**.
#. Click the **Display score settings** gear icon.
#. Select the check box for **Enable data collection**, and then click
   **Enable**.

You may then sign back in to your Drupal website, and re-enable the
module and its settings.

.. |Toggle to pause or resume data collection| image:: https://cdn2.webdamdb.com/220th_sm_wbUF4PNEFzR6.png?1527105912
  :alt: Toggle to pause or resume data collection

.. |cloud-ui| replace:: \ |acquia-product:ui|\ 
.. _cloud-ui: https://cloud.acquia.com

