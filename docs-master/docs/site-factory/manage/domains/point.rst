.. include:: /common/global.rst

Pointing your domain name
=========================

.. toctree::
   :hidden:
   :glob:

   /site-factory/manage/domains/point/*


.. container:: internal-navigation

   **Custom domains**

   * :doc:`Prepare </site-factory/manage/domains>`
   * Point
   * :doc:`Verify </site-factory/manage/domains/verify>`
   * :doc:`Email </site-factory/manage/domains/email>`
   * :doc:`Complete </site-factory/manage/domains/complete>`

After you have your new domain name (based on our `domain name registrar
recommendations </site-factory/manage/domains>`__), point your
domain name, subdomain name, or 
`path-based domain name </site-factory/manage/domains/path>`__ to your website
running on |acquia-product:edg|.

.. note::  If you are adding an additional custom domain name to an existing 
      |acquia-product:edg| subscription with a custom domain name, before you 
      point the additional domain name to your subscription you must first add 
      a 301 redirect for that domain to the ``.htaccess`` file for your 
      website's codebase. Failing to implement the redirect may cause HTTP 404 
      Not Found error messages to be cached for your new custom domain.

To point your domain name to a website, use one of the following
procedures, depending on whether you are adding a domain to a website or
a `site collection </site-factory/manage/website/site-coll>`__,
and the method supported by your domain name registrar:

-  **Adding a domain to a website**

   -  `Using CNAME with your website
      (preferred) </site-factory/manage/domains/point/cname-site>`__
   -  `Using the A Record with your
      website </site-factory/manage/domains/point/arecord-site>`__

-  **Adding a domain to a site collection**

   -  `Using CNAME with your site collection
      (preferred) </site-factory/manage/domains/point/cname-coll>`__
   -  `Using the A Record with your site
      collection </site-factory/manage/domains/point/arecord-coll>`__

Be patient, as this step can take up to 24 hours for DNS entries to
propagate across the Internet.

`Continue to the next step > </site-factory/manage/domains/verify>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
