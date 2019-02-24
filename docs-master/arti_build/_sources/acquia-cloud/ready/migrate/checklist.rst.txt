.. include:: /common/global.rst

Checklist for migrating your website to |acquia-product:ac|
===========================================================

Migrating your Drupal website to |acquia-product:ac|

-  `Assess </acquia-cloud/migrate>`__
-  Checklist

To help you prepare to launch your new Drupal website and to avoid
several common configuration or performance issues, use the following
suggestions, recommended settings, and information as a prelaunch
checklist for your website after `Assessing your Drupal website for
migration onto |acquia-product:ac| </acquia-cloud/migrate>`__.

Optimize your website with |acquia-product:ais|

|acquia-product:ais| can help you with many of these checks, with new
ones being added regularly. Find out more about `getting started with
|acquia-product:ais| </acquia-cloud/insight/using>`__.

Unless otherwise specified, the following suggestions apply to all
versions of Drupal:

.. _install:

Install and enable recommended modules
--------------------------------------

Drupal websites usually require that you install contributed modules to
be able to accomplish all of their necessary functions. Here are some
recommendations and potential problems to be aware of as you develop
your website if you intend to migrate the website to
|acquia-product:ac|.

Although none of these modules are required for your website to work
with |acquia-product:ac|, we recommend that you install and use these
modules with your |acquia-product:ac|-hosted websites to enhance
performance and to help you more easily diagnose website issues.

`Install and enable </acquia-cloud/develop/install-module>`__ the
following modules based on your needs and your version of Drupal:

+-----------------+-----------------+-----------------+-----------------+
| Module          | Description     | Drupal 7        | Drupal 8        |
+=================+=================+=================+=================+
| `[acquia-produc | Enables you to  | |yes|           | |yes|           |
| t:anc] <https:/ | connect any     |                 |                 |
| /www.drupal.org | Drupal website  |                 |                 |
| /project/acquia | to Acquia. If   |                 |                 |
| _connector>`__  | you're not      |                 |                 |
|                 | ready to        |                 |                 |
|                 | migrate yet,    |                 |                 |
|                 | you can use     |                 |                 |
|                 | this module to  |                 |                 |
|                 | get access to   |                 |                 |
|                 | `[acquia-produc |                 |                 |
|                 | t:ais] <https:/ |                 |                 |
|                 | /cloud.acquia.c |                 |                 |
|                 | om>`__          |                 |                 |
|                 | and take        |                 |                 |
|                 | advantage of    |                 |                 |
|                 | Acquia's tests  |                 |                 |
|                 | before you're   |                 |                 |
|                 | ready to go     |                 |                 |
|                 | live.           |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `[acquia-produc | Gives you       | |yes|           | |yes|           |
| t:ap] <https:// | significant     |                 |                 |
| www.drupal.org/ | control over    |                 |                 |
| project/acquia_ | your caches and |                 |                 |
| purge>`__       | is designed     |                 |                 |
|                 | with            |                 |                 |
|                 | [acquia-product |                 |                 |
|                 | :ac]            |                 |                 |
|                 | websites in     |                 |                 |
|                 | mind. It can    |                 |                 |
|                 | help you purge  |                 |                 |
|                 | down to the     |                 |                 |
|                 | individual node |                 |                 |
|                 | level, which    |                 |                 |
|                 | can ensure that |                 |                 |
|                 | new or changed  |                 |                 |
|                 | content shows   |                 |                 |
|                 | up immediately  |                 |                 |
|                 | instead of      |                 |                 |
|                 | waiting for the |                 |                 |
|                 | cache to        |                 |                 |
|                 | refresh.        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `[acquia-produc | Enables your    | |yes|           | |yes|           |
| t:as] </acquia- | website to      |                 |                 |
| search/modules> | integrate with  |                 |                 |
| `__             | [acquia-product |                 |                 |
|                 | :as].           |                 |                 |
|                 | Depending on    |                 |                 |
|                 | your            |                 |                 |
|                 | configuration,  |                 |                 |
|                 | additional      |                 |                 |
|                 | modules are     |                 |                 |
|                 | required or     |                 |                 |
|                 | recommended.    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `BlazeMeter <ht | Assists you     | |yes|           | |yes|           |
| tps://www.drupa | with creating   |                 |                 |
| l.org/project/b | and running     |                 |                 |
| lazemeter>`__   | load tests for  |                 |                 |
|                 | your website.   |                 |                 |
|                 | `Learn          |                 |                 |
|                 | more </acquia-c |                 |                 |
|                 | loud/performanc |                 |                 |
|                 | e/load#diy>`__. |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `Cookie Cache   | Replaces a      | |yes|           | |no|            |
| Bypass          | module that was |                 |                 |
| Advanced <https | part of Drupal  |                 |                 |
| ://www.drupal.o | 6 Pressflow,    |                 |                 |
| rg/project/cook | allowing you to |                 |                 |
| ie_cache_bypass | set cache       |                 |                 |
| _adv>`__        | lifetimes on    |                 |                 |
|                 | particular      |                 |                 |
|                 | cookies.        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `Fast           | Reduces the     | |yes|           | |no|            |
| 404 <https://ww | level of        |                 |                 |
| w.drupal.org/pr | bootstrap       |                 |                 |
| oject/fast_404> | required to     |                 |                 |
| `__             | serve error     |                 |                 |
|                 | pages for       |                 |                 |
|                 | requested,      |                 |                 |
|                 | nonexistent     |                 |                 |
|                 | static assets.  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `Redirect <http | Reduces your    | |yes|           | |yes|           |
| s://www.drupal. | reliance on     |                 |                 |
| org/project/red | path redirects  |                 |                 |
| irect>`__       | in the          |                 |                 |
|                 | ``.htaccess``   |                 |                 |
|                 | file. Because   |                 |                 |
|                 | path redirects  |                 |                 |
|                 | need to be      |                 |                 |
|                 | loaded at run   |                 |                 |
|                 | time for every  |                 |                 |
|                 | page request,   |                 |                 |
|                 | having too many |                 |                 |
|                 | redirects can   |                 |                 |
|                 | cause website   |                 |                 |
|                 | performance     |                 |                 |
|                 | problems.       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `Security       | Implements a    | |yes|           | |yes|           |
| Kit <https://ww | number of       |                 |                 |
| w.drupal.org/pr | protections     |                 |                 |
| oject/seckit>`_ | against serious |                 |                 |
| _               | security        |                 |                 |
|                 | issues, such as |                 |                 |
|                 | cross-site      |                 |                 |
|                 | scripting and   |                 |                 |
|                 | forgeries.      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Syslog core     | Stores logs     | |yes|           | |yes|           |
| module          | much faster     |                 |                 |
|                 | than the        |                 |                 |
|                 | Database        |                 |                 |
|                 | logging core    |                 |                 |
|                 | module.         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `Transliteratio | Converts        | |yes|           | |yes|           |
| n <https://www. | special         |                 |                 |
| drupal.org/proj | characters in   |                 |                 |
| ect/translitera | filenames to    |                 |                 |
| tion>`__        | ASCII.          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `Views          | Increases your  | |yes|           | |no|            |
| Litepager <http | website's       |                 |                 |
| s://www.drupal. | performance on  |                 |                 |
| org/project/vie | paginated       |                 |                 |
| ws_litepager>`_ | queries against |                 |                 |
| _               | large datasets. |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

