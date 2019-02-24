.. include:: /common/global.rst

Change management and maintenance
=================================

This topic describes Acquia's policies and procedures for change
management and system maintenance on |acquia-product:ac|.

.. _hardware:

Hardware and maintenance
------------------------

Acquia hosts |acquia-product:ac| customers using Amazon Web Services
(AWS) data centers; Amazon has overall responsibility for the hardware
that serves the website. Amazon maintains service agreements with the
hardware and software manufacturers in use in its data centers, which is
necessary to achieve ISO 27002 and SAS70/SSAE16 audit certifications.

.. _provisioning:

Provisioning tools
------------------

Acquia uses custom APIs and central management tools to provision new
hosting clusters, attach storage volumes, and install software and
dependencies in order to provide uniformity in each customer's
environment. Acquia also uses these central management tools to manage
OS and platform configurations and to apply security patches across all
systems.

.. _sla:

System maintenance and downtime
-------------------------------

Acquia is committed to delivering industry-leading, reliable hosting
services. Acquia’s policy regarding changes and updates to
infrastructure in use by customers is to make these changes with as
little customer impact as possible. Delivering these services requires,
on occasion, system maintenance.

The |acquia-product:ace| 99.95% SLA applies to unscheduled downtime and
does not include scheduled maintenance downtime.

.. _sched:

Scheduled maintenance
---------------------

The |acquia-product:ace| high availability cloud architecture ensures
that the vast majority of system maintenance takes place without impact
to services.

Acquia notifies customers at least 48 hours in advance of a scheduled
system maintenance that carries a risk of customer website downtime.
This maintenance is scheduled from 11:00 PM (23:00) to 7:00 AM (07:00)
local time for the `application's service
region </support/guide#platform_maintenance>`__.

.. _emergency:

Emergency maintenance
---------------------

From time to time, a website or infrastructure emergency may require
immediate maintenance. Acquia reserves the right to perform emergency
maintenance to correct website problems, address critical security
issues, and respond to critical alerts. Reasonable efforts will be made
to avoid website downtime.

.. _request:

Customer requested maintenance
------------------------------

Acquia Support will implement customer-requested changes that carry a
risk of outage at a time mutually agreeable to the customer and Acquia.

.. _related:

Related topics
--------------

-  `|acquia-product:ac| technology platform and supported
   software </acquia-cloud/arch/tech-platform>`__
-  `Security and compliance </acquia-cloud/arch/security>`__
-  `Monitoring and support </acquia-cloud/arch/monitor>`__
