.. include:: /common/global.rst

Purging Varnish cache on |acquia-product:ac|
============================================

There are major advantages to having long cache lifetimes and expires,
which means that it's important to use Varnish with Drupal for
performance improvements. However, when changes are made or new content
is published, you don't want to wait a long time for visitors (including
non-authenticated users) to see the changes. In these cases, you should
periodically purge your Varnish cache.

Varnish excels at storing pages, CSS, and JavaScript files, as well as
multimedia files, for as long as possible, so that visitor requests
don't hit the back-end (in most scenarios, this will be Apache). This
greatly helps with performance and allows an application to scale much
better than it would if only Apache was serving pages. When your
organization decides to implement a caching strategy, you will need to
explore all available options and decide what's best for your situation.
For more information, see `Using
Varnish </acquia-cloud/performance/varnish>`__.

Select from the following methods to purge your Varnish cache:

-  `Acquia Purge <#acquia_purge>`__
-  `Programmatic purging <#program>`__
-  `Acquia Cloud API <#api>`__
-  `Acquia Cloud Hooks <#cloud_hooks>`__
-  `Other methods <#other>`__

.. _acquia-purge:

Using Acquia Purge
------------------

The `Acquia Purge <https://www.drupal.org/project/acquia_purge>`__
module is the fastest and most convenient way to purge caches. It
provides a non-programmatic way to purge Varnish-powered load balancers
using a UI, and it integrates the
`Rules <https://www.drupal.org/project/rules>`__ and `Cache
Expiration <https://drupal.org/project/expire>`__ modules for extra
flexibility and proactive purging.

Read more about installing and using |acquia-product:ap| in the
`|acquia-product:ap|
documentation </articles/installing-acquia-purge>`__.

.. _program:

Purging programmatically
------------------------

While |acquia-product:ap| is the best method when it comes to
implementing a caching strategy, another good method is to use the
`Purge <https://www.drupal.org/project/purge>`__ and `Cache
Expiration <https://www.drupal.org/project/expire>`__ modules.

The Purge module clears URLs from reverse proxy caches like Varnish and
also issues an ``http PURGE`` request to them. It works with the Cache
Expiration module to act on events that are likely to expire URLs from
the proxy cache and interact with Rules and Drush. This results in
delivering faster content updates to end users. |acquia-product:ap| is
recommended on |acquia-product:ac| because it has many of the same
features, and the maintainers for Purge and |acquia-product:ap| work
closely to ensure compatibility.

If you absolutely must purge a page manually from |acquia-product:ac|,
you can `learn how to manually purge a
page </acquia-cloud/performance/varnish/manually-purge>`__.

.. _api:

Using the |acquia-product:ac| API
---------------------------------

Acquia has developed the `|acquia-product:ac| API </acquia-cloud/api>`__
to enable developers to take advantage of even more automation as part
of their daily workflow. The |acquia-product:ac| API is a RESTful web
interface that allows developers to extend, enhance, and customize
|acquia-product:ac|. It includes developer workflow, application
management, and provisioning capabilities. Of all its commands, the
relevant one here is the `delete the domain cache instance
method <https://cloudapi.acquia.com/#DELETE__sites__site_envs__env_domains__domain_cache-instance_route>`__:

``DELETE /sites/:site/envs/:env/domains/:domain/cache``

The preceding command triggers a Varnish cache purge for a specific
domain. It works exactly like clearing the cache for a domain using the
|acquia-product:ui|, as described in `Clearing the Varnish
cache </acquia-cloud/performance/varnish#clear>`__. Here's an example:

``curl -s -u user:pass -X DELETE \   https://site.com/v1/sites/site/envs/prod/domains/site.com/cache.json``

For more information about the |acquia-product:ac| API, see the
|acquia-product:ac| `API documentation page </acquia-cloud/api>`__, and
check out the `Cloud API reference
page <https://cloudapi.acquia.com/>`__.

.. _cloud_hooks:

Using |acquia-product:ac| Hooks
-------------------------------

`Cloud Hooks </acquia-cloud/api/cloud-hooks>`__ allow you to automate
almost anything as part of your workflow actions. A Cloud Hook is a
script in your code repository that |acquia-product:ac| executes on your
behalf when a triggering action occurs (for example, when a database,
some code or some files are copied from one environment to the other).
You can implement *Cloud API Varnish cache clears* as part of Cloud
Hooks triggers, for instance when you are deploying code from the
Development to the Staging .

.. important::

    Acquia strongly recommends that you use extreme caution when purging the
    Varnish cache on a production domain.

For more information about |acquia-product:ac| Hooks, read our
`|acquia-product:ac| Hooks </acquia-cloud/api/cloud-hooks>`__
documentation page, and check out the `Cloud Hooks GitHub
repository <https://github.com/acquia/cloud-hooks>`__.

.. _other:

Using other purge methods
-------------------------

Although |acquia-product:ap| is the preferred and safest method of cache
purging, there are some other methods that you can use if necessary:

-  `Clearing the cache for a
   domain </acquia-cloud/performance/varnish#clear>`__
-  `Manually purging a page from Varnish
   cache </acquia-cloud/performance/varnish/manually-purge>`__
