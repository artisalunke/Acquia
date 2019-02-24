.. include:: /common/global.rst

Create and modify custom reports
================================

.. container:: message-status

   This feature is available only to |acquia-product:lplpo| or 
   |acquia-product:lplp| subscribers. To upgrade your |acquia-product:cha| 
   subscription to this level, contact your Account Manager.

.. container:: internal-navigation

   **Using reports dashboards in Profile Manager**

   * Intro
   * :doc:`Overview </lift/profile-mgr/analytics/dashboards/operational>`
   * :doc:`Details </lift/profile-mgr/analytics/dashboards/details>`
   * :doc:`Config </lift/profile-mgr/analytics/dashboards/config>`
   * :doc:`Custom </lift/profile-mgr/analytics/dashboards/custom>`
   * :doc:`Fields </lift/profile-mgr/analytics/dashboards/custom/fields>`

After confirming you have `the correct
permissions </lift/profile-mgr/analytics/dashboards/custom>`__ to create
reports and learning about the `fields custom reports can
contain </lift/profile-mgr/analytics/dashboards/custom/fields>`__,
you're ready to create and modify your first report.

Creating a report
-----------------

Creating a custom report requires either the *Explore Data* or *Author
reports* `permission </lift/profile-mgr/analytics/dashboards/custom>`__.
To create a new custom report, complete the following steps:

