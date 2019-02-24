.. include:: /common/global.rst

Viewing the Activity tab
========================

.. container:: internal-navigation

   **Profile Manager person detail**

   * :doc:`Intro </lift/profile-mgr/person>`
   * :doc:`Summary </lift/profile-mgr/person/profile>`
   * :doc:`Insights </lift/profile-mgr/person/insights>`
   * Activity
   * :doc:`Details </lift/profile-mgr/person/profile-details>`


In **Person > Profile details**, after you have selected a specific
visitor, the **Activity** tab lists each *touch* recorded for that
visitor. A touch is a series of contiguous views with a duration between
events of no more than 30 minutes.

|lift-web-activity-details-tab.png|

Each touch includes the following information:

-  **Date** - The date the visitor made the touch
-  **Duration** - The duration of the touch
-  |Customer site|_ - If you
   have multiple websites using |acquia-product:lpm|, this field lists
   the website where this touch took place; if you have not defined any
   customer sites or have only one website using |acquia-product:lpm|,
   this field may be empty
-  **Source** - The location from where the touch originated — for
   example, **Web** for data originating from your websites, or
   **Marketo** for data imported from the `Marketo
   connector </lift/connectors/marketo>`__
-  **Page Views** - The number of pages the visitor viewed during the
   touch
-  **Score** - The computed engagement score at the touch level, which
   will vary depending on what events are included in the touch. Each
   event can be assigned its own engagement score — for example, a touch
   in which one of the events was a newsletter subscription could have a
   higher engagement score than a touch containing only page views


.. |Customer site| replace:: **Customer site**
.. _Customer site: /lift/profile-mgr/customer-sites

Touch properties
----------------

Clicking an individual touch and then selecting **Show Properties**
causes |acquia-product:lpm| to display additional information. Depending
on the type of touch, the displayed properties will vary. Here are
several of the most common properties:

-  **Referrer domain** - The host name of the external domain that
   referred the visitor to the first webpage visited on your website
   (displayed as **Direct** if there was no external referrer)
-  **Referrer Url** - The URL of the external website that referred the
   visitor to the first webpage visited on your website (displayed as
   **Direct** if there was no external referrer)
-  **Identifier** - The touch session identifier
-  **Search Terms** - Any search terms that came from the referrer,
   which provides information about how this visitor came to the
   customer's website
-  **Country** - The country from which the visitor accessed your
   website
-  **Region** - The region of the country the visitor was in when they
   accessed your website
-  **City** - The city the visitor was in when they accessed your
   website
-  **Latitude** - The latitude of the visitor, based on their IP address
-  **Longitude** - The longitude of the visitor, based on their IP
   address
-  **Visitor IP** - The visitor's IP address
-  **User Agent String** - The platform, operating system, and browser
   the visitor used during the touch

Activity section
----------------

The **Activity** section also provides a list of events, each of which
has a date, name, and customer site associated with it. A touch must be
selected before a list of events is displayed. Clicking an individual
event and selecting **Show Properties** displays additional information,
depending on the event type. For example, the properties of a **Content
View** include the following items:

-  **Engagement Score** - The computed engagement score at the event
   level, which depends on what type of event occurred — examples can
   include a page view or a newsletter subscription

   By default, all **Content View** events have an engagement score of
   **1**. The engagement score is included in the score for each
   individual touch, and each touch's score is included in the total
   engagement score for each visitor. The total engagement score
   includes all engagement scores for a 90-day period.

-  **Page Type** - The type or function of the webpage accessed during
   the event (such as **home page**, **tag page**, or **article page**)
-  **Page URL** - The URL of the webpage that the visitor accessed
-  **Content Type** - The content type of the accessed webpage
-  **Content Title** - The title of the webpage that the visitor
   accessed
-  **Content ID** - The node ID of the accessed webpage

More information
----------------

For more information about this visitor's behavior and activities on
your website, see `Examining visitor
information </lift/profile-mgr/person>`__.

.. |lift-web-activity-details-tab.png| image:: https://cdn2.webdamdb.com/1280_YavIr5hfVnI3.png?1527080687
   :width: 590px
   :height: 253px
