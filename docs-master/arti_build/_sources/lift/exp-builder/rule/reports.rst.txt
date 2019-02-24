.. include:: /common/global.rst

Rule reports
============

Rule reports help you understand `how your
rules </lift/exp-builder/rule>`__ are performing and can provide
valuable insight into how your users are spending time on your website.
Many of these reports are similar to `previous versions </lift/drupal/reports>`__ of
|acquia-product:cha|. These reports are now
part of the *rule card*. A rule card is the white, rectangular box that
contains all of the information for a rule.

To access rule reports on a rule card, click the three vertical dots and
then click **Reports**.

Types of reports
----------------

There are two types of reports to help you determine how and where your
users are using your website. They are based on whether you are
`targeting </lift/drupal/personalization-types>`__ your content
to a particular group, or if you are using A/B
`testing </lift/drupal/personalization-types>`__.

-  **Targeting** - Targeting reports show data for rules with only a
   single piece of content. They show the performance of the single
   content variation for the rule’s associated goals. There is no
   comparison between different content variations.
-  **Testing** - Testing reports show performance data for rules with
   multiple content items or A/B tests. Additional metrics applicable to
   tests will be shown, such as a **Winner** variant.


Rule report sections
--------------------

Rules reports are divided into three sections, which are the same for
both types of reports. The reports contain various reporting metrics,
which vary depending on the type of report and tested data:

-  **Goals list** - Allows users to change which goals the data being
   shown in the graph and table apply to. For example, a rule may have
   two goals, such as ``Click-Through`` and ``Purchase``. By default,
   the report displays combined performance data for all goals of a
   rule. Clicking the **Goals** list and selecting a single goal
   displays only the data for that goal.

   |Goals list menu|

-  **Line graph** - Displays the performance of the rule’s content
   variations for the selected goal or goals, which can be filtered by
   date and performance metric:

   -  **Conversion rate %** - Percentage of the selected goal or goals
      met for each display of the variation
   -  **Conversion value** - The average value of the content
      variation's ability to generate completed goals, based on the
      values assigned to the goals. By default, goals have a value of 1
      and can be configured on the |acquia-product:lpm|
      `Goals </lift/profile-mgr/goals>`__ tab.

   |Line graph filters|

-  **Content table** - A list of the rule’s content variations and
   associated data attributes. This defaults to **Times Shown**. Click
   the list to change the data metric.

   |Lift content filter menu|

   The following metrics are used for the content table. Metrics marked
   **Test only** are used only in testing personalizations.

   -  **Times Shown** - Number of times a given piece of content was
      displayed
   -  **Goals met** - Number of times that website visitors completed
      the selected goal or goals after viewing the content variation
   -  **Conversion rate %** - Percentage of the selected goal or goals
      met for each display of the variation
   -  **Chance to beat control (Test only)** - Represents a measure of
      confidence that this content variation will perform better than
      the control. By default, the control is the first content
      variation listed. Technically, this number is 1 minus the
      |p-value|_ of a
      hypothesis test, where the p-value is the probability of seeing
      the difference we have observed.
   -  **Lift (Test only)** - Estimated increase in conversions if this
      content variation were to be shown all the time, versus the
      control
   -  **Winner (Test only)** - The most effective content variation for
      website visitors. By default, the confidence threshold is set to
      95%.


.. |p-value| replace:: *p-value*
.. _p-value: https://en.wikipedia.org/wiki/P-value

.. |Goals list menu| image:: https://cdn4.webdamdb.com/1280_AilBz8T2YRw6.png?1526475762
   :width: 393px
   :height: 211px
.. |Line graph filters| image:: https://cdn3.webdamdb.com/1280_6ipO8RnLjC01.png?1526475464
   :width: 395px
   :height: 244px
.. |Lift content filter menu| image:: https://cdn2.webdamdb.com/1280_gwRYTduaMg40.png?1526475787
   :width: 396px
   :height: 273px
