.. include:: /common/global.rst

Upsizing your servers
=====================

To maintain acceptable website performance, Acquia will upsize your
website's infrastructure components to accommodate any anticipated (or
unanticipated) needs. Upsizes can be made both upon customer request in
anticipation of increased loads, or reactively in response to serious
performance issues that trigger operational monitoring alerts.

Before any changes are made, Acquia will complete an analysis of the
anticipated or real-time system performance issues (either in advance or
on-the-fly) to determine the necessary configuration requirements. In
either case, any added system resources are provided for an additional
charge, in accordance with the the terms of your contract with Acquia.

Planned upsize events
---------------------

Acquia requests that you provide at least one week notice for planned
`high traffic or load-inducing events </support/traffic>`__. In the case
of a planned event, use the following process:

#. `Create a detailed support ticket </support/traffic#ticket>`__.
#. Acquia Support will evaluate the anticipated system resource
   requirements, and both you and your Acquia Account Manager coordinate
   and approve any additional charges.
   If required, both you and Acquia Support will determine the timeline
   for the upsize maintenance window.
#. Acquia upsizes the appropriate components at the required time.
#. After the upsize event has completed, if it is safe to do so, Acquia
   will downsize the components.

Unplanned upsize events
-----------------------

For whatever the reason, unanticipated system loads may require Acquia
to temporarily increase the amount of system resources to restore
acceptable website performance. In these cases, before performing a
component upsize, Acquia will make every attempt to alert you to
coordinate both diagnosis and repair. If remediation is unsuccessful, or
application performance rapidly degrades and impairs critical website
functionality, Acquia may proactively upsize system resources in
accordance with the terms of your contract with Acquia.

System evaluations
------------------

Acquia `monitors </acquia-cloud/monitor>`__ and performs system
evaluations across the entire infrastructure, including balancers, web
servers, file servers, and database servers. When an operational alert
occurs, Acquia reviews the infrastructure to determine if the alert is
due to infrastructure (hardware and operating system issues) or with the
website's ability to handle traffic.

Traffic analysis is performed to determine whether the higher levels are
normal traffic or a malicious attack. After the analysis is complete,
Acquia will take actions that depend on the results of the analysis:

-  *Attack* - Measures are taken to block the attackers. Acquia may
   increase system resources simultaneously with defensive measures in
   order to regain acceptable performance as rapidly as possible.
-  *Normal but elevated* - The system is evaluated to determine what
   resources in the configuration can be upsized to effectively handle
   the traffic.

Acquia diagnoses system dynamics to ensure the most effective resolution
— the alerting component may not be the root cause of an issue, and may
have generated an alert due to upstream problems.

Website performance issues can result from problematic code that
generates excess load on the infrastructure. Temporary upsizes can
alleviate performance issues while the root cause is determined, and
while you repair the issue. Acquia Support will evaluate these
situations and help determine if website code is the root cause, and if
effective, will suggest a temporary upsize.

Emergency upsizing
------------------

After a rapid analysis, Acquia will upsize system resources in the least
disruptive manner possible. If the website is operational but suffering
from poor performance, Acquia will attempt to upsize resources while
maintaining the website's operation. In the event of an outage, Acquia
will attempt to upsize resources in a manner which returns the website
to an operational state as quickly as possible.

Websites not using Acquia's `high availability </acquia-cloud/arch/availability#ha>`__ architecture will experience downtime when some resources are upsized.

Customer notifications
----------------------

After Acquia performs a preliminary evaluation based on an operational alert, Acquia Support will create a proactive `Critical </support/tickets#urgency>`__ support ticket to notify customers. Depending on the severity and urgency of the issue, Acquia may take the following steps:

-  Coordinate with the customer on required actions, including obtaining permission to upsize whenever possible.
-  Take unilateral action to ensure website availability in accordance with contractual terms.

Actions performed by Acquia to ensure website stability will be documented in the ticket, which also notifies your Account Manager. Acquia will then coordinate with you to evaluate and perform infrastructure downsizes when it is safe and appropriate.

Acquia Support will diagnose performance issues based on the `scope of support services </support/guide#scope_support>`__ and, where possible, make optimization recommendations for both current and future needs. Your are responsible for implementing any provided recommendations. Acquia Support may also recommend engaging Acquia Professional Services or third-party resources for either a deeper analysis or the repair of highly complex problems.
