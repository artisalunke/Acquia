.. include:: /common/global.rst

Forwarding logs to an external source
=====================================

Many websites need to forward their log files to a central location for
processing and alerting. |acquia-product:ace| customers with both an
`Elite subscription </support/guide#overview_ace>`__ and an `Acquia
Technical Account
Manager <https://www.acquia.com/products-services/acquia-technical-account-manager>`__
have access to a certain amount of this centralized aggregation for
collectors by using TLS-based log forwarding.

Log forwarding is supported for remote destinations that support a
generic Syslog destination. Acquia uses ``syslog-ng``, which uses TLS
over TCP. If you enable log forwarding, |acquia-product:ac| will forward
all available logs to the remote destination.

.. note::  

   -  Log forwarding is provided on a best-effort basis, and is not
      guaranteed.
   -  You can also view many Acquia-provided log files in the
      |acquia-product:ac| interface. For more information about how to do
      this, see `Streaming log entries in real
      time </acquia-cloud/monitor/logstream>`__.

.. _reqs:

Procedure
---------

If you want your logs forwarded to a remote destination, you must
request that syslog forwarding be enabled by `contacting Acquia
support </support#contact>`__ and providing the following information:

-  IP address of the server to which the logs will be sent
-  Port on which the remote server is listening, usually port 443
-  Environment that you want forwarded
-  CA certificate to use for encrypting traffic - The CA certificate can
   be either a self-signed or a valid certificate and must not require a
   password to unlock. The following is an example of the commands used
   to generate a CA certificate:

   .. code-block:: none

      openssl genrsa -out acquia-ca.key 2048 && openssl req -x509 -new -nodes -key acquia-ca.key -days 1024 -subj "/C=US/ST=MA/L=Boston/O=Acquia/OU=My Website/CN=Acquia/emailAddress=my-username@acquia.com" -out acquia-ca.pem

Log forwarding is supported for a single endpoint. Changing your
endpoint configuration will require a new ticket.

.. _availability:

Log availability
----------------

If log forwarding is enabled, |acquia-product:ac| will forward all of
the generated logs for the following items:

-  `Apache </acquia-cloud/monitor/logs/apache-access>`__
-  `Apache error </acquia-cloud/monitor/logs/apache-error>`__
-  `Drupal request </acquia-cloud/monitor/logs/drupal-requests>`__
-  `Drupal watchdog </acquia-cloud/monitor/logs/drupal-watchdog>`__
-  FPM access
-  `FPM error </acquia-cloud/monitor/logs/fpm-error>`__
-  `PHP error </acquia-cloud/monitor/logs/php-error>`__
-  `Varnish </acquia-cloud/monitor/logs/varnish-request>`__ *(Only for
   websites with dedicated balancers. Logs from shared balancers are not
   supported. Forwarding Varnish logging is not enabled by default.)*

Splunk
------

With some configuration, Acquia supports the use of
`Splunk <http://www.splunk.com/>`__.

`Download this
example <https://gist.github.com/acquialibrary/b45a6996de265494bae9/download>`__
for information about how to set up an Acquia application and
``inputs.conf`` file to use with Splunk services.

.. note::  

   Although Acquia supports log forwarding to Splunk Enterprise accounts,
   Splunk Cloud is not supported due to limitations regarding direct TCP
   log forwarding.

.. _other:

Additional information
----------------------

Acquia does not support other services, such as
`Sumologic <https://www.sumologic.com/>`__ or
`Loggly <https://www.loggly.com/>`__.

Although it may be possible for you to forward logs to your own custom
endpoints, Acquia Support cannot provide any assistance with those
attempts.
