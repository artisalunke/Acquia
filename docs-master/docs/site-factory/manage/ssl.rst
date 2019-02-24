.. include:: /common/global.rst

HTTPS (SSL) and |acquia-product:edg|
====================================

HTTPS is a secure web protocol that allows each of your websites to
safely communicate with your website visitors.

Enabling SSL
------------

If you have dedicated load balancers and want to create a new
certificate or add domain names to an existing Unified Communications
certificate (UCC), perform the following steps to enable or update
HTTPS/SSL for your |acquia-product:edg| websites with custom domain
names:

#. Generate a Certificate Signing Request (CSR) through the command-line
   interface, as described in 
   `Creating CSR files </acquia-cloud/ssl/csr/cli>`__.
#. After you generate and copy the CSR, use it to 
   `obtain an SSL certificate </acquia-cloud/ssl/purchase>`__. If you need to cover
   multiple domains, you should obtain a Unified Communications
   certificate (UCC).
#. Upload the certificate, any intermediate certificate files, and
   private key, using the methods outlined in `How to securely provide
   information to Acquia
   Support </article/how-securely-provide-information-acquia-support>`__.
   *Do not email your SSL certificate or attach your SSL certificate to
   a support ticket.*
#. `Contact Acquia Support </support#contact>`__ to request the
   certificate be installed or updated for you. Only one certificate may
   be active at any time.

If you do not have your own dedicated load balancers, 
`contact Acquia Support </support#contact>`__ and request that Acquia add your website
to the shared SSL certificate for |acquia-product:ac|.

.. note::  
   
   SSL is not available for subdomains of ``acsitefactory.com``.

If you have any questions or uncertainty about the method that you
should use to enable HTTPS/SSL for your websites, 
`contact Acquia Support </support#contact>`__.


SSL and Varnish cache
---------------------

By default, pages and other assets sent over SSL do not use the Acquia
hosting platform's Varnish cache. If a significant portion of your
websites use SSL, you can significantly improve your websites'
performance by enabling SSL traffic through Varnish. To do this,
`contact Acquia Support </support#contact>`__ or your Technical Account
Manager.
