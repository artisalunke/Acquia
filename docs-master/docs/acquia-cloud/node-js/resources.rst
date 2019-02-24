.. include:: /common/global.rst

Resources and limitations for Node.js environments
==================================================

This documentation page describes the specific resources available for
your use in |acquia-product:ac| Node.js application environments, and
the current limitations of these environment types.

.. _size:

Application sizes
-----------------

Node.js applications have three sizes: Small, Medium, and Large. Each
application size has a corresponding production environment and a Small
development environment. The environment sizes have the following
limits:

+-------------+-------------+-------------+-------------+-------------+
| Feature     | Development | Production  | Production  | Production  |
|             | - Small     | - Small     | - Medium    | - Large     |
+=============+=============+=============+=============+=============+
| Max number  | 4           | 4           | 8           | 12          |
| of          |             |             |             |             |
| processes   |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Max RAM per | 1.875 (7.5  | 1.875 (7.5  | 1.875 (15   | 1.875 (22.5 |
| process     | total)      | total)      | total)      | total)      |
| (GB)        |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Resources
---------

Each environment in a Node.js application includes the following
components:

+-------------------+--------------+
| Component         | Version      |
+===================+==============+
| **Web server OS** | Ubuntu 16.04 |
+-------------------+--------------+
| **Load balancer** | Ngnix 1.12.1 |
+-------------------+--------------+
| **Node.js**       | 6.11.1       |
+-------------------+--------------+
| **npm**           | 2.15.11      |
+-------------------+--------------+

Also included are the following items:

-  |acquia-product:ac| pipelines feature
-  A Git repository

Limitations
-----------

Node.js environments in |acquia-product:ac| have the following
limitations:

-  The following features are not supported:

   -  |acquia-product:vpc|
   -  SSH access into servers
   -  Varnish or custom VCLs
   -  HIPAA or PCI compliance
   -  Memcached
   -  CD environments

-  There is no supported database service or file system asset manager,
   but you can connect to an external file system/database service, such
   as a Drupal website.
-  Node.js applications can expose only one port, indicated by
   ``process.env.PORT``, which is set by Acquia and cannot be
   overridden. You can, however, use
   `websockets </acquia-cloud/node-js/websockets>`__ to handle multiple
   concurrent connections.
