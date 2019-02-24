.. include:: /common/global.rst

Using Google Tag manager with |acquia-product:cha|
==================================================

When using |acquia-product:cha|, you can use `Google Tag
Manager <https://www.google.com/analytics/tag-manager/>`__ to instrument
`events </lift/profile-mgr/event/category>`__, which can both provide
more understanding and a better customized experience for your users.

Video: Tracking custom events
-----------------------------

The following video provides information regarding implementing custom
events.

.. raw:: html

   <iframe allowfullscreen="" class="shadow bord" frameborder="0" height="296" src="https://www.youtube.com/embed/TLAzomDT0is?rel=0" width="560"></iframe>

Creating custom events
----------------------

Using the following framework (with its own example values), you can
build an |acquia-product:cha|
`event </lift/profile-mgr/event/category>`__ with Google Tag Manager.
Modify any of the provided example names as appropriate for your
application.

#. Build an event that can be used for tracking purposes. In this
   example, we are using an event labeled as ``Add to Cart``.

   #. `Create an event </lift/profile-mgr/event/category>`__.
   #. Enter values in the following fields:

      -  **Event name** - Example value: ``Add to Cart``
      -  **Event ID** - This should auto-fill with the **Event name**,
         but can be modified
      -  **Customer Site** - Either click the appropriate website, or
         click ``Global``
      -  **Event type** - Example value: Click ``Click``

   #. Click **Save** to save the event.

   |Creating an event|

#. To map retrieved information to users, you must next `Add column
   metadata </lift/profile-mgr/admin/column-meta-data>`__ for the event
   to |acquia-product:lpm|. The following image is an example of the
   event details:

   |Profile manager column metadata|

   For the column metadata in this example, use the following values:

   -  **Display Name** - ``Product Name``
   -  **Display Order** - ``1``
   -  **Table** - ``Event``, for the `Event </lift/omni/event>`__ table
   -  **Accessor** - ``custom_field_1(getCustomField1)`` *(be sure to
      note the number for this field)*
   -  **Type** - ``String``
   -  **Description** - ``Product name from Add to Cart``

#. Configure the Google Tag Manager to expose the product name in the
   data layer of your website. Configure a *variable* in Google Tag
   Manager to store the product name: ``product-name``.
   For an explanation of Google Tag Manager configuration, see `Tags,
   triggers, variables, and the data
   layer <https://support.google.com/tagmanager/answer/6103657?hl=en#variablesAndTheDataLayer>`__.

   |Product name in GTM|

   | After configuring the variable, create a *trigger* that fires when
     a user clicks the **Add to Cart** button.

   |Trigger configuration in GTM|

#. Create a custom HTML tag that captures the *Add to Cart* trigger,
   using the |acquia-product:cha| JavaScript API method of `capturing a
   page view </lift/javascript/view#pageview>`__. To do this, use code
   similar to the following:

   .. code-block:: html

      <script>
      _tcaq.push(['capture', 'Add to Cart', { 'event_udf1':{{product-name}} }]);
      </script>

   The ``event_udf`` number (``event_udf1`` in this example) must match
   the number chosen in the **Accessor** field mentioned previously.
   After embedding this code, whenever a user clicks the **Add to Cart**
   button on a product page, an event will be returned in
   |acquia-product:lpm| as follows:

   |Lift event example|

   Other possible uses are to create triggers and events using the
   `captureIdentity </lift/javascript/identity>`__ or
   `updatePerson </lift/javascript/updateperson>`__ API functions.

.. |Creating an event| image:: https://cdn2.webdamdb.com/1280_Ef34wSw7rR52.png?1526475536
   :width: 977px
   :height: 623px
.. |Profile manager column metadata| image:: https://cdn4.webdamdb.com/1280_YA7nRTnjkte4.png?1526475767
   :width: 920px
   :height: 608px
.. |Product name in GTM| image:: https://cdn2.webdamdb.com/1280_gF4dGYLK91B8.png?1526475789
   :width: 446px
   :height: 365px
.. |Trigger configuration in GTM| image:: https://cdn2.webdamdb.com/1280_QLRcg0fTyte6.png?1526476084
   :width: 1071px
   :height: 499px
.. |Lift event example| image:: https://cdn2.webdamdb.com/1280_U6EXPe66CrF4.png?1526475730
   :width: 599px
   :height: 341px
