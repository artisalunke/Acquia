.. include:: /common/global.rst

Creating segments with Marketo activity data
============================================

Using Marketo activity data to create
`segments </lift/profile-mgr/segment>`__ allows you to expand your
ability to target website content to your visitors. These segments can
gather data based on the activities your website visitors perform.

.. container:: internal-navigation

   **Marketo connector**

   * :doc:`Intro </lift/connectors/marketo>`
   * :doc:`Config </lift/connectors/marketo/config>`
   * :doc:`Segments </lift/connectors/marketo/segments>`

|lift-web-marketo-segment-activity.png|

As an example, you want to show a particular piece of content to
visitors who have clicked on a Marketo email with a mailing ID of
``[SomeMailingID]`` at least once in the past 30 days. To create a
segment for these visitors, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface as an administrator, and
   then click the **Admin** tab.
#. Configure your Marketo connector to map the Marketo **Click Email**
   activity and its **Mailing ID** attribute to **custom_field_10** in
   the Event table. For more information about how to do so, see the
   `Adding activity mappings </lift/connectors/marketo/config>`__
   section in `Configuring the Marketo connector </lift/connectors/marketo/config>`__ in
   |acquia-product:lpm|.
#. Click the **Segments** tab.
#. Click the **Add new segment** link.
#. Enter values in the following fields for the new segment:

   -  **Name** - Name of the segment as displayed in the
      |acquia-product:lpm| Admin
   -  **ID** - Name of the segment when displayed as a context in the
      |acquia-product:alt| Drupal modules
   -  **Description** - Additional descriptive information about the
      segment, such as a narrative of its criteria

#. Select the **Apply segment to all customer sites** check box to use
   this segment across all your websites.

   To apply this segment to specific customer sites, complete the
   following steps:

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
   the segment. Select from the following values:

   -  **All** - The segment will display only those people that meet all
      of the defined criteria. (AND operator)
   -  **Any** - The segment will display those people that meet any of
      the defined criteria. (OR operator)
   -  **None** - The segment will display those people that do not meet
      any of the defined criteria. (NOT operator)

#. Click in the field that contains the value **Edit Criteria**.
   |acquia-product:lpm| displays a dialog box. To add segment criteria,
   complete the following steps:

   a. In the **Category Name** list, click **Event**.
   b. Click **Event Count**. |acquia-product:lpm| displays more fields.
   c. In the **Customer Site** list, click the customer site to which
      you want this segment to apply.
   d. In the **Event Name** list, click ``marketo_click_email``.
   e. In the **Operators** field, select **>=**.
   f. In the Values field, enter **1**.
   g. In the **Time Period** field, click **Past 30 Days**.
   h. Click **OK**. |acquia-product:lpm| displays the segment attribute
      on **Segments > Segment Detail**.

   You have now added the segment's first attribute, which states that
   the segment will contain all website visitors who clicked on a
   Marketo email at least once in the past 30 days. To add the mailing
   ID of ``[SomeMailingID]``, complete the following steps:

   #. Click **Sub-criteria**.
   #. In the initial list, keep the default value of **All**.
   #. Click the field that contains the value **Edit Criteria**.
      |acquia-product:lpm| displays a dialog box. To add the segment's
      mailing ID, complete the following steps:

      a. In **Category name**, click **Select Criteria**.
         |acquia-product:lpm| displays a list.
      b. Click **Marketo**. |acquia-product:lpm| displays another list.
      c. Click **Mailing ID**.
      d. In **Operators**, keep the default value of **Matches One**.
      e. In the **Values** field, enter ``[SomeMailingID]`` where
         ``[SomeMailingID]`` is the mailing ID of the email the visitor
         must have clicked at least once in the past 30 days in order to
         be included in this segment.
      f. Click **OK**. |acquia-product:lpm| displays the segment and its
         new subcriteria.
      g. Click **Save** to save this segment.

You have now created a segment using Marketo activity data. You can use
this segment to track your website visitors' behavior. You can also add
this segment to a
`personalization </lift/drupal/creating-personalizations>`__ in
|acquia-product:alt|. For more information about how to do so, see the
`Creating a target audience </lift/drupal/who>`__ section in
`Configuring the Who tab </lift/drupal/who>`__.

.. |lift-web-marketo-segment-activity.png| image:: https://cdn4.webdamdb.com/1280_fOLSrwMaE921.png?1526476059
   :width: 590px
   :height: 362px
