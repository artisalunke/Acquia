.. include:: /common/global.rst

Using GeoIP information
=======================

*The GeoIP feature is available for |acquia-product:ace| and
|acquia-product:edg| customers who have dedicated load balancers and is
not available for |acquia-product:acs| or |acquia-product:acfs|
customers.*

The GeoIP feature for |acquia-product:ace| and |acquia-product:edg| uses
the `MaxMind <http://www.maxmind.com/app/country>`__ GeoIP2 Country
Downloadable Database to identify the country of origin of HTTP
requests, based on the request's IP address. The IP address is obtained
from the ``X-Forwarded-For`` header or the client IP address if there is
no ``X-Forwarded-For`` header. The |acquia-product:ac| server then adds
the two-letter country code (`ISO-3166-1
alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__) in the
``X-Geo-Country`` header of the HTTP request. If the MaxMind GeoIP
Country Downloadable Database can't identify the country from the
request IP address, the country code is set to ``AA``. Your website's
backend code can then use the country code in the header to set your
visitor's country.

The GeoIP feature supports the MaxMind IPv4 and IPv6 country database.
The GeoIP feature requires you to maintain an active subscription to the
MaxMind GeoIP2 Country Downloadable Database. It is available for
|acquia-product:ace| customers who have dedicated load balancers and is
not available for |acquia-product:acs| or |acquia-product:acfs|
customers.

The GeoIP feature does not support region- or city-level IP targeting.
Targeting at these levels requires custom development, which is
available from Acquia as a Professional Services engagement. For a
different approach to geographical targeting, see
`|acquia-product:cha| </lift>`__, which supports targeting specific
content on your website based not just on geography, but on a host of
other criteria.

You may also want to investigate using the MaxMind `GeoIP2 JavaScript
Client API <http://dev.maxmind.com/geoip/geoip2/javascript/>`__, which
works on the client side, rather on your |acquia-product:ac| servers.
Contact
`MaxMind <https://www.maxmind.com/en/geoip2-precision-services>`__ for
further information.

.. _enable:

Enabling the GeoIP feature
--------------------------

To enable the GeoIP feature, complete the following steps:

#. Purchase a GeoIP2 Country Downloadable Database subscription from
   `MaxMind <http://www.maxmind.com/app/country>`__.
#. Get your MaxMind GeoIP2 Country Downloadable Database user ID and
   license key.
#. Install and enable the `Acquia GeoIP Country
   variation <https://www.drupal.org/project/acquia_geoip_vary_by_country>`__
   module.
#. `Contact Acquia Support </support#contact>`__ and indicate that you
   want to enable the GeoIP feature for your |acquia-product:ace| or
   |acquia-product:edg| application. Provide your MaxMind GeoIP2 Country
   Downloadable Database user ID and license key.

Acquia Support will enable the GeoIP feature for each of your
application's environments by including a ``addon-geoip.vcl`` in your
application's Varnish runtime. This requires restarting Varnish on your
dedicated load balancers, which clears the Varnish cache and can result
in reduced performance while the cache is rebuilt.

While your MaxMind subscription is active, Acquia will update the
Country Database from MaxMind. Acquia updates MaxMind Country Database
instances three times a week. If your subscription ends,
|acquia-product:ac| will continue to add the ``X-Geo-Country`` header,
but the value may be inaccurate due to stale data.
