.. include:: /common/global.rst

|acquia-product:cha|: Decide adaptor
====================================

The |acquia-product:cha| decide adaptor allows |acquia-product:aj| to
provide content for a unique user and a particular slot, based on the
segments the user belongs to. The adaptor uses the APIs provided by
|acquia-product:cha| and described in the |acquia-product:cha| `Decision
API documentation <http://docs.lift.acquia.com/decision/#>`__.

Creating the adaptor
--------------------

To use the |acquia-product:cha| decide adaptor, complete the following
steps:

#. `Create an adaptor </journey/adaptors>`__ of the type **Acquia
   Lift**.
#. Configure the following settings for the adaptor:

   -  **Adaptor Action** list - Click **Decide**
   -  **site_id** - Identifier for the customer website
   -  **prefech** - Boolean determining whether to prefetch the
      requested HTML content item — defaults to ``false``
   -  **account_id** - Identifier for the client
   -  **Request Body** - In the **Data Schema** panel, find the schema
      location that maps to the request body, click its name, and then
      click the left arrow icon |left arrow| to set the request body
      source in the adaptor to that location
   -  **Output** (located in the **Output** section at the bottom of the
      page) - In the **Data Schema** panel, find the schema location
      that is the output target for the adaptor, click its name, and
      then click the left arrow icon |left arrow| to set the adaptor
      output to that location

   For information about the |acquia-product:cha| decide API method, see
   the |acquia-product:cha| `Decision
   API <http://docs.lift.acquia.com/decision/#decide_post>`__.
#. After you have completed your changes, click **Save Query Parameters
   & URL Path / Update Parameters**.
#. To close the adaptor configuration page, click the **X** to the right
   of the adaptor name in the tab bar near the top of the webpage.

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Adaptor does not have           | It is necessary to create a       |
| connection set**                  | connection and choose it from the |
|                                   | **Adaptor Connection** drop down  |
+-----------------------------------+-----------------------------------+
| **This adaptor's configuration    | No data location for the output   |
| requires a data source to be      | has been selected                 |
| set**                             |                                   |
+-----------------------------------+-----------------------------------+

.. |left arrow| image:: https://cdn4.webdamdb.com/100th_sm_kR0cgUi72rf3.png?1526475474
   :class: no-sb
   :width: 24px
