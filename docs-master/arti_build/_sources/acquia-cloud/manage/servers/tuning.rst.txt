.. include:: /common/global.rst

Tuning your server configuration
================================

Computers have a finite amount of resources (including CPU power,
memory, and disk space). Hosting companies allocate these resources
differently according to the common uses of the servers they maintain.
The |acquia-product:ac| platform optimizes resources for hosting Drupal
applications. Acquia's mission is to provide the best Drupal hosting
platform, while also recognizing the need to allow for customization.
Acquia's server tuning formula provides a balance of stability,
performance, and customization.

To understand server tuning, it is important to understand these key
concepts:

-  **PHP process** - A PHP process is used whenever a page request
   reaches a web server. One PHP process is required for each page
   request
-  **Memcache** - A system used to store Drupal's cache tables in server
   memory, rather than on the hard drive
-  **Opcode cache** - A PHP caching layer, OPcache, which speeds up code
   execution time by caching compiled PHP
-  **PHP memory** - Memory reserved for a PHP process to store variables
   and use when computing

Acquia tunes servers to allocate half the memory for the database (or
less, in the case of multitier |acquia-product:ace| instances) and 200MB
for the operating system. The remaining memory can be allocated among
Memcache, opcode caching, and PHP.

.. _docroot:

Docroots and PHP processes
--------------------------

The |acquia-product:ac| platform hosts servers using Amazon's EC2
infrastructure. The processing power of EC2 servers is measured in units
called Elastic Computing Units (ECUs). As a general rule, it is best to
run no more PHP processes per docroot than three times the ECU of the
server.

By default, |acquia-product:ac| provisions each application with three
environments: Development, Staging, and Production. This means a server
running three applications must support nine docroots. While these
environments will share some resources, like CPU and MySQL memory, as
needed, other resources like PHP processes have per-environment and
per-server limits which help ensure overall hosting stability. These
limits cannot be modified to allocate more or fewer processes to a
single environment.

.. note::  

   PHP process limits will be reduced server-wide if more environments are
   added to your server, or if any memory limits (PHP, opcode cache,
   Memcache) are increased beyond their default values. As a result, we
   strongly recommend that customers carefully consider the impact of these
   changes to existing applications before making them.

When you are deciding how big a server you need to purchase, it is
important to make sure that you will have at least one available PHP
process per docroot. The more PHP processes a docroot is allocated, the
greater the number of simultaneous page views the server can handle.
When a server does not have an available PHP process for a page request,
a 503 "Service Unavailable" error is returned to the visitor. On an
Acquia-hosted application, the 503 error page looks like this:

|503 error page|

.. note::  

   |acquia-product:ac| replaces all HTTP ``500``, ``501``, ``502``, ``503``
   and ``504`` status code responses served to visitors of your *production
   environments* with a generic ``503 Service Unavailable`` response. This
   prevents the production environment from leaking error message
   information.

   To assist with troubleshooting during development, *non-production
   environments* pass all ``50x`` HTTP status codes through the load
   balancers back to the requesting client without any replacement.

When a Drupal application receives a page request, but there are no PHP
processes available or able to be spawned to handle it immediately, the
application skips the spawn request and waits for a process to become
available. This is called *skip-spawning*. After a while, the
application stops waiting to handle the request and the request fails
with a "Temporarily Unavailable" message.

If your application experiences frequent 503 errors caused by
skip-spawning, you have two primary options for increasing the number of
available PHP processes:

-  Optimize the code running the application
-  Purchase larger hardware

While purchasing larger hardware is an immediate solution, there are
circumstances where inefficiencies in the application code prevent
larger hardware from yielding benefits. It is always a good idea to
attempt to optimize an application, even if you wind up purchasing
larger hardware. For more information about optimizing your
applications, see `Improving application
performance </acquia-cloud/performance>`__.

.. |503 error page| image:: https://cdn3.webdamdb.com/1280_6ddhbbX57Gs5.png?1526475775
   :width: 590px
   :height: 89px
