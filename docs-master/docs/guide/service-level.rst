.. include:: /common/global.rst

Service Level Policy - Product Guide
====================================

**Last updated: November 2, 2016**

This Service Level Policy governs the use of |acquia-product:ace| and
|acquia-product:edg| (each, a “PaaS”) under the terms of the applicable
Order between Acquia and Customer.

#. **Service Commitment**

   Acquia will use commercially reasonable efforts to make PaaS
   infrastructure available for 99.95% during any calendar month during
   the applicable Subscription Term (the “Service Commitment”). In the
   event Acquia does not meet the Service Commitment, Customer will be
   eligible to receive a Service Extension as described below.

#. **Definitions**

   “Availability” will be calculated per calendar month, as follows:

   |Availability formula|

   where:

   -  *total* means the total number of minutes for the calendar month
   -  *nonexcluded* means downtime/unavailability that is not excluded
   -  *excluded* means the Service Commitment exclusions defined below.

   “Unavailability” means that the PaaS infrastructure is unresponsive
   or responds with an error.

#. **Service Extension**

   In the event Acquia does not meet 99.95% general availability of the
   PaaS for a calendar month, for each one-half hour of unavailability
   Customer will receive a one-day extension of their Subscription (each
   a “Service Extension”). To properly claim a Service Extension,
   Customer must inform Acquia within fifteen days of the purported
   outage and provide a full description of the service interruption,
   including logs if applicable. If Customer has accumulated Service
   Extensions during two consecutive months or three months in any
   six-month period, Customer may terminate the applicable Order upon
   seven days advance written notice to Acquia. In the event of an
   unavailability of the PaaS that is directly attributable to flaws in
   Customer’s environment (including the underlying code) where, despite
   reasonable notification from Acquia that such flaws are adversely
   impacting availability and Customer fails to correct such flaws, then
   Acquia may terminate the applicable Order upon 30-days written notice
   to Customer. The Service Extension and termination rights constitute
   Customer’s exclusive remedy and Acquia’s sole liability and
   obligation for any failure to maintain the Service Commitment.

#. **Service Commitment Exclusions**

   The Service Commitment does not apply to any Unavailability, outage,
   suspension or termination of any Acquia PaaS performance issues:

   i.    that are caused by factors outside of Acquia’s reasonable
         control, including any force majeure event, network intrusions
         or denial of service attacks;
   ii.   any outages that result from any actions or inactions of
         Customer or any third parties engaged by Customer, missing
         Customer Data, errors caused by Customer code or Drupal
         configuration errors, or usage capacity in excess of the
         Customer purchased amount;
   iii.  any outages caused by programming errors in Customer’s
         website(s), programming bugs in the third-party
         extensions/modules made available through |acquia-product:ac|
         or the |acquia-product:edg| Platform, Drupal Modules with
         |acquia-product:edg|;
   iv.   any outages attributable to flaws in Customer’s environment
         (including the underlying code) where, despite reasonable
         notification from Acquia that such flaws are adversely
         impacting availability and Customer fails to correct such flaws
         (e.g., failure to upsize to recommended hardware
         configuration);
   v.    any outages lasting less than 1 minute but no more than 3 such
         outages in a 24 hour period;
   vi.   any outages related to emergency maintenance to Customer’s
         website(s) (e.g., to install security fixes);
   vii.  any outages resulting from scheduled maintenance (typically
         11pm to 7am at the datacenter location identified on Customer’s
         Order), if Acquia notified Customer 48 hours prior to the
         commencement of the maintenance work (there will be no more
         than two hours of scheduled maintenance downtime per calendar
         year);
   viii. Unavailability that relates to any malware, viruses, Trojan
         horses, spyware, worms or other malicious or harmful code in
         the website that (1) was not introduced by Acquia or (2) was
         not introduced as a result of Acquia’s failure to perform the
         Services in compliance with the standard included herein or in
         the Subscription and Services Agreement;
   ix.   acts or omissions caused by Customer’s CDN.

   In addition, unavailability of some specific features or functions
   within the website while other features remain available will not
   constitute Unavailability of the website, so long as the unavailable
   features or functions are not, in the aggregate, material to the
   website.

   In the event of any outages described above, Acquia will use
   commercially reasonable efforts to minimize any disruption,
   inaccessibility and/or inoperability of the website in connection
   with outages, whether scheduled or not. Such efforts will include
   instances in another Availability Zone if available.

.. container:: message-status

   Acquia Inc. reserves the right to change the Products and Services Guide based on prevailing market practices and the evolution of our products. Changes will not result in a degradation in the level of services provided during the period for which fees for such services have been paid.

.. |Availability formula| image:: https://cdn4.webdamdb.com/1280_s4WBuzXj6661.png?-62169955200
   :class: no-sb
   :width: 420px
   :height: 69px
