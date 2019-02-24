.. include:: /common/global.rst

Custom VCL engagements
======================

Varnish Cache is a caching reverse proxy that is installed in front of
all |acquia-product:ac| load balancing servers. Varnish is configured
with its own domain-specific programming language,
`VCL <https://www.varnish-cache.org/trac/wiki/VCL>`__ (Varnish
Configuration Language). If you are interested in deploying a custom
Varnish configuration, |acquia-product:onb| can provide one or more of
several standard VCL modifications that require minimal customization,
and can also assist with the deployment and testing process.

Note

For more information about Varnish caching, see `Using
Varnish </acquia-cloud/performance/varnish>`__.

.. _types:

Types of custom Varnish templates
---------------------------------

The |acquia-product:onb| team has pre-written templates to address
common custom VCL use cases. The current list of provided custom VCL
templates that we provide include the following:

-  *Hash on device string* - This is an edge-case mobile strategy.
   Customers implement hashes on device strings when they do not want to
   do redirects to a mobile- and/or tablet-specific subdomain, and they
   do not have a responsive theme.

   Note

   Acquia strongly discourages this strategy in favor of mobile
   redirects or responsive themes, for the following reasons:

   -  Determining which content to serve (for example, mobile content
      versus desktop content) is a task that properly belongs to the
      application and not to a caching mechanism.
   -  Increases complexity, complicating troubleshooting, and increasing
      the burden on support.
   -  Increased cost of ownership, due to the previously listed reasons.

-  *Hash on cookie value* - This is an edge-case strategy where
   customers want to serve different content on a single URL to
   anonymous traffic, based on a cookie value. Acquia strongly
   discourages cookie-dependent architectures for reasons similar to
   those previously listed.
-  *IP whitelisting* - Customers can ask for IP whitelisting when they
   want to ensure that their website can be accessed only from certain
   IP addresses. Some customers insist on having it in the VCL due to
   perceived performance consequences related to doing the whitelisting
   in ``.htaccess``. Acquia's recommended strategy is to implement
   whitelisting in ``.htaccess``, or similar.
-  *Alternative Backend* - There is an alternative using Apache's
   ``mod_proxy`` which does not require a custom VCL.

Some of these use cases may require customer-specific modifications. The
|acquia-product:onb| team will handle these modifications, for up to one
hour of work.

.. _alternatives:

When custom VCL is not the best solution
----------------------------------------

It should be verified that a custom VCL is indeed the only solution to a
customer's feature requirements. A Custom VCL is not the best solution
in the following circumstances:

-  *Redirects* - Acquia strongly discourages implement redirects in a
   Custom VCL, due to the inherently long test and deployment cycle. For
   small numbers of redirects, instead use either ``.htaccess`` or the
   Drupal `Redirect <https://www.drupal.org/project/redirect>`__ module.
-  *Edge Side Includes (ESI)* - ESIs enable Varnish to assemble HTTP
   responses by fetching multiple objects from either cache or backends.
   Current versions of Varnish (4.x or greater) and Drupal (8.x or
   greater) do not respond well with ESI, and its use is discouraged in
   the strongest terms.
-  *Customize Cache headers* - Some use cases warrant the modification
   of default cache headers, depending on variables such as URL or user
   agent. This can be done effectively in both ``.htaccess``,
   ``settings.php`` or widely used contrib modules.
-  *Access restrictions* - Various solutions exist.
-  *Vary Cache* - Acquia's default Varnish template will vary its cache
   content only with ``URL`` and ``Session Cookie``. Customers may have
   reasons that require these variations for unauthenticated users not
   be mixed in the cache — for example, additional cookies and/or
   headers such as ``ACCEPT-LANGUAGE`` or custom headers. Often, this
   involves only a small subset of easily identifiable requests. Before
   resorting to a Custom VCL, investigate what would occur if these
   exceptions were not cached by Varnish.

.. _scope:

Out-of-scope areas
------------------

The following are out of scope for the |acquia-product:onb| offering and
require a Professional Services engagement:

-  Combinations of the customizations listed
-  VCL work for self-hosted customers
