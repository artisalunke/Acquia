.. include:: /common/global.rst

Redirecting visitor requests with the .htaccess file
====================================================

Your website's
`.htaccess <https://en.wikipedia.org/wiki/.htaccess>`__ file
controls how your website's visitors are able to access your website,
and can be configured to handle many different visitor scenarios. Some
of the configuration methods you can use with you Acquia-hosted
website's ``.htaccess`` file include the following:

-  `Redirecting bare domain names to the www subdomain <#www>`__
-  `Redirecting traffic between HTTP and HTTPS <#https>`__

When implementing redirects in your ``.htaccess`` file, be aware of the
following best practices:

-  Be sure to place all of the following code examples *immediately
   after* the ``RewriteEngine On`` line in your ``.htaccess`` file.
-  Ensure that this line of code is included in your rewrite code:
   ``RewriteCond %{HTTP_HOST} !\.acquia-sites\.com [NC]  # exclude Acquia domains``
-  Too many redirects can cause minor to serious performance issues for
   your website. Every page request must the redirect rules, requiring
   additional load time on a per-request basis. Acquia recommends
   regular reviews of rules for consolidation and removal as part of
   your normal maintenance practices.
-  Redirects do not preserve Google campaign tracking information. If
   you rely on this information, ensure your links do not rely on Acquia
   server-side redirects. |acquia-product:ace| customers can use a
   `custom VCL file </acquia-cloud/performance/varnish/custom>`__ to
   alter this behavior.

For more information about ``.htaccess`` rewrite rules, see
`Introduction to htaccess rewrite
rules </article/introduction-htaccess-rewrite-rules>`__.

.. important:: 
    Redirects on |acquia-product:edg|

    |acquia-product:edg| subscriptions may need to modify the examples
    provided on this page, such as:

    -  When testing for ``AH_SITE_ENVIRONMENT``, you may need values other
       than ``prod``, such as ``_01live`` or ``01live``.
    -  Default domain names use ``acsitefactory.com`` instead of
       ``acquia-sites.com``.

.. _www:

Redirecting bare domain names to the www subdomain
--------------------------------------------------

You can modify your application's ``.htaccess`` file so that when
visitors request your application's URL without the ``www`` subdomain,
the request redirects to the ``www`` subdomain. For example, requests to
``http://example.com`` will be redirected to ``http://www.example.com``.

The following lines in the Drupal 8 and Drupal 7 versions of
``.htaccess`` accomplish this, but can cause problems in development:

.. code-block:: none

    # RewriteCond %{HTTP_HOST} !^www\. [NC] 
    # RewriteRule ^ http://www.%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

Because these lines unconditionally redirect visitors to a ``www``
subdomain, it can cause problems if the website is intended to work with
different domains, for example, with non-production environments.
Instead, replace the commented lines with code similar to the following,
modifying it for your own domain name:

.. code-block:: none

    RewriteCond %{HTTP_HOST} ^example\.com$ [NC] 
    RewriteCond %{HTTP_HOST} !\.acquia-sites\.com [NC] 
    RewriteRule ^ http://www.%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

.. _https:

Redirecting traffic between HTTP and HTTPS
------------------------------------------

For Acquia-hosted websites, secure HTTPS connections are terminated at
the load balancer level, which can cause many common ``.htaccess``
recipes for HTTPS redirects to not work as expected. Because the
X-Forwarded-Proto header indicates to the webserver if a request came in
over HTTPS, this what you need to validate in your rewrite conditions.

The examples in each of the available redirect methods use rewrite rule
flags. For a thorough explanation of the flags that you can use, see
`RewriteRule
Flags <https://httpd.apache.org/docs/2.4/rewrite/flags.html>`__.

.. _non-to-secure:

Redirecting all HTTP traffic to HTTPS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This sample rule sets ``HTTP_X_FORWARDED_PROTO`` to ``https`` when
accessing the website using HTTPS:

.. code-block:: none

    RewriteCond %{HTTPS} off 
    RewriteCond %{HTTP:X-Forwarded-Proto} !https 
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [NE,L,R=301]

.. _secure-to-non:

Redirecting all HTTPS traffic to HTTP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If website visitors are receiving insecure content warnings due to
Google indexing documents using the HTTPS protocol, traffic may need to
be redirected from HTTPS to HTTP. For this case, use the following rule
set:

.. code-block:: none

    RewriteCond %{HTTP:X-Forwarded-Proto} =https 
    RewriteRule ^(.*)$ http://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

.. _all-https:

Redirecting all traffic to the www SSL domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To force all traffic to use both the ``www`` domain and SSL (even if not
initially requested), use the following rules:

.. code-block:: none

    # ensure www. 
    RewriteCond %{HTTP_HOST} !^www\. [NC] 
    RewriteRule ^ https://www.%{HTTP_HOST}%{REQUEST_URI} [L,R=301] # ensure https 
    RewriteCond %{HTTP:X-Forwarded-Proto} !https  
    RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

.. _all-bare:

