.. include:: /common/global.rst

PECL memcache extension
=======================

About Memcached

-  `Intro </acquia-cloud/memcache/intro>`__
-  PECL
-  `Drupal </acquia-cloud/memcache/drupal>`__

The PECL memcache extension provides PHP with an API to communicate with
the Memcached service. The classes and functions in the extension
accomplish the following tasks:

-  Consume the list of configuration and connection details of the
   servers running Memcached from the Drupal Cache API configuration.
-  Receive directives from Drupal's `Cache
   API​ <https://www.drupal.org/docs/8/api/cache-api/cache-api>`__, such
   as ``cache_set()`` and ``cache_get`` and translates them into
   commands that can be interpreted by the Memcached service. For more
   information about Drupal integration, see `Drupal and the memcache
   module </acquia-cloud/memcache/drupal#memcache>`__.
-  Maintain a *hash ring​* on which data objects are plotted. This loop
   determines which server should store the current item.

   -  In an effort to maintain a uniform distribution when plotting data
      and to spread data evenly amongst all servers running Memcached,
      every server is plotted several times to the loop. Changing the
      number of servers hosting a single Memcached loop can cause a
      key-value pair to be stored on a different server.
   -  For each data object, a series of hashing algorithms converts the
      key into an integer — this integer is plotted to the loop. The
      extension uses this to determine where to look for information.
      Acquia recommends against assigning cache bins to specific servers
      as this has a negative impact on high availability on our hosting
      platform.

.. _scaling:

Servers and scaling
-------------------

The PECL memcache extension creates a single storage pool of cached data
based on Drupal's Cache API configuration. Each server holds an
associative array that represents part of the hash ring. Each key-value
pair is stored in one location, with no duplication across a distinct
loop of servers. This virtual architecture enables Memcached to either
share memory with other processes across multiple servers or be
consolidated to one more dedicated Memcached servers.

|Hash ring diagram|

Memcached servers in a hash ring are unaware of each other. Each server
knows which data in its local array is least recently used and will
purge that data accordingly to make room for newer requests.

Hashing algorithm
~~~~~~~~~~~~~~~~~

By default, the PECL memcache extension on |acquia-product:ac| employs a
caching strategy called *consistent hashing*. You can verify that this
is implemented in your ``php.ini`` file:

``memcache.hash_strategy=consistent``

As an example, using `n mod
64 <https://en.wikipedia.org/wiki/Modular_arithmetic>`__ as the
(simplified) consistent hashing algorithm results in an integer that
falls between 0 and 63. Because of this, any hashed object is going to
have to fit somewhere on the following loop:

|Modulus loop|

At the beginning of a request, Drupal uses the `Memcache API and
Integration <https://www.drupal.org/project/memcache>`__ module to pass
all connection information to the PECL memcache PHP extension. This
includes an array of available servers. For example:

``web-1234, web-1235, web-1236``

Each of these hostnames are hashed and converted to an integer,
decreasing the likelihood that the servers will appear in alphanumeric,
sequential order. By doing this, the process increases the likelihood of
webs being distributed evenly in the hash ring. The array of servers is
then passed to the Memcached service, which plots each value to a hash
ring. Memcache does this several times per server, using different
hashing parameters, with the goal of creating an even distribution of
server endpoints throughout the loop. After all hostname points have
been plotted, objects are encoded using the following:

``$full_key = urlencode($prefix . $bin . '-' . $key);``

This creates a key in the following format:

``examplesite_-cache_page-https%3A%2F%2Fwww.example.com``

The objects are hashed using the crc32 hashing algorithm and plotted in
a similar fashion.

|memcache crc32 hash plot|

Servers and objects are plotted to the hash ring with an absolute value,
allowing the Memcached service to quickly determine where they exist. If
any servers in the loop or array are removed, the website will not lose
all of its cached data and the PECL memcache extension will evenly
distribute the load amongst the remaining servers.

.. |Hash ring diagram| image:: https://cdn2.webdamdb.com/md_2YyTEiMEbWd0.png?1526476101
   :class: align-center no-sb
   :width: 450px
.. |Modulus loop| image:: https://cdn4.webdamdb.com/md_QRStWzmSFvo4.png?1526476089
   :class: align-center no-sb
   :width: 400px
.. |memcache crc32 hash plot| image:: https://cdn3.webdamdb.com/md_Mw6zRg27Pb41.png?1526475958
   :class: align-center no-sb
   :width: 550px
