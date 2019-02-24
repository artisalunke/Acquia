.. include:: /common/global.rst

Configuring the Eloqua connector
================================

.. container:: message-status

   Eloqua connector integration is currently in a private beta. Contact your account manager if you wish to participate*.

.. container:: internal-navigation

   **Eloqua connector for Acquia Lift**

   * :doc:`Intro </lift/connectors/eloqua/>`
   * Config
   * :doc:`Segments </lift/connectors/eloqua/segments>`


In the |acquia-product:lpm| **Admin** tab, you can configure connectors to import visitor information from Oracle Eloqua marketing software into |acquia-product:lpm|.

Creating an Eloqua connector
----------------------------

To configure a new Eloqua connector, complete the following steps:

#. `Sign in to the Profile Manager interface </lift/profile-mgr#signing>`__, and then click the **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Connectors** link.
#. In the **Select a connector type** list, click **Eloqua** as the connector type that you want to configure.
#. Click **Add connector**. |br| 
   |acquia-product:lpm| displays the Eloqua connector configuration settings in JSON format.
#. In the Eloqua connector configuration section, enter values in the following fields for the new connector:

   -  *Initial section*

      -  ``name`` - Provide a descriptive name for your connector based on the type of information it will import (for example, ``Eloqua email information connector``)
      -  ``host`` - IP address of the Eloqua endpoint
      -  ``accessKey`` - The Eloqua access key
      -  ``secretKey`` - The Eloqua secret key
      -  ``accountID`` - The |acquia-product:lpm| account ID
      -  ``customerId`` - *Supplied by Acquia*

   -  *``awsConfig`` section*

      -  ``region`` - *Supplied by Acquia*
      -  ``dynamoDBTablePrefix`` - *Supplied by Acquia*
      -  ``dynamoDBEndpoint`` - *Supplied by Acquia*

   -  *``eloquaConfig`` section:*

      -  ``siteName`` - The company name that the Eloqua user belongs to
      -  ``username`` - The user's Eloqua username
      -  ``password`` - The user's Eloqua password
      -  ``startPullDate`` - The first date that data can be imported from Eloqua |br| 
         If |acquia-product:cha| does not have a date set already, the connector uses this date as a starting point. If a new activity is added to the mappings, it will use the ``startPullDate`` for the initial import.
      -  ``bucketRegion`` - *Supplied by Acquia*
      -  ``bucketName`` - *Supplied by Acquia*
      -  ``personFieldMapping`` - Sends specific customer data to Eloqua — `Learn more <#contact>`__
      -  ``eventFieldMapping`` - Sends specific activity data to Eloqua — `Learn more <#activity>`__

#. Click **Save configuration**.

Adding mappings to your connector
---------------------------------

You can configure a Eloqua connector to import data by adding mappings to it. Mapping configurations are determined by the type of mapping, and you can configure the Eloqua connector to import data by adding mappings to it. All mappings are defined in a text file that is displayed on the connector's configuration page.

Fields associated with an activity can be mapped to fields in the `Person </lift/omni/person>`__, `Touch </lift/omni/touch>`__, or `Event </lift/omni/event>`__ tables. For example, you could map the Eloqua activity **EmailClickthrough**, and it will be reflected in |acquia-product:cha| as the event ``Eloqua_EmailClickthrough``. You would then map a field associated with this activity, such as ``CampaignID`` to ``event_udf5`` in the Event table.

In the following examples, ``eloquaFieldStatement`` matches an Eloqua-supplied field, and the ``mapTo`` applies to a field in |acquia-product:cha|.

Activity mappings
~~~~~~~~~~~~~~~~~

In Eloqua, a *lead* (a visitor that Eloqua is tracking) performs activities that are captured by Eloqua, such as opening an email or signing up for a mailing list. The Eloqua connector allows you to map these activities to events in |acquia-product:cha|, along with corresponding attributes (such as the associated ``CampaignID``).

In |acquia-product:cha|, activities are prefixed with ``Eloqua_{activityname}``, where ``{activityname}`` is the name of an activity tracked in Eloqua. You must manually create these activities in |acquia-product:cha| as events. For more information, see `Creating and managing events </lift/profile-mgr/event/category>`__.

As an example, activity mapping in the connector configuration file to map the ``Subscribe`` activity and several associated fields into Lift event fields can appear similar to the following:

.. code-block:: none

         "eventFieldMapping":{
            "Subscribe": {
                "eventName": "Subscribe",
                "attributesMappings": {
                    "CampaignId" : "event_udf5",
                    "ExternalId" : "event_udf6",
                    "AssetId" : "event_udf7"
                }
            }
           }

For a full list of mappable activities, see `Oracle's documentation regarding activity fields <https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAB/index.html#Developers/BulkAPI/Reference/activity-fields.htm>`__.

Contact mappings
~~~~~~~~~~~~~~~~

Adding contact mappings to your Eloqua connector allows you to import data related to visitors' contact information and create segments from that information. When you have mapped this lead to a field, it can be imported into |acquia-product:lpm| and this additional data can be used in segments.

As an example, adding contact mapping in the connector configuration file to map the ``C_Industry1`` field from Eloqua can appear similar to the following:

.. code-block:: none

        "personFieldMapping":{
        "C_Industry1": {
        "isIdentity": false,
        "eloquaFieldStatement": "{{Contact.Field(C_Industry1)}}",
        "mapTo": "person_udf5"
        },
                }

For a full list of mappable contact fields, see `Oracle's documentation regarding contact] fields <https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#Help/ContactFields/ContactFieldsDefinitions.htm>`__.

Enabling your connectors
------------------------

For your connectors to start importing Eloqua information into [acquia-product:lpm, they must be enabled.

To do this, in **Manage configuration data > Connectors**, find the connector that you want to enable, and then set the switch to **On**.

Creating segments with Eloqua activity and lead information
-----------------------------------------------------------

After you have created and enabled your connector, the next step is to use the imported Eloqua activity and lead data to `create segments </lift/connectors/eloqua/segments>`__.

Managing your connectors
------------------------

To view and manage your available connectors, complete the following steps:

#. `Sign in to the Profile Manager interface </lift/profile-mgr#signing>`__, and then click the **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Connectors** link.

|acquia-product:lpm| displays a list of the available connectors for your environment. The Connectors page contains options for the following available actions, including enabling/disabling, deleting, or editing connectors:

Enabling or disabling a connector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable a connector, set the switch to **On**. To disable the connector, set the switch to **Off**.

Deleting a connector
~~~~~~~~~~~~~~~~~~~~

To permanently remove a connector or its mapping information, complete the appropriate steps depending on your needs:

-  *Connector* - Find the connector in the list of displayed connectors, and then click **Delete**.
-  *Activity mapping for a connector* - Complete the following steps:

   #. Find the connector in the list of displayed connectors, and then click **Configure**.
   #. In the **Configuration settings (JSON)** field, remove the entire ``eventFieldMapping`` section.
   #. Click **Save Configuration**.

-  *Contact mapping for a connector* - Complete the following steps:

   #. Find the connector in the list of displayed connectors, and then click **Configure**.
   #. In the **Configuration settings (JSON)** field, remove the entire ``personFieldMapping`` section.
   #. Click **Save Configuration**.
