.. include:: /common/global.rst

Creating and configuring content recommendations
================================================

*Content recommendation rules* in |acquia-product:cha| allow you to
create dynamic personalized experiences without significant manual
intervention, based on criteria that you specify.

Recommendations allow you to create a rule once, and then configure the
number of items that you want the rule to return. Instead of returning a
specific result, your recommendations will return either the most
recent, or most popular, content that matches your filters.

Creating a content recommendation
---------------------------------

To create a content recommendation, complete the following steps:

#. `Sign in </lift/exp-builder/access>`__ to the |acquia-product:leb|
   interface.
#. Identify a content slot for which you want to create a content
   recommendation.
#. `Create and save a filter for content </lift/exp-builder/rule/filters>`__.
#. After you save the filter, in the |acquia-product:leb| sidebar, click
   **Create**.

   |Create link|

#. In the **Content** tab, click **Saved Filters**.
#. Identify your desired filter that contains the content that you want
   to feature in the slot.
#. Select the filter, drag it to your desired slot, and then drop it
   into the desired slot.
#. Dismiss the notification that the rule has been created.

Your newly-created recommendation will display a single piece of
content, and will recommend the most recent piece of content matching
your filter. You will next need to configure the content recommendation.

Configuring a content recommendation
------------------------------------

By configuring a recommendation rule after creating it, you can alter
what content is displayed, the manner the content is displayed, and the
audience to whom it is displayed. To configure a recommendation rule,
perform the following steps:

#. `Sign in </lift/exp-builder/access>`__ to the |acquia-product:leb|
   interface.
#. Expand your |acquia-product:leb| sidebar.
#. Click the **Rules** tab.
#. Identify the recommendation rule that you want to modify.
   Recommendation rules are marked with the following icon:
   |Recommendations icon|
#. Click the three dots icon |Three dots icon| for your desired rule.
#. Click **Configure** to expand the rule, which provides additional
   information about the rule.
#. Click the **Settings** tab for your desired rule to display the
   following configuration options:

   |Rule settings|

   -  **Rule Name** - The name of the recommendation rule; by default,
      the rule name assumes the name of the saved filter
   -  **Segment** - The segment targeted by the recommendation rule
   -  **Algorithm** - The primary recommendation method
      |acquia-product:cha| used to determine which piece of content gets
      recommended to a user — by default, the *Most recently published
      content* and *Most viewed content* methods are included
   -  **Content Layout** - The view mode used to display the content
   -  **Number of content items** - The number of content items
      |acquia-product:cha| should return; set to 1 by default
   -  **Exclude Previously Viewed Content** - If set to *Yes*,
      |acquia-product:cha| will not display content that this visitor
      has previously been served

      .. note::  

         *Viewed content* is defined as content items which have a
         registered Content View event in |acquia-product:cha|. This
         functionality will not filter out content which has been shown to
         a user in a decision.

#. Click **Save** to save your unpublished changes.

To publish the recommendation live on your site, click the three dots
icon |Three dots icon| again in the **Rules** in your desired rule, and
then click **Publish**.

Recommendation fallbacks
~~~~~~~~~~~~~~~~~~~~~~~~

For those occasions when the number of items returned is fewer than your
website's design expects, it is important to build fallbacks for your
recommendation rules. Some examples of why fallbacks are necessary to
ensure your website's design appears as designed include the following:

-  **Missing content** - No content is returned, leaving your slot empty
-  **Incomplete content** - Fewer items than expected are returned,
   leaving your slot partially filled

Acquia recommends that you create a second rule that fetches a result
that excludes the items returned in the first rule, and then appending
the results of this second rule to your initial rule. Following this
recommendation ensures that your display always contains the number of
items that you expect.

.. |Create link| image:: https://cdn3.webdamdb.com/1280_s4eaMwVIn576.png?1526475537
   :width: 414px
   :height: 158px
.. |Recommendations icon| image:: https://cdn2.webdamdb.com/1280_AeU8y5qA0f80.png?1526475753
   :class: no-sb
   :width: 13px
   :height: 13px
.. |Three dots icon| image:: https://cdn4.webdamdb.com/1280_EeEOFHy0b649.png?1526476158
   :width: 20px
   :height: 24px
.. |Rule settings| image:: https://cdn3.webdamdb.com/1280_EzONsytb0D06.png?1526475815
   :width: 386px
   :height: 646px
