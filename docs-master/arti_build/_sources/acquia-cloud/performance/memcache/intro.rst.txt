.. include:: /common/global.rst

Memcached and Acquia hosting
============================

About Memcached

-  Intro
-  `PECL </acquia-cloud/memcache/pecl>`__
-  `Drupal </acquia-cloud/memcache/drupal>`__

Memcached plays a critical role in any Drupal website's\ `caching
strategy on Acquia's </acquia-cloud/performance/memcached>`__ hosting
platform. Memcached may seem like a black box, but with a little
research, we can demystify many of its confusing aspects.

There are four major pieces that comprise Acquia's Memcached solution:
Drupal core, the Memcache API and Integration module, the PECL memcache
PHP extension, and the Memcached service.

|memcache stack|

.. _memcached:

Memcached service
-----------------

Memcached is a service with several components that work together to
ensure stability and uptime for a website.

.. _key-value:

Key/Value storage
~~~~~~~~~~~~~~~~~

Memcached is a *key-value store*, which is a data storage paradigm
designed for storing, retrieving, and managing associative arrays —
commonly known as a *hash*. This contrasts with relational database
object models that enable advanced concepts such as mapping and
datatypes.

Protocols
~~~~~~~~~

Acquia's memcache configuration uses a small group of commands for
handling data in Memcached storage:

-  ``get`` - Retrieve an existing item from storage.
-  ``set`` - Save a new item to storage.
-  ``flush_all`` - Mark an item as ``expired`` so that it cannot be
   retrieved. This method pushes the current item to the front of the
   line, to be replaced by the next cacheable item. It does not free the
   memory used by that item.
-  ``delete`` - Remove an item from storage.
-  ``stats`` - Query the service for aggregated data about the objects
   saved to storage.

.. _partition:

Memory partitioning
~~~~~~~~~~~~~~~~~~~

When the Memcached daemon is started, it reserves memory for object
storage (by default, 64MB). The memory allocated is divided into 1MB
*pages*, which by default provides 64 pages. Memcached initializes a
memory organization concept called a *slab* class on startup. A slab
defines the number of items (chunks) which can be inserted into a 1MB
memory page. By dividing 1MB by that number of chunks, you can determine
that slab’s chunk size.

By default, Memcached creates 42 slabs and assigns a single page to
each. Each successive slab holds fewer, larger chunks based on the
*factor* (by default, 1.25). In the following sample representation of
slabs, notice that the item size (or chunk size) increases by a factor
of 1.25 from the second to the third slab:

``#   Item_Size  Max_age   Pages   Count   Full?  Evicted Evict_Time OOM  2      120B   1168824s       1     170      no        0        0    0  3      152B   1831103s       1     196      no        0        0    0  4      192B   1847211s       1     988     yes       30     9183    0 ... 36   246.8K     27236s       6      21     yes        7     2676    0 37   308.5K      1224s       2       3     yes       91    29174    0 ... 40   602.5K      1696s      11       4     yes        0        0    0 41   753.1K        64s       4       1     yes        6       35    0 42  1024.0K     44944s       5       1     yes       20        1   20``

Memcached saves items by evaluating an item's size, and then writing it
to a slab. In the previous example, note that slab 37 contains items
that range in size from 246.8KB to 308.5KB.

When a slab cannot fit a new item and there is additional memory
available to Memcached, a new page will be assigned to the slab. In the
previous example, slab 37 can contain at most four items, but, depending
on the items' size, may contain only three items:

-  If objects are 248KB, four items equals 992K, which is less than 1MB.
-  If objects are 300KB, because four items equals 1.2MB, after three
   items a new page is created.

When the ``set()`` method is called, Memcached determines the size of
the object, and then locates the slab with the appropriate memory
allocation.

.. _memory:

Memory management
~~~~~~~~~~~~~~~~~

Each Memcached server is configured to manage its memory with Least
Recently Used (LRU) prioritization. The servers oversee their local slab
arrays, producing a list of candidates for removal. When a new item is
assigned to a full slab and there are no free pages to assign to that
slab, the full slab evicts the LRU item from the same slab. This is both
healthy and accepted behavior — assuming that the objects being evicted
are outdated and due to be safely removed.

.. _scale:

Scaling
~~~~~~~

Memcached does not internally provide mechanisms for adding capacity
through additional processes. Instead, this functionality is handled
entirely by an external client, such as the `PECL memcache extension for
PHP </acquia-cloud/memcache/pecl>`__.

.. |memcache stack| image:: https://cdn3.webdamdb.com/md_kBTuJADcdb91.png?1526475495
   :class: align-center no-sb
   :width: 331px
   :height: 364px
