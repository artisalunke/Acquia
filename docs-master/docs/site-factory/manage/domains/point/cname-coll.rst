.. include:: /common/global.rst

Using CNAME with your site collection
=====================================

Custom domains

-  `Prepare </site-factory/manage/domains>`__
-  `Point </site-factory/manage/domains/point>`__
-  `Verify </site-factory/manage/domains/verify>`__
-  `Email </site-factory/manage/domains/email>`__
-  `Complete </site-factory/manage/domains/complete>`__

**CNAME forwarding** is the preferred method for connecting a `domain
name you have purchased </site-factory/manage/domains>`__ to an
|acquia-product:edg| site collection.

A CNAME record redirects website visitors from the domain name they
entered in their browsers to another domain name — in this case, your
|acquia-product:edg| site collection. Using CNAME to point to a site
collection location instead of an IP address also allows
|acquia-product:edg| to better guarantee high availability.

Note

`Forwarding your domain name directly to a single IP address using an A
Record </site-factory/manage/domains/point/arecord-coll>`__ is
possible, but can compromise your |acquia-product:edg| site collection's
availability to visitors.

To use a CNAME record for your domain name:

#. Contact your domain name registrar and learn how to manage your
   domain name. In most cases, you can access DNS controls by logging in
   to your domain name registrar's website. Your domain name registrar
   is your best resource for information about managing your domain name
   on their website.
#. Using your domain name registrar's instructions, create the ``www``
   subdomain of your domain, as well as any other required subdomains.
   Subdomains are addresses based on your second-level domain name, but
   prefixed with an additional descriptor, such as ``www`` or ``blog``.
   For example, if your domain name is ``cars2rentorbuy.com``, you would
   create ``www.cars2rentorbuy.com`` along with any other required
   subdomains.
#. Create a CNAME entry or record to point the complete ``www``
   subdomain (and, separately, any other subdomains) to your
   |acquia-product:edg| site collection.

   Notes

   -  Not all domain registrars offer DNS services, and not all DNS
      services allow CNAME record changes. In these cases, you can
      `point your domain name to your |acquia-product:edg| site
      collection using an A
      record </site-factory/manage/domains/point/arecord-coll>`__.
   -  Be patient, because it can take up to 48 hours for forwarding and
      CNAME entries to propagate across the Internet.

After you create a CNAME record for your custom domain, you must add the
domain to your |acquia-product:edg| site collection.

Adding your domain
------------------

To add the ``www`` subdomain (and any other subdomains you created for
your domain name) to your |acquia-product:edg| site collection:

#. `Sign in to the Factory interface </site-factory/manage/login>`__,
   find the site collection to which you want to add a custom domain
   name, and then open its actions menu.

   |Select Manage domains from the actions menu|

#. Click **Manage domains**.
#. In the **Associate a domain** section, enter your domain name (such
   as ``www.cars2rentorbuy.com``).

   Important

   Some domain name registrars list domain names in all capital letters
   in their web interfaces. Be sure to enter your domain name into the
   **Add a domain** field using **lowercase letters only**. For example,
   enter ``www.cars2rentorbuy.com`` instead of
   ``WWW.CARS2RENTORBUY.COM``.

#. Click **Associate domain**.

Note

If your domain's CNAME record has not been created properly or if it has
not yet fully propagated, you will not be able to add it to your
|acquia-product:edg| website. Wait some time and try again.

Your ``www`` subdomain directs visitors to your |acquia-product:edg|
website and all its URLs will be listed.

Because some users will not use the ``www`` when visiting your website,
forward your domain name (such as ``cars2rentorbuy.com``) to the ``www``
subdomain (``www.cars2rentorbuy.com``) based on your domain name
registrar's instructions.

Your website's visitors can then find your website with or without the
``www``.

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

`Continue to the next step > </site-factory/manage/domains/verify>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |Select Manage domains from the actions menu| image:: https://cdn3.webdamdb.com/1280_Az8OibKrbGz0.png?1526475872
   :width: 750px
   :height: 493px
