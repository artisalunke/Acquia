.. include:: /common/global.rst

Configuring the Marketo connector
=================================

.. container:: internal-navigation

   **Marketo connector**

   * :doc:`Intro </lift/connectors/marketo>`
   * :Config
   * :doc:`Segments </lift/connectors/marketo/segments>`

In the |acquia-product:lpm| **Admin** tab, you can configure connectors
to import visitor information from Marketo marketing software into
|acquia-product:lpm|.

Creating a Marketo connector
----------------------------

To configure a new Marketo connector, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, click the **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Connectors** link.
#. In the **Select a connector type** list, click **Marketo** as the connector type that you want to configure, and then click **Add connector**.

   In the panel on the left, |acquia-product:lpm| displays the Marketo
   connector configuration section.

#. To enter your |acquia-product:lpm| and Marketo account information,
   in the Marketo connector configuration section, enter values in the
   following fields for the new connector:

   -  **Host Name** - Name for your connector that reflects the type of
      information it will import from Marketo — for example,
      ``Test Company Marketo Email Information Connector``
   -  **REST Base Endpoint Domain** - Domain of the Marketo host REST
      API endpoint, provided by Marketo — for example,
      ``999-ZZZ-999.mktorest.com``

      .. note::  

         Enter the base domain of the endpoint. Do not include a
         ``https://`` prefix or ``/rest`` suffix.

      For more information on how to configure a REST API in Marketo,
      see `Quick Start Guide for Marketo REST
      API <http://developers.marketo.com/blog/quick-start-guide-for-marketo-rest-api/>`__.

   -  **Client ID** - Marketo Client ID, provided by Marketo
   -  **Client Secret** - Marketo Client Secret, provided by Marketo
   -  **Lift API User** - The API user email address included in your
      |acquia-product:lpm| account information (|acquia-product:cha|
      retrieves the Access Key and Secret Key that are associated with
      this account)
   -  **Pull Date** - The date and time on which |acquia-product:lpm|
      will begin to import data from Marketo
   -  **Notification Email (optional)** - The email address to which
      |acquia-product:lpm| will send alerts and error messages

#. Click **Save Configuration**.

|acquia-product:lpm| displays the **Activity Mapping** tab.

Adding mappings to your connector
---------------------------------

You can configure a Marketo connector to import data by adding mappings
to it. Activity leads are prefixed with ``marketo_{activityname}``,
where ``{activityname}`` is the name of an activity tracked in Marketo.

The fields associated with that activity can be mapped to fields in the
`Person </lift/omni/person>`__, `Touch </lift/omni/touch>`__, or
`Event </lift/omni/event>`__ tables. For example, you could map the
Marketo activity **Click Email** and it will be reflected in
|acquia-product:cha| as the event ``marketo_click_email``. You would
then map a field associated with this activity, such as ``Mailing ID``,
to ``custom_field_10`` in the Event table.

Adding activity mappings
~~~~~~~~~~~~~~~~~~~~~~~~

|lift-web-marketo-activity-mapping.png|

To add activity mappings to your Marketo connector (with example values
based on the previously described situation), complete the following
steps:

#. In the **Activity Mapping** tab, click **Add Activity**.

   |acquia-product:cha| displays the **Add Activity Mapping** dialog
   box.

#. In the **Select Activity** list, click the activity that you want to
   add to the connector. After you select an activity,
   |acquia-product:cha| displays several options for mapping the
   attributes of this activity. The available attributes vary by
   activity.
#. The **Primary Attribute** section allows you to map the *primary
   attribute* of your selected activity to the
   `Person </lift/omni/person>`__, `Touch </lift/omni/touch>`__, or
   `Event </lift/omni/event>`__ tables. The primary attribute of an
   activity is what Marketo has determined to be the most important
   piece of information that this activity contains. The primary
   attribute varies by activity. For example, if the activity is **Click
   Email**, the primary attribute is **Mailing ID**. To map the primary
   attribute, complete the following steps:

   a. In the **Select Table** list, click the |acquia-product:cha| table
      to which you want to map this attribute.

      For the example, map it to the **Events** table.

   b. In the **Select Field** list, click the field to which you want to
      map this attribute.

      For the example, map it to **custom_field_10**.

#. The **Other Attributes** section allows you to map other attributes
   of your selected activity to the Person, Touch, or Event tables. An
   activity's other attributes are additional pieces of information that
   may be useful for you to import. For example, for **Click Email**,
   other attributes include **Device** and **Is Mobile Device**. To map
   other attributes, complete the following steps:

   a. In the **Select Table** list, click the table to which you want to
      map this attribute.
   b. In the **Select Field** list, click the field to which you want to
      map this attribute.
   c. Depending on your needs, repeat the previous two steps until you
      have mapped all the attributes you want to import.

