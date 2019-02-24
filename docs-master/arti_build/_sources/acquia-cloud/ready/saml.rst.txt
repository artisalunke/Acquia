.. include:: /common/global.rst

|acquia-product:onb| SimpleSAMLphp engagement
=============================================

The goal of the |acquia-product:onb| SimpleSAMLphp add-on engagement is
to assist customers in making the correct changes to the SimpleSAMLphp
configuration that allow the system to work correctly with Acquia
hosting — it is not meant as a replacement for customer involvement in
the configuration.

The SimpleSAMLphp engagement offering is limited to ensuring the
implementation of a standard configuration that allows Drupal to
authenticate against the customer's Identity Provider (IdP). This
process requires that the customer either already have an IdP, or have
someone available during the engagement with knowledge of how their IdP
is configured.

While the platform supports IdP first-flow or IdP initiated
authentication, |acquia-product:onb| has limited visibility into these
configurations. This offering assumes SP initiated authentication. With
SP initiated, Acquia can more thoroughly test the application from the
SP side and view the corresponding logs.

The SimpleSAMLphp offering is not a general single sign-on solution. It
does not cover customizing the interaction between Drupal and the IdP or
the ability to shape and use the data returned by the IdP other than to
the use the `simpleSAMLphp
Authentication <https://www.drupal.org/project/simplesamlphp_auth>`__
Drupal module to allow Drupal users to be created and authenticated by
the IdP.

.. _reqs:

Requirements
------------

-  The customer has one or more SAML 2.0 compliant IdPs identified and
   lined up.
-  The customer is able to identify a primary technical contact at each
   IdP.
-  The customer will use SimpleSAMLphp for the SP and the `simpleSAMLphp
   Authentication <https://www.drupal.org/project/simplesamlphp_auth>`__
   module to integrate with Drupal.

.. _acquia:

|acquia-product:onb| responsibilities
-------------------------------------

-  Install and configure SimpleSAMLphp and the `simpleSAMLphp
   Authentication <https://www.drupal.org/project/simplesamlphp_auth>`__
   module to communicate with the customer’s chosen IdP.
-  Assist and advise with troubleshooting SimpleSAMLphp to function
   against customer’s identified IdPs, including coordinating developer
   and IdP technical resources.
-  Perform the following services for up to three websites (service
   providers):

   -  Each of a customer's Dev, Stage, and Prod websites counts as a
      separate *site*. If the customer wants all three of these to
      authenticate against their IdP, that would account for the full
      scope of our work.
   -  In a Drupal multisite, individual website domains on Dev, Stage,
      and Prod environments count as a separate website; for example,
      ``www.example.com``, ``dev-site1.example.com``, and
      ``dev-site2.example.com`` are three distinct websites.
   -  Coordination will occur with the use of Acquia’s ticketing system.
   -  The customer is entitled to as many as three coordination calls
      per SimpleSAML subscription.

-  Collaborate with the Customer technical resources for the testing of
   the SimpleSAMLphp configuration.

.. _customer:

Customer responsibilities
-------------------------

-  Obtain and install SP metadata at the IdP.
-  Collaborate with Acquia technical resources for the testing of the
   SimpleSAMLphp configuration.
-  Ensure the availability of technical resources with access to and
   knowledge of the IdP.
-  Own all custom code and testing of custom workflows beyond what is
   provided by the `simpleSAMLphp
   Authentication <https://www.drupal.org/project/simplesamlphp_auth>`__
   Drupal module and the SimpleSAMLphp library.
-  Own testing and validation of all Drupal configurations and workflows
   that integrate with simpleSAMLphp Authentication module functionality
   (including custom role assignments and cookie based redirection).

Note

There is no critical support around the deployment of SimpleSAMLphp
configurations to the customer’s production environment. An
|acquia-product:onb| engineer will be available to the customer during
`stated business hours </support/guide#hours>`__ to provide standard
support around production deployments.
