.. include:: /common/global.rst

Managing domains
================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/domains/*

After you create or import your application into |acquia-product:ac|,
you can access each of your application's environments using its default
domain name. An environment’s default domain name is based on its
application name (for example, the domain name for a Production
environment could be ``examplesite.devcloud.acquia-sites.com``). You
should then `configure a DNS domain name <#name>`__ for the Production
environment, such as ``www.example.com``, and `configure DNS
records </acquia-cloud/manage/domains/dns>`__ to use your public IP
addresses, rather than using the ``acquia-sites.com`` default domain
name.

.. admonition:: Note for |acquia-product:edg| subscribers

   |acquia-product:edg| subscribers must use the |edgdomains|_
   to add additional domains to their subscriptions. Domains added using
   the |acquia-product:ac| user interface will not work, and may be deleted
   by automated processes.

.. |edgdomains| replace:: \ |acquia-product:edg|\  domains functionality
.. _edgdomains: /site-factory/manage/website/domains/point/cname-site

To view the domain information for an environment, go to the
**Applications > [Environment] > Domains** page.

|Domains page|

Note that when each environment is created, it is provisioned with a
single custom |acquia-product:ac| subdomain with a name that ends in
``acquia-sites.com``. After creation, |acquia-product:ac| subdomains
cannot be changed, and additional custom |acquia-product:ac| subdomains
cannot be added to an environment.

After you add a domain name to the Production environment, the
|acquia-product:ac| load balancers can send incoming requests to your
application for that domain name. Your DNS provider has to point your
domain names to the IP address of the environment (Dev, Stage, or Prod)
so that requests for that domain name are directed to the
|acquia-product:ac| load balancers for your application. You can also
add domain names to your Development and Staging environments.

.. _view:

Viewing your IP address
-----------------------

The IP address and the name of the elastic load balancer (ELB) — if
applicable — for each of your environments is on the **Domains** page.

|acquia-product:acs| accounts have a single IP address for all three
environments. |acquia-product:ace| accounts can have multiple addresses.

.. _name:

Adding a domain name
--------------------

.. admonition:: Unsupported for |acquia-product:acfs|

   If you are an |acquia-product:acfs| subscriber, custom domain names are
   not supported. |learnmore|_.


.. |learnmore| replace:: Learn more about \ |acquia-product:acfs|\  and how to upgrade your  \ |acquia-product:ac|\  subscription
.. _learnmore: /acquia-cloud/free

To add a domain to one of your application's environments, complete the
following steps:

#. On the **Domains** page for the environment into which you want to
   add a domain, click **Add Domain** in the upper right.

   |The add domain icon|

   The **Add a domain** dialog box appears.

#. In the **Domain to add** field, enter the domain name without the
   protocol header. For example, use ``mysite.com`` instead of
   ``http://mysite.com``.

   .. note::  

      You can use the wildcard character ( ``*`` ) to make your environment
      available for multiple subdomains (for example, ``*.example.com``).

#. Click **Add domain**.

If you want to make your application available to multiple related
domain names (such as ``example.com`` and ``www.example.com``),
individually add each domain name. Otherwise, you can use the wildcard
character ( ``*`` ) in a single domain entry to allow for subdomains.

.. note::  

   You cannot use the same, exact domain name with two different
   environments or codebases at the same time, unless one environment is
   part of an |acquia-product:acs| subscription and the other environment
   is part of an |acquia-product:ace| subscription.

Subscribers with many domains may have several pages of domain names
displayed on their **Domains** page. You can either use the pager to
browse for a domain, or use the **Filter Domains** field to search.

.. _non-latin:

Adding domains with non-Latin characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the domain name that you use must be composed of Latin-based
characters. If you have a domain that uses non-Latin characters, you can
use `Punycode <https://en.wikipedia.org/wiki/Punycode>`__ to `convert
these characters <https://www.punycoder.com/>`__ into values recognized
by standard DNS.

After converting your characters with Punycode and using them with your
domain name in place of the non-Latin characters, you should be able to
configure your DNS entries normally.

.. _check:

Checking domain status
----------------------

You can determine whether your domain name is properly resolving to your
|acquia-product:ac| website. On the **Applications > [Environment] >
Domains** page, click the **Status** link for the domain. Acquia
performs a DNS lookup for your domain name and displays one of the
following status messages:

-  **DNS resolves to Acquia** - Your DNS settings and
   |acquia-product:ac| are properly configured.
-  **DNS doesn't resolve directly to Acquia** - Your DNS provider is
   pointing your domain name to an IP address different from your Acquia
   application. The Domain Status report displays the IP address and any
   alias found for the domain name. This status is normal if you use a
   CDN with your website. Otherwise, your domain name and DNS settings
   may be misconfigured.
-  **DNS does not resolve** - You have not set up the domain name with
   any DNS provider.

If your domain name does not resolve to your Acquia application, or if
it does not resolve at all, be sure that you have followed the
instructions in `Pointing DNS records to your public IP
addresses </acquia-cloud/manage/domains/dns>`__.

Because |acquia-product:ac| cannot determine the status of wildcard (*)
domains, the **Status** link is disabled for these domains.

.. _remove:

Removing a domain name
----------------------

To remove a domain from an environment, complete the following steps:

#. Go to the **Applications > [Environment] > Domains** page.
#. Find the domain that you want to delete, and then click **Remove**
   for that domain.
#. To confirm your choice, click **Remove**.

.. note::  

   The ``acquia-sites.com`` default domain name cannot be removed — it is
   necessary to enable Acquia Support and Operations to reach your
   application (even if DNS is not working).

.. _varnish:

Managing your application's Varnish cache
-----------------------------------------

.. container:: message-status

   This section does not apply to 
   `Node.js environments </acquia-cloud/node-js>`__, as they do not have a 
   Varnish cache.

Each domain name associated with your account has its own Varnish cache
to speed page access.

If your application supports Varnish caching, clearing these caches
ensures that anonymous website visitors are served the most up-to-date
version of your application after you make any changes.

To clear the Varnish cache for a domain name, click the **Clear
Varnish** link for the domain. For more information, see `Using
Varnish </acquia-cloud/performance/varnish>`__.

.. _robots:

Search indexing is blocked for acquia-sites.com domains
-------------------------------------------------------

Since applications that use the default domain name ending in
``acquia-sites.com`` aren't intended to be publicly available,
|acquia-product:ac| uses a ``robots.txt`` file to disallow indexing of
those domains by search engine robots. Robots that reach your
application using your DNS domain name, such as ``www.example.com``,
will operate normally and will be able to index your application for
searches.

.. _related:

Related topics
--------------

-  `Pointing DNS records to your public IP
   address </acquia-cloud/manage/domains/dns>`__
-  `Improving application performance </acquia-cloud/performance>`__

.. |Domains page| image:: https://cdn4.webdamdb.com/1280_U6MGqfHf5GK0.png?1526475565
   :width: 749px
   :height: 309px
.. |The add domain icon| image:: https://cdn2.webdamdb.com/1280_6F3BGVr1fbe1.png?1526475717
   :width: 752px
   :height: 358px
