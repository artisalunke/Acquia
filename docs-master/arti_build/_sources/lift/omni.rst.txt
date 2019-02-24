.. include:: /common/global.rst

|acquia-product:cdw|
====================

.. toctree::
  :hidden:
  :glob:

  /lift/omni/*

.. container:: internal-navigation

   **Acquia Lift data warehouse**

   * Intro
   * :doc:`Person </lift/omni/person>`
   * :doc:`Touch </lift/omni/touch>`
   * :doc:`Segments </lift/omni/segments>`

|acquia-product:cha| |acquia-product:ldb| provides access to a
cloud-based |acquia-product:ldw| that contains all of your
|acquia-product:cha|-hosted visitor data. You can directly connect to
this data warehouse to use your own business intelligence tools to
analyze your visitors and discover new insights.

You can also extend your use of the visitor data warehouse by using the |acquia-product:cha| `APIs </lift/omni/api>`__ or the manual |acquia-product:lpm| `file upload feature </lift/omni/api/file/import>`__ to import external visitor information (such as from your CRM system) into |acquia-product:lpm|, providing you with a single location for your aggregated visitor information.

The data warehouse updates either every 10,000 records or approximately
every 15 minutes, depending upon which threshold is first met. However,
it may take up to 24 hours for processed data to be available in all
tables.

After you purchase a license for |acquia-product:ldb|, you will be
provided with connection instructions to your visitor
|acquia-product:ldw|.

Field layouts
-------------

The |acquia-product:ldw| structure uses the following field layouts for
organizing and presenting its data:

-  `Person </lift/omni/person>`__ - This field layout describes
   visitors that have been uniquely identified with first-party cookies,
   their email addresses, or some other identifier.
-  `Touch </lift/omni/touch>`__ - This field layout describes a
   series of contiguous events (such as content views) with a duration
   between events of no more than 30 minutes. Each touch has a *Person*
   record as its parent.
-  `Event </lift/omni/event>`__ - This field layout describes
   discrete visitor actions, such as a content view of an article or a
   click-through on a subscription offer. An event has a *Touch* record
   as its parent. Events also contain information about the specific
   content that a visitor is consuming.
-  `Segments </lift/omni/segments>`__ - This field layout describes
   the segments that are associated with each event for a given person,
   and is made up of a ``segments`` table (for specific segment
   information) and the ``matching_segments`` table (links events with
   their associated segments).

Mapping taxonomy terms to |acquia-product:cha|
----------------------------------------------

With Drupal, you can map taxonomy terms to the user-defined fields for `Person </lift/omni/person>`__, `Touch </lift/omni/touch>`__, and `Event </lift/omni/event>`__ types. These mapped terms will appear as meta tags when applicable for a page. Mapping Drupal-tagged content to |acquia-product:cha| allows you to obtain a better understanding of the kinds of content that your visitors are consuming.

To map your existing taxonomies into |acquia-product:cha|, complete the
following steps:

#. Sign in to your website as a user with the permission to administer
   the personalization settings.
#. In the admin menu, click **Configuration**.
#. In the **Web Services** section, click the **Acquia Lift** link.
#. In the **Data collection settings** section, click the **Field
   Mappings** left tab.
#. For the **Content Section**, **Content Keywords**, and **Persona**
   lists, click your website's taxonomy that most closely correlates
   with the item affected by that list.

   |Mapping taxonomies|

#. *Optional* - If your website contains any additional taxonomy
   vocabularies that you want to map to |acquia-product:cha|, complete
   the following steps:

   #. In the left tab listing, click the tab with the vocabulary that
      you want to modify:

      -  **User Person Mappings**
      -  **User Touch Mappings**
      -  **User Event Mappings**

   #. Select the taxonomy that you want to map for each field.

#. Click **Save configuration**.

For examples of content mapping for several industries, see `Content
tagging use case examples </lift/profile-mgr/segment/tagging>`__.

.. |Mapping taxonomies| image:: https://cdn4.webdamdb.com/1280_2tk976zRBG60.png?-62169955200
   :width: 650px
   :height: 194px
