.. include:: /common/global.rst

Obtaining an SSL certificate
============================

.. container:: internal-navigation

   **Using SSL**

   * :doc:`Introduction </acquia-cloud/ssl>`
   * :doc:`Generate </acquia-cloud/ssl/csr>`
   * Purchase
   * :doc:`Manage </acquia-cloud/ssl/cert>`

After you `generate a Certificate Signing Request
(CSR) </acquia-cloud/ssl/csr>`__ for an environment, the next step in
enabling SSL is to obtain an SSL certificate.

You can purchase SSL certificates from many vendors. Each vendor will
have its own prices and purchase process, but all of them should accept
the CSR that you generated and copied using the |acquia-product:ui| and
the procedure described in `Generating a Certificate Signing Request
(CSR) </acquia-cloud/ssl/csr>`__. Paste the encoded CSR into the
vendor’s purchase form. You can use any type of SSL certificate with
|acquia-product:ac|, including single domain, multidomain (Unified
Communications Certificate (UCC) /Subject Alternative Name (SAN)),
wildcard, extended validation, and even self-signed certificates. If
your vendor requires you to specify the server type for the certificate,
choose nginx or, as a second choice, Apache.

.. _vendor:

Selecting a vendor
------------------

In general, certificates from reputable vendors will work properly on
|acquia-product:ac|. In some cases, you may need to locate and upload
intermediate certificates, depending on your vendor and the architecture
of your application.

Acquia is aware of the following issues:

-  *Let's Encrypt* - Acquia does not support the one-click renewal
   feature from Let's Encrypt, but the certificates are valid and will
   work if installed through the |acquia-product:ui|.
-  *No Elliptic Curve (EC) format support* - |acquia-product:ac| does
   not support the `Elliptic Curve Diffie
   Hellman <https://wiki.openssl.org/index.php/Elliptic_Curve_Diffie_Hellman>`__
   format for certificates.

Certificate requirements
------------------------

Be aware of the following requirements when you obtain your certificate:

-  The SHA-1 cryptographic hash algorithm is being deprecated. You
   should ensure that the SSL certificate you purchase uses an SHA-2
   signature. For more information, see `Deprecation of SHA-1 for SSL
   certificates <%5Bacquia-product:kb%5Darticles/deprecation-sha-1-ssl-certificates>`__.
-  SSL certificates must be Base64 encoded. |acquia-product:ac| will not
   install certificates without Base64 encoding.

.. _chain:

About SSL certificates and chain certificates
---------------------------------------------

Your website's SSL certificate is at the head of a chain of certificates
that starts with your website and ends at a root certificate, issued by
a trusted Certificate Authority, or CA. Every certificate indicates who
it was issued by and who it was issued to, which enables web browsers to
follow the chain to see if the certificates should be trusted.

Your SSL certificate vendor will provide you with an SSL certificate and
may possibly also provide you with additional certificates, called
Certificate Authority intermediate certificates or chain certificates.
If your SSL certificate vendor is Thawte, `click here to see the
intermediate
certificate <https://www.tbs-certificates.co.uk/FAQ/en/thawte_ssl_ca_g2.html>`__.
If your SSL certificate depends on one or more Certificate Authority
intermediate certificates, you need to `install
them </acquia-cloud/ssl/cert#install>`__ on your |acquia-product:ac|
environment along with the SSL certificate.

Some SSL certificate vendors can combine multiple certificates into a
single certificate. Combined certificates of this nature have not been
extensively tested on the |acquia-product:ac| platform, but Acquia is
not aware of any issues with these certificates on our platform.

.. _self:

Self-signed certificates
------------------------

For some limited purposes, such as `enabling IPv6
support </acquia-cloud/manage/ipv6>`__ without SSL, or testing SSL, you
can create a self-signed SSL certificate to use with
|acquia-product:ac|. You can then upload this self-signed certificate
instead of purchasing a certificate. For more information, see `Creating
a self-signed SSL certificate </acquia-cloud/ssl/self-signed>`__.

.. _install:

Next step
---------

After you receive an SSL certificate from your SSL certificate vendor,
install it on your |acquia-product:ac| environment. See `Managing SSL
certificates </acquia-cloud/ssl/cert>`__ for information about how to do
this.