#. To update the Person table without creating an
   `event </lift/profile-mgr/event/category>`__ for this activity,
   select the **Update person only without creating events** check box.
   You can select this check box to prevent certain activities from
   generating a large number of events that you may not want to import.
   For example, the **Change Score** activity allows you to import the
   Marketo score value for an activity. Marketo tracks every change in
   score as a discrete activity, which means a new event is created for
   each change in score. Select the **Update person only without
   creating events** check box to prevent events from being created.
#. Click **OK**. |acquia-product:cha| displays a list of the saved
   activity mappings for this connector.

You have now added activity mappings to your Marketo connector. If
required, you can use the preceding procedure to add additional activity
mappings to this connector.

Depending on your needs, you can now add lead mappings or enable your
connector to begin importing data from Marketo into
|acquia-product:lpm|.

Adding lead mappings
~~~~~~~~~~~~~~~~~~~~

|marketo_connector_lead_mapping.png|

You can also add *lead mappings* to your Marketo connector, such as job
title or company ID. The Marketo connector allows you to map these leads
to fields in the `Person </lift/omni/person>`__ table.

For example, you could map the Marketo lead **Job Title** to
``custom_field_11`` in the Person table. To add a lead mapping that
would allow you to import visitors' job titles, use the following steps:

#. In the **Lead Mapping** tab, click **Add Lead**.

   |acquia-product:cha| displays the **Add Lead Mapping** dialog box.

#. In the **Marketo Lead Field** list, click the lead that you want to
   add to the connector.

   For this example, click **Job Title**.

#. In the **Lift Person Field** list, click the field to which you want
   to map this lead.

   For the example, click **custom_field_11**. Job title data will now
   be mapped to this custom field in the Person table.

#. Click **OK**.

|acquia-product:cha| displays a list of the saved lead mappings for this
connector.

You can use the preceding procedure to add additional lead mappings to
this connector.

After you have finished adding activity and lead mappings to your
connector, click the **Back to connector list** link to return to a list
of your connectors. Your activity and lead mapping information is saved.
The next step is to enable your connector.

Enabling your connectors
------------------------

For your connectors to start importing Marketo information into
[acquia-product:lpm, they must be enabled. To enable your connectors,
use one of the following methods:

-  In **Manage configuration data > Connectors**, find the connector
   that you want to enable, and then set the switch to **On**.
-  In the Marketo connector configuration section, set the switch to
   **On** in the panel on the left.

Creating segments with Marketo activity and lead information
------------------------------------------------------------

After you have created and enabled your connector, the next step is to
use the imported Marketo activity and lead data to `create
segments </lift/connectors/marketo/segments>`__.

Managing your connectors
------------------------

To view and manage your available connectors, complete the following
steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the
   **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Connectors** link.

|acquia-product:lpm| displays a list of the available connectors for
your environment. The Connectors page contains options for the following
available actions, including enabling/disabling, deleting, or editing
connectors:

Enabling or disabling a connector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable a connector, set the switch to **On**. To disable the
connector, set the switch to **Off**.

Deleting a connector
~~~~~~~~~~~~~~~~~~~~

To permanently remove a connector or its mapping information, complete
the appropriate steps depending on your needs:

-  *Connector* - Find the connector in the list of displayed connectors,
   and then click **Delete**.
-  *Activity mapping for a connector* - Complete the following steps:

   #. Find the connector in the list of displayed connectors, and then
      click **Configure**.
   #. In the **Activity Mapping** tab, find the activity mapping in the
      list of displayed activity mappings.
   #. Click **Delete**.

-  *Lead mapping for a connector* - Complete the following steps:

   #. Find the connector in the list of displayed connectors, and then
      click **Configure**.
   #. In the **Lead Mapping** tab, find the lead mapping in the list of
      displayed lead mappings.
   #. Click **Delete**.

Editing a connector
~~~~~~~~~~~~~~~~~~~

To modify or edit a connector, complete the following steps:

#. Find the connector in the list of displayed connectors, and then click **Configure**.
   
   The page reloads with the connector's configuration information.

#. To modify or edit the connector's configuration information, click **Edit configuration**.

   .. note::  

      Clicking **Edit configuration** will remove all mapping information from this connector.

#. To modify or edit the connector's activity mappings, in the list of mapped 
   activities, click the activity's name and then modify its settings as required.

#. To modify or edit the connector's lead mappings, in the list of mapped leads, 
   click the lead's name and then modify its settings as required.

#. Click **Save** to save your changes.

.. |lift-web-marketo-activity-mapping.png| image:: https://cdn4.webdamdb.com/1280_AGHn7vkVAym6.png?1526476034
   :width: 590px
   :height: 433px
.. |marketo_connector_lead_mapping.png| image:: https://cdn2.webdamdb.com/1280_YRWK18KxjhE5.png?1526476138
   :width: 590px
   :height: 407px
