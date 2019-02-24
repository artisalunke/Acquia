.. include:: /common/global.rst

|acquia-product:ace| Product Guide
==================================

.. container:: message-status

   |Acquia Cloud logo| For additional information about |acquia-product:ac|, see its `product documentation </acquia-cloud>`__.

**Last updated: December 4, 2017**

Acquia will provide the PaaS services described below only if purchased by Customer, as indicated in the Order.

|acquia-product:ace| is a managed Platform as a Service for Customer’s Drupal website(s). |acquia-product:ace| includes all the features of |acquia-product:ac|, is subject to the `Service Level Policy </guide/service-level>`__, and includes the additional features set forth below.

#. **Platform Services**

   - 1.1 **Drupal Services** |br| 
      Acquia will maintain Customer’s Drupal applications on the Platform during the Subscription Term in the Region as indicated in the Order. Customer may submit an unlimited number of support requests related to the Platform. Such tickets will not be counted towards the Support Services ticket allotment (if applicable) unless such issue was caused by an error in Customer’s website(s). Acquia will conduct daily backups of the Drupal application and related databases for disaster recovery purposes. Customer may also perform on-demand backups and restores.

      - 1.1.1 **Drupal Migration Services** |br| 
         Acquia will work with the Customer to migrate the website(s) onto the Platform. Once migrated, Acquia will conduct a light infrastructure audit of the website to determine whether any issues with the website may cause the launch to be unsuccessful. Following such audit, Acquia will disclose any launch blockers to Customer. Customer may elect to fix the launch blockers or engage Acquia at its standard consulting services rates to fix the blockers. If Customer elects not to correct the launch blockers identified by Acquia, any unavailability due to such launch blockers will not be counted when determining unavailability of the website pursuant to the Service Level Policy. Customer may purchase a full infrastructure site audit for an additional fee and subject to a separate Order.

   - 1.2 **Node.js Services** |br| 
      |acquia-product:ac| provides application platform services for Node.js applications. Deploying Node.js applications on |acquia-product:ac| requires that the Customer purchase a Node.js platform package along with their |acquia-product:ace| subscription.

      #. The Node.js Service has four main components:

         -  *Source code repository service* - Enables developers to track and manage multiple versions of the application
         -  *Automated build and deployment service* - Deploys build artifacts to the development and production environments
         -  *Node.js development environment* - For development activities by Customer’s |acquia-product:ac| users
         -  *Node.js production environment* - For production deployment

      #. The Node.js Service includes support for the services listed above and the underlying platform infrastructure. Support for Customer’s Node.js application code and any third-party dependencies deployed by the Customer is not included.

#. **Drupal Web Server Administration Tasks** |br| 
   |acquia-product:ace| includes the following web server administration tasks:

   -  Review system logs to diagnosis issues or upon request
   -  Adjustments to Apache, MySQL, and PHP configuration including:

      -  Changes for service diagnostics, deployment of new websites/Code Bases
      -  ``apache.conf`` changes (such as modify conf change Code Base locations and add new sites)
      -  ``php.ini`` changes (such as adjust memory limit or enable error logging)
      -  ``my.cnf`` changes (such as enable slow query logs or modify slow query time)
      -  Updates or upgrades to Apache, PHP, databases, or the operating system

   -  LAMP stack changes pertaining to performance tuning
   -  Installing or upgrading server applications

#. **Backup and Disaster Recovery for Acquia Cloud Enterprise** |br| 

   - 3.1 **Data Centers** |br| 
      The |acquia-product:ace| Platform is physically remote from Acquia’s office facilities. A disaster affecting one or more of Acquia's offices would not impact the availability of Customer website(s) or Customer Data. The |acquia-product:ace| environment consists of major Regions and Availability Zones. Availability Zones are separate yet interconnected data centers within major Regions in Acquia’s global infrastructure. |acquia-product:ace| utilizes a highly available redundant architecture that distributes replicated redundant server types (load balancing, caching, web and database servers) across multiple Availability Zones within the same Region. Acquia will use commercially reasonable efforts to restore the services in an alternate Availability Zone within the same Region (or alternate Region if Multi-Region Failover service has been purchased) in the event service in Customer's assigned Availability Zone (or Region) is severely impacted.
   - 3.2 **Backups** |br| 
      Acquia will maintain a comprehensive backup solution which includes website code, static assets/files, and databases. Acquia will automatically export MYSQL database one time per day and retain these backups for three days. Customer may also make on-demand backups of any database at any time on the workflow tab of the |acquia-product:ac| UI, or using SSH/SCP. During the Subscription Term, Acquia will retain these on-demand backups for Customer until Customer chooses to delete them. Backups will count against the storage space purchased in Customer’s Order. Customer may download these database backups as well as restore a previous backup on the backups tab of the |acquia-product:ac| UI. At the Drupal code layer, Customer-developed code may be managed and deployed by Customer using Acquia’s Git code repository service. This service allows Customer to roll-back and re-deploy the Drupal code, effectively backing up the Drupal layer so that the website code may be re-deployed to a new web server instance as needed. In addition, Acquia conducts daily backups of each website’s files and maintains a complete and current copy of each website, which will be used in the event Acquia must restore the website due to a failure of the Service. Backups are performed daily over the previous week, weekly over the previous month, and monthly thereafter.
   - 3.3 **Disaster Recovery** |br| 
      The |acquia-product:ace| Platform will make hourly internal disaster recovery snapshots of Customer Data. Acquia will retain these snapshots on a diminishing schedule for three months. These backups will be used to restore Customer website(s) at another location within the same Region in the event of a total data center loss or a loss of multiple disk systems. Acquia will not provide Customer access to these snapshots and will not use these snapshots to restore websites due to data-loss or deletion by Customer.

