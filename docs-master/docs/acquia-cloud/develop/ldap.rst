.. include:: /common/global.rst

Using LDAP with an |acquia-product:ac| application
==================================================

You can configure your |acquia-product:ac| website to communicate with
the LDAP (Lightweight Directory Access Protocol) server on your internal
network and access the directory information it contains. Use LDAP only
if you do not require a web-friendly single sign-on (SSO) system (such
as SimpleSAML).

.. _enable:

Enable LDAP: Main steps
-----------------------

Complete these main steps to enable communication between your LDAP
server and your |acquia-product:ac| application:

#. `Install and enable the LDAP module <#md>`__.
#. `Optionally, get an Elastic IP address (EIP) for your
   |acquia-product:ac| environments <#eip>`__.
#. `Configure SSL/TLS (Secure Sockets Layer/Transport Layer Security)
   certificate validation <#validation>`__.
#. `Test your connection to the LDAP server <#test>`__.
#. `Configure LDAPS </acquia-cloud/develop/ldaps>`__.

.. _md:

Install and enable the LDAP module
----------------------------------

Make sure that your code repository contains a properly installed and
enabled LDAP integration module for your application that matches your
installed version of Drupal:

-  *Drupal 8.x* - `Download the version 8.x
   module <https://www.drupal.org/project/ldap>`__ from the LDAP project
   page at Drupal.org.

   Note

   The Drupal 8 version is currently in alpha state. To use LDAP
   Authorization, you need the
   `Authorization <https://www.drupal.org/project/authorization>`__
   module.

-  *Drupal 7.x* - `Download the version 7.x
   module <https://www.drupal.org/project/ldap>`__ from the LDAP project
   page at Drupal.org.

.. _eip:

Get EIPs for your |acquia-product:ac| environments (optional)
-------------------------------------------------------------

Depending on how your LDAP server is configured, you may need to
whitelist your |acquia-product:ac| Production or non-Production
environments or both. Since the IP address of an |acquia-product:ac|
server instance can change at any time, this may require you to get a
static IP address, using an Elastic IP (EIP) address. To get an EIP for
your |acquia-product:ac| environments, open an Acquia support ticket.
For more information, see `Using an Elastic IP
address </acquia-cloud/manage/domains/dns#eip>`__.

.. _validation:

Configure SSL/TLS certificate validation
----------------------------------------

The best practice in a production environment is to use SSL and
certificate validation for communication between your LDAP server and
your |acquia-product:ac| website, as described in `Configuring
LDAPS </acquia-cloud/develop/ldaps>`__. Initially, however, configure
your system to not require certificate validation.

Turn off SSL/TLS certificate validation in ldap.conf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create an ``ldap.conf`` file that includes this line:

``TLS_REQCERT never``

You can put this file anywhere that your application can access. The
best place is in your application's codebase, at the same level, but not
in your application's docroot. For example, you could create a directory
named ``ldap`` and put the ``ldap.conf`` file there.

Specify the location of your ``ldap.conf`` file with an environment
variable, ``LDAPCONF``. For example, add a line like this to your
``settings.php`` file:

``putenv('LDAPCONF=../ldap/ldap.conf');``

As a simpler alternative, instead of creating an ``ldap.conf`` file, you
can add this line to your ``settings.php`` file:

``putenv('LDAPTLS_REQCERT=never');``

.. _test:

Test your connection to the LDAP server
---------------------------------------

Test whether your application can connect to the LDAP server. `Connect
to your server with SSH </acquia-cloud/ssh>`__, and then enter a command
similar to the following:

``openssl s_client -connect [ldapserver.address.com]:[port]``

.. _secure:

Final step - Set up secure communication
----------------------------------------

After you have confirmed that your website can connect to the LDAP
server, set up secure communication with LDAPS, as described in
`Configuring LDAPS </acquia-cloud/develop/ldaps>`__.