.. _uninstall:

Uninstall and remove incompatible modules
-----------------------------------------

Disable and uninstall the following modules or classes of modules:

-  *`Boost <https://www.drupal.org/project/boost>`__* - This module
   conflicts with Varnish caching, and is not needed in
   |acquia-product:ac|.
-  *Database logging core module* - The Syslog core module can store
   logs much faster, because it does not need to write to the database.
   *(Monitored by |acquia-product:ais|)*
-  *PHP Filter core module* - Incorrect use of this module can cause
   security problems for your website. *(Monitored by
   |acquia-product:ais|)*
-  *Server-side statistics modules* - Instead, use client-side
   statistics services, such as `Google
   Analytics <https://www.google.com/analytics>`__ or
   `Omniture <https://my.omniture.com/login/>`__.
-  *Remove unneeded modules* - Remove modules such as
   `Devel <https://www.drupal.org/project/devel>`__ and views_ui (part
   of the `Views <https://www.drupal.org/project/views>`__ module),
   which are not needed on a production website, to reduce your
   website's startup (bootstrap) overhead.

Note

Be sure to review the modules listed in `Modules and applications
incompatible with
|acquia-product:ac| </acquia-cloud/develop/drupal/module-incompatibilities>`__.

.. _performance:

Configure performance settings in Drupal
----------------------------------------

On the Performance page (`URL
info <%5Bacquia-product:kb%5Darticles/url-paths-different-drupal-versions#performance>`__),
configure or enable the following values:

-  Enable page caching for anonymous website visitors. *(Monitored by
   |acquia-product:ais|)*

   -  Drupal 8 does this by default.
   -  Drupal 7 - **Caching** section > **Cache pages for anonymous
      users** check box

-  Ensure that block caching is enabled. *(Monitored by
   |acquia-product:ais|)*

   -  Drupal 8 - This is handled in the Cache API.
   -  Drupal 7 - **Caching** section > **Cache blocks** check box

-  In the **Caching** section > **Minimum cache lifetime** list, set the
   amount of time that cached pages won't be re-created to ``none``.
   *(Monitored by |acquia-product:ais|)*
-  In the **Caching** section > **Expiration of cached pages** list, set
   the maximum amount of time that an external cache can use an old
   version of a page to greater than or equal to five minutes (300
   seconds). *(Monitored by |acquia-product:ais|)*
-  Enable CSS aggregation in the **Bandwidth Optimization** section >
   **Aggregate and compress CSS files** check box. *(Monitored by
   |acquia-product:ais|)*
-  Enable JavaScript aggregation in the **Bandwidth Optimization**
   section > **Aggregate JavaScript files** check box. *(Monitored by
   |acquia-product:ais|)*
