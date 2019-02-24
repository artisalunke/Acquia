.. include:: /common/global.rst

Email connection
================

To use an email `adaptor </journey/adaptors>`__ with your project, you
must first configure an *email connection* to send emails over a SMTP
connection.

For information about creating, configuring, or testing connections, see
|connections|_.

.. |connections| replace:: Managing \ |acquia-product:aj| \ connections
.. _connections: /journey/connect

.. _properties:

Connection properties
---------------------

The following list describes properties for the email connection:

-  **Type** - The type of email connection. The only available value is
   **SMTP**.
-  **Host** - The IP address or fully qualified domain name of the email
   server.
-  **Port** - The port on which the email server is listening for
   connections.

   -  *Default port* - ``25``
   -  *SSL connections* - ``465``

-  **User Name** - The name of the user to connect to the email server.
-  **Password** - The password for the user to connect to the email
   server.

.. _known:

Email systems known to work with |acquia-product:aj|
----------------------------------------------------

|acquia-product:aj| is known to work with the following transactional
email systems:

-  `Amazon Simple Email Service (SES) <https://aws.amazon.com/ses/>`__
-  `GMail SMTP
   Server <https://support.google.com/a/answer/176600?hl=en>`__
-  `Mailchimp (formerly
   Mandrill) <https://mandrill.zendesk.com/hc/en-us/categories/200277207>`__

   -  Use port 465 instead of the documented and suggested port 587
   -  Ensure that your ``From:`` field is set to a full name and email
      of the form: ``'FirstName LastName '``

-  `Mailgun <http://www.mailgun.com/>`__
-  `Sendgrid <https://sendgrid.com/>`__
