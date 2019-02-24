.. include:: /common/global.rst

Configuring LDAPS
=================

As described in `Using LDAP with an |acquia-product:ac|
application </acquia-cloud/develop/ldap>`__, you can configure an
|acquia-product:ac| application to communicate with the LDAP server on
your internal network and access the directory information it contains.
That document described the basics of configuring an |acquia-product:ac|
application and LDAP. This document describes how to configure LDAPS
(LDAP over SSL), which uses SSL to secure communication between your
|acquia-product:ac| application and your LDAP server.

.. _before:

Before you begin
----------------

Before you enable LDAPS, follow the procedures described in `Using LDAP
with an |acquia-product:ac| application </acquia-cloud/develop/ldap>`__.

-  Configure your LDAP server to use LDAPS (LDAP over SSL) for secure
   LDAP communications.
-  Optionally, install a firewall (or its equivalent) on your network
   between the LDAP server and |acquia-product:ac|. VPNs (Virtual
   Private Networks) are *not* currently supported for this purpose.

.. _enable:

Enable LDAPS: Main steps
------------------------

You need to complete these main steps to enable SSL communication
between your LDAP server and your |acquia-product:ac| application:

#. `Locate the CA (certificate authority) certificate
   chain <#locate>`__.
#. `Convert the certificate to PEM format <#pem>`__.
#. `Verify that the certificate works <#test>`__.
#. `Add the CA certificate to your repository <#repository>`__.
#. `Set the environment variable with the certificate's
   location <#env>`__.

.. _locate:

Locate the CA certificate chain
-------------------------------

To communicate with your LDAP server, your |acquia-product:ac|
application needs access to the CA certificates used to secure
communications. If you don't already know where these certificates are,
you may be able to use the ``openssl s_client`` command to view details
about the certificates:

``openssl s_client -connect [ldapserver.address.com]:[port]``

Use the URL and port number of your LDAP server. This command should
return information about the CA certificate chain used by the LDAP
server and the success or error messages for any certificates that are
not present on your machine.

After you've located the CA certificates, download them to your local
machine. There may be multiple PEM files required to complete the SSL
chain. Combine all these files into a single PEM file.

.. _pem:

Convert the certificate to PEM format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the certificate is not provided in PEM format, you need to convert
it. If the certificate is in PEM format, it will contain the lines
"BEGIN CERTIFICATE" and "END CERTIFICATE" with base64 encoded data
between them. If it is in DER format, it will contain binary data.

To convert from DER to PEM format, use the following command:

``openssl x509 -in input.der -inform DER -out output.pem -outform PEM``

.. _test:

Verify that the certificate works
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you download and (if necessary) convert the CA certificate, you
should verify that it works to communicate with the LDAP server using
the following command:

``openssl s_client -connect [ldapserver.address.com]:[port] -CAfile        /path/to/certificate/file/certificatefilename.pem -quiet``

This command should return something like this:

``depth=2 /C=US/O=Equifax/OU=Equifax Secure Certificate Authority verify return:1 depth=1 /C=US/O=InterMediate Inc/CN=InterMediate Certificate Authority verify return:1 depth=0 /C=US/ST=California/L=Xanadu/O=Example Inc/CN=*.example.com verify return:1``

If the certificate succeeds, this command should return
``verify return:1`` at every level of the certificate chain. If it
returns ``verify return:0``, you are still missing one or more
certificates in the chain. You will need to find the missing
certificates and package them with your existing certificate into a
single PEM file.

.. _repository:

Add the CA certificate to your |acquia-product:ac| code repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CA certificate needs to be available to your PHP code. To do this,
add it to your application's code repository:

#. Create a directory named ``ldap``. Place this directory in your code
   repository above the ``docroot``, so that it is not accessible on the
   web.
#. Copy the CA certificate into the ``ldap`` directory.

.. _env:

Set the environment variable with the certificate's location
------------------------------------------------------------

Make the CA certificate location known to the LDAP functions in PHP by
setting the ``LDAPTLS_CACERT`` environment variable in the
``settings.php`` file of your application. Add this to ``settings.php``:

``if (isset($_ENV['AH_SITE_GROUP']) && isset($_ENV['AH_SITE_ENVIRONMENT'])) {   $ldap_cacert = "/var/www/html/" .      $_ENV['AH_SITE_GROUP'] . "." .     $_ENV['AH_SITE_ENVIRONMENT'].     "/ldap/[PEM_FILE].pem";    if (file_exists($ldap_cacert)) {     putenv("LDAPTLS_CACERT=$ldap_cacert");   } }``

where ``[PEM_FILE]``\ is the name of the ``.pem`` certificate file.

The application should now be able to make an SSL connection to the
remote LDAP server.
