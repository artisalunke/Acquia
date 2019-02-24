.. include:: /common/global.rst

Monitoring and support
======================

To ensure high availability for hosted applications,
|acquia-product:ace| includes internal, security, and infrastructure
monitoring services and support 24 hours a day, seven days a week
(24/7).

The current status of |acquia-product:ac| services is always available
at `status.acquia.com <https://status.acquia.com/>`__ and is also
updated on
`twitter.com/acquia_support <https://twitter.com/acquia_support>`__.

.. _internal:

Internal monitoring
-------------------

Acquia uses the Nagios monitoring platform to provide instant access to
vital, real-time, and historical metrics of the servers it provisions in
the AWS infrastructure, which includes the applications that Acquia
manages for its customers. Acquia monitors over 40 metrics, which are
linked to alerts by email, SMS, and pager. Metrics include, but are not
limited to, the following:

-  Disk usage
-  CPU usage
-  Memory usage and swap activity
-  Running processes
-  Database size and available storage space

Acquia monitors dozens of system parameters and periodically tunes
various thresholds across different system types to optimize platform
monitoring. Acquia does not publish alert thresholds due to the quantity
and changing nature of these operational parameters. Systems are managed
to provide the best managed service possible and to meet or exceed
platform uptime commitments.

Acquia's monitoring systems use alerting and escalation to ensure that
our Operations team is notified when alerts are generated. Acquia
Operations team members work on three continents and respond to alerts
24/7.

Acquia does not independently monitor the health and performance of the
applications you host on |acquia-product:ac|. If your application's
health or performance are impacted by server-related issues detected by
our monitoring systems, then the previously mentioned notification and
mitigation practices will apply. If, however, the application is down or
impaired as a result of application-layer issues which do not impact the
stability of the application’s servers, then Acquia will be able to
provide assistance only if the Acquia Support team is contacted by phone
or Support ticket.

|acquia-product:ac| provides a self-service feature called `uptime
monitoring </acquia-cloud/manage/uptime>`__. You can use this feature to
monitor application performance and availability, and it can be
configured to notify members of your team in the event that issues are
detected. Uptime monitoring does not automatically contact Acquia
Support, and many issues detected by this feature either quickly resolve
themselves or can be resolved without the assistance of Acquia Support.
If you detect any issues with this feature that require Acquia’s
assistance to resolve, and your subscription includes Acquia Support
tickets, create a Support ticket and we will be happy to assist you with
your investigation.

.. _security:

Security monitoring
-------------------

Acquia uses OSSEC, an open-source, host-based Intrusion Detection System
(IDS), which performs log analysis, integrity checking, and time-based
alerting.

.. _infra:

Infrastructure monitoring
-------------------------

Amazon monitors critical infrastructure availability and health
including power and environmental conditions, network and Internet
peering, and hardware. The Acquia Support team is kept abreast of any
infrastructure issues that can impact our customers.

.. _self:

Self-service monitoring
-----------------------

Acquia provides tools that you can use to monitor the state of your
applications, including the `Acquia uptime monitoring
service </acquia-cloud/manage/uptime>`__. You can opt to `receive email
notifications </acquia-cloud/manage/uptime#email>`__ of critical issues
detected by the uptime monitoring service.

.. _24-7:

24/7 Support
------------

Acquia’s Support team is available 24/7 to respond to critical,
application-impacting issues. For more information, see the `Support
Users Guide </support/guide>`__.

.. _related:

Related topics
--------------

-  `|acquia-product:ac| technology platform and supported
   software </acquia-cloud/arch/tech-platform>`__
-  `Security and compliance </acquia-cloud/arch/security>`__
-  `Change management and maintenance </acquia-cloud/arch/change>`__
