.. include:: /common/global.rst

Best practices for developing on |acquia-product:ac|
====================================================

Acquia provides a plethora of tools and documentation aimed at enabling
developers to write and manage scalable and maintainable code. We
recommend you start with the following best practices and familiarize
yourself with the following tools and concepts. Your
|acquia-product:onb| team will provide additional guidance to ensure you
can take full advantage of these and other tools.

.. _s_and_p:

Coding standards and best practices
-----------------------------------

Good coding hygiene is a broad subject. In our experience, the following
recommendations address the most common coding issues we see on a daily
basis.

.. _coding:

Follow Drupal.org coding standards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure that you understand and adhere to Drupal coding standards. These
standards are documented on Drupal.org's `Coding
standards <https://www.drupal.org/docs/develop/standards>`__ webpage.
The `Coder <https://www.drupal.org/project/coder>`__ module can help you
conduct internal code reviews against the documented standards.

.. _modifying:

Avoid modifying Drupal core files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Changing Drupal’s core files makes your application difficult to
maintain because you must keep track of and reapply your changes as you
apply security and other updates. `Remote Administration </ra>`__ does
not cover modified core or contributed modules, so Acquia recommends you
implement any customizations using custom modules or theming files. This
allows the Remote Administration team to implement updates, while
allowing the client development team to modify custom code without any
loss of modifications.

If your application requires modification of Drupal core, or of
contributed modules, refer to `Patching and locking
modules </ra/patching>`__ for details on how to patch or lock modified
modules properly to ensure your application remains compatible with
Acquia security updates.

For a more in-depth discussion of why altering Drupal core files can be
problematic, see `Never hack
core <https://www.drupal.org/docs/7/site-building-best-practices/never-hack-core>`__.

.. _scalable:

Write scalable and maintainable code
------------------------------------

Consider carefully how your architecture and supporting code will scale.
Although we cannot mention everything you should do and everything you
should avoid, consider these questions:

Are my database queries performant?

.. raw:: html

   <div class="answ">

-  Avoid creating views with too many relationships. These generate
   queries with lots of joins, which can cause an undue load on the
   database. We recommend you simplify complex views, use `views
   caching <%5Bacquia-product:kb%5Darticle/views-caching>`__, or write
   an optimized query as a custom module.
-  ŽUse `New
   Relic <%5Bacquia-product:kb%5Darticles/using-new-relic-troubleshoot-site-issues>`__
   to identify slow queries. We can provide you with a copy of the `slow
   query log </acquia-cloud/monitor/slow-query>`__ for your
   environments.
-  Engage your support and |acquia-product:onb| engineer to help you
   find ways to `optimize slow
   queries <%5Bacquia-product:kb%5Darticles/how-fix-slow-queries>`__.

.. raw:: html

   </div>

Am I accessing the file system as little as possible?

.. raw:: html

   <div class="answ">

-  |acquia-product:ace| uses the Gluster distributed file system.
   Although Gluster is highly fault tolerant, we do see performance
   issues under conditions of frequent disk I/O. Gluster performance can
   be seriously degraded when handling more than 1000 files in a single
   directory. The extent of the degradation depends on the size of the
   files in question.
-  ŽWe recommend you consider ways to reduce the number of files in a
   single directory, or implement a CDN or a third-party file serving
   service such as Amazon S3. For more details, see:

   -  `Optimizing file paths: Organizing files in
      subfolders <%5Bacquia-product:kb%5Darticles/optimizing-file-paths-organizing-files-subfolders>`__
   -  `Using external storage for large numbers of
      files <%5Bacquia-product:kb%5Darticles/using-external-storage-files>`__

.. raw:: html

   </div>

Is my application as cacheable as it can be?

.. raw:: html

   <div class="answ">

-  Avoid setting Drupal session cookies (Drupal’s SESS\* cookies that
   hold Drupal session information) for anonymous users.
-  Avoid varying content based on HTTP headers or cookie values.
-  Implement AJAX for dynamic elements on a mostly static webpage (for
   example, the cart button on a product catalog).

.. raw:: html

   </div>

Is my memory footprint as small as possible?

.. raw:: html

   <div class="answ">

