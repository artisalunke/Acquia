.. include:: /common/global.rst

Using |acquia-product:cha| with single-page applications
========================================================

When creating a single-page `decoupled application </lift/decoupled>`__
with |acquia-product:cha| using Drupal as your backend content
management system (CMS), requests for customized content are handled as
described in the following diagram:

|Decoupled architectures|

#. Content is authored in Drupal, and then published and stored in
   |acquia-product:ch|.
#. The front-end JavaScript application calls the |acquia-product:cha|
   service (using the |acquia-product:cha| `Decision
   API <http://docs.lift.acquia.com/decision/>`__) to track visitor
   behavior and request personalized content.
#. The Decision API requests the personalized content from
   |acquia-product:ch|.
#. The Decision API returns the metadata for personalized content (and
   HTML and JSON versions of the content) through JavaScript events.
#. The front-end JavaScript application consumes the customized content,
   renders it, and then displays it to the visitor.

When personalizing the content delivered by a single-page application,
give consideration to the special needs of a single-page application
during these points in the website-building process:

-  `Preparing for Acquia Lift with single-page
   applications <#preparing-to-use-acquia-lift-with-single-page-applications>`__
-  `Installing and configuring Acquia Lift <#install>`__
-  `Publishing content into Content Hub <#publishing-content-into-content-hub>`__
-  `Creating personalized rules on single-page applications <#creating-personalized-rules-on-single-page-applications>`__
-  `Calling personalization through the Decision API <#calling-acquia-product-cha-personalization-through-the-javascript-api>`__
-  `Listening for the personalization event, and rendering
   content <#listening-for-the-acquia-lift-personalization-event-and-rendering-content>`__


Preparing to use Acquia Lift with single-page applications
-------------------------------------------------------------------

When planning your use of |acquia-product:cha| with a single-page,
decoupled application, you must ensure that you are aware of specific
needs, including your `routing strategy <#routing-strategy>`__, and `URL
rewriting <#url-rewriting>`__.


Routing Strategy
~~~~~~~~~~~~~~~~

|acquia-product:cha| is incompatible with a hash-based routing system,
which uses URLs similar to ``myapp/#/myroute``, as it requires full URLs
pushed by the history API. These URLs can be updated by configuration in
most frameworks:

-  `EmberJS <https://guides.emberjs.com/v2.12.0/configuring-ember/specifying-url-type/>`__
-  `ReactJS <https://reacttraining.com/react-router/web/api/BrowserRouter>`__
-  `AngularJS <https://angular.io/guide/router#!#location-strategy>`__


URL Rewriting
~~~~~~~~~~~~~

|acquia-product:leb| authenticates users with OAuth2, returning to the
application URL with a special token query parameter. If your JavaScript
application rewrites the URL and strips this query parameter, your
|acquia-product:leb| application will freeze after successful login. A
successful implementation of your single-page application will allow the
query parameter to be passed through the URL string.


Configuring |acquia-product:cha| for single-page applications
-------------------------------------------------------------

To run |acquia-product:cha| on your single-page application, you should
`install it directly using the JavaScript
tag </lift/exp-builder/install/non-drupal>`__.

Inside the JavaScript tag configuration, you must `set the content
replacement mode </lift/exp-builder/config/modes>`__ to **Customized**,
which prevents |acquia-product:cha| from returning content through the
normal rendering process, instead returning only raw decision content
data.

Because single-page applications do not typically create additional page
loads during navigation, the |acquia-product:cha| standard JavaScript
implementation will not track data without further configuration. You
must implement data collection using the `Acquia Lift
JavaScript API </lift/javascript>`__ in your application to ensure data
is captured. Additional information on these methods can be found here:

-  `Acquia Lift JavaScript API - Capture </lift/javascript/view>`__
-  `Acquia Lift JavaScript API - Capture variables </lift/javascript/view/variables>`__
-  `Acquia Lift JavaScript API - Capture visitor information </lift/javascript/identity>`__

The following example displays the kind of information sent during a
page load:

