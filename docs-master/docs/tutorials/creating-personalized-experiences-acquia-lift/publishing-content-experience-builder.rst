.. include:: /common/global.rst

Publishing Content to |acquia-product:leb|
============================================================

.. container:: message-status

   Creating Personalized Experiences with |acquia-product:cha| – |Back to intro|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/creating-personalized-experiences-acquia-lift

.. |Next lesson| replace:: Creating Slots
.. _Next lesson: /tutorials/creating-personalized-experiences-acquia-lift/creating-slots

Lesson Goal
-----------

.. container:: message-status
    
   Publish a new hero banner into |acquia-product:leb| for use in personalizations.

Before creating personalizations using |acquia-product:cha|, we must
first publish variations in |acquia-product:leb|. In this example, we
will create a new hero banner to leverage in future personalizations.

Personalizations consist of the following three elements:

-  **Content** - used for the personalization
-  **Slots** - the place on the website that is personalized
-  **Rules** - a segment of people that view the personalization

Our website stores hero images in a custom block called **Hero**.
Therefore we will use the **Hero** block type to create this
personalization.

|Displays Part 1 of Steps|

#. Navigate to Experience Builder using following URL path:
   */admin/config/services/acquia-contenthub/configuration*

   -  In other words, this page can also be found with using the
      click-through path of **Configuration > Web Services > Content Hub
      > Entity Configuration**

#. Select the **Publish** check box by the **Custom Block > Hero**
   entity we want to publish to **Content Hub**. Publishing this
   Content to |acquia-product:leb| will allow us to use this content in
   a targeted personalization.
#. Additionally, select **Publish View Modes** and add at least one
   **View mode** to use for our personalization. (Note: In order for
   Content to be available in |acquia-product:leb|, it needs to be
   published with at least one **View mode** enabled)
#. Scroll to the bottom of the form and click **Save configuration**

   |Part 2 of Steps|
   
#. Save the new variation of the **Hero** block
#. Go to the URL path */admin/structure/block/block-content* and add or
   modify the **Hero** block as applicable
#. Save the block edit form. The customized hero will now be available
   in |acquia-product:leb|
#. (Optional) If |acquia-product:leb| has been 
   `previously set up </lift/exp-builder/access>`__, you can view your newly-published
   **Hero** block on your homepage under the **Content** tab for use in
   personalizations

|Part 3 of directions|

Congratulations, your content is now ready for use in a personalization.

Next Lesson > `Creating Slots </tutorials/creating-personalized-experiences-acquia-lift/creating-slots>`__
----------------------------------------------------------------------------------------------------------

.. |Displays Part 1 of Steps| image:: /sites/docs.acquia.com/files/inline-images/PublishingExperienceBuilder1-optimize.gif
.. |Part 2 of Steps| image:: /sites/docs.acquia.com/files/inline-images/PublishingExperienceBuilder2-optimize.gif
.. |Part 3 of directions| image:: /sites/docs.acquia.com/files/inline-images/PublishingExperienceBuilder3-optimize.gif

