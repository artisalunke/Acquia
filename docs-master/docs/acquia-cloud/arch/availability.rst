.. include:: /common/global.rst

|acquia-product:ace| availability and disaster recovery
=======================================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/arch/availability/*

|acquia-product:ace| is designed for high availability, with guaranteed
99.95% uptime. This page describes how Acquia delivers high availability
for |acquia-product:ace|.

-  `High availability architecture <#ha>`__
-  `Disaster recovery - Multiregion replication <#multiregion>`__
-  `Backups </acquia-cloud/arch/availability/backups>`__

.. _ha:

High availability architecture
------------------------------

|acquia-product:ac| is built on Amazon Web Services (AWS)
infrastructure, which is physically remote from the Acquia offices.
|acquia-product:ac| customers may choose the `geographic
region </acquia-cloud/arch#aws>`__ for their application's location.

Each region contains multiple Availability Zones. AWS Availability Zones
are separate yet interconnected data centers within the major regions.
|acquia-product:ace| offers high availability by using multiple AWS
Availability Zones in one AWS region with redundant servers serving each
layer of the technology stack. The following are the three main
components of a Drupal application hosted by |acquia-product:ace|:

-  Reverse proxy caching and load balancing servers (Nginx and Varnish)
-  Web servers (Apache with PHP and Drupal code)
-  Database servers (Percona (MySQL))

At the Internet-facing tier, a software-based load balancer is deployed
with a hot standby in a different availability zone in the same region.
The load balancer distributes load across multiple web servers, which
are also distributed across multiple availability zones. Acquia's expert
operations team adds additional web servers to the resource pool as
needed. The load balancer continuously monitors the web servers, and if
a server becomes unavailable, it removes it from the pool of hosts
serving the application. Web servers use a shared network file system
(GlusterFS) so that all files are kept in sync and redundant to each
other.

At the database layer, a scalable database cluster serves the
application with active and passive database servers in multiple
availability zones. The active master database server continuously
updates the passive master database using MySQL replication. In the
event of a failure of the master database, the passive database becomes
primary through a DNS-based failover.

It is Acquia’s policy to restore customer services in the event of a
major disaster in the best time frames. If the services in the current
zone or region were severely impacted, Acquia would do its best to
restore services in an alternate Availability Zone or region.

.. _multiregion:

Disaster Recovery - Multiregion replication
-------------------------------------------

Optionally, for customers with very high availability requirements,
Acquia offers |acquia-product:ace| customer environments with hot
standby applications in an alternate region, thus providing live
failover capabilities for disaster recovery.

|Replication logical.png|

Related topics
--------------

-  `|acquia-product:ac| technology platform and supported
   software </acquia-cloud/arch/tech-platform>`__
-  `Security and compliance </acquia-cloud/arch/security>`__
-  `Monitoring and support </acquia-cloud/arch/monitor>`__
-  `Change management and maintenance </acquia-cloud/arch/change>`__

.. |Replication logical.png| image:: https://cdn4.webdamdb.com/1280_I9fEvjwjeue2.png?1526476037
   :class: no-sb align-center
   :width: 500px
   :height: 450px