-  Avoid using PHP memory-limit overrides. Use `memory profiler, XHProf,
   and New
   Relic <%5Bacquia-product:kb%5Darticles/memory-consumption-tracking-tools>`__
   to identify memory leaks and processing bottlenecks.
-  ŽYou may consider conditional memory overrides on select
   administrative webpages, but if high-traffic webpages still require
   higher memory limits after being optimized, you may need additional
   hardware, which could be an additional cost.

.. raw:: html

   </div>

Am I avoiding unnecessary HTTP requests?

.. raw:: html

   <div class="answ">

-  Calling external services inline (for example, in PHP using
   ``drupal_http_request()``) can hang PHP processes, resulting in 503
   errors under load. These calls should be done with AJAX or in a Drush
   job executed by cron.
-  Avoid executing Drupal’s ``cron.php`` file using an HTTP request
   (also known as poor man’s Cron). Acquia’s documentation describes how
   to set up Cron for
   `|acquia-product:ac| </acquia-cloud/manage/cron>`__ and for
   `|acquia-product:edg| </site-factory/manage/tasks/cron>`__.

.. raw:: html

   </div>

Workflow
--------

Acquia’s network tools encode best deployment practices. We give you
development, stage, and production environments for building, testing,
and deploying your code. Remote Administration customers will also see a
`Remote Administration environment </ra/environment>`__. You can use
these environments however you choose, or not at all. If you need custom
environments, you can contact |acquia-product:onb| or Acquia Support to
have these set up for you. Depending on how you want to use these
environments, you may need additional hardware.

An |acquia-product:onb| Customer Onboarding Manager (COM) will walk your
team through using Acquia’s network tools during the network
walkthrough.

.. _vcs:

Version control
---------------

|acquia-product:ac| uses the `Git </acquia-cloud/develop/repository>`__
version control system to manage your application’s code. Git is an
industry standard technology that allows you to manage and track changes
to your application’s code. Basic documentation on using Git is
available from `Resources for learning
Git <%5Bacquia-product:kb%5Darticles/resources-learning-git>`__. For
using version control on |acquia-product:ac|, note the following tips:

-  |acquia-product:ac| offers a feature known as `Live
   Development </acquia-cloud/develop/livedev%20>`__ that enables you to
   change code directly on your servers. This feature can be useful for
   making quick changes. However, we strongly recommend against using it
   as your primary development workflow, because it prevents you from
   taking advantage of some of |acquia-product:ac|’s features, and could
   cause problems with keeping your repository in a consistent state.
-  ŽDo not commit large files into your Git repository. Large files can
   cause your repository to balloon in size, potentially causing
   problems deploying even small code changes. Most binary files (for
   example, documents, images, and videos) belong in Drupal’s public
   files directory, which is not part of your repository. If you do
   commit large files to your repository, note that they cannot be
   removed simply by deleting them, since they will remain in your
   repository’s history.
-  ŽBe sure to deploy to tags, not branches.

Drush
-----

`Drush <https://www.drupal.org/project/drush>`__ is a command-line tool
that is capable of executing Drupal code without accessing the Drupal
web interface. To use Drush with |acquia-product:ac|, you can set up an
aliases file to execute commands against your Acquia application
locally, or you can SSH into your environment and execute Drush commands
anywhere within your application’s docroot. Drush aliases are explained
in more detail in `Drush aliases </acquia-cloud/drush/aliases>`__.

If Drush is not functional on your application (for example, errors
prevent Drush commands from successfully completing), your application
will not be able to receive automated updates through Acquia’s `Remote
Administration automation </ra/automation>`__ services.

.. _cloudapi:

Cloud API
---------

The |acquia-product:api| allows developers to extend, enhance, and
customize |acquia-product:ac|. Some customers use |acquia-product:api|
to integrate with third-party command-line tools, such as Jenkins, to
build automated testing and other QA and acceptance steps into Acquia’s
development/stage/production workflow.

The |acquia-product:api| has three major components:

-  A RESTful web interface that allows direct control of
   |acquia-product:ac| applications. Complete documentation for the
   |acquia-product:api| web interface is available at `Acquia Platform
   APIs </api>`__.