.. code-block:: none

   //These can be matched to the parameters at https://docs.acquia.com/lift/javascript/view/variables
   _tcaq.push([
               'capture',
               'My_Custom_Event', {
                  'author':'Tolkien',
                  'engagement_score':'50',
                  'page_type':'interior',
                  'post_id':'12345',
                  'published_date':'1501270246',
                  'content_title':'New Title',
                  'content_type':'345type',
                  'content_section':'4term',
                  'content_keywords':'5term',
                  'persona':'6term',
                  'custom_column_metadata':'custom_value'
               }
         ]);



Publishing content into Content Hub
-------------------------------------------

You can configure content to be published into |acquia-product:ch| with
the `Acquia Content Hub
module <https://www.drupal.org/project/acquia_contenthub>`__. Once the
module is installed, it can be configured to publish certain content
types directly into |acquia-product:cha|.

.. container:: message-status

   |Learning Services logo|\ For a step-by-step video tutorial introducing you to publishing content types into |acquia-product:cha|, see |tutorial|_.

.. |Learning Services logo| image:: https://cdn3.webdamdb.com/1280_w1WjsvuWixS1.png?-62169955200
   :class: no-sb float-left logo-sm-lift
   :width: 36px
   
.. |tutorial| replace:: Publishing Content to \ |acquia-product:leb|\ 
.. _tutorial: /tutorials/creating-personalized-experiences-acquia-lift/publishing-content-experience-builder


Creating personalized rules on single-page applications
-------------------------------------------------------

Since your front-end JavaScript application will control the rendering
of the content on the webpage, the creation of slots in exactly the
pages and locations you want to personalize is not critical.
|acquia-product:leb| provides `documented methods to refresh
data </lift/javascript/exp-builder-methods>`__, which are useful when
navigating a single-page application.

The following methods can be used to create personalized rules:

-  `Creating exact locations for slots <#creating-exact-locations-for-slots>`__ *(recommended)*
-  `Creating slots on an inaccessible page <#creating-slots-on-an-inaccessible-page>`__


Creating exact locations for slots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By creating slots with embed codes or CSS selectors on the exact
locations inside your single-page application, you can drag-and-drop
content into slots to create personalized rules. The content displayed
in the slot will not receive styling, but does receive access to
click-through goals for rules created by |acquia-product:cha|.


Creating slots on an inaccessible page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By creating slots on an inaccessible page on your website, you can
drag-and-drop content into the slots to create personalized rules. The
content displayed in the slot will not receive styling, as it is
provided from the backend content management system without styling
applied.

Calling |acquia-product:cha| personalization through the JavaScript API
-----------------------------------------------------------------------

After setting up content, slots, and rules, there are multiple ways to
call ``personalize`` functions in |acquia-product:cha|. You must call
the ``customize`` `JavaScript function </lift/javascript/personalize>`__
directly on every webpage and action in which you want
|acquia-product:cha| to return new or updated personalized content to
your single-page application.

-  *If you have created exact locations for slots,* you can directly
   call the |acquia-product:cha| ``customize`` JavaScript method, which
   will evaluate any slots configured to run on the current page, and
   fetch the necessary personalized content.
-  *If you have created slots on an inaccessible page,* you can directly
   call the |acquia-product:cha| ``customize`` JavaScript method for
   specific slots, even if those slots don't exist on the current view
   of the page.


Listening for the Acquia Lift personalization event, and rendering content
-----------------------------------------------------------------------------------

After configuring personalization, the final step in creating a
personalized single-page application is setting up a JavaScript event
listener inside it which will listen for the |acquiaLiftContentCustomizable|_, interpret the
data returned, and render the personalized content using the returned
data.


.. |acquiaLiftContentCustomizable| replace:: Lift ``acquiaLiftContentCustomizable`` event
.. _acquiaLiftContentCustomizable: https://docs.acquia.com/lift/javascript/events

.. |Decoupled architectures| image:: https://cdn2.webdamdb.com/1280_oBFkiWLkZjw3.png?1526475736
   :class: no-sb align-center
   :width: 550px
