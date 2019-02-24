.. include:: /common/global.rst

Creating and managing segments
==============================

.. toctree::
   :hidden:
   :glob:

   /lift/profile-mgr/segment/*

If you can identify and organize all of your website's different
visitors based on factors that include their persona, the content that
they prefer the most, and visitor actions that they have taken in the
past, your marketing can be much more effective. With this information,
you can personalize their experience on your website and track the
results of that personalization, all while continuing to make
incremental improvements. To do this, |acquia-product:cha| uses
segments.

A *segment* is an organizational unit that describes one or more
attributes that you want to track in |acquia-product:cha|. Assuming that
your visitors meet a segment's criteria, visitors can be assigned to one
or more segments. |acquia-product:cha| continuously evaluates your
segments' membership lists based on visitors' behavior.

If you use |acquia-product:leb|, the ID of each segment that you create
is also displayed.

.. container:: message-status

   |Learning Services logo|\ or a step-by-step video tutorial introducing you 
   to personalization with |acquia-product:cha|, including creating segments, 
   see |tutorial|_.


.. |Learning Services logo| image:: https://cdn3.webdamdb.com/1280_w1WjsvuWixS1.png?-62169955200
   :class: no-sb float-left logo-sm-lift
   :width: 36px

.. |tutorial| replace:: Creating Personalized Experiences with \ |acquia-product:cha|\ 
.. _tutorial: https://customers.acquiacademy.com

Managing your segments
----------------------

To manage your segments, or to make any changes to your available
segments, `sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
interface, and then click the
**Segments** tab.

|Lift segments display|

The Segments page contains options for the following actions that you
can take with the available segments:

-  *Display* - To view a list of your segments, enter your search
   criteria in the **Find segments** field (leave blank to display all
   segments), and then click **Find**.
-  *Edit* - To modify or edit a segment, find the segment in the list of
   displayed segments, and then click its **Name**. The page reloads
   with the segment's configuration information. If you make any changes
   to the segment, click **Save** to save your changes.
-  *Delete* - To permanently remove a segment, find the segment in the
   list of displayed segments, and then click its **Delete** link.
-  *Clone* - To make a copy of a segment, find the segment that you want
   to copy in the list of displayed segments, and then click its
   **Clone** link.


Adding new segments
-------------------

To create a new segment, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface as an administrator, and
   then click the **Segments** tab.
#. Click the **Add new segment** link.
#. Enter values in the following fields for the new segment:

   -  **Name** - Name of the segment as displayed in the
      |acquia-product:lpm| Admin.
   -  **Segment ID** - Optional name of the segment when displayed as a
      context in the |acquia-product:alt| modules. By default, it will
      create an ID based on the **Name**. Click **Edit Segment ID** to
      set a custom ID.
   -  **Description** - Additional descriptive information about the
      segment, such as a narrative of its criteria.

#. Select the **Apply segment to all customer sites** check box to use
   this segment across all your websites. To apply this segment to
   specific customer sites, complete the following steps:

   a. Clear the **Apply segment to all customer sites** check box.
      |acquia-product:lpm| displays a list of your customer sites.
   b. Click a customer site to which you want to apply this segment.
   c. Click **Add**. |acquia-product:lpm| displays a list containing the
      following information:

      -  **Name** - The name of your customer site as displayed in the
         web browser
      -  **External ID** - The name you specified when you created this
         customer site in |acquia-product:lpm|
      -  **URL** - The web address of your customer site
      -  **Actions** - Additional steps you can take regarding this
         customer site's use of this segment, including removing this
         customer site from the list of customer sites to which the
         segment will apply

   d. To add more customer websites that will use this segment, click
      their names in the list of your customer websites.
      |acquia-product:lpm| displays the new customer website in the list
      of websites to which this segment will apply.
   e. Click the **Delete** link to remove this website from the list of
      customer sites to which this segment will apply.

#. In the **Segment criteria** section, use the initial drop-down list
   to set the relationship between each of the criteria you select for
   the segment. |Adding criteria to segments|

   Select from the following values:

   -  **All** - The segment will display only those people that meet all
      of the defined criteria. (AND operator)
   -  **Any** - The segment will display those people that meet any of
      the defined criteria. (OR operator)
   -  **None** - The segment will display those people that do not meet
      any of the defined criteria. (NOT operator)

#. Click in the field that contains the value **Edit Criteria** to add
   the segment's first attribute.

   |acquia-product:lpm| displays a dialog box that you can use to enter
   information about the criteria item.

   .. note::  

      For more information about criteria items, including the types of
      criteria available, see `Default segment
      criteria </lift/profile-mgr/segment/category>`__.

#. In the **Category name** list, click the category of the criteria
   that you want to use. The fields in the dialog box will change
   depending on the criteria that you select.
#. Enter the remaining values for the criteria item, and then click
   **OK**.
#. To add additional criteria items, click the plus ( **+** ) icon for
   each criteria item, and refer to the previous steps.

   You can also define relationships for sub criteria in a single
   criteria item by clicking the right arrow ( **>** ) to the right of
   the plus icon. This adds a new criteria with its own sub criteria and
   relationships.

#. To delete criteria items, click the minus ( **-** ) icon next to the
   criteria item you want to remove.

Using a where clause to refine your segment criteria
----------------------------------------------------

Using a *where clause* helps you define very specific segments. For
example, in a particular segment, you add an event count specifying that
if a website visitor views two pieces of content on your website in the
past 30 days, the visitor enters that segment. To further narrow the
focus of this segment, you specify that in order to enter this segment,
the content viewed by the visitor in that time period must be in either
the astrology or the sports section of your website. To create this
segment and its where clause, complete the following steps:

`Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
interface as an administrator, and then
click the **Segments** tab.

Follow steps 1 through 4 in `Adding new segments <#adding>`__.

In the **Segment criteria** section, in the initial drop-down list,
select **All**. The segment will display only those website visitors
that meet all of the defined criteria. (AND operator)

Click the field that contains the value **Edit Criteria**.
|acquia-product:lpm| displays a dialog box. To add the segment's first
attribute, complete the following steps:

a. Click **Event**.
b. Click **Event Count**. |acquia-product:lpm| displays more fields.
c. In the **Customer Site** list, click the customer site to which you
   want this segment to apply.
d. In the **Event Name** list, click **Content View**.
e. In the **Operators** field, keep the default value of **=**.
f. In the **Values** field, enter ``2``.
g. In the Time Period field, click **Past 30 Days**.
h. Click **OK**. |acquia-product:lpm| displays the segment attribute on
   **Segments > Segment Detail**.

You have now added the segment's first attribute, which states that the
segment will contain all website visitors who viewed two pieces of
content on your specified customer site in 30 days. To add the where
clause to this segment, complete the following steps:

#. Click **Sub-criteria**.
#. In the initial list, keep the default value of **All**.
#. Click the field that contains the value **Edit Criteria**.
   |acquia-product:lpm| displays a dialog box. To add the segment's
   where clause, complete the following steps:

   a. In **Category name**, click **Select Criteria**.
      |acquia-product:lpm| displays a list.
   b. Click **Page Content**. |acquia-product:lpm| displays another
      list.
   c. Click **Content Section**.
   d. In **Operators**, keep the default value of **Matches One**.
   e. In the Values field, enter ``astrology`` and ``sports``. These are
      the content sections in which the visitor must have viewed content
      in the past 30 days in order to be included in this segment.
   f. Click **OK**. |acquia-product:lpm| displays the segment and its
      new where clause.
   g. Click **Save** to save this segment.

You have now created a segment that includes website visitors who viewed
two pieces of content in the past 30 days **where** the value **Content
Section** matches one of these sections: astrology or sports.

Evaluating your segment's reach
-------------------------------

Either during the creation of your segment or after it has already been
saved, you can use |acquia-product:lpm| to determine how effectively the
segment connects with your visitors (also known as its *reach*).

This can be helpful in several circumstances — for example, if you
create a segment that is too specific based on your visitors, it may
never apply to any visitor interactions. In this case,
|acquia-product:lpm| would indicate zero interactions for each of the
items that the |acquia-product:cha| service tracks as compared to the
total number of tracked interactions.

To examine your segment's potential or current reach, complete the
following steps:

|lift-segment-estimates.png|

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface as an administrator, and
   then click the **Segments** tab.
#. Complete the following step based on your requirements:

   -  *If you want to review a previously created segment*, click the
      name of the segment that you want to review from the list of
      available segments.
   -  *If you haven't yet created your segment*, complete the steps in
      the `Adding new segments <#adding>`__ section of this page, but do
      not yet save your segment.

#. Scroll down the page to the **Size estimation** section, which allows
   you to review the segment's performance against the data stored in
   the |acquia-product:cha| service across three areas of information
   (displayed as **Groupings** in the table):

   -  **Person** - Visitors that have been uniquely identified with
      first-party cookies, their email addresses, or some other
      identifier.
   -  **Touch** - A series of contiguous events (such as content views)
      with a duration between events of no more than 30 minutes.

      .. note::  

         |acquia-product:cha| only loads the most recent 100 touches for
         analysis. This prevents performance problems due to large
         profiles, and ensures current patterns are targeted. This should
         generally affect only content creators or administrators, who
         spend the most time on a website.

   -  **Event** - Discrete visitor actions, such as a content view of an
      article or a click-through on a subscription offer.

#. In the **Date range** list, click one of the following options based
   on the timeframe of your segment's comparison against data stored by
   the |acquia-product:cha| service:

   -  **Last 7 Days**
   -  **Last 30 Days**

#. Click **Show results**.

After a few moments of collecting information from the
|acquia-product:cha| service, |acquia-product:lpm| will display your
segment's performance against each of the groupings. Each of the
time-based columns in the table (**Daily**, **Weekly**, and **Monthly**)
have an **Estimate** and a **Total**. Based on the selected **Date
range**, the *estimate* is the number of items in the grouping that
apply to the segment, and the *total* is the total number of items for
that grouping as collected by the service.

The final column of the table is **% Total**, and it represents the
estimate versus the total for the grouping row. A total of 100.00%
indicates that the segment applies to all items collected by the
service, and may not be specific enough. A total of 0.00% indicates that
the segment does not apply to any items for the selected date range, and
may be too specific.

.. note::  

   If you are evaluating your new segment's reach as part of the creation
   process, be sure to save your segment at the end of this process.

Verifying segments
------------------

To verify if |acquia-product:lpm| is returning segments, visit a webpage
that you are tracking with |acquia-product:cha|, and use one of these
methods:

-  Activate the |acquia-product:leb| bookmarklet, and look in the
   **Segment** field. If your segment is available, it should be there.
-  Open your browser's debugger console:

   -  If you are using |acquia-product:cha| for Drupal 8, in the
      console's search field, enter ``decide?`` to filter the list of
      displayed results. Click the **Response** tab. If this request
      returns one or more segments, they are displayed here as part of
      the response, such as:

      .. code-block:: none

            "segments":[
            {"id":"visitors_50_years_in_age","name":"Visitors 50+ years in age","description":"Visitors 50+ years in age"}
            ,
            {"id":"first_time_visitors","name":"First time visitors","description":"First time visitors"}
            ],

   -  If you're using an older version of |acquia-product:cha|, click
      the **Network** tab. In the console's search field, enter
      ``tcaction`` to filter the list of displayed results. Click the
      **Response** tab. If this request returns one or more segments,
      they are displayed here, preceded by ``segments``.


.. |Lift segments display| image:: https://cdn3.webdamdb.com/1280_glPK3Oqi981.png?1526476093
   :width: 895px
   :height: 339px
.. |Adding criteria to segments| image:: https://cdn2.webdamdb.com/1280_Ij2f80OAL0u2.png?1526475777
   :width: 859px
   :height: 270px
.. |lift-segment-estimates.png| image:: https://cdn2.webdamdb.com/1280_Mzgfb8mXa53.png?1526475920
   :width: 882px
   :height: 417px