-  |acquia-product:ac| Drush commands that allow you to use all the
   features of the |acquia-product:api| either on the command line or
   from shell scripts using the Drush command-line tool. These Drush
   Cloud commands are documented in the `Drush Cloud
   Reference </acquia-cloud/api/drush-reference>`__.
-  ŽCloud hooks, which are scripts in your code repository that
   |acquia-product:ac| executes on your behalf when a triggering action,
   including certain |acquia-product:api| functions, occurs. Complete
   documentation, templates, and sample scripts for cloud hooks are
   available from GitHub at https://github.com/acquia/cloud-hooks.

The |acquia-product:api| is available to all |acquia-product:ac|
customers. To get started with it, including information about your
Cloud API credentials, Drush aliases, and |acquia-product:ac|, see
`Developing with the Cloud API </acquia-cloud/api>`__.

.. _hooks:

Cloud hooks
-----------

Cloud hooks provide a mechanism for automatically executing scripts in
response to certain platform events, such as code deployments. For
example, you can set up a script to perform database updates
automatically and do feature reversions whenever new code is pushed to a
tag. For more information on how to set up cloud hooks, see `Automating
with Cloud hooks </acquia-cloud/api/cloud-hooks>`__.

Caching
-------

The |acquia-product:ac| platform uses Varnish for caching. All Acquia
load balancers, whether shared or dedicated, have Varnish running and
serving traffic. Certain conditions can prevent Varnish from caching
requests:

-  If your application sets a session cookie for anonymous users,
   Varnish does not cache requests. A common example of this is setting
   session cookies to track a visitor through the application. Also note
   that if you enable printing messages to the screen, Drupal sets a
   session cookie to prevent caching of anonymous traffic. This makes
   sense for development, but it does not make sense for production.
-  ŽSeveral contributed modules can break Varnish caching. Some of them
   are listed in `Module incompatibilities with
   |acquia-product:ac| </acquia-cloud/develop/drupal/module-incompatibilities>`__.
   Some of these modules break caching by setting session cookies.
   Others break caching by setting ``no-cache`` headers.

As you consider your caching strategy, keep the following in mind to
ensure you are making the best use of Varnish, as well as Drupal’s own
internal caching mechanisms:

-  Ensure that your build includes the basic set of modules for enabling
   selective purging of Varnish cache:

   -  `|acquia-product:ap| <https://www.drupal.org/project/acquia_purge>`__
   -  `Cache Expiration <https://www.drupal.org/project/expire>`__
   -  `Advanced Page Expiration <https://www.drupal.org/project/ape>`__

-  Set cache headers on webpages that may require a lower cache lifetime
   (for example, your homepage). See `Bypassing Varnish
   cache <%5Bacquia-product:kb%5Darticles/bypassing-varnish-cache>`__
   for more information.
-  ŽConsider loading dynamic elements asynchronously. If every element
   on your webpage is static except for one, then loading that one
   dynamic element using JavaScript can keep the rest of the webpage
   cacheable.
-  ŽVerify that Varnish is caching optimally prior to load and
   performance testing.
-  You can prevent Varnish from caching in your development environment,
   so your developers can quickly evaluate changes. See `Disabling
   caching and aggregation in non-production
   environments <%5Bacquia-product:kb%5Darticles/disabling-caching-and-aggregation-non-production-environments>`__
   for more information.
-  ŽAvoid varying content based on cookie and header values. This is
   common with websites that want to enable users to set language
   preferences or that want to serve different content to users in
   different countries. Ideally, all content variances are addressable
   on the URL and therefore are compatible with caching. If this is not
   possible, you may need to engage Acquia to create a custom Varnish
   configuration.
-  Create an adaptive or responsive theme. Server-side device detection
   is incompatible with Varnish caching.

.. _md:

Incompatible modules
--------------------

Ensure that you validate your build against Acquia’s list of
incompatible modules. A list of those modules is available at `Module
incompatibilities with
|acquia-product:ac| </acquia-cloud/develop/drupal/module-incompatibilities>`__.
|acquia-product:onb| engineers will alert you if they find one of these
modules in your build. However, it is best to catch these early, before
too many dependencies have been built upon them.
