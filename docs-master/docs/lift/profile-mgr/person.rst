.. include:: /common/global.rst

Examining visitor information
=============================

.. toctree::
   :hidden:
   :glob:

   /lift/profile-mgr/person/*

.. container:: internal-navigation

   **Profile Manager person detail**

   * Intro
   * :doc:`Summary </lift/profile-mgr/person/profile>`
   * :doc:`Insights </lift/profile-mgr/person/insights>`
   * :doc:`Activity </lift/profile-mgr/person/activity>`
   * :doc:`Details </lift/profile-mgr/person/profile-details>`

Although you can learn a lot about your website's visitors as a group,
there are times when it is helpful to focus on an individual and their
specific behavior. Using |acquia-product:lpm|, you can obtain a detailed
summary of visitors' behavior and interests, including when they
accessed different websites on which you are operating
|acquia-product:cha|.

Searching for a visitor
-----------------------

By default, the People tab displays a list of visitors who accessed your
website or websites in the last 30 days.

To perform a search for a particular visitor or visitors, complete the
following steps:

#. In the **Match Criteria** list, select from the following values to
   perform a search for an exact or partial match against any of the
   `identifiers </lift/profile-mgr/admin/customer>`__ that
   |acquia-product:cha| associates with a visitor:

   -  **Exact Match** - This will limit your search results to the exact
      value you enter in the **Find People** field. For example, this
      option matches a search for ``JohnSmith`` with the visitor saved
      as *JohnSmith*.
   -  **Begins With** - This will limit your search to results that
      begin with the value you enter in the **Find People** field. For
      example, using this option when searching for ``John`` would
      display visitors saved as *JohnSmith* and *JohnBrown*.
   -  **Ends With** - This will limit your search to results that end
      with the value you enter in the **Find People** field. For
      example, using this option when searching for ``Smith`` would
      display visitors saved as *JohnSmith* and *JaneSmith*.

#. In the **Find People** field, enter your search criteria for the
   visitors that you want to display (leave blank to display all
   visitors).
#. Click **Find**.

|acquia-product:lpm| displays a list of the visitors that meet the
search criteria, along with each visitor's primary
`identifier </lift/profile-mgr/admin/customer>`__ and the first and last
times that visitor's information was modified.

|People summary|


Inspecting visitors' information
--------------------------------

To view detailed information for a visitor, click the visitor's tracking
ID.

|lift-web-visitor-summary.png|

The webpage displays several sections containing information about the
visitor's activities and engagement with your content:

-  `Profile summary </lift/profile-mgr/person/profile>`__ - Lists
   identifying information including the visitor's tracking ID, status
   as an anonymous or identified user, and engagement score
-  `Insights tab </lift/profile-mgr/person/insights>`__ - Contains
   information about what types of website content the visitor has
   viewed most often and what platform the visitor used to view content
-  `Activity tab </lift/profile-mgr/person/activity>`__ - Details
   the visitor's touches, including information about when the visitor
   made a touch and the combined engagement score for all events within
   that touch
-  `Profile Details
   tab </lift/profile-mgr/person/profile-details>`__ - Contains more
   information about the visitor's interaction with your website,
   including whether they are accessing your website for the first time
   and whether they have asked not to be tracked

.. |People summary| image:: https://cdn2.webdamdb.com/1280_wd53SxcTih01.png?1527080571
   :width: 1020px
   :height: 379px
.. |lift-web-visitor-summary.png| image:: https://cdn3.webdamdb.com/1280_EXufW4Hy2dO2.png?1527080587
   :width: 750px
   :height: 549px
