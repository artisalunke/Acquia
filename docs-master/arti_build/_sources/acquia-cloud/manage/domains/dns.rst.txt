.. include:: /common/global.rst

Pointing DNS records to your public IP addresses
================================================

Each |acquia-product:ac| application has a single public IP address.
This is true even if it is an |acquia-product:ace| application is hosted
on a high-availability hosting cluster of several web servers. This
address points to a load balancer that detects incoming connections to
your application and spreads them among the cluster of web servers.

For your application to be available on the Internet, incoming
connections must go to the |acquia-product:ac| load balancer. You can
enable this through your DNS provider by pointing your domain name's A
record entry to the public IP address. In your DNS provider's web
interface, change the A record entry for your domain name to point to
the public IP address, which is listed on the Domain page of the
|acquia-product:ui|. For example, suppose your application's domain name
is ``www.example.com`` and your public IP address is 123.123.123.123.
Set the A record entry for ``www.example.com`` to 123.123.123.123.

|Your site's IP address|

Do not set your domain name's CNAME entry to an ``acquia-sites.com``
domain. Doing so can make your application load more slowly, and can
cause unpredictable results or even downtime, especially if
configuration changes are being made or tested to the load balancers. In
addition, DNS service is not included in Acquia's uptime guarantee. This
means that if the Acquia DNS provider has an outage, requests to
``*.prod.acquia-sites.com`` would fail to resolve, and any domains that
are pointed to the Acquia domain (rather than to a public IP address or
an Elastic Load Balancer) would fail.

.. note::  

   Acquia does not provide reverse DNS services.

.. _elb:

DNS settings with an Elastic Load Balancer
------------------------------------------

If you have an Elastic Load Balancer (ELB) for your application (which
would be the case if you have `enabled a legacy SSL certificate for your
application </acquia-cloud/ssl#sni>`__), instead of changing the A
record entry, `change the CNAME
entry </acquia-cloud/ssl/cert#activate>`__ for your domain name. In your
DNS provider's web interface, change the CNAME entry for your domain
name to point to the URL of your |acquia-product:ac| environment, which
will be the URL of your Elastic Load Balancer and which is listed on the
|acquia-product:ui| Domains page for the environment. Don't use a DNS A
record to point to the underlying IP address of the ELB, since the IP
address may change from time to time.

For example, suppose your application's domain name is
``www.example.com`` and your Production environment's URL is
``ab-1234-us-east-1.elb.amazonaws.com``. Set the CNAME entry for
``www.example.com`` to ``ab-1234-us-east-1.elb.amazonaws.com``.

.. note::  

   The URL of your |acquia-product:ac| environment may be too long for some
   DNS providers. Verify with your DNS provider to ensure that they can
   handle a CNAME for a URL of that length.

Acquia may require verification of your DNS TXT record. If that is the
case, the verification will be sent with a hash value.

.. _eip:

Using an Elastic IP address
---------------------------

An |acquia-product:ac| application can use an Elastic IP Address (EIPs)
in order to have a static IP address assigned to its server instance.
Without an Elastic IP, your instances' IP addresses are subject to
change at any time as the underlying hardware is relaunched or replaced.
For most purposes, that doesn't make a difference for
|acquia-product:ac| applications. However, you might want to use EIPs if
it is important to you to maintain the same IP address, for example, so
that you can add them to a whitelist, integrate them with a
Single-Sign-On (SSO) solution, or use a third-party service that
requires a static IP address.

An EIP persists when a server is relaunched or rebooted. It will be lost
if a server is suspended — for example, after being removed due to a
downsize.

For |acquia-product:ace| customers, using EIPs can reduce your
flexibility if you need additional server capacity to meet increased
application traffic. While Acquia can quickly provision new instances
for your application in response to demand, the additional instances
can't be brought into service until the new EIPs associated with them
can be added to your whitelist or other system.

.. _changes:

Changes to IP address
---------------------

If you have an existing application that is hosted on
|acquia-product:ace| and you move the application to
|acquia-product:vpn|, your IP address will change (which includes any
elastic IP addresses (EIPs)). IP addresses cannot be moved into or out
of a Virtual Private Cloud (VPC).

As a result, when you set up your application in |acquia-product:vpn|,
you need to point the DNS records of your application to the new IP
address in the VPC. For more information, see |shieldlink|_.

.. |shieldlink| replace:: \ |acquia-product:vpc|\ 
.. _shieldlink: /acquia-cloud/shield

.. _related:

Related topics
--------------

-  `Enabling SSL </acquia-cloud/ssl>`__

.. |Your site's IP address| image:: https://cdn4.webdamdb.com/1280_wPWk2oP5Q0Y1.png?1526475804
   :width: 700px
   :height: 281px
