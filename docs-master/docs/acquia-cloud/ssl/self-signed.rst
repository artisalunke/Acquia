.. include:: /common/global.rst

Creating a self-signed SSL certificate
======================================

You might want to create a self-signed SSL certificate for an
|acquia-product:ac| application to test the application with SSL on
|acquia-product:ac| before you purchase an SSL certificate. You might
also use a self-signed SSL certificate If you are using a network that
`supports IPv6 </acquia-cloud/manage/ipv6>`__; to support IPv6 on
|acquia-product:ac|, you need an Elastic Load Balancer (ELB) , which
requires supplying an SSL certificate to work with |acquia-product:ac|.

.. _enable:

Enable SSL
----------

To install an SSL certificate, you need to `enable SSL support for an
environment </acquia-cloud/ssl>`__. This feature is not available to
|acquia-product:acfs| users.

.. _create:

Creating SSL certificates
-------------------------

To create a self-signed SSL certificate, you will create both a `root
certificate <#root-cert>`__ and a `site certificate <#site-cert>`__.

.. _root-cert:

Create a root certificate
~~~~~~~~~~~~~~~~~~~~~~~~~

To create a root certificate, complete the following steps:

#. Create a private key for your root certificate. `Connect to your
   environment with SSH </acquia-cloud/ssh/enable#access>`__
#. To ensure that you are in a writable directory (such as
   ``/mnt/tmp/``), use a command similar to the following:

   .. code-block:: none

      openssl genrsa -out root-CA.key 2048

#. Next, enter a command similar to the following example to self-sign
   the certificate:

   .. code-block:: none

      openssl req -x509 -new -nodes -key root-CA.key -days 1024 -out root-CA.pem

#. The following result (or something similar to it) will be displayed.
   Enter the values that are appropriate to your site, system, and
   location.

   .. code-block:: none

      You are about to be asked to enter information that will be 
      incorporated into your certificate request. 
      What you are about to enter is what is called a Distinguished Name or a DN. 
      There are quite a few fields but you can leave some blank 
      For some fields there will be a default value, 
      If you enter '.', the field will be left blank. 
      ----- 
      Country Name (2 letter code) [AU]:US 
      State or Province Name (full name) [Some-State]:Oregon 
      Locality Name (eg, city) []:Portland 
      Organization Name (eg, company) [Internet Widgits Pty Ltd]: My Name (Root CA) 
      Organizational Unit Name (eg, section) []: 
      Common Name (e.g. server FQDN or YOUR name) []:www.mysite.com 
      Email Address []:myusername@mysite.com

The root certificate is created in the same directory, with the name
``root-CA.pem``; its key is created with the name ``root-CA.key``.

.. _site-cert:

Create the site certificate
---------------------------

Next, use the following procedure to create the site certificate.

.. note::  

   You need to use different values for the **Organization Name** than you
   used when creating the root certificate, or the process will fail, and
   the certificate will not work properly.

   You need to use the same values for the **Common Name** that you used
   when creating the root certificate. The ``Common Name`` must begin with
   a subdomain, such as ``www``.

#. Create the private key with the following command:

   .. code-block:: none

      openssl genrsa -out site-key.pem 2048

#. Use the following command to generate the certificate signing request
   (CSR):

   .. code-block:: none

      openssl req -new -key site-key.pem -out site-csr.csr

#. You will be presented with similar text as when you `created the root
   certificate <#step3>`__. Use the same values as you did for the root
   certificate *except for the* **Organization Name***. For the
   **Organization Name**, use a different value, such as
   ``My Name (Site CA)``.

   The following questions will also be displayed:

   .. code-block:: none

      Please enter the following 'extra' attributes 
      to be sent with your certificate request 
      A challenge password []: 
      An optional company name []:

   .. note::  

      Skip ``A challenge password`` by pressing the Enter key.

#. Enter a command similar to this example this to sign the CSR with the
   root key and output in ``PEM`` format with the ``.pem`` extension:

   .. code-block:: none

      openssl x509 -req -in site-csr.csr -CA root-CA.pem -CAkey root-CA.key -CAcreateserial -out site-crt.pem -days 500

The site certificate CSR is created in the same directory, with the name
``site-csr.csr``; the site certificate key is created with the name
``site-crt.pem``, and its key is created with the name ``site-key.pem``.

.. _upload:

Install your certificates
-------------------------

Next, install the root certificate and site certificate, as described in
`Installing an SSL certificate not based on an Acquia-generated
CSR </acquia-cloud/ssl/cert#button>`__. As you install the certificates,
select **Install legacy SSL certificate** to instruct
|acquia-product:ac| to provision an ELB for the environment.

After the **Install SSL certificate** task in |acquia-product:ac| is
completed, an ELB will be provisioned for the environment. Visit the
**SSL** page to verify that the certificate has been installed and visit
the **Servers** page for the environment to see the address of the
domain you'll need to use to create a CNAME record to point to. The
domain address will end with ``elb.amazonaws.com``.

For more information about configuring your DNS settings, see
`Configuring DNS settings with legacy
SSL </acquia-cloud/ssl/cert#dns>`__.
