.. include:: /common/global.rst

Custom Varnish configuration for |acquia-product:ace| applications
==================================================================

This page describes how to implement custom Varnish® configurations,
which are available only for |acquia-product:ace| applications that have
dedicated load balancers.

Varnish Cache is a caching reverse proxy that is installed in front of
all |acquia-product:ac| load balancing servers. For more information,
see `Using Varnish </acquia-cloud/performance/varnish>`__. Varnish Cache
is configured with its own domain-specific programming language,
`VCL <https://www.varnish-cache.org/trac/wiki/VCL>`__. If you are
interested in deploying a custom Varnish configuration, contact Acquia
Support. Acquia will provide you with a test environment for one week to
test your new custom VCL, but coding and testing is the customer’s
responsibility. For more complex changes, consider purchasing an Acquia
Professional Services engagement.

|acquia-product:ace| customers can `contact Acquia
Support </support#contact>`__ to create a support ticket to request a
copy of the full VCL, based on their contractual NDA. Acquia does *not*
disclose the configuration of our Nginx servers, as the configuration is
both proprietary and subject to change without notice.

.. _schedule:

Custom Varnish configuration schedule
-------------------------------------

Acquia deploys custom Varnish configurations on a weekly schedule. To
deploy your custom Varnish configuration, you must meet the following
weekly schedule:

#. Request a copy of your current VCL from Acquia.
#. Supply Acquia the list of environments in front of which you want to
   place the test load balancer.
#. Supply your new VCL file no later than 12:00 Eastern (North America)
   Time (`find UTC
   equivalent <http://www.worldtimebuddy.com/utc-to-est-converter>`__)
   on Monday. You must supply the entire VCL file, and not only the
   lines that are changing.

   .. note::

      VCL files on |acquia-product:ac| are limited to a maximum of 128KB in
      size.

#. Acquia deploys a test load balancer with the new VCL no later than
   17:00 Eastern (North America) Time on Tuesday. You should then test
   to verify that the functionality is working as desired. To test the
   VCL on the test load balancer, it may be helpful to `modify the
   /etc/hosts file on your local
   computer <https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=/using-etchosts-file-custom-domains-during-development>`__
   to point to the IP address of the test load balancer.
#. If you encounter any issues that require a revised VCL, you must
   submit a revised VCL no later than 09:00 Eastern (North America) Time
   on Wednesday for Acquia to apply the revised VCL to the test load
   balancer.
#. You must complete any testing and confirm your approval no later than
   15:00 Eastern (North America) Time on Wednesday.
#. Acquia performs code reviews between 15:00 Eastern (North America)
   Time on Wednesday and 15:00 Eastern (North America) Time on Thursday.
#. Acquia begins to deploy all VCLs that have been approved both by the
   customer and by Acquia starting at 15:00 Eastern (North America) Time
   on Thursday.

.. _usecase:

Custom Varnish configuration use cases
--------------------------------------

Here are some examples of use cases for which custom Varnish
configurations can be useful:

-  Changes to IP access control lists (ACLs)
-  Device-based redirection (however, `using
   .htaccess </acquia-cloud/develop/mobile>`__ instead of custom Varnish
   configuration is a more flexible approach)
-  Caching 404 responses

Unsupported use cases
~~~~~~~~~~~~~~~~~~~~~

Acquia does not support the following types of Varnish configuration use
cases:

-  Inline C in custom VCLs
-  Customer-requested Varnish
   `VMODs <https://www.varnish-cache.org/vmods/>`__

.. _related:

Related topics
--------------

-  `Using Varnish </acquia-cloud/performance/varnish>`__
-  `Introduction to
   Varnish <%5Bacquia-product:kb%5Darticles/varnish-intro>`__
-  `Simplified VCL for
   Varnish <%5Bacquia-product:kb%5Darticles/simplified-vcl-varnish>`__
-  `Using an /etc/hosts file for custom domains during
   development <%https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=/using-etchosts-file-custom-domains-during-development>`__

*Varnish is a registered trademark of Varnish Software AB and its
affiliates.*
