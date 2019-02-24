.. include:: /common/global.rst

Acquia Cloud Edge
=================

.. toctree::
  :hidden:
  :glob:

  /edge/*

.. container:: message-status

   Available only to `Acquia Cloud Enterprise </acquia-cloud>`__ and `Acquia Cloud Site Factory </site-factory>`__ subscribers

|acquia-product:cf| consists of two products that are available for |acquia-product:ace| and |acquia-product:edg| subscriptions:

-  |acquia-product:cfp| |--| Secures your application with protection against distributed denial of service (DDOS) attacks, a Web Application Firewall (WAF), and high-speed DNS. |acquia-product:cfp| examines web traffic looking for suspicious activity.
-  |acquia-product:cfc| |--| Provides a globally load balanced content delivery network (CDN) so that visitors interact with your application at the fastest possible speeds, no matter where on the globe they are located.

|acquia-product:cfp| and |acquia-product:cfc| can be purchased and used together or separately.

.. note::

  |acquia-product:cfc| does not currently support:

  -  `Authenticated Origin Pulls <https://blog.cloudflare.com/protecting-the-origin-with-tls-authenticated-origin-pulls/>`__
  -  `Railgun <https://www.cloudflare.com/website-optimization/railgun/>`__
  -  `Mirage <https://www.cloudflare.com/website-optimization/mirage/>`__
  -  `Rocket Loader <https://www.cloudflare.com/website-optimization/>`__

Configuration options for these features appear in the |acquia-product:cf| administration user interface, but are not supported by Acquia.

.. _setup:

Setting up Acquia Cloud Edge
----------------------------

To add |acquia-product:cfp| or |acquia-product:cfc| to your |acquia-product:ace| or |acquia-product:edg| subscription, contact your account manager at Acquia. Acquia will set up and support |acquia-product:cf| for you.

You can then use the |acquia-product:cf| web user interface to manage the service for your domains.

.. _access:

Accessing Acquia Cloud Edge
---------------------------

To access the |acquia-product:cf| web user interface, `sign in to Cloudflare <https://www.cloudflare.com/a/login>`__ using the email address and password provided for your |acquia-product:cf| account by Acquia.

For more information about how to use |acquia-product:cf| after it is set up, see the `CloudFlare knowledge base <https://support.cloudflare.com/hc/en-us>`__.

.. _test:

Testing Acquia Cloud Edge
-------------------------

You can test |acquia-product:cf| by editing your ``/etc/hosts`` file to point your domain to the CloudFlare IP address for the domain. To do this, complete the following steps:

.. note::

  Domains that are protected by |acquia-product:cf| must use a CNAME instead of an A record. If you use CNAME integration with |acquia-product:cf|, you must handle the termination of the apex (root) domain, and the redirect of subdomains such as the ``www`` subdomain must be handled outside of Acquia.

#. Find the IP address of the subdomain to be routed through |acquia-product:cf| using a command similar to the following:

   .. code-block:: none

      dig [domain_name].cdn.cloudflare.net

   where ``[domain_name]`` is your fully qualified domain name. |br| 
   For example, if your domain name is ``test.example.com``, the command would be:

   .. code-block:: none

      dig test.example.com.cdn.cloudflare.net

   The response will appear similar to these results:

   .. code-block:: none

      ; <<>> DiG 9.8.3-P1 <<>> test.example.com.cdn.cloudflare.net
      ;; global options: +cmd
      ;; Got answer:
      ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 64242
      ;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 0
      ;; QUESTION SECTION:
      ;test.example.com.cdn.cloudflare.net. IN A
      
      ;; ANSWER SECTION:
      test.example.com.cdn.cloudflare.net. 300 IN A 111.22.33.44 
      test.example.com.cdn.cloudflare.net. 300 IN A 111.22.34.44 
      test.example.com.cdn.cloudflare.net. 300 IN A 111.22.35.44 
      test.example.com.cloudflare.net. 300 IN A 111.22.36.44 
      test.example.com.cdn.cloudflare.net. 300 IN A 111.22.37.44

#. Select one of the IP addresses in the ``ANSWER SECTION`` of the ``dig`` response.
#. Edit your ``/etc/hosts`` file to add a line based on the following format, using the IP address and your domain name:

   .. code-block:: none

      111.22.33.44 test.example.com

   For information about how to edit your ``/etc/hosts`` file, see the `Using an /etc/hosts file for custom domains during development <https://knowledge.acquia.com/using-etchosts-file-custom-domains-during-development>`__ knowledgebase article.
#. Enter the domain name in your browser and examine the page response headers.

If |acquia-product:cf| is functioning properly, you will see that the page response headers include a ``cf-ray`` header.

.. _traffic:

Confirm that traffic is going through Acquia Cloud Edge
-------------------------------------------------------

The first step in testing a site with |acquia-product:cf| is ensuring that requests to the website are being sent through the Edge network. This can be done in one of two ways:

-  *Using the browser address bar* |br| 
   Enter ``www.example.com/cdn-cgi/trace`` in any browser, where ``www.example.com`` is the domain you are testing. The response will show details similar to the following:

   .. code::

      fl=4f64
      h=www.camilia.me
      ip=108.162.209.36
      ts=1437437272.84
      visit_scheme=http
      uag=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
      colo=SJC
      spdy=off
   
   This response identifies that the request was processed by the Edge network.

-  *Using the Claire plugin for Chrome* |br| 
   The `Claire plugin <https://chrome.google.com/webstore/detail/claire/fgbpcgddpmjmamlibbaobboigaijnmkl?hl=en-US>`__ is a free download that you can get from the Chrome web store. |br| 
   After you install the plugin, any website that you access through the Edge network will cause the plugin to display an orange cloud icon in the Chrome address bar. This provides a visual indicator the request was processed by the Edge network. |br| 
   If you do not see the expected results, then the domain is not yet correctly configured for |acquia-product:cf|. Confirm that the DNS configurations have been made correctly.

.. _ssl:

Acquia Cloud Edge and HTTPS (SSL)
---------------------------------

|acquia-product:cfc| and |acquia-product:cfp| include a single SAN certificate per domain that covers the bare domain and wildcard third-level domains. If you want to use your own custom SSL certificates with |acquia-product:cf|, you can upload the same certificate that you use on |acquia-product:ac| to |acquia-product:cf|. If you do this and you change or rekey your SSL certificate, you must apply the updated or new certificate to both |acquia-product:ac| and |acquia-product:cf| to maintain consistency and simplify support.

.. admonition:: Note for China and HTTPS usage

   If you anticipate having visitors that will both use HTTPS and are based in China, Cloudflare `requires <https://www.cloudflare.com/network/china/>`__ that you place your private SSL keys in their China data centers.

.. _timeout:

Timeouts
~~~~~~~~

|acquia-product:cf| typically waits 100 seconds for a response from your backend (origin) servers before timing out. If a response has not been received from your origin server after 100 seconds, the connection is closed and an ``Error 524: A timeout occurred`` will be served. Long-running processes, such as report generation, may trigger this error.

|acquia-product:ace| customers can request a timeout increase to a maximum of 600 seconds. Alternately, the application should be modified to return HTTP responses in the time limit.

.. _throttle:

Traffic throttling
------------------

Rate limiting of traffic is available as an add-on feature for |acquia-product:cfp| subscribers. If you need to throttle responses from a given IP for a specified amount of time, contact your Acquia account manager for additional details.

.. _log-sharing:

Logs and Log sharing
--------------------

|acquia-product:cf| supports log sharing, which enables subscribers to access web log data on a per-domain basis. These logs can be forwarded for aggregation and analysis.

Audit logs for |acquia-product:cf| are retained for eighteen months. Access logs are retained for three days. These logs are accessible to the customer using the Cloudflare API.

.. _always-on:

Always online
-------------

|acquia-product:cf| does not support the Always Online feature.
