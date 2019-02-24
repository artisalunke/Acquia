.. include:: /common/global.rst

|acquia-product:lpm|
====================

.. toctree::
   :hidden:
   :glob:

   /lift/profile-mgr/*

.. container:: message-status

   |liftlogo| |acquia-product:lpm| is a component of `Acquia Lift </lift>`__.

.. |liftlogo| image:: https://cdn4.webdamdb.com/1280_6hBD2tUaE8E2.png?-62169955200
   :class: no-sb logo-sm-lift
   :width: 20px

|lpmlogo|

.. |lpmlogo| image:: https://cdn3.webdamdb.com/150th_sm_c6X7m3brFd91.png?1526475558
   :class: float-right
   :width: 61px

The |acquia-product:lpm| unifies person profile data collected from your
websites, both Drupal and non-Drupal, and optionally can integrate data
from other sources, such as email or a CRM.

Using |acquia-product:lpm| and the information that you collect, you can
create a high-resolution profile of your visitors, create and manage
your segments and goals, run reports and analytics against your data,
and administer how data is collected and mapped.

.. container:: message-status

 **QUICK LINKS:**   `Managing segments </lift/profile-mgr/segment>`__  |  
 `Managing events </lift/profile-mgr/event/category>`__  |  
 `Default segment criteria </lift/profile-mgr/segment/category>`__  |  
 `Release notes </lift/profile-mgr/release-notes>`__

.. _signing:

Signing in to |acquia-product:lpm|
----------------------------------

To sign in to the |acquia-product:lpm| interface and manage your
campaigns and visitor information, visit the URL appropriate for your
local |acquia-product:lpm| Admin region:

-  **Americas** –
   `us-east-1.lift.acquia.com <https://us-east-1.lift.acquia.com>`__
-  **Europe, Middle East, and Africa** –
   `eu-central-1.lift.acquia.com <https://eu-central-1.lift.acquia.com>`__
-  **Asia-Pacific and Japan** –
   `ap-southeast-2.lift.acquia.com <https://ap-southeast-2.lift.acquia.com>`__

If you are a |lplplink|_ or |lplpolink|_ subscriber, the |liftapilink|_ reference websites are available at the following URLs:

.. |lplplink| replace:: \ |acquia-product:lplp|\ 
.. _lplplink: /lift#packages

.. |lplpolink| replace:: \ |acquia-product:lplpo|\ 
.. _lplpolink: /lift#packages

.. |liftapilink| replace:: \ |acquia-product:liftapi|\ 
.. _liftapilink: /lift/omni/rest_api

-  **Americas** –
   `us-east-1-api.lift.acquia.com <https://us-east-1-api.lift.acquia.com>`__
-  **Europe, Middle East, and Africa** –
   `eu-central-1-api.lift.acquia.com <https://eu-central-1-api.lift.acquia.com>`__
-  **Asia-Pacific and Japan** –
   `ap-southeast-2-api.lift.acquia.com <https://ap-southeast-2-api.lift.acquia.com>`__

Information about your local |acquia-product:lpm| Admin region is
normally provided to you with your keys. `Contact Acquia
Support </support#contact>`__ if you need assistance connecting to
either website.

.. _password:

Password policy
~~~~~~~~~~~~~~~

When you first sign in to |acquia-product:lpm|, you may be asked to
change your password. |acquia-product:lpm| uses `the same password
security policy </acquia-cloud/access/password-strength>`__ as
|acquia-product:ac|.

For a comprehensive explanation of the rules employed by |acquia-product:lpm| regarding password complexity, see `Realistic
password strength estimation <https://blogs.dropbox.com/tech/2012/04/zxcvbn-realistic-password-strength-estimation/>`__.

.. _tab:

Documentation resources by tab
------------------------------

Use the following pages to help you configure and use |acquia-product:lpm|:

.. list-table::
   :widths: 25 75
   :header-rows: 1 

   * - Tab
     - Resource link
   * - **People**
     - `Examining visitor information </lift/profile-mgr/person>`__
   * - **Segments**
     - `Managing your website's segments </lift/profile-mgr/segment>`__
   * - **Goals**
     - `Managing your website's goals </lift/profile-mgr/goals>`__
   * - **Analytics**
     - `Accessing reports and visualizations </lift/profile-mgr/analytics/dashboards>`__
   * - **Admin**
     - 
       * `Creating and managing users </lift/profile-mgr/users>`__
       * `Creating and managing events </lift/profile-mgr/event/category>`__
       * `Exporting visitor information </lift/profile-mgr/file/export>`__
       * `Managing your visitor capture settings </lift/profile-mgr/admin/javascript>`__
       * `Customer sites </lift/profile-mgr/customer-sites>`__
       * `Using column meta data </lift/profile-mgr/admin/column-meta-data>`__


Adding tracking codes to your webpages
--------------------------------------

Drupal websites that use the |acquia-product:leb| can add tracking code
to their pages by |makeslots|_.

.. |makeslots| replace:: creating slots in \ |acquia-product:cha|\ 
.. _makeslots: /lift/exp-builder/slots

If your website uses a content management system (CMS) other than
Drupal, you can add a simple JavaScript code snippet to your website,
which will insert personalized content directly into your website,
regardless of the content management system that you use. Users with
|acquia-product:cha| version 8.x-3.0 or greater can get started by
following the steps in |nondrupal|_.

.. |nondrupal| replace:: Using \ |acquia-product:cha|\  with a non-Drupal website
.. _nondrupal: /lift/exp-builder/install/non-drupal

After you start collecting information about how your visitors interact
with your website, you can review and segment those interactions by
using |acquia-product:lpm|.

.. admonition:: Note for Drupal 7 users
   
   If you use Drupal 7 as your website's CMS, instead of manually adding the JavaScript tracker code to each of your webpages, we recommend that you use the included `|acquia-product:alt| </lift/exp-builder/install>`__ modules to send your website's visitor interactions to the |acquia-product:cha| service.

