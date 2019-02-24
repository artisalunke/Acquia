.. include:: /common/global.rst

Acquia Ready Onboarding Services Product Guide
==============================================

**Last updated: March 2, 2018**

Acquia will provide the |acquia-product:onb| Onboarding Services described below only if purchased by Customer, as indicated in the Order.

#. **Acquia Ready Basic** |br| 

   As part of the |acquia-product:onb| onboarding process, Acquia will set up the Customer's |acquia-product:ac| subscription. Acquia will provide the Customer with links to the Support Users Guide and associated resources, and will also provide the Customer with an introduction to the |acquia-product:sub| with a self-paced video tutorial. Customers that purchased |acquia-product:ais|, |acquia-product:acs|, |acquia-product:ace|, or |acquia-product:edg| will also receive access to self-service videos.

#. **Acquia Ready Concierge**

   |acquia-product:onb| Concierge applies to the first, initial website launch of one website on |acquia-product:ac| — as either one codebase, or one codebase with up to three websites in a multisite configuration. Acquia may elect to automate portions of the onboarding process. This must be started within six months of the contract start date. Additional |acquia-product:onb| onboarding engagements can be purchased on-demand. |acquia-product:onb| Concierge is available only for Drupal 7 and Drupal 8 websites.

   - Assess Customer’s environment
   - Seek to understand Customer’s development lifecycle stage, timeline requirements, and testing and validation plans
   - Share best practices
   - Coordinate initial load testing and monitoring; and
   - Review the pre-launch checklist with Customer

   |acquia-product:onb| Onboarding Services are performed remotely. Acquia will require an administrative login to Customer’s website and access to Customer's personnel. Customer agrees to cooperate with Acquia to the extent necessary for Acquia to perform the services. Customer should anticipate a minimum of three weeks for the completion of the |acquia-product:onb| Onboarding process. Customers who request expedited service will be subject to an additional fee. Any delays resulting from Customer’s failure to perform or fulfill its responsibilities (for example, not having systems ready or failing to provide necessary data) will not affect the term of the applicable services or the payment schedule.

   .. list-table::
    :widths: 15 25 15 15 15 15
    :header-rows: 1

    * - 
      - 
      - |acquia-product:ais|
      - |acquia-product:acs|
      - |acquia-product:ace|
      - |acquia-product:edg|
    * - **Acquia Ready Basic**
      - *Welcome Package* |br| 
        An introduction to Customer’s |acquia-product:sub|
      - |Yes|
      - |Yes|
      - |Yes|
      - |Yes|
    * - **Acquia Ready Basic**
      - *Insight Tools* |br| 
        A guided tour of Acquia Content Services
      - |Yes|
      - |Yes|
      - |Yes|
      - |Yes|
    * - **Acquia Ready Concierge**
      - *Onboarding Manager* |br| 
        A single point of contact through Customer’s onboarding process
      - |No|
      - Optional
      - |Yes|
      - |Yes|
    * - **Acquia Ready Concierge**
      - *Onboarding Engineer* |br| 
        A technical engineer will be made available to advise and provide Customer with |acquia-product:ac| platform best practices
      - |No|
      - Optional
      - |Yes|
      - |Yes|
    * - **Acquia Ready Concierge**
      - *Technical Discovery* |br| 
        To ensure the highest level of compatibility between your website and the |acquia-product:ac| platform
      - |No|
      - Optional
      - |Yes|
      - |Yes|
    * - **Acquia Ready Concierge**
      - *Platform-Level Load Test Monitoring* \* |br| 
        An in-depth platform performance report on load testing results
      - |No|
      - Optional
      - |Yes|
      - |No|
    * - **Acquia Ready Concierge**
      - *Pre-Launch Best Practices Review* |br| 
        A pre-launch review of best practices and tasks
      - |No|
      - Optional
      - |Yes|
      - |No|
    * - **Acquia Ready Concierge**
      - *Launch Support* |br| 
        A smooth and successful website launch with support from Acquia
      - |No|
      - Optional
      - |Yes|
      - |No|

   \* Not available for |acquia-product:acs|
