.. include:: /common/global.rst

Configuring report filters in |acquia-product:lpm|
==================================================

.. toctree::
   :hidden:
   :glob:

   /lift/profile-mgr/analytics/dashboards/*

.. container:: internal-navigation

   **Using reports dashboards in Profile Manager**

   * :doc:`Intro </lift/profile-mgr/analytics/dashboards>`
   * :doc:`Overview </lift/profile-mgr/analytics/dashboards/operational>`
   * :doc:`Details </lift/profile-mgr/analytics/dashboards/details>`
   * Config
   * :doc:`Custom </lift/profile-mgr/analytics/dashboards/custom>`
   * :doc:`Fields </lift/profile-mgr/analytics/dashboards/custom/fields>`


Depending on the type of report that you are viewing, you can filter the
data that is displayed in each report by configuring its **Filters**
settings.

|lift-web-analytics-reports-filters.png|

To display a report's filter settings, complete the following steps:

#. Click the down arrow to the right of **Filters**.
#. If you `modify any of these filter settings <#available>`__, the
   color of the **Run** button will change to purple.
#. After you have made all of your filter changes, click **Run**.

The report displays according to the new parameters that you have set.

.. note::  

   - To maintain optimal website performance, reports do not display until
     you click the **Run** button.
   - To ensure reports run quickly, report data is refreshed daily.

Modifying your filters
----------------------

The available filter settings vary by report, and you can modify filter
values based on the directions for each filter type. Different filters
allow you to limit the number of returned customer websites based on
different values. To modify your filter settings, complete the following
steps:

#. In the list of filtering options for the field, click the filter that
   you want to use (for example, **is equal to**).
#. In the empty field to the right of the filtering option list, enter
   the desired value based on the filter:

   -  **Customer Site** - Enter the customer site for which you want to
      search.
   -  **Date** - Enter a number that signifies your selected date range
      or time period.
   -  **Event Name** - Enter the event name for which you want to
      search. Depending on the characters you enter,
      |acquia-product:lpm| automatically suggests website events you can
      select.
   -  **Channel Type** - Enter the channel type for which you want to
      search (for example, ``email`` or ``Marketo``).
   -  **Campaign ID** - Enter the ID of the campaign to which you want
      to limit your search results.
   -  **Segment Name** - Enter the name of the segment to which you want
      to limit your search results. Depending on the characters you
      enter, |acquia-product:lpm| automatically suggests segments for
      you to select.

#. If you entered a value for the **Date** filter, click the appropriate
   unit of time measurement. For example, click **quarters** to limit
   search results to content viewed within a specific three-month
   period.
#. If required, click the plus sign ( **+** ) to create additional
   customer site filters.

Be sure to click **Run** after you create all of your required filters.

.. note::  

   For the **Date** filter, |acquia-product:lpm| displays up to 13 months
   of historical data.

.. |lift-web-analytics-reports-filters.png| image:: https://cdn3.webdamdb.com/1280_bpT8xwB7f71.png?-62169955200
   :width: 590px
   :height: 371px
