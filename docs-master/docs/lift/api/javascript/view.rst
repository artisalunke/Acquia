.. include:: /common/global.rst

capture - |acquia-product:cha| JavaScript API
=============================================

.. toctree::
   :hidden:
   :glob:

   /lift/javascript/view/*

Although |acquia-product:cha| can capture visitors' webpage views on
their own, there are other methods that can be used to capture data as
well. Each of the following methods can make use of additional
`variables </lift/javascript/view/variables>`__ to capture more specific
information:

-  `Metatags <#metatags>`__
-  `JavaScript variables <#js-variable>`__
-  `Tracking script <#tcaq>`__
-  `Drupal taxonomy mappings <#taxonomy>`__

Metatags
--------

|acquia-product:cha| determines the page context to utilize when
tracking captures and segmenting users. |acquia-product:cha| can collect
custom additional page information using the `Capture
API <http://apidoc.dev.lift.acquia.com/#capture>`__. visitor profile custom 
fields allow the definition of user-defined fields to capture information 
specific to a customer site. |acquia-product:cha| passes these values along 
with capture data when specified within ``<meta>`` tags in the ``<head>`` 
section of a page or when specified in the global |acquia-product:cha| 
JavaScript scope. To pass capture data or user-defined fields using a metatag, 
the metatag should be added to the ``<head>`` in the following format:

``<meta itemprop="acquia_lift:custom-field-name" content="custom-field-value">``

From the preceding format, ``custom-field-name`` is the parameter used by 
``captureView``, which is the field name used by the data warehouse. The 
``custom-field-value`` parameter is the value to track for that field. The 
custom field name uses the format ``acquia_lift:[TABLE]_udf[NUMBER]``, where:

- ``[TABLE]`` is either ``person``, ``touch``, or ``event``.
- ``[NUMBER]`` is the custom field selected when creating the custom column meta data.

For example, if ``person_udf50`` represents Industry, and the current visitor's industry is the healthcare industry, then the metatag for the page capture will be the following:

``<meta itemprop="acquia_lift:person_udf50" content="Healthcare">``

To pass the same information directly using JavaScript, use the following code:

.. code-block:: javascript

   window.AcquiaLift = window.AcquiaLift || {};	
   window.AcquiaLift.profile = window.AcquiaLift.profile || {};	
   window.AcquiaLift.profile.person_udf50 = 'Healthcare';

If the same field is defined in both a metatag and within JavaScript, the value defined within JavaScript will be used.

.. note::  Metatags must be defined in the page *before* the ``lift.js`` reference 
   on the initial page load. If the tags are defined after the JavaScript is 
   called, the script will not work properly because updates will be reflected 
   only in the next script call.

JavaScript variables
--------------------

You can also define variables directly in your page's JavaScript, similar to the following:

.. code-block:: javascript

   window.AcquiaLift.profile.person_udf5 = 'my dynamic content goes here';

The default timeout that is set in both ``lift.js`` and the ``/decide-js`` 
endpoint is 30 seconds. You can alter the timeout value for all calls 
(except authentication calls) by providing a different timeout value. For 
example, the following code increases the timeout value to 60 seconds:


.. code-block:: javascript

   window.AcquiaLift.loadTimeout = 60;

Tracking script
---------------

|acquia-product:cha| users can add 
`a tracking script </lift/offers/tracker/add>`__ to a webpage to capture this 
information. To do this, the tracking script uses the ``_tcaq.push`` function 
to send the page view information to the |acquia-product:cha| service.

.. admonition::  Note for Drupal users

   To interact with the Acquia Lift service, we recommend installing the 
   `Acquia Lift-related Drupal modules </lift/exp-builder/install>`__ on your website.

This function allows you to perform the following actions:

- `Capture a page view </lift/javascript/view#pageview>`__
- `Capture additional page view information </lift/javascript/view#capture>`__
- `Capture do_not_track information </lift/javascript/view#user>`__
- `Pass custom events through the JavaScript API </lift/javascript/view#passing>`__

Capturing a page view
---------------------

To capture a page view, add the following JavaScript code to your webpage:

.. code-block:: none

   <script type="text/javascript">
   _tcaq.push(['capture', 'Content View']);
   </script>

|acquia-product:cha| captures the page view and associates it with the website visitor's information.

.. note::  Because you will generally want to capture the page view for every 
   tracked webpage, you can add the instruction to the end of the |acquia-product:cha| tracker script.

Capturing additional page view information
------------------------------------------

The capture method includes several parameters that you can use to include additional information about the webpage or the website visitor:

.. code-block:: none

   _tcaq.push(['capture', '<category>', {'<parameter>':<value>'}]);

Capturing do_not_track information
----------------------------------

|acquia-product:cha| provides the ability to set do_not_track information for a 
user. The capture API (POST call) allows the user to send a capture while 
indicating whether or not the visitor should be tracked. The capture must use 
the following event_name: ``updatePersonTracking``. For example:

.. code-block:: none

   {
   "identity": "qa_5373_2016-12-01 13:21:46.109@test.com",
   "identity_source": "email",
   "do_not_track": true,
   "return_segments": true,
   "captures": [
      {
         "event_source": "app",
         "event_name": "updatePersonTracking",
         "event_date": "2016-11-24 13:21:57.418",
         "engagement_score": 0
      }
   ]
   }

Passing custom events through the JavaScript API
------------------------------------------------

To use custom events with |acquia-product:cha|, create an event in |acquia-product:lpm|.

You can then pass the event to the |acquia-product:cha| service by using the following JavaScript command:

.. code-block: javascript::

   <script type="text/javascript">
   _tcaq.push(['capture', '[event_id]']); 
   </script>

where ``[event_id]`` is the ID of the event that you created.

Drupal taxonomy mappings
------------------------

You can use Drupal taxonomy terms in your page capture by ensuring that you have mapping fields set to taxonomy vocabularies in your |acquia-product:cha|-enabled Drupal website. These can be set in the |acquia-product:cha| settings, under **Configuration > Acquia Lift**, in the **Data collection settings** section.