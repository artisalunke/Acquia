.. include:: /common/global.rst

|acquia-product:liftapi| reference
==================================

.. container:: message-status

   This feature is available only to |lplp|_ and |lplpo|_ subscribers.


.. |lplp| replace:: \ |acquia-product:lplp|\ 
.. _lplp: /lift

.. |lplpo| replace:: \ |acquia-product:lplpo|\ 
.. _lplpo: /lift

Subscribers with access to |acquia-product:ldb| can use the
|acquia-product:liftapi| to integrate their websites and applications
with |acquia-product:cha|.


Using the |acquia-product:liftapi|
----------------------------------

Similar to many other APIs, the [acquia-liftapi] uses standard HTTP
methods to communicate with |acquia-product:cha|, including ``GET``,
``PUT``, and ``DELETE``. You can view the list of available
|acquia-product:liftapi| calls at the following URL:

`http://docs.lift.acquia.com/profilemanager <http://docs.lift.acquia.com/profilemanager/>`__

You can also view |acquia-product:liftapi| information at
``[region-based endpoint]-api.lift.acquia.com``, replacing
``[region-based endpoint]`` with the server for your local
|acquia-product:lpm| Admin region, such as ``us-east-1``,
``eu-central-1``, or ``ap-southeast-2``.


Keys and access information
---------------------------

Acquia will provide you with your keys after you subscribe to
|acquia-product:ldb|.

Users with the following
`permissions </lift/profile-mgr/admin/permissions>`__ can view
credentials and access information:

-  **Experience Builder Admin**
-  **Content Hub Admin**
-  **Profiles API Goals**
-  **Profiles API Segments**


If a user has one of the previous permissions, complete the following
steps to view access information:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm| interface.
#. Click the **Admin** tab.
#. Click the **Manage customers** link.

The |acquia-product:lpm| will display the 
`Customer information </lift/profile-mgr/admin/customer>`__ page, which includes
your key information. In most circumstances, the page will display only
a single result — your own customer subscription. If more than one
website is displayed, click the **Account ID** of the desired
subscription.


Sample |acquia-product:liftapi| methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are some examples of the methods provided in the
|acquia-product:liftapi|:

.. list-table::
   :widths: 40 60
   :header-rows: 1 

   * - API call
     - Description
   * - ``capture``
     - Accepts captures and returns segments matched by the captures
   * - ``event_import``
     - Import one or more events for a person into |acquia-product:cha|
   * - ``events``
     - Create or delete individual event types
   * - ``export_visitor_data``
     - Export visitor data from |acquia-product:cha| as files
   * - ``export_visitor_data_status``
     - Report on the status of an export process initiated by ``export_visitor_data``
   * - ``goals``
     - Obtain information about goals in |acquia-product:cha|
   * - ``segments``
     - Obtain information about segments in |acquia-product:cha|
   * - ``visitor_query``
     - Return visitor data for a single person from |acquia-product:cha|


API call format
~~~~~~~~~~~~~~~

Use the following URL structure when you send commands to the
|acquia-product:liftapi|:

``{region-based endpoint}/{account_id}/{command}``

where:

-  ``{region-based endpoint}`` is the API server URL of the
   |acquia-product:lpm| Admin. This information may be provided to you
   with your keys, and is available from your
   `Insight <https://cloud.acquia.com>`__ page. This varies based on
   your assigned API server.
-  ``{account_id}`` is your customer account ID.
-  ``{command}`` is the operation that you want to complete.

The API service request uses an
`HMAC-SHA256 </lift/omni/api/hmac-intro>`__ message hash, with the
following required request header for its authorization:

``Authorization : HMAC {access_key_id}:{signature}``

where:

-  ``{access_key_id}`` is an access key string that is used to select
   the corresponding secret access key.
-  ``{signature}`` is an HMAC-SHA256 hash of the canonical
   representation of the request, using the secret access key.
   ``Accept``, ``Host``, ``User-Agent``, and ``sorted query string`` are
   used as the payload to calculate HMAC signature.
