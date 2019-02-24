.. include:: /common/global.rst

Using IPv6 IP addresses
=======================

|acquia-product:ac| supports
`IPv6 <http://en.wikipedia.org/wiki/IPv6>`__ IP addresses. In order to
use IPv6 for your website, you need to:

-  `Enable SSL for your site <#ssl>`__ using a `legacy SSL
   certificate </acquia-cloud/ssl#sni>`__
-  `Configure your domain name with the appropriate prefix <#prefix>`__

.. _ssl:

Enable SSL for your site
------------------------

IPv6 support on |acquia-product:ace| or |acquia-product:acs| requires an
Amazon Web Services Elastic Load Balancer (ELB) instance. For an ELB to
be provisioned for an environment, you need to enable SSL support for
the environment, which requires you to purchase and upload an SSL
certificate as a `legacy SSL certificate </acquia-cloud/ssl#sni>`__ in
the |acquia-product:ui|. Having an ELB enables IPv6 support. For
|acquia-product:acs| websites, there is an additional charge to reflect
the cost of the ELB. For information about how to enable SSL, including
how to upload a legacy SSL certificate, read `Enabling
SSL </acquia-cloud/ssl>`__. If you want IPv6 support, but not SSL,
`contact Acquia Support </support#contact>`__. You may be able to use a
self-signed SSL certificate to use with |acquia-product:ac|. You can
then upload this self-signed certificate instead of purchasing a
certificate. For more information, see `Creating a self-signed SSL
certificate </acquia-cloud/ssl/self-signed>`__.

.. _prefix:

Configure your domain name with the appropriate prefix
------------------------------------------------------

In your DNS provider's web interface, add the appropriate prefix to your
domain name. In most cases, prefix your CNAME domain name with the
``dualstack`` prefix to support both IPv4 and IPv6 visitors. Prefix your
CNAME domain name with the ``ipv6`` prefix to support only IPv6
visitors. For example, suppose your website's domain name is
``www.example.com`` and your Prod environment's URL is
``1234-4321.us-east-1.elb.amazonaws.com``. Set the CNAME entry for
``www.example.com`` to
``dualstack.1234-4321.us-east-1.elb.amazonaws.com``.

For more information about configuring your DNS settings, read `Pointing
DNS records to your public IP
addresses </acquia-cloud/manage/domains/dns>`__.
