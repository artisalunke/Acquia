.. include:: /common/global.rst

About email in |acquia-product:ac| applications
===============================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/email/*

Your principal contact email is the default return address for your
|acquia-product:ac| applications. The return path is included in the
headers of all email sent by your application and appears as the address
of the email sender. Email error messages are also sent to this address.

|acquia-product:ac| supports `limited outgoing
emails <https://www.acquia.com/about-us/legal/acquia-acceptable-use-policy#email>`__,
such as Drupal registration confirmation emails and node subscription
emails. Because the |acquia-product:ac| email servers are a shared
resource, you cannot send mass emails (such as marketing messages or
newsletters). This service is provided as a courtesy and has no uptime
or service level agreements associated with it. For any mass mailings
that you may need to make, you should instead use other, external email
services or applications with a specified service level for email. For
more information, see `Using a third-party email
service </acquia-cloud/manage/email/3rdparty>`__.

For more information about managing outgoing emails, see
`Troubleshooting Drupal email
issues <%5Bacquia-product:kb%5Darticles/troubleshoot-drupal-mail-issues-without-actually-sending>`__.

The logs for the shared |acquia-product:ac| email servers are not
accessible to customers.

.. admonition:: Note for |acquia-product:acfs| users

   You cannot send email from |acquia-product:acfs| applications. You must
   instead `use a third-party email
   service </acquia-cloud/manage/email/3rdparty>`__.

.. _address:

Configuring the default email return address
--------------------------------------------

If you are an |acquia-product:ace| customer, complete the following
steps to configure the default email return address:

.. note::  

   This feature is not available for |acquia-product:acs| or
   |acquia-product:acfs|.

#. `Sign in <https://cloud.acquia.com>`__ to the |acquia-product:ui|,
   and select the application you want to configure.
#. Click the name of the environment that you want to configure, and
   then click **Configure**.

   |Configure an environment|

#. In the **Sendmail Path** field, enter the default email return
   address.
#. Click **Save**.

.. _spf:

Configuring SPF records
-----------------------

To deal with unwanted email, some email servers refuse email with FROM
addresses in a domain that comes from an unrecognized mail server. Email
servers use the Sender Policy Framework (SPF), as defined in RFC 4408,
to validate the hosts and domains that are allowed to send email.

If you use SPF records, configure the SPF records to include all of
Acquia's defined SPF records for mail servers as allowed senders for
your domain. For detailed instructions, see `Configuring SPF records for
domains on Acquia Cloud </acquia-cloud/manage/email/spf>`__.
Because Acquia does not support whitelisting of its mail server IP
addresses, these IP addresses can change at any time. Acquia supports
only SPF whitelisting.

Issues with emails sent by your Drupal application are typically caused
by one of two problems:

-  Your email reader or company's email server spam filters are blocking
   messages.
-  Mail servers are blocking messages due to missing SPF records for
   Acquia's email servers.

.. _related:

Related topics
--------------

-  `Configuring an environment </acquia-cloud/manage/configure>`__
-  `SMTP Authentication Support
   module <https://www.drupal.org/project/smtp>`__ page at drupal.org

.. |Configure an environment| image:: https://cdn3.webdamdb.com/1280_Mj7Qie9plM93.png?1526475785
