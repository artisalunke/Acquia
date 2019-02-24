.. include:: /common/global.rst

|acquia-product:edg| and |acquia-product:ac|
============================================

|acquia-product:ace| (upon which |acquia-product:edg| is built) is a fully managed, high-availability, scalable, clustered platform built for the most complex Drupal websites with the highest performance and uptime
requirements. As a customer of |acquia-product:edg|, you have access to
many of the features and abilities of |acquia-product:ace|, including
the following items:


Supported and included features
-------------------------------

-  |CFP link|_ – Secures your website with protection against distributed denial of service (DDOS) attacks, a Web Application Firewall (WAF), and high-speed DNS. |acquia-product:cfp| examines web traffic looking for suspicious activity. Contact your Acquia technical account manager for additional information if you want to use this service.
-  |CFC link|_ – A globally load balanced content delivery network (CDN) so that visitors interact with your site at the fastest possible speeds, no matter where on the globe they are located. Contact your Acquia technical account manager for additional information if you want to use this service.
-  |VPC link|_ – A dedicated, logically
   isolated section of |acquia-product:ace| that adds more network-level
   security and capabilities to the stack. |acquia-product:vpc| is
   available as an additional service.
-  |AS link|_ – A plug-and-play search
   service for your websites that lets you deliver great search
   functionality in minutes. Contact your Acquia sales representative
   for additional information if you want to use this service.
-  `Varnish </acquia-cloud/performance/varnish>`__ – Installed in
   front of all |acquia-product:ace| load balancing servers, Varnish
   increases website performance by caching anonymous user connections
   and then serving them from memory instead of making requests directly
   to the web server.

.. |CFP link| replace:: \ |acquia-product:cfp|\ 
.. _CFP link: /edge

.. |CFC link| replace:: \ |acquia-product:cfc|\ 
.. _CFC link: /edge

.. |VPC link| replace:: \ |acquia-product:vpc|\ 
.. _VPC link: /shield

.. |AS link| replace:: \ |acquia-product:as|\ 
.. _AS link: /acquia-search


|acquia-product:edg| infrastructure diagram
-------------------------------------------

For your reference, the following diagram describes the infrastructure
used for the |acquia-product:edg| application, and how its components
interact with one another:

|ACSF_diagram_v1-01.png|

.. |ACSF_diagram_v1-01.png| image:: https://cdn2.webdamdb.com/1280_AVkNej6xrw97.png?-62169955200

For information about |acquia-product:ace|, including detailed diagrams
regarding the |acquia-product:ac| platform's specific components, see |acquia-product:ac|
`architecture and key concepts </acquia-cloud/arch>`__.


Non-supported features and differences
--------------------------------------

-  Use the `Site Factory API </site-factory/extend/api>`__ to create and
   manage your hosted websites and to obtain the status of your
   |acquia-product:sfi| jobs, instead of the Cloud API.
-  Use the |acquia-product:sfi| to `test and deploy changes to your
   websites </site-factory/workflow/staging>`__ instead of using the
   workflow in the |acquia-product:ui|.



