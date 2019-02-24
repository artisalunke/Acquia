.. include:: /common/global.rst

Creating segments with Marketo lead data
========================================

.. container:: internal-navigation

   **Marketo connector**

   * Intro
   * :doc:`Config </lift/connectors/marketo/config>`
   * :doc:`Segments </lift/connectors/marketo/segments>`


You can use Marketo lead data to create
`segments </lift/profile-mgr/segment>`__. These enable you to follow a
lead through your website.

|lift-web-marketo-segment-lead.png|

To show a particular piece of content to visitors with the job title of
Senior Developer, complete the following steps:

#. Configure your Marketo connector to map the Marketo **Job Title**
   lead to **custom_field_11** in the Person table. For more information
   about how to do so, see the `Adding lead
   mappings </lift/connectors/marketo/config>`__ section in `Configuring
   the Marketo connector </lift/connectors/marketo/config>`__ in
   |acquia-product:lpm|.
#. Configure **custom_field_11** to be usable for segmentation by giving
   it the name ``Job Title`` and placing it in the category ``Marketo``.
   For more information about how to do so, see `Configuring column meta
   data fields for use in
   segments </lift/connectors/marketo/segments#mapping>`__.
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

   a. In the **Category Name** list, click **Marketo**.
      |acquia-product:lpm| displays an additional list.
   b. Click **Job Title**.
   c. In the **Operators** field, select **=**.
   d. In the Values field, enter **Senior Developer**.
   e. Click **OK**. |acquia-product:lpm| displays the segment attribute
      on **Segments > Segment Detail**.
   f. Click **Save** to save this segment.

.. |lift-web-marketo-segment-lead.png| image:: https://cdn4.webdamdb.com/1280_sXrVZbLdxsZ4.png?1526476054
   :width: 590px
   :height: 433px
