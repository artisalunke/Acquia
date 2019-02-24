.. include:: /common/global.rst

Drupal and the memcache module
==============================

About Memcached

-  `Intro </acquia-cloud/memcache/intro>`__
-  `PECL </acquia-cloud/memcache/pecl>`__
-  Drupal

Drupal core provides a `Cache
API <https://www.drupal.org/docs/8/api/cache-api/cache-api>`__ that
provides a structure for cached data objects (both key and value). This
API allows for access to multiple storage implementations through a
consistent set of functions — one of which is the Memcache API &
Integration Module.

.. _memcache:

Memcache API and Integration module
-----------------------------------

The `Memcache API and
Integration <https://www.drupal.org/project/memcache>`__ module acts as
an interface between Drupal core and the PECL memcache PHP library. The
following files play a large role:

-  ``settings.php`` - Provides the following storage implementation (in
   this case, Memcached) configuration and connection information:

   -  ``cache_backends`` - ``use memcached``
   -  ``cache_class_`` - ``select these particular cache bins``
   -  Acquia Hosting default memcached port - ``11211``
   -  ``Memcache_servers``

-  ``memcache.inc`` - Part of the Memcache API and Integration module
   that plugs in to Drupal, pulling all configuration and connection
   data into objects that can be used by the module. This is the heart
   of the storage implementation
-  ``dmemcache.inc`` - Plugs in to the PECL memcache extension, and
   performs the following tasks, in order:

   #. Creates the key (memcache key prefix, cache bin, and the CID​).
   #. Trims the key using the SHA1 hashing algorithm if it exceeds 250
      characters.
   #. ``Dmemcache_get​`` takes the full key name, and then generates a
      new dmemcache_object.
   #. Determines where to write the object on our `hash
      ring </acquia-cloud/memcache/pecl#scaling>`__.

.. _memory:

Memory management over 1MB
--------------------------

On Acquia's hosting platform, Memcached is configured to save items of
up to 1MB in size. Starting with Memcache API and Integration version
7.x-1.5, the module includes the ability to takes objects larger than
1MB and then break them into smaller, equal objects (called *multi-part
data*). One method to determine that this has occurred is when you see
the ``string _multi`` in your Memcached item's key. Here is a key from a
random website's slab 42 (which contains items ranging in size between
754KB and 1MB):

``ITEM randomcustomer_-cache_views_data-randomcustomer_-cache-_multi5-randomcustomer_user_c ontent%253Apanel_pane_1%253A7ece55917020be962b0b81f576f55022%253Aresults%253A924f8f375f1b9cd3431700faf3acd15d [776277 b; 1478647027 s]``

The end result is an object (a panel pane) being saved to Memcached that
is approximately 5MB.
