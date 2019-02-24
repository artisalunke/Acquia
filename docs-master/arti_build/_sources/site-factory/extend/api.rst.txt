.. include:: /common/global.rst

Using the |acquia-product:sfa|
==============================

.. toctree::
   :hidden:
   :glob:

   /site-factory/extend/api/*

|acquia-product:edg| includes a REST API that you can use to create and
manage your hosted websites and to obtain the status of jobs in your |acquia-product:sfi|.

.. note::  You cannot use the `Acquia Cloud API </acquia-cloud/api>`__ 
      to access or interact with |acquia-product:edg| environments.


Obtaining your API key
----------------------

Each of the |acquia-product:edg| API calls requires you to enter your
|acquia-product:edg| username and API key to either complete the action
or to return results. To obtain your API key, complete the following
steps:

#. `Sign in </site-factory/manage/login>`__ to your |acquia-product:sfi| 
   using an account with the |platformadmin|_ role.
#. In the admin menu, click your username.
#. Click the **API key** tab.

.. |platformadmin| replace:: *platform admin*
.. _platformadmin: /site-factory/users/admin/platform-admin

|acquia-product:edg| displays your API key. Because the key is required
for use by the different |acquia-product:edg| API calls, save the key to
a text file or some other secure location.


Using the REST API
------------------

Similar to many other APIs, the |acquia-product:edg| API uses standard
HTTP methods to communicate with the service, including GET, PUT, and
POST. You can view the list of available |acquia-product:edg| API calls
on your instance of |acquia-product:edg|, along with specific parameters
and examples of their use, at the following URL (where ``[site_URL]`` is
the URL of your |acquia-product:edg| interface):

.. code-block:: none

   https://[site_URL]/api/v1

You can also review complete documentation for all of the available
|acquia-product:edg| API methods by visiting the `Acquia Cloud Site Factory
API Reference <https://www.demo.acquia-cc.com/api/v1>`__ or view
customer `Factory API examples </site-factory/extend/api/examples>`__.

.. note::  
   
   Anonymous users do not have permission to view all endpoints in the
   |acquia-product:sfa|. To view all endpoints, 
   `sign in </site-factory/manage/login>`__ to your |acquia-product:sfi| 
   before attempting to view the available endpoints.


Sample API methods
~~~~~~~~~~~~~~~~~~

Here are some examples of the methods provided in the
|acquia-product:edg| API:

+-----------------------------------+-----------------------------------+
| REST API call                     | Description                       |
+===================================+===================================+
| ``groups``                        | Obtain a group listing, or create |
|                                   | a group                           |
+-----------------------------------+-----------------------------------+
| ``ping``                          | Determine if the API is           |
|                                   | responding                        |
+-----------------------------------+-----------------------------------+
| ``sites``                         | Create, duplicate, or manage      |
|                                   | backups for a website             |
+-----------------------------------+-----------------------------------+
| ``stage``                         | Start the staging process         |
+-----------------------------------+-----------------------------------+
| ``status``                        | Obtain or modify the status of    |
|                                   | the factory                       |
+-----------------------------------+-----------------------------------+
| ``theme``                         | Send or process theme             |
|                                   | modifications                     |
+-----------------------------------+-----------------------------------+
| ``users``                         | Create, modify, list, or delete   |
|                                   | user accounts in the factory      |
+-----------------------------------+-----------------------------------+

For complete documentation, see the `Acquia Cloud Site Factory API
Reference <https://www.demo.acquia-cc.com/api/v1>`__.


Testing your connection
~~~~~~~~~~~~~~~~~~~~~~~

When you first start using the |acquia-product:edg| API, we encourage
you to use the ``ping`` call to test your connection to the API. To do
this, complete the following steps:

#. `Obtain your user account's API key <#api-key>`__ from the
   |acquia-product:sfi|.
#. Open a command prompt, and then enter the following command:

   .. code-block:: none
   
      curl 'https://[site_URL]/api/v1/ping' -u [user_name]:[api_key]

   where:

   -  ``[site URL]`` is the URL of your |acquia-product:sfi|
   -  ``[user_name]`` is your |acquia-product:sfi| user account name
   -  ``[api_key]`` is your user account's API key from the
      |acquia-product:sfi|

#. Verify that the API call returns results similar to the following:

   .. code-block:: none
   
      {"message":"pong","server_time":"2014-11-18T13:44:57+00:00"}


Using the REST API with staging environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because staging environments do not have access to the SSL certificates
that are made available to production environments, you must append the
``-k`` command line switch to your ``curl`` command when you make calls
to a staging environment using the |acquia-product:edg| API.

For example, using the ``ping`` call on a staging environment would
require a command similar to the following:

.. code-block:: none

   curl 'https://[site_URL]/api/v1/ping' -u [user_name]:[api_key] -k