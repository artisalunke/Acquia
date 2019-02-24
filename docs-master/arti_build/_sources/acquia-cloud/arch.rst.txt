.. include:: /common/global.rst

|acquia-product:ac| architecture and key concepts
=================================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/arch/*

This section of the |acquia-product:ac| documentation describes how
|acquia-product:ac| works, including information about the
|acquia-product:ac| architecture, security, high availability features,
and compliance with standards and regulations.

|acquia-product:ac| provides a robust managed solution for
mission-critical Drupal applications. Traditional hosting services may
provide little more than virtual machines, leaving you with the task of
managing and running the servers. With |acquia-product:ac|, you bring
your code and files, and Acquia handles the rest. Acquia takes care of
selecting, deploying, and maintaining a Drupal-optimized platform.
|acquia-product:ac| provides high availability elastic cloud resources,
with configuration management, monitoring, optimization, and caching
built in, all backed up by an operations team staffed by cloud and
Drupal experts, ready to respond 24 hours a day, seven days a week.

.. _infra:

|acquia-product:ac| infrastructure
----------------------------------

|acquia-product:ac| applications run on a Drupal-optimized platform
hosted in the Amazon Web Services (AWS) cloud environment. The core of
the platform is an open-source LAMP server stack, combining the Linux
(Ubuntu) operating system, Apache web server, MySQL (Percona) database,
and PHP programming language with Drupal. |acquia-product:ac| servers
are built on the AWS Elastic Compute Cloud (EC2), Elastic Block Storage
(EBS), and Elastic IPs (EIP).

The exact configuration of an |acquia-product:ac| application's
infrastructure depends on several factors, including whether the
application is part of |acquia-product:ace| or |acquia-product:acs|. For
example, here is an diagram of an |acquia-product:ace| application, and
how the components interact with one another for different user
profiles:

|Enterprise architecture|

As a comparison, the following is an example of an |acquia-product:acs|
application, and its component interactions:

|Professional architecture|

As indicated in the diagrams, there are four main components for both
|acquia-product:ace| and |acquia-product:acs| applications:

-  *Reverse proxy caching and load balancing servers* - Varnish/nginx
-  *Web servers* - Apache with PHP and Drupal code
-  *Database servers* - MySQL (Percona)
-  *Network file system* - (GlusterFS)

For more information, see `|acquia-product:ac| technology platform and
supported software </acquia-cloud/arch/tech-platform>`__.

Compared to |acquia-product:acs|, |acquia-product:ace| offers additional
features for high availability, including redundant server instances at
each level of the stack, and higher levels of support, including
unlimited application support and an operations team that is available
24x7 to remotely administer your applications and to change your
infrastructure on demand. For more information, see `Comparing
|acquia-product:acs| and
|acquia-product:ace| </acquia-cloud/arch/compare-ace-acp>`__.

.. _aws:

AWS server regions
------------------

|acquia-product:ac| is built on Amazon Web Services (AWS)
infrastructure, which is physically remote from Acquia's offices. The
AWS environment consists of major regions and Availability Zones.
|acquia-product:ac| customers may choose the geographic region for their
application's location. |acquia-product:ac| currently supports the
following zones:

-  US (East and West)
-  EU (Frankfurt and Ireland)
-  Asia Pacific (Tokyo, Singapore, and Sydney)
-  South America (São Paulo)

.. |Enterprise architecture| image:: https://cdn3.webdamdb.com/1280_o6ESUmglG4C2.png?1526475851
   :class: no-sb
   :width: 3000px
   :height: 1688px
.. |Professional architecture| image:: https://cdn3.webdamdb.com/1280_UJk1BjRHMb36.png?1526475677
   :class: no-sb
   :width: 3000px
   :height: 1688px
