.. include:: /common/global.rst

Acquia Commerce Manager Product Guide
=====================================

.. container:: message-status

   |Acquia Commerce Manager logo| For additional information about |acquia-product:acm|, see its `product documentation </commerce>`__.

**Last updated: December 11, 2017**

|acquia-product:acm| connects the Acquia platform to the Customer’s eCommerce platform so that merchandisers can quickly and securely create unique tailored online shopping experiences that best represent their brand.

An |acquia-product:acm| Subscription consists of the following components:

#. Either a single website on `Acquia Cloud Enterprise </guide/cloud-ace>`__ or number of websites permitted within the relevant `Acquia Cloud Site Factory </guide/site-factory>`__ subscription, in a `PCI Virtual Private Cloud <#pci>`__. |br| 
   For specific entitlements related to the portion of |acquia-product:acm| (based on the corresponding level of |acquia-product:acm|), see the relevant sections of the Acquia Product and Services Guide for `Acquia Cloud Enterprise </guide/cloud-ace>`__ or `Acquia Cloud Site Factory </guide/site-factory>`__.
#. **Commerce Connector Service for use with Lightning for Commerce** |br| 
   This is a SaaS (Software as a Service) that connects eCommerce stores to Drupal applications running on either |acquia-product:ace| or |acquia-product:edg|, and is subject to the following:

   - 2.1 **Commerce Connector Service** |br| 
      The |acquia-product:ccs| is to be used the latest version of the open source |acquia-product:ld| for Commerce sub-distribution of Drupal and the latest version of eCommerce platform extension as available for specific platforms in their relevant marketplaces.
   - 2.2 **5 Terabytes of data** |br| 
      Up to 5 Terabytes of data can be transferred through the |acquia-product:ccs| per year. Customers trending towards maximum data usage must work with Acquia Support to address application issues causing the unnecessary transfer of large volumes of data.
   - 2.3 **Data Centers, Backup, and Disaster Recovery for |acquia-product:ccs|:** |br| 
      The infrastructure supporting the |acquia-product:ccs| is physically remote from Acquia’s office facilities. The |acquia-product:ccs| environment consists of major Regions and Availability Zones. Availability Zones are separate yet interconnected data centers within major Regions in the global infrastructure. |acquia-product:ccs| utilizes a highly available redundant architecture that distributes replicated redundant server types (load balancing, caching, web and database servers) across multiple Availability Zones within the same Region. Acquia will use commercially reasonable efforts to restore the services in an alternate Availability Zone within the same Region in the event service in Customer's assigned Availability Zone is severely impacted. The |acquia-product:ccs| transmits data and does not process or store it as such there is no data to backup performed as part of the service.
   - 2.4 **Service Level Policy** |br| 
      |acquia-product:ccs| inherits the SLA of the applicable
      |acquia-product:ace| or |acquia-product:edg| subscription
      purchased with the |acquia-product:acm|.

#. **Payment Card Industry Data Security Standard (PCI DSS) Compliant Environment (“PCI Environment”)** |br| 
   Acquia provides a PCI-compliant hosting environment as part of |acquia-product:acm|. PCI DSS compliance applies to merchants and service providers that process, store, or transmit credit card data. PCI DSS is a multifaceted security standard that includes requirements for security management, policies and procedures, network architecture, software design, and other critical protective measures. This comprehensive standard helps organizations proactively protect credit card data that is transmitted or stored with this environment. Only those Customer applications built on the PCI Environment or via a dedicated PCI VPC Shield offering included with the applicable |acquia-product:acm| subscription enjoy such PCI protections. |br| 
   Acquia’s PCI Environment is reviewed and validated by a PCI Security Standards Council authorized independent Quality Security Assessor (QSA) on an annual basis to against the then-current PCI-DSS standards applicable to a Level 1 service provider. Customers are responsible for assessing and implementing applicable PCI Compliance requirements for their applications they built on the PCI Environment.
#. **Support Services** |br| 
   Customer’s subscription to |acquia-product:acm| includes unlimited diagnosis support for |acquia-product:ccs|, as described in the `Supportability Matrix </support/guide#supportability>`__ in the Support Users' Guide. The Customer can `contact Acquia Support </support#contact>`__ in accordance with both the `Support Users Guide </support/guide>`__ and the stated `Urgency Levels </support/guide#problem%20>`__. Initial response times for support requests vary on both the urgency level and Customer’s Subscription tier, as described in the Support Users Guide.

.. container:: message-status

   Acquia Inc. reserves the right to change the Products and Services Guide based on prevailing market practices and the evolution of our products. Changes will not result in a degradation in the level of services provided during the period for which fees for such services have been paid.

.. |Acquia Commerce Manager logo| image:: https://cdn4.webdamdb.com/1280_UeZm7eSSjE91.png?1527867137
   :class: no-sb
   :width: 30px
