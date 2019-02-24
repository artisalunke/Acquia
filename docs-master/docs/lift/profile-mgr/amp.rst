.. include:: /common/global.rst

Using Accelerated Mobile Pages
==============================

To increase both your website's responsiveness and the usability of its
webpages for mobile device users (such as those on tablets and phones)
while retaining the ability to analyze your website visitors and their
behaviors, |acquia-product:cha| supports the use of `Accelerated Mobile
Pages <https://www.ampproject.org/learn/overview/>`__ (AMP).

If you want to serve personalized content with AMP, you must use the
`Acquia Lift API </content-hub/api>`__ or its software
development kit (SDK) to create the personalized content and serve the
entire webpage to AMP with the personalized content already included (as
AMP does not support the modification of pages with custom JavaScript).

Enabling AMP
------------

To enable |acquia-product:cha| to use AMP with one of your Drupal
websites, complete the following steps:

#. Sign in to |acquia-product:lpm| using an administrative account.
#. Click **Admin > Manage customers**.
#. In the **Account ID** column, click the customer name you want to
   configure.
#. On the customer details page, click the **Add new person identifier
   type** link.
#. Enter values for the following fields, based on your requirements:
   Field
#. Select the **Resolvable** check box.
#. Click **OK**.
#. Download, install, and enable the `Accelerated Mobile Pages
   (AMP) <https://www.drupal.org/project/amp>`__ module on your Drupal
   website.

Basic Google AMP Cache usage
----------------------------

After you have enabled AMP for your website, you must include HTML code
on relevant pages that points to an AMP proxy for serving content to
visitors. To accomplish this, |acquia-product:cha| provides specific
support for `Google AMP
Cache <https://developers.google.com/amp/cache/>`__.

To enable webpage analytics, be sure to include the following AMP
analytics script in a webpage's ``header`` tag before you include the
general AMP script.

.. code-block:: none

   <script async custom-element="amp-analytics" src="https://cdn.ampproject.org/v0/amp-analytics-0.1.js"></script>

As an example, you can use code similar to the following, embedded into
a webpage where you want to use AMP to track page views:

.. code-block:: none

   <amp-analytics type="acquialift" id="acquialift">
   <script type="application/json">
   {
   "vars": {
      "siteId":"my-acquia-lift-site-id",
      "accountId": "MYACCOUNTID",
      "decisionApiUrl": "us-east-1-decisionapi.lift.acquia.com"
   }
   }
   </script>
   </amp-analytics>

with the following ``vars`` values set to `your customer
details </lift/exp-builder/install/drupal8>`__:

-  ``siteId`` - Your |acquia-product:cha| Site ID
-  ``MYACCOUNTID`` - Your |acquia-product:cha| account ID
-  ``decisionApiUrl`` - Your regional Decision API URL

Examples
--------

Use the following examples to help you use AMP with your website and its
content.

Sending a click-through event when clicking on a specific button
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example configures AMP to use a customer specific event type when
the user clicks on an element that is identified by the css id
``#test1``.

.. code-block:: javascript

   <amp-analytics type="acquialift" id="acquialift">
   <script type="application/json">
   {
   "requests":
      "customEvent": "${basicCapture}&en=${eventName}"
   },
   "vars": {
      "siteId":"my-acquia-lift-site-id",
      "accountId": "MYACCOUNTID",
      "decisionApiUrl": "us-east-1-decisionapi.lift.acquia.com"
   },
   "triggers": {
      "pageLoad": {
         "on": "visible",
         "request": "pageview"
      },
      // Sends a Custom event.
      "clickCustomEvent": {
         "on": "click",
         "selector": "#test1",
         "request": "customEvent",
         "vars": {
         "eventName": "MyCustomEventId"
         }
      }
   }
   }
   </script>

Sending a custom event
~~~~~~~~~~~~~~~~~~~~~~

This example configures AMP to use a customer specific event type when
the user clicks on an element that is identified by the css id
``#test1``.

.. code-block:: javascript

   <amp-analytics type="acquialift" id="acquialift">
   <script type="application/json">
   {
   "requests":
      "customEvent": "${basicCapture}&en=${eventName}"
   },
   "vars": {
      "siteId":"my-acquia-lift-site-id",
      "accountId": "MYACCOUNTID",
      "decisionApiUrl": "us-east-1-decisionapi.lift.acquia.com"
   },
   "triggers": {
      "pageLoad": {
         "on": "visible",
         "request": "pageview"
      },
      // Sends a Custom event.
      "clickCustomEvent": {
         "on": "click",
         "selector": "#test1",
         "request": "customEvent",
         "vars": {
         "eventName": "MyCustomEventId"
         }
      }
   }
   }
   </script>
