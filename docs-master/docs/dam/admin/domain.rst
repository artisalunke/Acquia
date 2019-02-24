.. include:: /common/global.rst

Using a custom domain name
==========================

You can customize your |acquia-product:dam| domain name to match your
company's domain name, such as ``images.company.com``.

All |acquia-product:dam| accounts are securely encrypted using Secure
Socket Layer (SSL). To ensure your |acquia-product:dam| account is
always secure, we require you to provide an SSL certificate when
implementing custom domains for your account.

.. _start:

Getting Started
---------------

#. `Contact Acquia Support </support#contact>`__ if your company is
   interested in implementing a custom domain.
#. Obtain an SSL certificate for your custom domain. Here are two
   options for obtaining an SSL certificate:

   -  Purchase an SSL certificate for the custom domain from a
      certificate signing request (CSR). You can request a certificate
      signing request (CSR) from your Acquia Account Manager.
   -  A CSR is required for purchasing an SSL certificate.
   -  Your IT team may already have a process for obtaining an SSL
      certificate. |acquia-product:dam| will require the private key in
      addition to the SSL certificate.

#. Provide your SSL certificate to Acquia Support.
#. Have your IT team set up a CNAME record for the custom domain to
   point to your |acquia-product:dam| domain.

Acquia will notify you when the SSL certificate is set up. At that
point, you will be able to securely access your |acquia-product:dam|
account through your custom domain.

.. _moreinfo:

Additional information
----------------------

|acquia-product:dam| supports the following certificate types:

-  Single domain (most common)
-  Subject alternative name (SAN)

|acquia-product:dam|-installed certificate are on an Apache web server,
and any certificate that you provide must be in PEM format.
