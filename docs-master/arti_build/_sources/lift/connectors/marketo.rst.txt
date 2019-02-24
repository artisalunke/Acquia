.. include:: /common/global.rst

Marketo connector for |acquia-product:cha|
==========================================

.. toctree::
   :hidden:
   :glob:

   /lift/connectors/marketo/*

.. container:: internal-navigation

   **Marketo connector**

   * Intro
   * :doc:`Config </lift/connectors/marketo/config>`
   * :doc:`Segments </lift/connectors/marketo/segments>`

|acquia-product:cha| allows you to configure a connector to the
`Marketo <https://www.marketo.com/>`__ marketing automation software,
letting you import visitors' *lead* and *activity* data from Marketo and
combine it with |acquia-product:cha| visitor profiles:

-  *Leads* are visitors and their attributes, such as job title or date
   of birth.
-  *Activities* are visitors' actions on and off your website, such as
   receiving an email or downloading a whitepaper.

This additional data provides deeper insights into visitors' identities,
preferences, and behavior both on your website and through other
channels such as email. You can use this data to create
`segments </lift/profile-mgr/segment>`__ and target visitors with
personalized content. For example, you can create a segment that
includes visitors who have clicked a link for a particular email
marketing campaign, and then target those visitors with personalized web
experiences.


Connecting visitor profiles
---------------------------

For data imported from Marketo to be useful in |acquia-product:cha|, it
must be assigned to the correct |acquia-product:cha| visitor profile.
Marketo information can be incorporated into an |acquia-product:cha|
profile in the following two ways:

-  *Email address*

   An anonymous visitor accesses your website. |acquia-product:cha|
   assigns this visitor a tracking ID. The visitor then fills out a
   Marketo webform to indicate interest in further information — for
   example, the visitor subscribes to a mailing list. The visitor's
   email address is then captured in |acquia-product:cha| and associated
   with the tracking ID. It can now be used as the basis for matching
   and importing information from Marketo. For this process to happen,
   you need to add custom JavaScript to the webpages on your website
   that contain Marketo forms. Once the visitor submits a Marketo form,
   the custom JavaScript uses the `Marketo forms
   API <http://developers.marketo.com/javascript-api/forms/>`__ to
   extract the email address, and then pushes it to |acquia-product:cha|
   using the `JavaScript API </lift/javascript/identity>`__.

   The following PHP example collects an email address from a Marketo
   form and sends it to |acquia-product:cha|:

   .. code-block:: PHP

      $redirect = ', function(form){';
      $redirect .= '   form.onSuccess(function(values, followUpUrl){';
      // These next 3 lines are to send the user email to Lift.
      if (module_exists('acquia_lift_profiles')) {
      $redirect .= '     var vals = form.vals();';
      $redirect .= '     var formEmail = vals.Email;';
      $redirect .= '     _tcaq.push(["captureIdentity", formEmail, "email"]);';
      }
      $redirect .= '     location.href = "' . $href . '";';
      $redirect .= '     return false;';
      $redirect .= '   });';
      $redirect .= '});';

-  *Marketo lead ID*

   Marketo `can be configured to
   send <https://docs.marketo.com/display/public/DOCS/Add+Tokens+to+an+Email+Link>`__
   a marketing email with a unique Marketo lead ID appended to each link
   in the email. A visitor clicks one of these links, visits your
   website, and |acquia-product:cha| assigns this visitor a tracking ID.
   In addition to this ID, the lead ID from the email link that the
   visitor clicked is imported into |acquia-product:cha| and mapped to
   the |acquia-product:cha| ``account`` identifier type.
   |acquia-product:cha| captures the Marketo lead ID rather than the
   visitor's email address to prevent exposing personally identifying
   information in email links. After the Marketo lead ID has been
   captured, |acquia-product:cha| links these two IDs and creates a
   unified visitor profile.


Configuring Acquia Lift Profiles settings
-----------------------------------------

For the Marketo lead ID to be imported into |acquia-product:lpm|, it
must be mapped to the correct identifier type. The |acquia-product:cha|
personalization settings need to be configured to accept this mapping.
To learn more about data mapping, see `Configuring personalization
settings </exp-builder/data-mapping>`__.

To configure these settings for Marketo, complete the following steps:

#. Sign in to your website as a user with the permission to administer
   the personalization settings, and then go to **Configuration > Acquia
   Lift**.
#. In the **Identity parameter** field, enter the value ``Id``. This is
   the Marketo lead ID.
#. Ensure that the value in the **Identity type parameter** field is
   ``identityType`` and the value in the **Default identity type** field
   is ``account``. This maps the Marketo lead ID to the
   |acquia-product:cha| identifier type ``account``.
#. Click **Save** to save your changes.

|acquia-product:cha| is now configured to assign data from Marketo to
the correct visitor profile in |acquia-product:lpm|.


Mappings
--------

Depending on the information that you want to import from Marketo into
|acquia-product:lpm|,
`mappings </lift/connectors/marketo/config>`__ will help you
identify users and patterns. You can add activity mappings, lead
mappings, or both to your Marketo connector.


Activity mappings
~~~~~~~~~~~~~~~~~

In Marketo, a lead, or a visitor that Marketo is tracking, performs
activities or actions that are captured by Marketo, such as opening an
email or signing up for a mailing list. The Marketo connector allows you
to map these activities to events in |acquia-product:cha|.

Once you have mapped this activity to an |acquia-product:cha| event, it
can be imported into |acquia-product:lpm| and used to create a
`segment </lift/profile-mgr/segment>`__.

Lead mappings
~~~~~~~~~~~~~~~~~

Adding `lead mappings </lift/connectors/marketo/config>`__ to
your Marketo connector allows you to import data related to visitors'
identities and create segments from that information.

When you have mapped this lead to a field, it can be imported into
|acquia-product:lpm| and used to create a
`segment </lift/profile-mgr/segment>`__.


Salesforce integration
----------------------

Marketo is also integrated with
`Salesforce <https://www.salesforce.com/>`__ `customer relationship
management <https://en.wikipedia.org/wiki/Customer_relationship_management>`__
software. Organizations often use Salesforce to track prospective
customer interactions when they become *sales-qualified leads* — after
the organization's sales team decides that a customer is a good fit for
their product. The Marketo connector can import any lead or activity
data that Salesforce has provided to Marketo, such as opportunity size
or projected close date. This data can then be imported into
|acquia-product:cha| through the connector. Data from Salesforce can
provide you with more detailed information about visitors' demographics,
their interest in your website, and the likelihood that they will
complete transactions such as purchasing your products.

.. note::  

   Salesforce data is not distinguished from Marketo data after its import
   into |acquia-product:lpm|. Both Salesforce and Marketo data are labeled
   as originating from Marketo when you `view a visitor
   profile </lift/connectors/marketo/segments#viewing>`__.

Configuring Marketo connectors
------------------------------

To configure Marketo connectors in |acquia-product:lpm|, see
`Configuring the Marketo connector </lift/connectors/marketo/config>`__ in
|acquia-product:lpm|.


Exporting data back to Marketo
------------------------------

Although the Marketo connector can import data from Marketo, the
connector cannot export data back into Marketo. To export your
|acquia-product:cha| data to Marketo, create a custom import script
using Marketo's `Bulk Import
API <http://developers.marketo.com/rest-api/bulk-import/>`__, and then
use the script to import your data back into Marketo.
