.. include:: /common/global.rst

Cloud Service Management limitations
====================================

Cloud Service Management is incompatible with the following products and
features:

-  Scaling changes cannot be scheduled
-  Elastic IP (EIP) addresses to support IP whitelisting
-  |acquia-product:edg|
-  Dedicated cron and memcache servers
-  PCI support
-  HIPAA support
-  |acquia-product:cf| or SecureVPN

   .. note::

     Production and staging environments can be deployed in
     |acquia-product:cf|, but development environments cannot. Because of
     this behavior, development environments will not have network
     isolation or VPN access.

-  Multi-region failover
-  Apache's ``mod_proxy`` module
-  Custom server configuration settings, including ``mod_proxy`` and
   memcached sizes greater than 64MB
