.. include:: /common/global.rst

Using Lift Inspector
====================

|acquia-product:cha| Inspector

-  `Intro </lift/drupal/inspector>`__
-  Using

Note

|acquia-product:cha| Inspector requires jQuery 1.7 or newer.

After you enable the |acquia-product:cha| Inspector,
|acquia-product:cha| displays a menu bar at the bottom of the webpage.
To view the |acquia-product:cha| inspector, click its up arrow icon |Up
arrow|.

|lift-inspector.png|

|acquia-product:cha| Inspector features
---------------------------------------

The |acquia-product:cha| Inspector contains the following three tabs:

-  **`Lift Profile <#profile>`__**
-  **`Site Preview <#preview>`__**
-  **`Event Log <#event>`__**

.. _profile:

Lift Profile tab
~~~~~~~~~~~~~~~~

This tab displays information that is normally stored in cookies that
are sent to the |acquia-product:alw| service. Its displayed information
includes:

-  **Person tracking id** - A combination of letters and numbers unique
   to this particular website visitor.
-  **Touch tracking id** - The combination of letters and numbers that
   uniquely identifies this website visitor's touch. A touch is a series
   of contiguous views with a duration between events of no more than 30
   minutes. For more information about touches, see `Examining visitor
   information </lift/drupal/web/person>`__.
-  **Evaluated segments** - The website segments into which this website
   visitor currently fits, based on their activity on the website. For
   more information about segments, see `Managing your site's
   segments </lift/drupal/web/segment>`__.

Site Preview tab
~~~~~~~~~~~~~~~~

The **Site Preview** tab allows you to examine your personalizations as
if you are a visitor that has been assigned to a particular segment.
Depending on the segments that you select, |acquia-product:alt| displays
the content that is targeted to the corresponding audiences. For
example, if you select the segment ``first-time-visitor`` and you have
configured a content variation that displays a pop-up registration
window to the audience ``first-time visitors``, |acquia-product:cha|
will display this pop-up window.

You can add or remove any segment that you have configured in
|acquia-product:alw|.

|lift-inspector-site-preview.png|

Adding segments
^^^^^^^^^^^^^^^

To add segments for debugging, complete the following steps:

#. If you are currently previewing your website as a visitor in selected
   segments, click **Stop Preview**.
#. On the **Site Preview** tab, click **Enter a segment**.
   |acquia-product:cha| displays a list of available segments.
#. Click the segment that you want to add, and then click **Add**.
#. To add additional segments, repeat the previous two steps.

To preview your website as it will now appear to the selected segments,
be sure to click **Start Preview**, and then refresh the webpage.

Removing segments
^^^^^^^^^^^^^^^^^

To remove a segment, complete the following steps:

#. If you are currently previewing your website as a visitor in selected
   segments, click **Stop Preview**.
#. Click the X icon |lift-inspector-x.png| for the segment that you want
   to remove.

To preview your website as it will now appear to the selected segments,
be sure to click **Start Preview**, and then refresh the webpage.

For more information about creating and managing segments, see `Creating
and managing segments </lift/drupal/web/segment>`__.

.. _event:

Event Log tab
~~~~~~~~~~~~~

|lift-inspector-errorlog.png|

To display several different kinds of log messages that come from
|acquia-product:alt| or |acquia-product:alw|, click the **Event Log**
tab.

 

The following logs, based on their **Type** column value, are available
for review:

-  **Lift Web**

   -  **Information logs** - These logs are marked with an information
      icon |lift-inspector-info.png| and display the segments you are
      put into as you navigate your website. Lift Inspector saves logs
      from previous webpages you have visited, so that you can see how
      your segments change as you move through your website.

-  **Drupal**

   -  **Error logs** - These log messages are marked with an error icon
      |error.png| and detail ways in which your personalizations are not
      functioning properly.
   -  **Warning logs** - These log messages are marked with a warning
      icon |lift-inspector-warning.png| and identify outdated goals and
      personalizations. For example, if you update your website and
      remove a component that was included in a personalization, but
      that personalization is still running, the log displays an error
      message such as
      ``No DOM element for the following selector in the chrome personalization: "#node-3 img"``
      where ``DOM element`` is the component that was removed,
      ``chrome`` is the name of the personalization, and ``#node-3 img``
      is the selector that is used to identify the component.
   -  **Information logs** - These log messages are marked with an
      information icon |lift-inspector-info.png| and allow you to see
      what personalization groups you qualify for as you browse your
      website. The logs also display what goals are being met — for
      example, if you click on a picture of a cat, and you have defined
      that visitor action as a goal, the log lists that goal as having
      been sent to the |acquia-product:alw| service.

Advanced

Logs of the **Developer** type display debugging information that can be
helpful to website developers. For example, if a personalization
requests that the decision engine pick a variation from the set to
display, this information will be displayed as a developer log message.

The log messages can be filtered based on their **Severity** (available
options are **Error**, **Warning**, and **Info**) and their **Type**
(**Drupal**, **Lift Web**, or **Developer**).

Minimizing and closing the Inspector
------------------------------------

To minimize the menu bar, click the down arrow icon
|lift-inspector-down-arrow.png|.

To close the |acquia-product:cha| Inspector, click its X icon
|lift-inspector-bar-x.png|. After you close the Inspector, you will have
to `re-enable it in your browser </lift/drupal/inspector>`__ to use it.

.. |Up arrow| image:: https://cdn2.webdamdb.com/1280_EFFjBkXOZ21.png?1526475656
   :class: inline-img
.. |lift-inspector.png| image:: https://cdn4.webdamdb.com/1280_dHftjXvEhT21.png?1526475832
   :width: 590px
   :height: 228px
.. |lift-inspector-site-preview.png| image:: https://cdn4.webdamdb.com/1280_6vpMLBakZEq8.png?1526476033
   :width: 590px
   :height: 102px
.. |lift-inspector-x.png| image:: https://cdn4.webdamdb.com/1280_MWeO0rEFLF51.png?1526475662
   :class: inline-img
   :width: 14px
   :height: 13px
.. |lift-inspector-errorlog.png| image:: https://cdn3.webdamdb.com/1280_MytDPf2aJfc5.png?1526476016
   :width: 590px
   :height: 160px
.. |lift-inspector-info.png| image:: https://cdn2.webdamdb.com/1280_hGPVqaB7is91.png?1526476012
   :class: inline-img
   :width: 18px
   :height: 18px
.. |error.png| image:: https://cdn3.webdamdb.com/1280_wrTOxnMlih91.png?1526476097
   :class: inline-img
   :width: 16px
   :height: 16px
.. |lift-inspector-warning.png| image:: https://cdn3.webdamdb.com/1280_oU67c0M3Un36.png?1526475922
   :class: inline-img
   :width: 18px
   :height: 18px
.. |lift-inspector-down-arrow.png| image:: https://cdn3.webdamdb.com/1280_ojeysSGd95Z5.png?1526475664
   :class: inline-img
   :width: 27px
   :height: 27px
.. |lift-inspector-bar-x.png| image:: https://cdn4.webdamdb.com/1280_cY85sEudUDI7.png?1526475866
   :class: inline-img
   :width: 26px
   :height: 24px