-  For the `Views <https://www.drupal.org/project/views>`__ and
   `Panels <https://www.drupal.org/project/panels>`__ modules, check the
   views content caches, time-based caches, and panels caches.
   *(Monitored by |acquia-product:ais|)*
-  Do not override the PHP memory limit on a global basis. Acquia tunes
   its servers to use the exact number of threads possible for the
   memory available to your application, and overriding it on a global
   basis will lead to 5XX errors for your website's users. If your
   application needs more than 128MB of memory for each page request,
   `contact Acquia Support </support#contact>`__ to request your memory
   allocation be altered to provide fewer threads, but more memory per
   thread.

   Note

   `Conditionally overriding the memory
   limit <%5Bacquia-product:kb%5Darticles/conditionally-increasing-memory-limits>`__
   for certain administration pages can sometimes be acceptable.
   `Contact Acquia Support </support#contact>`__ to discuss your
   options.

-  Use the `|acquia-product:as| </acquia-search>`__ service, which
   removes search load from MySQL and offers feature and usability
   improvements.
-  | Ensure that you're using InnoDB as your website's table engine.
   | Although InnoDB is now the default for Drupal, you should confirm
     that you're using it instead of the MyISAM table engine, which has
     performance problems. To examine your current database tables to
     determine if any other engines are in use, use the following SQL
     query (where ``[db_name]`` is your database's name):

   ``SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '[db_name]' AND ENGINE <> 'InnoDB';``

   If you need to convert tables in your database to InnoDB, use `this
   script <https://gist.github.com/acquialibrary/c901288145ea6c57ddb9>`__
   after you modify it with your own credentials and database
   information.

.. _best:

Best practices
--------------

Acquia recommends the following best practices:

-  Use HTTP authentication during development. `Learn
   more <%5Bacquia-product:kb%5Darticles/password-protect-your-non-production-environments-acquia-hosting>`__.
   Note that HTTP authentication invalidates Varnish caching and should
   never be used on a production website.
-  Avoid putting all user files in a single directory. A directory with
   thousands of files needs more time to read files in the directory,
   causing serious performance problems that can affect your website's
   availability. To restructure your files into subdirectories, see
   `Proactively set your file fields to use
   paths <%5Bacquia-product:kb%5Darticles/proactively-organizing-files-subfolders>`__.

Cache your website with Varnish
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ac| uses Varnish in front of all of its websites to help
ensure responsiveness. `Learn more about
Varnish </acquia-cloud/performance/varnish>`__. As part of setting up
your website on |acquia-product:ac|, you may need to `bypass the Varnish
cache <%5Bacquia-product:kb%5Darticles/bypassing-varnish-cache>`__, `set
redirects <%5Bacquia-product:kb%5Darticles/caching-redirects-varnish>`__,
or `purge it entirely </article/purging-varnish-cache-acquia-cloud>`__.

Configure Memcached
~~~~~~~~~~~~~~~~~~~

Memcached is a general-purpose memory cache server daemon. It can
improve Drupal application performance by moving Drupal's standard
caches out of the database and by caching the results of other expensive
database operations. `Learn more about
Memcached </acquia-cloud/performance/memcached>`__.

Protect your website with SSL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Secure Socket Layer, or SSL, is of major importance to many websites,
and critical for websites serving personal or financial information. The
`Enabling SSL </acquia-cloud/ssl>`__ documentation page provides an
overview of how you can use SSL with |acquia-product:ac|.

.. _ttl:

Shorten cutover time by lowering your TTL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several days before DNS cutover, lower your DNS's Time to Live (TTL)
setting to 5-10 minutes. Doing so reduces the amount of time your DNS
change will take to propagate when you are ready to turn your new
website live, and help you shorten the time that web traffic and email
are routed to both your old and new servers. Once the cutover to your
new website is complete, you can set your domain's TTL back to its
previous value. Since the method of lowering TTL can differ from
provider to provider, you will need to contact your domain name (DNS)
provider for specific instructions on how to lower your TTL.

.. _notify:

Contact Acquia if you expect a high-traffic event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're expecting an event that will send a significant amount of
traffic to your website, we encourage you to contact Acquia Support in
advance, so that we can help you prevent a website outage. Events that
can cause enough traffic to affect your website's availability include:

-  Website launches
-  Marketing campaigns
-  Performances

For more information on exactly how to notify Acquia of an important
event on your website, visit `Expecting a high-traffic
event <%5Bacquia-product:kb%5Darticles/expecting-high-traffic-event>`__.

.. _additional:

Additional resources
--------------------

The Acquia |acquia-product:lib| includes several other articles that may
be helpful to you as you configure your new Drupal website, including
the following:

-  `Caching
   overview <%5Bacquia-product:kb%5Darticles/caching-overview>`__
-  `Preparing your website for
   |acquia-product:ac| <%5Bacquia-product:kb%5Darticles/preparing-your-site-acquia-cloud>`__

If you require additional assistance, Acquia provides additional
services to Enterprise and Elite customers that include website
installation and configuration.