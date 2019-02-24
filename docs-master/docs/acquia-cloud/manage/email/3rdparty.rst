.. include:: /common/global.rst

Using a third-party email service
=================================

A Drupal application may need to send email for several purposes, such
as password resets, user registrations, or other notifications. However,
you cannot send email from |acquia-product:acfs| sites. To send email
from an |acquia-product:acfs| site, you'll need to use a third-party
email service. One email service that integrates easily with Drupal
applications is `SendGrid <http://sendgrid.com/>`__, a cloud-based
service that lets you send up to 200 emails per day for free.

.. _sendgrid:

Using SendGrid with |acquia-product:ac|
---------------------------------------

To use SendGrid as an email service for your |acquia-product:ac|
application:

#. `Sign up <https://sendgrid.com/user/signup>`__ for a SendGrid
   account.
#. Download, install, and enable the
   `SMTP <https://www.drupal.org/project/smtp>`__ Drupal module.
#. Configure the SMTP module with your SendGrid account settings.

Advanced users

In addition to the Drupal module, you can also use the Sendgrid API to
send email. See `How to Send an SMTP
Email <https://sendgrid.com/docs/API_Reference/SMTP_API/getting_started_smtp.html>`__
for more information.

.. _mod:

Configuring the SMTP module
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure the SMTP module:

#. Sign into your Drupal application as an administrator and go to the
   **Admin > Configuration** page for the SMTP module.

   |Configure the SMTP module|

#. Under **Install Options**, select **On** to turn the module on.
#. Under **SMTP Server Settings**, enter the following:

   -  SMTP server: ``smtp.sendgrid.net``
   -  SMTP port: ``25``

#. Under **SMTP Authentication**, enter the following:

   -  Username: Your SendGrid username
   -  Password: Your SendGrid password

#. Under **Email options**, enter a valid from address and a name for
   the sender of the email (such as your name or your site's name).
#. Click **Save configuration**.

You can also use encryption with your connection. Instead of the
previous values, use the following values in the appropriate places:

-  Set the SMTP port to ``587``
-  Set **Use encrypted protocol** to ``TLS``.

Your Drupal application can now send email through SendGrid.

There are many other third party mailing services available. As always,
it is important to do your research and select the one that best
integrates with your service needs.

Related topics
~~~~~~~~~~~~~~

-  `About email in your Acquia Cloud
   environment </acquia-cloud/manage/email>`__
-  `Acquia Cloud Free subscriptions </acquia-cloud/free>`__

.. |Configure the SMTP module| image:: https://cdn4.webdamdb.com/1280_ksespK8Sk481.png?1526475715
   :width: 590px
   :height: 461px
