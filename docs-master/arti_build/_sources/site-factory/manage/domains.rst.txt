.. include:: /common/global.rst

Adding custom domains to your site
==================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/manage/domains/*

.. container:: internal-navigation

   **Custom domains**

   * Prepare
   * :doc:`Point </site-factory/manage/domains/point>`
   * :doc:`Verify </site-factory/manage/domains/verify>`
   * :doc:`Email </site-factory/manage/domains/email>`
   * :doc:`Complete </site-factory/manage/domains/complete>`


Which of these URLs do you think your site visitors would rather enter
when they're accessing your website:
``product.company.acquiasites.com``   or   ``www.product.com``?

**We think so too.**

Use the following steps to associate custom domain names with your
websites and `site
collections </site-factory/manage/website/manage/site-coll>`__ hosted on
|acquia-product:edg| :

#. Obtain a second-level domain name for your website or site
   collection.
#. `Point your new domain name </site-factory/manage/domains/point>`__ to your hosted website. 
#. `Verify your CNAME record </site-factory/manage/domains/verify>`__ (if used). 
#. `Set up email for your domain. </site-factory/manage/domains/email>`__
#. Reconfigure external font accounts (if used) and 
   `complete the process. </site-factory/manage/domains/complete>`__

If you have more than one custom domain name that you want to add to
your hosted website or site collection, use these procedures for each
custom domain name. Websites with custom domains count against your
subscription's maximum number of websites; for more information on
checking your total number of websites with custom domains, see
`Managing subscription usage </site-factory/manage/usage>`__.

You can add custom domain names to websites and site collections before
you obtain the name from your domain name registrar.

.. note::  

   -  You can also add 
      `path-based domain names </site-factory/manage/domains/path>`__, in the form of
      ``www.example.com/foo``.
   -  Because custom domains are required to use SSL, SSL is not available
      for default domains ending with ``acsitefactory.com``.


Getting your custom domain
--------------------------

If you haven't already done so, get a second-level domain name for your
website or site collection (for example, ``example.com``).

You can buy a domain name from a *domain name registrar*, which is a
company or organization that manages domain names under the supervision
of `ICANN <http://www.icann.org/>`__. Domain name registrars control how
domain names are managed on the many Internet DNS (Domain Name System)
servers. DNS is the system that translates machine-readable computer
addresses, such as ``184.73.171.26``, to memorable addresses, such as
``www.yoursite.com``.

Visit the ICANN website for a list of |ICANN-accredited registrars|_.

.. |ICANN-accredited registrars| replace:: ICANN-accredited registrars
.. _ICANN-accredited registrars: http://www.icann.org/registrar-reports/accredited-list.html

.. note::  Acquia is not a domain name registrar and does not provide DNS services.

Domain name registrar recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select a domain name registrar based on these recommendations in order
to provide the best experience with |acquia-product:edg| to you and your
site visitors.

-  Choose a domain name registrar that supports the use of **CNAME
   records** for domain names.
   (A CNAME record tells DNS that the domain name site visitors enter in
   their browsers is actually an alias of another domain name — in your
   case, your |acquia-product:edg|-hosted website.)
-  Be sure that the domain name registrar you choose offers DNS
   services.
-  Some domain name registrars use objects called *iframes* to redirect
   site visitors to existing websites when using the new domain name.
   Because iframes block several |acquia-product:edg| functions from use
   (including the ThemeBuilder), you **cannot** use the iframe redirect
   method for your new domain name. We recommend that you use CNAME
   records for your domain names, or at the very least, A Records.

How do I determine if my registrar is using iframes for my website?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access your website at the new domain URL provided by your registrar,
and then view the HTML page source in your browser.

If the page source looks similar to the following, your registrar is
using iframes for your website:

.. code::

   <!-- frames -->
   <frameset rows="50%,75" border="0" framespacing="0">
   <frame name="destframe" src="http://[site URL]" marginwidth="0" marginheight="0" scrolling="auto" frameborder="0">
   <frame src="http://example.registrar.com/us?example.com" name="bottom" frameborder="0" scrolling="NO" marginwidth="0" marginheight="0" noresize>
   </frameset><noframes></noframes>

`Continue to the next step > </site-factory/manage/domains/point>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
