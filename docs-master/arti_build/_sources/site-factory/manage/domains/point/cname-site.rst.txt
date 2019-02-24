.. include:: /common/global.rst

Using CNAME with your website
=============================

.. container:: internal-navigation

   **Custom domains**

   * :doc:`Prepare </site-factory/manage/domains>`
   * :doc:`Point </site-factory/manage/domains/point>`
   * :doc:`Verify </site-factory/manage/domains/verify>`
   * :doc:`Email </site-factory/manage/domains/email>`
   * :doc:`Complete </site-factory/manage/domains/complete>`


*CNAME forwarding* is the preferred method for connecting a `domain name
you've already purchased </site-factory/manage/website/domains>`__ to
your website on |acquia-product:edg|.

A CNAME record redirects site visitors from the domain name they entered
in their browsers to another domain name — in your case, your website
running on |acquia-product:edg|. Using CNAME to point to a website
location instead of an actual IP address also allows
|acquia-product:edg| to better guarantee high-availability.

.. note::  
    
    `Forwarding your domain name directly to a single IP address using an A Record </site-factory/manage/website/domains/point/arecord-site>`__ (rather than a CNAME record) is possible, but can compromise your website's availability.

To use a CNAME record for your domain name:

#. Contact your domain name registrar and learn how to manage your
   domain name. In most cases, you can access DNS controls by logging in
   to your domain name registrar's website. Your domain name registrar
   is your best resource when it comes to managing your domain name on
   their website.
#. Using your domain name registrar's instructions, create the ``www``
   subdomain of your domain, as well as any other required subdomains.

   Subdomains are addresses based on your second-level domain name, but
   prefixed with an additional descriptor, such as www or blog. For
   example, if your domain name is ``example.com``, you could create
   ``www.example.com`` along with any other required subdomains.

#. Create a CNAME entry or record to point the complete ``www``
   subdomain (as well as separately, any other subdomains) to your
   website on |acquia-product:edg|.

.. note::  

   -  Not all domain registrars offer DNS services, and not all DNS
      services allow CNAME record changes. In these cases, you can
      point your domain name to your |acquia-product:edg| website 
      `using an A record </site-factory/manage/website/domains/point/arecord-site>`__.
   -  Be patient, because it can take a day or more for forwarding and
      CNAME entries to propagate across the Internet.

After you create a CNAME record for your custom domain, you must add
your domain to your website on |acquia-product:edg|.

Adding your domain
------------------

To add the ``www`` subdomain (and any other subdomains you created for
your domain name) to your website:

#. `Sign in </site-factory/manage/login>`__ to the |acquia-product:sfi|,
   find the website to which you want to add a custom domain name, and
   then open its actions menu.

   |Site actions menu|

#. Click **Manage domains**.
#. In the **Associate a domain** section, enter your domain name (such
   as ``www.example.com``).

   .. important:: Some domain name registrars list domain names in all capital 
        letters in their web interfaces. Be sure to enter your domain name into 
        the **Add a domain** field using **lowercase letters only**. For 
        example, enter ``www.example.com`` instead of ``WWW.EXAMPLE.COM``.

#. Click **Associate domain**.

Your ``www`` subdomain directs visitors to your website and all its URLs
will be listed.

Because some users won't type the ``www`` when visiting your website,
forward your domain name (such as ``example.com``) to the ``www``
subdomain (``www.example.com``) based on your domain name registrar's
instructions.

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

`Continue to the next step > </site-factory/manage/website/domains/verify>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |Site actions menu| image:: https://cdn4.webdamdb.com/1280_AWiMn320x121.png?1526476057
   :width: 750px
   :height: 356px
