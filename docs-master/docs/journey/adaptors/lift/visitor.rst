.. include:: /common/global.rst

|acquia-product:cha|: Visitor adaptor
=====================================

The |acquia-product:cha| visitor query adaptor allows
|acquia-product:aj| to retrieve data from multiple faucets of a user's
profile in |profile manager|_. The adaptor
uses the APIs provided by |acquia-product:cha| and described in the
|acquia-product:cha| `Decision API
documentation <http://docs.lift.acquia.com/decision/#>`__.

.. |profile manager| replace:: \ |acquia-product:lpm| \ 
.. _profile manager: /lift/profile-mgr

Creating the adaptor
--------------------

To use the |acquia-product:cha| visitor query adaptor, complete the
following steps:

#. `Create an adaptor </journey/adaptors>`__ of the type **Acquia
   Lift**.
#. Configure the following settings for the adaptor:

   -  **Adaptor Action** list - Click **Visitor**
   -  **identifier** - Key related to specific user to query
   -  **identifier_type** - Key type, such as *email* or *tracking*
   -  **person_tables** - Data to return, specified as a comma separated
      list
   -  **Output** (located in the **Output** section at the bottom of the
      page) - In the **Data Schema** panel, find the schema location
      that is the output target for the adaptor, click its name, and
      then click the left arrow icon |left arrow| to set the adaptor
      output to that location

   For information about the |acquia-product:cha| visitor query API
   method, see the |lift api|_.
#. After you have completed your changes, click **Save Query Parameters
   & URL Path / Update Parameters**.
#. To close the adaptor configuration page, click the **X** to the right
   of the adaptor name in the tab bar near the top of the webpage.

.. |lift api| replace:: \ |acquia-product:cha| \  \ |acquia-product:liftapi| \ 
.. _lift api: http://docs.lift.acquia.com/profilemanager/#visitor_query_get

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
