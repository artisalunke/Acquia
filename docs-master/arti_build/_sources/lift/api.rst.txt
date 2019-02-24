.. include:: /common/global.rst

Using the |acquia-product:cha| APIs
===================================

.. toctree::
   :hidden:
   :glob:

   /lift/api/*

|acquia-product:cha| includes several interfaces that you can use to
interact with stored visitor data. These interfaces are exposed as APIs 
that you can use to both import and export data from the
|acquia-product:cha| service.

For more information about each of the APIs available as part of
|acquia-product:cha|, visit the page for each API:

-  `Content Hub API </content-hub/api>`__ – Enables you to
   create custom applications that publish, update, and consume content,
   and then render that content natively
-  `Decision API <http://docs.lift.acquia.com/decision/>`__ –
   Enables you to set and review administrative functions for how
   decisions about content may be displayed to users
-  `File Import API </lift/omni/api/file/import>`__ – Enables you to
   import user information from other sources into |acquia-product:cha|
-  `JavaScript API </lift/javascript>`__ – Enables you to send
   additional information about your users and activities
-  `Profiles API </lift/omni/rest_api>`__ – Enables
   integration between |acquia-product:cha| and other websites
-  `Push API </lift/omni/api/push>`__ – Enables real-time sending of
   notifications when users enter selected segments

Availability
------------

|acquia-product:cha| includes the following APIs for each available
package:

.. list-table::
   :widths: 40 15 15 15 15
   :header-rows: 1 

   * - API
     - |acquia-product:lplpw|
     - |acquia-product:lplpo|
     - |acquia-product:lpls|
     - |acquia-product:lplp|
   * - |chapi link|_
     - |no|
     - |no|
     - |yes|
     - |yes|
   * - `Decision API <http://docs.lift.acquia.com/decision/>`__
     - |no|
     - |yes|
     - |no|
     - |yes|
   * - `File Import API </lift/omni/api/file/import>`__
     - |no|
     - |yes|
     - |no|
     - |yes|
   * - `JavaScript API </lift/javascript>`__
     - |yes|
     - |yes|
     - |yes|
     - |yes|
   * - |liftapi|_
     - |no|
     - |yes|
     - |no|
     - |yes|
   * - `Push API </lift/omni/api/push>`__
     - |no|
     - |yes|
     - |no|
     - |yes|


.. |chapi link| replace:: \ |acquia-product:ch|\  API
.. _chapi link: /content-hub/api


.. |liftapi| replace:: \ |acquia-product:liftapi|\ 
.. _liftapi: /lift/omni/rest_api


Additional toolkit for |acquia-product:cha|
-------------------------------------------

|acquia-product:cha| includes the 
`Acquia Lift SDK <https://github.com/acquia/lift-sdk-php>`__ (software development
kit) for |acquia-product:lplp| and |acquia-product:lplpo| subscribers,
enabling them to develop software applications targeting the Decision
API.

Testing your API implementations
--------------------------------

You can test your implementation of the |acquia-product:cha| APIs with
`Postman <https://www.getpostman.com/>`__ and the package provided at
`Postman HTTP-HMAC <https://github.com/acquia/http-hmac-postman>`__ on
GitHub. To test your implementation, your code must meet both of the
following requirements:

-  Pass your customer ID as a header parameter for Decision API
-  Add a client ID for the |acquia-product:ch| API