#. To identify the fields suited to your needs, review the `fields that
   custom reports can
   contain </lift/profile-mgr/analytics/dashboards/custom/fields>`__.
#. Sign in to your |acquia-product:lpm| user interface.
#. In the top menu, click **Analytics**.
#. Click **Explore Data**.
#. To identify your desired fields, search for the data using one of the
   following methods:

   -  In the **Profiles** section in the left sidebar, in the **Search**
      field, enter your search criteria.
      |acquia-product:lpm| will display the categories and dimensions
      that match your text.
   -  Click the triangle next to a category to display its dimensions.

#. | Click the name of a dimension to add it to the results canvas.

   |Search for a dimension|

   | |acquia-product:lpm| will display the dimensions you select as
     columns in the **Visualization** section.

   |Visualization example|

#. After adding all of the dimensions that you want to view, click
   **Run**.
   |acquia-product:lpm| will search your website's data warehouse in
   real-time and display its results.
#. Click **Create Report**.
#. Enter values for the following fields:

   -  **Report Name**
   -  **Analytics Category**
   -  **Description**

#. Click **Submit**.

You can access your custom report by clicking the **Analytics Category**
that you selected for your custom report. |acquia-product:lpm| will
display your custom report in your selected category with **Custom
Report** icon |Custom Report|.

|Custom report link example|

Enhancing and extending your report
-----------------------------------

After you have created a report, you can add the following data elements
to better meet your reporting needs:

-  Pivots and filters, to reorganize or summarize data
-  Measures, to perform calculations
-  Visualizations, like charts and graphs

You can also delete dimensions that you no longer need.

Adding pivots and filters
~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to viewing dimensions in your custom report, you can add a
dimension as either a *filter* or a *pivot*. Adding a dimension as a
filter allows you to return only those results that match your filter
criteria. Adding a dimension as a pivot will display each value in the
selected dimension horizontally in your report (instead of vertically),
which may make your report easier to read and understand.

You can add dimensions as filter or pivot criteria (instead of columns
to the results canvas) by performing the following steps:

#. After you search for criteria as previously described in Creating
   custom reports, point to the desired option.
#. Select from the following options, based on your requirements:

   -  **Pivot** - The results canvas will pivot based on that dimension
   -  **Filter** - The desired filter will appear in the **Filters**
      section

      |Filter example|

Adding measures
~~~~~~~~~~~~~~~

In custom reporting, *measures* add an additional column containing a
mathematical calculation, such as a total or average, to your results
canvas. To add a measure to your custom report, perform the following
steps:

#. Search for criteria as described in Creating custom reports.
#. Review the results displayed in yellow text.

   |Measures in search results|

#. Click the desired measure to add it as a column in your results
   canvas. |acquia-product:lpm| displays measures with a tan background.

   |Measures column in search result|

Adding visualizations to your report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After creating a report, you can enhance it with charts and graphs by
building a visualization. For example, the following visualization
displays the relationship between content views, decisions,
click-throughs, and goals.

|Visualization example|

To create and customize a visualization, perform the following steps:

#. Search for criteria as described in Creating custom reports.
#. Click **Visualization**.

   |Visualization accordion|

   |acquia-product:lpm| will display a list of available visualization
   option icons.

   |Visualization bar|

#. Click the icon for the type of your desired visualization type from
   the list:

   -  |Table icon|  **Table**
   -  |Column icon|  **Column**
   -  |Bar icon|  **Bar**
   -  |Scatterplot icon|  **Scatterplot**
   -  |Line icon|  **Line**
   -  |Area icon|  **Area**
   -  |Pie icon|  **Pie**
   -  |Map icon|  **Map**
   -  |Single Value icon|  **Single Value**
   -  |More Options icon|  **More options** - Less frequently-used
      options such as funnel, timeline, static map (regions), static map
      (points), donut multiples, and single record

Deleting a dimension from a report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To remove a dimension when editing a custom report, perform the
following steps:

#. Point to the dimension that you want to delete.
#. Click the dimension's gear icon |Settings icon|.
#. Click **Delete**.

.. _next:

Next steps
----------

After you have created and modified your custom report, you can
`download, edit, or delete your custom
report </lift/profile-mgr/analytics/dashboards/custom/manage>`__.

.. |Search for a dimension| image:: https://cdn3.webdamdb.com/md_s5ywEHu6Ai93.png?1526476166
   :width: 316px
   :height: 284px
.. |Visualization example| image:: https://cdn3.webdamdb.com/1280_wX60TLVYu339.png?1527027638
   :width: 750px
   :height: 200px
.. |Custom Report| image:: https://cdn3.webdamdb.com/100th_sm_QaJdBCV2Bjw7.png?1527028046
   :class: no-sb
.. |Custom report link example| image:: https://cdn3.webdamdb.com/310th_sm_sw2r8L0tH6U0.png?1527027527
   :width: 303px
   :height: 117px
.. |Filter example| image:: https://cdn2.webdamdb.com/1280_Mdq3X5Uq6Ct7.png?1527027510
   :width: 702px
   :height: 156px
.. |Measures in search results| image:: https://cdn3.webdamdb.com/md_ktN4YpT9d01.png?1526476069
   :width: 338px
   :height: 301px
.. |Measures column in search result| image:: https://cdn2.webdamdb.com/md_633MA73Oab51.png?1526476041
   :width: 550px
   :height: 110px
.. |Visualization example| image:: https://cdn2.webdamdb.com/md_QNK8oHw7CRJ2.png?1526475986
   :width: 550px
   :height: 268px
.. |Visualization accordion| image:: https://cdn2.webdamdb.com/md_gehFssVDzvn6.png?1526476047
   :width: 323px
   :height: 163px
.. |Visualization bar| image:: https://cdn2.webdamdb.com/md_2feZyR2ffl33.png?1526475753
   :width: 521px
   :height: 43px
.. |Table icon| image:: https://cdn3.webdamdb.com/100th_sm_AnaEGeQosFg6.png?1526475789
   :width: 20px
   :height: 20px
.. |Column icon| image:: https://cdn2.webdamdb.com/100th_sm_2M72SoLbY11.png?1526475461
   :width: 18px
   :height: 18px
.. |Bar icon| image:: https://cdn3.webdamdb.com/100th_sm_wekY67L691.png?1526476088
   :width: 18px
   :height: 18px
.. |Scatterplot icon| image:: https://cdn3.webdamdb.com/100th_sm_cf7OhAY8t0R2.png?1526476127
   :width: 18px
   :height: 18px
.. |Line icon| image:: https://cdn2.webdamdb.com/100th_sm_EpnkYP6tqC74.png?1526475739
   :width: 18px
   :height: 18px
.. |Area icon| image:: https://cdn4.webdamdb.com/100th_sm_sNT3PP8tCtA7.png?1526475741
   :width: 18px
   :height: 18px
.. |Pie icon| image:: https://cdn3.webdamdb.com/100th_sm_swrkxe17KDG0.png?1526476076
   :width: 18px
   :height: 18px
.. |Map icon| image:: https://cdn4.webdamdb.com/100th_sm_IkETu1nMjKp9.png?1526475625
   :width: 18px
   :height: 18px
.. |Single Value icon| image:: https://cdn2.webdamdb.com/100th_sm_I7JXBOWmXah1.png?1526476067
   :width: 18px
   :height: 18px
.. |More Options icon| image:: https://cdn3.webdamdb.com/100th_sm_opVw0J4OGsF7.png?1526475676
   :width: 20px
   :height: 18px
.. |Settings icon| image:: https://cdn2.webdamdb.com/100th_sm_YaBGvEirLM61.png?1526476110
   :width: 22px
   :height: 22px