Redirecting all traffic to the bare SSL domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ace| customers with dedicated load balancers have the
option of redirecting all traffic to the bare domain using the HTTPS
protocol. To do this, use rules similar to the following:

.. code-block:: none

    # Redirecting http://www.domain.com and https://www.domain.com to https://domain.com 
    RewriteCond %{HTTP_HOST} ^www\.(.+)$ [NC] 
    RewriteRule ^(.*)$ https://%1%{REQUEST_URI} [L,R=301] 
    # Redirecting http://domain.com to https://domain.com 
    RewriteCond %{HTTPS} off 
    RewriteCond %{HTTP:X-Forwarded-Proto} !https 
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [NE,L,R=301]

.. _acquia_hosted:

Excluding Acquia domains and non-production environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To exclude the default Acquia domains from your redirects, or specific
environments (such as Dev and Stage), add one or more of the following
conditionals to the top of any group of rewrite rules:

.. code-block:: none

    RewriteCond %{ENV:AH_SITE_ENVIRONMENT} prod [NC] # only prod 
    RewriteCond %{ENV:AH_SITE_ENVIRONMENT} !prod [NC] # not prod 
    RewriteCond %{HTTP_HOST} !\.acquia-sites\.com [NC]  # exclude Acquia domains

As an example, if you wanted to ensure that all the domains were
redirected to ``https://www.`` except for Acquia domains, you would use
rules similar to the following:

.. code-block:: none

    # ensure www. 
    RewriteCond %{HTTP_HOST} !\.acquia-sites\.com [NC]  # exclude Acquia domains
    RewriteCond %{HTTP_HOST} !^www\. [NC] 
    RewriteRule ^ https://www.%{HTTP_HOST}%{REQUEST_URI} [L,R=301] # ensure https 
    RewriteCond %{HTTP:X-Forwarded-Proto} !https  
    RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

Example
~~~~~~~

The preceding examples of how and when you would use a rewrite are
complex. Here is a breakdown of the scenarios, which may help you
determine what your website really needs.

A security warning will occur on a bare domain only if the request
specifically includes the HTTPS protocol (such as
``https://example.com``), and there is no SSL certificate on the load
balancer that covers the bare domain. A request for
``http://example.com`` using the HTTP protocol, however, will not
produce a security warning because a secure connection to the bare
domain has not been requested.

+-----------------------+-----------------------+-----------------------+
| Domain                | DNS record type       | IP/Hostname           |
+=======================+=======================+=======================+
| ``www.example.com``   | CNAME                 | dc-2459-906772057.us- |
|                       |                       | east-1.elb.amazonaws. |
|                       |                       | com                   |
+-----------------------+-----------------------+-----------------------+
| ``example.com``       | A                     | 123.45.67.89          |
+-----------------------+-----------------------+-----------------------+

For |acquia-product:ac|, ``www.example.com`` has a CNAME record that
points to the hostname of the elastic load balancer, because that's
where the SSL certificate is installed when it's uploaded using the
`self-service UI </acquia-cloud/ssl>`__. However, bare domains/non-FQDNs
such as ``example.com`` cannot have CNAME records without a service
similar to Route 53. Because of this, it must point to the elastic IP
address of the balancer pair behind the ELB.

If there is a redirect in the ``.htaccess`` file that will take all
requests for the bare domain and redirect them to ``www``, due to how
the DNS records are set up, the following process is what occurs if you
request ``http://example.com``:

#. The request for ``http://example.com`` hits the load balancers behind
   the ELB.
#. The ``.htaccess`` rule 301 redirects request to
   ``https://www.example.com``.
#. A new request for ``https://www.example.com`` hits the ELB (where the
   certificate exists), and the procedure completes successfully.

However, if a specific request is sent to ``https://example.com`` with
the HTTPS protocol, the following occurs:

#. A request for ``https://example.com`` hits the load balancers behind
   the ELB.
#. Your browser displays the normal security warning.
#. You examine the certificate and decide to move ahead.
#. The ``.htaccess`` rule 301 redirects the request to
   ``https://www.example.com``.
#. A new request for ``https://www.example.com`` hits the ELB (where the
   certificate exists), and the procedure completes successfully.

Depending on your |acquia-product:ac| subscription type, there may be
additional requirements or steps to remove the security warning:

-  *Acquia Cloud Professional with shared balancers*
   In the case of |acquia-product:acs| with shared balancers, only a
   bare domain service (such as Route 53 or CloudFlare) will be helpful
   in removing the security warning. This is because with a bare domain
   service you are able to use a CNAME record for the bare domain, which
   allows you to point the bare domain at the hostname of the ELB.
-  *Acquia Cloud Enterprise*
   There are two available options for resolving the security warning,
   depending on the balancer situation:

   -  If you have dedicated balancers and if the existing certificate
      already covers at least both ``www.example.com`` and
      ``example.com``, you can `contact Acquia
      Support </support#contact>`__ to have the certificate that you
      uploaded using the self-service interface installed on the
      dedicated balancers. After this is complete, requests that hit the
      balancer before being redirected to the ELB also will not receive
      the security warning.
   -  Use Route 53, CloudFlare, or another bare domain service.
