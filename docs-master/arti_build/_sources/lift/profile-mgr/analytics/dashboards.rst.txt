.. include:: /common/global.rst

Using reports and dashboards in |acquia-product:lpm|
====================================================

.. toctree::
   :hidden:
   :glob:

   /lift/profile-mgr/analytics/dashboards/*

.. container:: internal-navigation

   **Using reports dashboards in Profile Manager**

   * Intro
   * :doc:`Overview </lift/profile-mgr/analytics/dashboards/operational>`
   * :doc:`Details </lift/profile-mgr/analytics/dashboards/details>`
   * :doc:`Config </lift/profile-mgr/analytics/dashboards/config>`
   * :doc:`Custom </lift/profile-mgr/analytics/dashboards/custom>`
   * :doc:`Fields </lift/profile-mgr/analytics/dashboards/custom/fields>`

|Analytics tab|

|acquia-product:lpm| provides a set of pre-built reports and
visualizations that allow you to gain insights about visitors' behavior
and actions on your websites, and optionally across other channels.
These reports can be filtered to display data for different customer
websites and different time periods. In certain cases, you can add
additional filters based on specific event names of interest or other
criteria.

Viewing the available reports
-----------------------------

To view these reports, click the **Analytics** tab on any webpage in the
|acquia-product:lpm| interface.

|acquia-product:lpm| includes both reports that provide an overview of
how your visitors are interacting with your websites, and reports that
provide a fine-level of detail based on specific attributes of their
interactions. By default, |acquia-product:lpm| displays the reports that
each section contains. To hide a section's reports, click the name of
the section.

The following reports and visualizations are available for your use:

Overview report
~~~~~~~~~~~~~~~
 
-  `Operational dashboard </lift/profile-mgr/analytics/dashboards/operational>`__ –
   Displays dashboard-style summaries that consolidate reports and
   visualizations into a single at-a-glance view

Detailed reports
~~~~~~~~~~~~~~~~

-  `Content </lift/profile-mgr/analytics/dashboards/details>`__ –
   Contains reports displaying content-related data, such as number of
   views of a certain content type
-  `Conversion </lift/profile-mgr/analytics/dashboards/details>`__ –
   Contains the **Offers and recommendations campaign summary** report,
   which displays campaign actions and click-throughs from the previous
   90 days
-  `Engagement </lift/profile-mgr/analytics/dashboards/details>`__ –
   Lists reports that display data relating to engagement scores, the
   number of page views over certain periods of time, and the amount of
   time a customer spends on your website or websites
-  `Events </lift/profile-mgr/analytics/dashboards/details>`__ –
   Contains reports displaying data related to the frequency of unique
   events on your website or other channels
-  `People </lift/profile-mgr/analytics/dashboards/details>`__ –
   Lists reports containing data relating to the different ways
   |acquia-product:cha| tracks visitors to your website or other
   channels. For example, the People by identifier type report displays
   the number of visitors captured in |acquia-product:cha| over the past
   30 days, organized by identifier types such as email address and
   Facebook ID.
-  `Segment </lift/profile-mgr/analytics/dashboards/details>`__ –
   Contains reports displaying data related to the segments into which
   your visitors fell when visiting your website
-  `Touches </lift/profile-mgr/analytics/dashboards/details>`__ –
   Contains reports consisting of data relating to the touches
   associated with visitors in |acquia-product:cha|. A touch is a series
   of contiguous views with a duration between events of no more than 30
   minutes.

Downloading report data
-----------------------

|acquia-product:lpm| allows you to download and save data from each of
the available reports. To download data from an individual report,
complete the following steps:

#. Click the cog icon |cog icon| at the top right of the report you want
   to download.
#. Click **Download data** to display a dialog box that contains the
   following configurable options for your download file:

   -  **File format** – Available file formats for the download file
   -  **Values**

      -  **Unformatted** – Save the download file in a plain text format
      -  **Formatted** – Save the download file using the file format
         that you previously selected

   -  **Limit**

      -  **Results in table** – Limit the downloaded report data to what
         is currently displayed in the table
      -  **Custom** – Selecting this option displays the **Row** field,
         into which you can enter a limit for the amount of exported
         rows, starting from the beginning of the table (default value
         is ``5000``).

   -  **Filename** – The default filename for your download file, which
      you can modify

#. Click either **Open in browser** to open the download file as a
   webpage in your browser, or **Download** to export the download file
   to your computer.

Getting help
------------

In the **Operational** dashboard, to display help text for a displayed
report, click the speech bubble icon |speech bubble icon| located to the
bottom left of the report. You can also display a description of each
report by pointing to its name in the sidebar.

.. |Analytics tab| image:: https://cdn4.webdamdb.com/1280_PaM5ExKuap02.png?1526475825
   :width: 590px
   :height: 302px
.. |cog icon| image:: https://cdn4.webdamdb.com/1280_IMXGnBrNLtv6.png?1526475505
   :class: no-sb inline-img
   :width: 25px
   :height: 25px
.. |speech bubble icon| image:: https://cdn2.webdamdb.com/1280_U35h0vf4wIq3.png?1526475647
   :class: no-sb inline-img
   :width: 24px
   :height: 23px
