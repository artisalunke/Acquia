.. include:: /common/global.rst

Segment examples
================

Building your segments correctly is a critical and sometimes complex
task. Although it is impossible to provide a full list of every segment
that you could build for your website, here are several examples that
you can use to help you understand how to build segments correctly for
the most effective targeting:

-  :ref:`geosegments`
-  :ref:`devicetype`
-  :ref:`utmreferral`
-  :ref:`1stvisit`
-  :ref:`repeatview`
-  :ref:`multipleinsingletouch`
-  :ref:`preferredcontenttype`
-  :ref:`eventbased`
-  :ref:`abandoncart`

For information about building segments, see `Creating and managing
segments </lift/profile-mgr/segment>`__, which includes a list of
`default segment criteria </lift/profile-mgr/segment/category>`__ that
are available for your use.


.. _geosegments:

Geolocation segments
--------------------

You can create a geolocation segment for an entire country by searching
for a country in the **Find Country** field.

|Editing geolocation segment|

**Current Location : Country**   —   **Matches One [AU]**

|AU geolocation segment displayed|

You can create a larger segment by combining countries, such as creating
a *North America* segment by identifying users whose country is Canada,
the United States, or Mexico. Conversely, if you need to target
highly-specific areas, geolocation segments can also be as small as a
city or suburb.

.. _devicetype:

Device type
-----------

By examining your users' platform, you can identify visitors using
mobile phones or tablets to visit your website.

**Current System Info : Platform**   —   **Matches One [Mobile]**

|Mobile visitors|

For a list of platform segmentation options, see `Person
Ranking </lift/profile-mgr/segment/category#person-ranking>`__.

.. _utmreferral:

Marketing campaign referral
---------------------------

If you're using UTM codes on your marketing campaigns, you can identify
visitors referred through an email link by matching UTM query strings in
URLs, such as ``utm_source=email`` or ``utm_campaign=campaign-name``, to
the Segment Criteria field in |acquia-product:cha|. For more information
about available fields, see `External
Campaign </lift/profile-mgr/segment/category#external-campaign>`__.

.. _1stvisit:

First-time visitor
------------------

By targeting **Frequency**, you can identify first-time visitors to your
website.

.. _repeatview:

Behavioral-based segment
------------------------

By identifying users who view a specific page more than once, you can
target visitors with a stronger interest in a topic.

| **Event Count : Content View**   —   **>= [2] in [Past 30 Days]**
| Sub-Criteria - **All**   —   **Page Content : Page
  Url**   —   **Contains One [/business/a000**

|Views a page more than once|

.. _preferredcontenttype:

Preferred content types
-----------------------

You can identify browsing behavior by identifying users according to the
*Favorite Content Type*. You can also combine multiple criteria to build
a more complex segment as shown in this example, which looks for
visitors who have viewed more than three pieces of content in the past
30 days that contained the string ``/health`` in the URL.

| **Event Count : Content View**   —   **>= [3] in [Past 30 Days]**
| Sub-Criteria - **All**   —   **Page Content : Page
  Url**   —   **Contains One [/health-**

|Browsing behavior|

For more information about other default properties attached to
visitors, see `Person
properties </lift/profile-mgr/segment/category#person-properties>`__.

.. _multipleinsingletouch:

Multiple page views in a touch
------------------------------

You can identify visitors who view the number of pages you specify
during a single touch of your website:

**Touch : Number of Page Views**   —   **>= [2]**

|Two or more pageviews in a touch|

.. _eventbased:

Event-based
-----------

You can identify users who perform a specified action on your website,
such as subscribing to a newsletter. For more information, see `Creating
and managing events </lift/profile-mgr/event/category>`__.

.. _abandoncart:

Shopping cart abandonment
-------------------------

You can identify users who have performed events external to your system
if you have created a `custom
event </lift/profile-mgr/event/category>`__ connecting that system to
|acquia-product:cha|. For example, visitors who have abandoned a
shopping cart with items in it can be targeted with *Event: Abandoned
Cart*. For more information, see `Creating and managing
events </lift/profile-mgr/event/category>`__.

.. |Editing geolocation segment| image:: https://cdn4.webdamdb.com/1280_6ANRt0GDekz6.png?1526475730
   :width: 550px
   :height: 524px
.. |AU geolocation segment displayed| image:: https://cdn4.webdamdb.com/1280_6XOEDFsOLt01.png?1526475759
   :width: 550px
   :height: 165px
.. |Mobile visitors| image:: https://cdn2.webdamdb.com/1280_MPiFV6YpuSL9.png?1526476161
   :width: 550px
   :height: 73px
.. |Views a page more than once| image:: https://cdn4.webdamdb.com/1280_6DXu3k3iAhl0.png?1526475817
   :width: 550px
   :height: 149px
.. |Browsing behavior| image:: https://cdn3.webdamdb.com/1280_MLRWrLeWN191.png?1526476122
   :width: 600px
   :height: 153px
.. |Two or more pageviews in a touch| image:: https://cdn2.webdamdb.com/1280_ftNyK8YFe18.png?1526475557
   :width: 550px
   :height: 79px
