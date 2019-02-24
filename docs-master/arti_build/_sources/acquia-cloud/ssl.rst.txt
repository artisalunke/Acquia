.. include:: /common/global.rst

Enabling SSL
============

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/ssl/*

.. container:: internal-navigation

   **Using SSL**

   * Introduction
   * :doc:`Generate </acquia-cloud/ssl/csr>`
   * :doc:`Purchase </acquia-cloud/ssl/purchase>`
   * :doc:`Manage </acquia-cloud/ssl/cert>`

SSL enables your web application to use the HTTPS secure web protocol to
safely communicate with your users online. To use SSL, your environment
must have an SSL certificate, which you must purchase from a Certificate
Authority (CA) or SSL certificate vendor and upload to
|acquia-product:ac|.


.. important::
   
   If you are an |acquia-product:acfs| customer, SSL is not supported.
   `Learn more about Acquia Cloud Free </acquia-cloud/free>`__ and how
   to upgrade your |acquia-product:ac| subscription.

.. _sni:

Standard certificates and legacy certificates
---------------------------------------------

|acquia-product:ac| offers two models for SSL support: the standard
model and the legacy model.

The *standard model* uses Server Name Indication (SNI). SNI is an
extension to the TLS protocol that serves multiple certificates from the
same IP address and TCP port number, enabling more than one website to
use HTTPS from the same IP address, but without requiring all websites
to use the same SSL certificate.

.. note::

    Acquia supports newer versions of TLS. The acronyms TLS (Transport Layer
    Security) and SSL (Secure Socket Layer) are often used interchangeably.
    For consistency, Acquia's documentation and the |acquia-product:ui|
    generally refer to SSL. For more information, see `What's the difference
    between SSL, TLS, and
    HTTPS? <https://security.stackexchange.com/questions/5126/whats-the-difference-between-ssl-tls-and-https>`__.

The *legacy model* uses a domain name-based system (rather than an IP
address-based system) and requires use of an Elastic Load Balancer
(ELB). Those certificates are labeled as **legacy certificates** in the
|acquia-product:ui| **SSL** page. Legacy certificates continue to
function as normal on |acquia-product:ac|.

While both methods are currently accepted, Acquia strongly recommends
that you use the standard model with your certificates.
|acquia-product:ace| customers with multi-region servers are strongly
suggested to use the standard model.

It is possible, however, to have a standard and a legacy certificate
installed in the same environment at the same time. To do, complete the
following items:

-  To use the legacy certificate, you will need to repoint the DNS
   settings for your domains to the provided ``CNAME``.
-  To use the standard certificate, you will need to confirm that the
   DNS settings for your domain are pointed to your assigned IP address.

If you have a legacy certificate (which works with the ELB) you can
separately add the new certificate, and then update to the Elastic IP
address (EIP) as necessary.

If an Acquia-managed SSL certificate is installed directly on an
application's load balancers and the self-service SSL facility is used
to activate a certificate, the newly activated certificate will then
take priority.

.. note::

    If you use Akamai and upgrade your application from a legacy certificate
    to a standard certificate, you must contact Akamai to inform them that
    your application's certificate is now based on SNI. Not informing Akamai
    of the change will cause Akamai to not work with your application.

.. _diff:

Differences in support for the standard and legacy models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Standard                          | Legacy                            |
+===================================+===================================+
| Support for bare domains (for     | No support for bare domains       |
| example, ``example.com`` rather   | without additional configuration  |
| than ``www.example.com``). This   | and services, since the load      |
| is possible because the load      | balancer is addressed by CNAME,   |
| balancer has an Elastic IP        | rather than by IP address         |
| address (EIP)                     |                                   |
+-----------------------------------+-----------------------------------+
| Install certificate on any        | Install certificate only on       |
| environment                       | Production environment on         |
|                                   | |acquia-product:ace|; one         |
|                                   | certificate can cover all         |
|                                   | environments on                   |
|                                   | |acquia-product:acs|              |
+-----------------------------------+-----------------------------------+
| Install any number of             | Install only one certificate -    |
| certificates on an environment    | installing a new certificate      |
| (*only one certificate can be     | overwrites the previous one       |
| active at any time*)              |                                   |
+-----------------------------------+-----------------------------------+
| Not supported by some `very old   | Supported by old and new browsers |
| browsers <https://en.wikipedia.or |                                   |
| g/wiki/Server_Name_Indication#Sup |                                   |
| port>`__                          |                                   |
+-----------------------------------+-----------------------------------+
| Does not use ELBs and uses        | Uses ELBs in an HA configuration, |
| active/passive load balancers in  | which offer round-robin load      |
| an HA configuration               | balancers, instead of             |
|                                   | active/passive load balancers     |
+-----------------------------------+-----------------------------------+
| Load balancer requests have a 600 | All requests through an ELB have  |
| second timeout                    | a 60 second timeout               |
+-----------------------------------+-----------------------------------+

.. _permissions:

Roles and permissions for SSL management
----------------------------------------

|acquia-product:ac| provides these two permissions for managing SSL:

-  Add or remove SSL certificates for the non-production environments
-  Add or remove SSL certificates for the production environment

By default, users with the *Administrator*, *Team Lead*, and *Senior
Developer* roles have these permissions, while users with the
*Developer* role do not. Learn more about `roles and
permissions </acquia-cloud/teams/roles>`__.

.. important:: 

    Do not email your SSL certificate or attach your SSL certificate to a
    support ticket. Instead, if you need to transmit a certificate to Acquia
    other than through the |acquia-product:ui|, `contact Acquia
    Support </support#contact>`__ and we will advise you how to upload your
    SSL certificate and private key securely.

.. _billing:

SSL on |acquia-product:acs|
---------------------------

There is an additional charge for using legacy SSL certificates for an
|acquia-product:acs| subscription — the charge is per
|acquia-product:acs| codebase. You can use a multidomain SSL
certificate, however, and will be charged only for one certificate. If
you pay for |acquia-product:acs| using purchase orders, contact your
salesperson to get SSL set up. For more details, see `About
billing </support/billing>`__.

.. _ace:

SSL on |acquia-product:ace|
---------------------------

There is no extra charge for |acquia-product:ace| subscriptions. Acquia
strongly suggests these subscriptions use the standard model.

SSL on |acquia-product:ace| should generally be self service. However,
some customer configurations may require additional assistance.

-  Customers who have a `Premium, Enterprise, or
   Elite </support/guide#overview_subscriptions>`__ subscription. These
   customers can still buy a certificate through us, but Acquia will no
   longer install certificates provided by customers.
-  Customers who have purchased a certificate purchased through Acquia
   which needs to be updated until the customer renews.

If you are a customer that falls into one of these categories, contact
`Acquia Support </support#contact>`__.

.. _related:

Related topics
--------------

-  `Best practices for a fully SSL-protected
   site <https:support.acquia.com/articles/best-practices-fully-ssl-protected-site>`__
-  `Watch a video about managing certificates in
   Acquia Cloud <https://player.vimeo.com/video/195992204>`__
