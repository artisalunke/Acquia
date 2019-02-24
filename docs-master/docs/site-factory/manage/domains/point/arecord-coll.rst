.. include:: /common/global.rst

Using the A Record with your site collection
============================================

Custom domains

-  `Prepare </site-factory/manage/domains>`__
-  `Point </site-factory/manage/domains/point>`__
-  `Verify </site-factory/manage/domains/verify>`__
-  `Email </site-factory/manage/domains/email>`__
-  `Complete </site-factory/manage/domains/complete>`__

Note

This is *not* the preferred method for connecting your domain name to
your |acquia-product:edg| site collection. The preferred method is
`CNAME
forwarding </site-factory/manage/domains/point/cname-coll>`__.

Use the following procedure to forward DNS requests to your
|acquia-product:edg| site collection with an A record (address record)
that points directly to your site collection's IP address.

Disadvantages
-------------

If you use an A record to forward DNS requests for your website to a
specific IP address, your site collection's primary website can
experience the following issues:

-  You can only create A records for your second-level domains (*not*
   subdomains). For example, you can use an A record to point
   ``example.com`` to an IP address, but not ``www.example.com``. Your
   DNS provider must point the ``www`` subdomain to your
   |acquia-product:edg| site collection for you.
-  To maintain high availability, |acquia-product:edg| is built on
   dynamic cloud infrastructure and uses elastic IP addresses to
   guarantee high availability. Tying your site collection to a single
   IP address potentially compromises its high availability.
-  If your site collection is moved from one IP address to another (for
   maintenance or other technical reasons), your domain forwarding will
   no longer work until you update it to reflect the new IP address.
-  If the |acquia-product:edg| team has to change your site collection's
   IP address in a hurry (for emergency fixes, for example), there might
   not be time to warn you of the change beforehand.

Procedure
---------

To point your domain name at your site collection using an A Record:

#. On your computer, open a terminal or command prompt window and run
   the following command to obtain your site collection's IP address:

   ``host [site_name].[SF_domain].com``

   where ``[site_name]`` is your site collection's name, and
   ``[SF_domain]`` is the domain name for |acquia-product:edg|.

   Note that you need to enter the complete |acquia-product:edg| URL for
   your website.

#. Record the IP address displayed by the host command.
#. Follow your DNS provider's instructions to set up an A Record
   pointing your domain name to your site collection's IP address.

Notes

-  Be patient, because it can take up to 24 hours for your A record
   information to propagate across the Internet.
-  If you use an A record with your site collection and your site
   collection becomes unavailable, run the host command using your site
   collection's URL to ensure that the IP address hasn't changed.

   If the IP address has changed from its previous value, contact your
   DNS provider to update the A record to use the new IP address.

.. _problems:

Troubleshooting domain issues
-----------------------------

You can add domain names to only one environment. Attempting to add a
domain to a second environment causes |acquia-product:edg| to both fail
with a logged warning message, and send an email similar to the
following to the user who attempted to add the domain:

    The following domains could not be added to the ``[sitename]`` site:
    ``[domain list]``. If you wish to add this domain to the
    ``[sitename]`` site, remove it from the site that has claimed the
    domain and then add it again at ``[factory URL]``.

To resolve the problem, remove the domain name from *both* environments
and then add the domain name to the single, appropriate environment.

`Continue to the next step > </site-factory/manage/domains/email>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
