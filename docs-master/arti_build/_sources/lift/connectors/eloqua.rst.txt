.. include:: /common/global.rst

Eloqua connector for |acquia-product:cha|
=========================================

.. toctree::
   :hidden:
   :glob:

   /lift/connectors/eloqua/*

.. container:: message-status

   Eloqua connector integration is currently in a private beta. Contact your account manager if you wish to participate*.

.. container:: internal-navigation

   **Eloqua connector for Acquia Lift**

   * Intro
   * :doc:`Config </lift/connectors/eloqua/configure>`
   * :doc:`Segments </lift/connectors/eloqua/segments>`

|acquia-product:cha| allows you to configure a connector to the
`Eloqua <https://www.oracle.com/marketingcloud/products/marketing-automation/index.html>`__
marketing software, letting you import visitors' *contact* and
*activity* data from Eloqua and then combine it with
|acquia-product:cha| visitor profiles. This additional data provides
deeper insights into visitors' identities, preferences, and behavior
both on your website and through other channels such as email.

You can use this data to create `segments </lift/profile-mgr/segment>`__
and target visitors with personalized content. For example, you can
create a segment that includes visitors who have clicked a link for a
particular email marketing campaign, and then target those visitors with
personalized web experiences.

When connected to Eloqua, |acquia-product:cha| does the following
things:

-  Imports contacts and activities from Eloqua into |acquia-product:cha|
-  Creates configurable field mappings and activity types
-  Obtains new Eloqua data every five minutes
-  Imports the contact and activity fields (based on the configured
   field mapping) each time there is an activity for a given contact
   that matches a configured activity, and the activity is created as an
   event in |acquia-product:cha|
-  Pull date is tracked for each mapped activity


Connecting visitor profiles
---------------------------

For data imported from Eloqua to be useful in |acquia-product:cha|, it
must be assigned to the correct |acquia-product:cha| visitor profile.
Eloqua information can be incorporated into an |acquia-product:cha|
profile by using an *email address* or an *Eloqua contact ID*.

-  *Email address* |br|
   Whenever an anonymous visitor accesses your website,
   |acquia-product:cha| assigns the visitor a tracking ID. The visitor
   then completes an Eloqua webform to indicate interest in further
   information — for example, the visitor subscribes to a mailing list.
   The visitor's email address is then captured in |acquia-product:cha|
   and is associated with the tracking ID, which allows the email
   address to be used as the basis for matching and importing
   information from Eloqua.
   For this process to occur, you need to add the following custom
   JavaScript to the webpages on your website that contain Eloqua forms.
   After a visitor submits an Eloqua form, the custom JavaScript to
   extracts the email address, and then pushes it to
   |acquia-product:cha| using the `JavaScript API </lift/javascript/identity>`__.

   .. code-block:: none

      <script>
         _tcaq.push(['captureIdentity', 'my.username@domain.com', 'email']);
      </script>

-  *Eloqua contact ID* |br|
   Eloqua can be configured to send_
   a marketing email with a unique Eloqua contact ID that is appended to
   each link in the email. When a visitor clicks one of these links and
   visits your website, |acquia-product:cha| assigns this visitor a
   tracking ID. In addition to the tracking ID, the `contact ID from the
   email
   link <https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/Help/FieldMerges/FieldMerges.htm>`__
   that the visitor clicked is imported into |acquia-product:cha| and
   mapped to the |acquia-product:cha| ``account`` identifier type.
   |acquia-product:cha| captures the Eloqua contact ID (rather than the
   visitor's email address) to prevent exposing personally identifying
   information in email links. After capturing the Eloqua contact ID,
   |acquia-product:cha| links these two IDs and creates a unified
   visitor profile.

.. _send: https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/Help/ContactFields/ContactFieldsDefinitions.htm

Configuring |acquia-product:cha| Identity settings
--------------------------------------------------

For the Eloqua contact ID to be imported into |acquia-product:lpm|, it
must be mapped to the correct identifier type. The settings on the
**Identity** tab in **|acquia-product:cha|** settings need to be
configured to accept this mapping. To configure these settings, complete
the following steps:

#. Sign in to your website as a user with the permission to administer
   the personalization settings, and then go to **Configuration >
   Personalization settings > Acquia Lift Profiles**.
#. In the **Identity parameter** field, enter the value ``Id``. This is
   the Eloqua contact ID.
#. Ensure that the value in the **Identity type parameter** field is
   ``identityType`` and the value in the **Default identity type** field
   is ``account``. This maps the Eloqua contact ID to the
   |acquia-product:cha| identifier type ``account``.
#. Click **Save** to save your changes.

.. _mapping:

Mappings
--------

Depending on the information that you want to import from Eloqua into
|acquia-product:lpm|,
`*mappings* </lift/connectors/eloqua/configure#mapping>`__ will help you
identify users and patterns. You can add activity mappings, lead
mappings, or both to your Eloqua connector.


Activity mappings
~~~~~~~~~~~~~~~~~

In Eloqua, a *lead* (a visitor that Eloqua is tracking) performs
activities or actions that are captured by Eloqua, such as opening an
email or signing up for a mailing list. The Eloqua connector allows you
to create `*activity
mappings* </lift/connectors/eloqua/configure#activity>`__ that link
these activities to events in |acquia-product:cha|.

After you have mapped this activity to an |acquia-product:cha| event, it
can be imported into |acquia-product:lpm| and used to create a
`segment </lift/profile-mgr/segment>`__.

Contact mappings
----------------

Adding `contact mappings </lift/connectors/eloqua/configure#contact>`__ to your Eloqua
connector allows you to import data related to visitors' identities and
create segments from that information.

When you have mapped this lead to a field, it can be imported into
|acquia-product:lpm| and used to create a
`segment </lift/profile-mgr/segment>`__.


Salesforce integration
----------------------

Eloqua is also integrated with
`Salesforce <https://www.salesforce.com/>`__ `customer relationship
management <https://en.wikipedia.org/wiki/Customer_relationship_management>`__
software. Organizations often use Salesforce to track prospective
customer interactions when they become *sales-qualified leads* — after
the organization's sales team decides that a customer is a good fit for
their product. The Eloqua connector can import any lead or activity data
that Salesforce has provided to Eloqua, such as opportunity size or
projected close date. This data can then be imported into
|acquia-product:cha| through the connector.

Data from Salesforce can provide you with more detailed information
about visitors' demographics, their interest in your website, and the
likelihood that they will complete transactions such as purchasing your
products. For more information about Eloqua and Salesforce integration,
see `Oracle's
whitepaper <https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/pdf/OracleEloqua_Salesforce_IntegrationGuide.pdf>`__.

.. note::  

   Salesforce data is not distinguished from Eloqua data after its import
   into the |acquia-product:cha| service. Both Salesforce and Eloqua data
   are labeled as originating from Eloqua when you `view a visitor
   profile </lift/connectors/marketo/segments#viewing>`__.