#. **Acquia Ready Add-On Services**

   #. **Extended Launch Support Services**

      The |acquia-product:onb| team will perform additional risk
      mitigation and limited critical path remediation activities as
      part of the Extended Launch Support Service. Acquia can provide
      this service in a *Small* or *Large* size. Level of effort for
      Extended Launch Support Small may not exceed five hours. Level of
      effort for Extended Launch Support Large may not exceed ten hours.

      Extended Launch Support scope is restricted to existing builds,
      along with any special configuration or custom code.
      |acquia-product:onb| cannot execute development of new feature
      requests as part of this offering. Activities that are covered
      include, but are not limited to, the following items:

      -  Deep dive into custom code or configuration troubleshooting
      -  Modify ``.htaccess`` for up to ten redirect or rewrite rules and/or modify ``settings.php`` for custom logic
      -  Deploy code from one customer environment to another, merge branches, and other related tasks
      -  Modify custom code as necessary to stand up newly migrated websites
      -  *Smoke test* code merges and deploys — customer must provide test criteria as user stories

      .. important::

         Extended Launch Support Large may not be sold with Expedited Onboarding.

      Use the following table as a guide for sizing Extended Launch Support, but note that the following is a guideline only. Multiple engagements (such as two *Large* engagements) may be purchased to cover additional effort, especially related to multisites.

      .. list-table::
       :widths: 20 40 40
       :header-rows: 1

       * - 
         - **Small (5-7 hours)**
         - **Large (7-10 hours)**
       * - **Code**
         - Deep dive into custom code or configuration troubleshooting
         - Modify custom code as necessary to stand up newly-migrated websites
       * - **Code**
         - Modify ``.htaccess`` for up to ten redirect or rewrite rules and/or modify ``settings.php`` for custom logic
         - Use tools such as XHProf and Memory Profiler to track down memory leaks
       * - **Code**
         - Deploy code from one customer environment to another, merge branches, and other related tasks
         - *Smoke test* code merges and deploys — customer must provide test criteria as user stories
       * - **Database**
         - Modify databases in preparation for migration, such as pruning data, adjusting collation, and removing prefixes
         - 
       * - **Files**
         - 
         - Restructure the ``files`` directory into a date- and time-based subdirectory structure
       * - **Testing**
         - Security document review
         - Review and troubleshoot customer-created load testing scripts
       * - **Testing**
         - 
         - Execute customer-designed load test using Blazemeter
#. **Acquia Ready Custom VCL Scope**

   The |acquia-product:onb| team has pre-written templates that address common custom VCL use cases. The current list of VCL templates currently available are set forth below:

   3.1 Hash on device string: This is an edge case mobile strategy. Customers do this when they do not want redirects to a mobile and/or tablet specific subdomain and Customer does not have a responsive theme. Acquia strongly discourages this strategy in favor of mobile redirects or responsive themes, for the following reasons:

   - Determining which content to serve (for example, mobile content vs desktop content) is a task that properly belongs to the application and not to a caching mechanism.
   - Increases complexity, complicating troubleshooting and increasing the burden on support.
   - Increased cost of ownership, due to the above.
  
   3.2 Hash on cookie value: This is an edge case strategy whereby Customer wants to serve different content on a single URL to anonymous traffic, based on a cookie value. Acquia strongly discourages cookie dependent architectures for reasons similar to those enumerated above.

   3.3 IP white listing: Customer may request IP white listing when they want to ensure that their website can be accessed only from certain IP addresses. Some customers insist on having it in the VCL due to perceived performance consequences related to doing the white listing in ``.htaccess``. Acquia's recommended strategy is to implement white listing within ``.htaccess`` or similar.

   3.4 Google FCF (First Click Free) support: If Customer participates in Google's First Click Free program then Customer will need custom VCL support.

.. container:: message-status

   Acquia Inc. reserves the right to change the Products and Services Guide based on prevailing market practices and the evolution of our products. Changes will not result in a degradation in the level of services provided during the period for which fees for such services have been paid.

.. |Yes| image:: https://cdn2.webdamdb.com/1280_EqxUKAqtA07.png?-62169955200
   :class: no-sb
.. |No| image:: https://cdn2.webdamdb.com/1280_MIQySTMO5Mh1.png?-62169955200
   :class: no-sb