#. **Server Capacity**

   - 4.1 **Emergency Capacity** |br| 
      In the event Acquia becomes aware that Customer’s instances become, or may become overloaded due to greater than normal usage, Acquia will notify Customer and will take reasonable actions to increase the server capacity in an effort to maintain website performance. Customer agrees that Acquia, in its reasonable discretion, can unilaterally add capacity up to three-times the procured capacity, at Acquia’s then current daily rates. Such additional capacity will remain provisioned for a minimum of five calendar days. In the event Acquia determines that such additional capacity is necessary to maintain website performance for the remainder of the Term, Acquia will contact Customer to obtain approval to increase their server capacity. If, despite reasonable notification from Acquia that failure to upgrade the server is adversely impacting availability and Customer fails to upgrade, Acquia may downsize the server capacity to the original contracted amount. Acquia reserves the right to not provision additional server capacity if Customer has any outstanding amounts due or if it determines that additional capacity is unlikely to significantly improve performance, including, without limitation, when the overload is caused by an error in Customer's software (for example, PHP code), Customer Drupal Instance or during a denial-of-service attack. Acquia reserves the right to bill Customer for traffic associated with a denial-of-service attack.
   - 4.2 **Emergency Storage Capacity Increase** |br| 
      In the event Acquia becomes aware that Customer's instances have reached, or may reach, their allocated storage capacity, Acquia will notify Customer and will take reasonable actions to increase the storage capacity in an effort to maintain website availability. Customer agrees that Acquia, in its reasonable discretion, can unilaterally increase storage to the next standard storage size available at Acquia's then current daily rates. Such additional storage capacity will remain provisioned for the remainder of the Term. Customer agrees to pay for such additional storage capacity for the remainder of the Term. Acquia reserves the right to not provision additional storage capacity if Customer has any outstanding amounts due. Acquia reserves the right to remove Customer from monitoring in the event that a recommended or completed storage capacity increase is refused or otherwise disputed by Customer. Downtime incurred while Customer instances are out of monitoring will be excluded from service level policy calculations.
   - 4.3 **Additional Capacity** |br| 
      Customer may request Acquia to increase their server capacity upon prior written request. Acquia will also make reasonable efforts to contact Customer when it is determined a server upgrade is needed. Any additional servers provisioned will be billed at the then current daily rates for a minimum of five calendar days. If Customer requests additional capacity to the Platform for two (2) consecutive months, such capacity will remain at such level for the remainder of the Subscription Term.
   - 4.4 **Shared Environments** |br| 
      If Customer is on shared development or staging environments, Customer acknowledges that such environments are only for low impact testing and development activities. Should Customer’s use of the shared development or staging environment adversely impact server performance, Customer will be required to move to a dedicated environment and will need to pay the associated server fees. Furthermore, Customer will not perform any load tests or vulnerability tests on live website(s) unless it has purchased dedicated servers and will provide Acquia at least five (5) business days advance notice of any such testing.
   - 4.5 **Server Capacity** |br| 
      If Customer regularly consumes (for example, more than two times in any week) more than 20% of the shared server capacity (CPU, memory, disk, PHP processes) assigned to Customer based on the information provided to Acquia on the Platform Questionnaire, Customer understands that Acquia may provision additional capacity for Customer and/or move Customer to a dedicated server instance at Customer’s expense.
   - 4.6 **Acquia Cloud CD environments** |br| 
      |acquia-product:ccd| environments (CDEs) are on-demand development environments available as part of |acquia-product:ccd| subscriptions and can be added to |acquia-product:ace| subscriptions. CDEs enable a Customer to dynamically create new environments and deploy code, data and files to those environments in a self-service model. A Customer will be provided the ability to create CDEs up to the number specified within the Customer’s Order. |acquia-product:ccd| has two components:

      -  *CD environments (CDEs)* - For rapid creation of development environments
      -  *CD pipelines* - For continuous delivery activities

   - 4.7 **Cloud Service Management Capacity** |br| 
      | For |acquia-product:ac| products with Cloud Service Management, Customer may use the Cloud Service Management features of |acquia-product:ac| to add or remove web server capacity. Customer may not decrease web server capacity below the minimum capacity as set forth in the applicable Order. Customers who add web server capacity using Cloud Service Management will be billed at the daily upsize rate with a minimum of one day. All such fees will be calculated and invoiced quarterly in arrears, and Customer shall pay all applicable fees in accordance with the terms of the applicable Order.

      Customer understands that the content request capacity of Cloud Service Management environments is specified as a benchmark and does not constitute a performance guarantee. Content request capacity is benchmarked with an application built on the Demo Framework distribution of Drupal 8 (https://www.drupal.org/project/df). The following assumptions were used, applications with different characteristics may see variation in performance:

      -  Drupal 8 application running PHP 7.1 (earlier versions of Drupal and/or PHP may perform differently)
      -  Varnish caching disabled for testing purposes (not recommended in production)
      -  256 MB of RAM per PHP process (configurable)
      -  96 MB of APC memory (configurable)
      -  64 MB OF memcache memory (configurable)
      -  Median PHP latency of 300ms, peak PHP latency of 1.6s (applications with a tolerance for higher latency may be able to service more requests)

      Acquia reserves the right to change the underlying infrastructure at any time as long as benchmark performance is not degraded. Acquia also reserves the right to perform future benchmark tests with updated versions of the Demo Framework.

.. container:: message-status

   Acquia Inc. reserves the right to change the Products and Services Guide based on prevailing market practices and the evolution of our products. Changes will not result in a degradation in the level of services provided during the period for which fees for such services have been paid.

.. |Acquia Cloud logo| image:: https://cdn4.webdamdb.com/1280_s0InPk2T0pQ2.png?-62169955200
   :class: no-sb
   :width: 30px
