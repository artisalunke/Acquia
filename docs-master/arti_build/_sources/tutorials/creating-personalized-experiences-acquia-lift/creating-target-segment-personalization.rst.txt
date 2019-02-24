.. include:: /common/global.rst

Creating a Target Segment for Personalization
=================================================

.. container:: message-status

   Creating Personalized Experiences with |acquia-product:cha| – |Back to intro|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/creating-personalized-experiences-acquia-lift

.. |Next lesson| replace:: Publishing Content to \ |acquia-product:leb|\ 
.. _Next lesson: /tutorials/creating-personalized-experiences-acquia-lift/publishing-content-experience-builder


Lesson Goal
-----------

.. container:: message-status

   Create a categorization to enable content that targets returning visitors in the Boston area.

In this lesson, we will learn how to create a segment of our visitors so
we can serve them personalized content.

Segments are used to categorize visitors into different buckets. Once we
have created a segment of visitors, we can then serve targeted,
personalized content. We can further A/B test content within a given
segment.

The first step in creating any segment is to determine who you are
trying to target with your personalized content. For this example, we
will target returning visitors who are in the Boston area.

|Image follows Steps 1 to 5|

.. |Image follows Steps 1 to 5| image:: /sites/docs.acquia.com/files/inline-images/CreatingSegments1-optimize.gif


#. `Sign in </lift/profile-mgr#signing>`__ to |acquia-product:lpm|. 
#. Click the **Segments Tab**
#. Click **Add New Segment **
#. Enter a name for the segment. For this example, we will call the
   segment *“Returning Visitors in Boston”*
#. Enter a description for the segment. For this example, we will
   describe the segment as *“Visitors who are coming back to the site
   for a second time and are in the Boston area”*
#. Click the **Edit Criteria** field
#. Click the **Select Criteria** field
#. Choose **Current Location**, then select **City**
#. In the **Country** field, start typing *“United States”*. An
   autocomplete list will appear below. Select *United States*
#. In the **Region** field, start typing “Massachusetts”. An
   autocomplete list will appear below. Select *Massachusetts*
#. In the **City** field, start typing *“Boston”*. An autocomplete list
   will appear below. Select *Boston *
#. Click the **Add** button in blue
#. The operator should remain as **Matches One**
#. Click **Ok** 

You have just created criteria for a segment targeting visitors from
Boston. We can now add additional criteria to target repeat visitors
from the Boston area.

|Image for remaining steps|

.. |Image for remaining steps| image:: /sites/docs.acquia.com/files/inline-images/CreatingSegments2-optimize.gif

#. Click the **Plus** icon under the first criteria field
#. Click the **Edit Criteria** field
#. Click the **Select Criteria** field
#. Click **Person Properties**
#. Click **First Time Visitor**
#. Leave the operator as **Equals**, and change the **Values** field to
   *No*
#. Click **Ok**
#. Click **Save**

`There are many more fields and capabilities for segments to review that are not covered in this tutorial. </lift/profile-mgr/segment/category>`__

Congratulations, the segment created is now for visitors who are in the
Boston area, and are not first time visitors (or in other words,
returning).

Resources
~~~~~~~~~

-  `Default segment criteria available </lift/profile-mgr/segment/category>`__ on
   |acquia-product:cha| 
-  `Creating and managing segments </lift/profile-mgr/segment>`__
-  `Do you have a question or comment regarding this
   lesson? <mailto:tutorial-help@acquia.com?subject=Creating%20Personalized%20Experiences%20Lesson#1>`__

Next Lesson > |publishcontent|_
---------------------------------------------------


.. |publishcontent| replace:: Publishing Content to \ |acquia-product:leb|\ 
.. _publishcontent: /tutorials/creating-personalized-experiences-acquia-lift/publishing-content-experience-builder


