.. include:: /common/global.rst

Limiting content discovery to a single site
===========================================

By default, all content under the same |acquia-product:lpm| account
displays in the |acquia-product:leb| list of content. If you are sharing
an account with others, but you would rather not to see other users'
pushed content, you can use the following procedure to display only the
content from a single website.

#. Create and use your own Drupal website with |acquia-product:cha|. You
   will need exclusive access to that ensure no other users are
   unexpectedly changing your Drupal website or creating new content.
#. Create and use your own `Lift Site
   ID </lift/profile-mgr/customer-sites>`__.

   a. Create your own **Customer Site**. You will need the resulting
      **External ID** in the following steps.
   b. Configure your website to use the **External ID**:

      -  In your |acquia-product:cha| Configuration page, enter the
         **External ID** as the **Site ID**.
      -  In your |acquia-product:ch| Configuration page, enter the
         **External ID** as the **Client Name**.

      After you save your changes, you'll find that your Configuration
      page now displays the **Site's Origin UUID**, which you will need
      in the following steps.

#. Set your Drupal website to limit its list of contents to only one
   |acquia-product:cha| website (by its **Site's Origin UUID**). By
   design, this feature is not configurable in the UI and must be
   enabled using a Drush command while `connected to your
   website </acquia-cloud/ssh/enable>`__.
   To limit content, use the following Drush commands, based on your
   website's installed Drupal version:

   -  *Drupal 8*

      .. code-block:: none

         drush @[YOUR SITE].[ENVIRONMENT] config-set acquia_lift.settings credential.content_origin '[SITE ORIGIN UUID]'

      To return to the default (all content is visible), use the
      following command:

      .. note::  

         There are two single quotes ( ``'`` ) at the end of the command,
         and they are both required.

      .. code-block:: none

         drush @[YOUR SITE].[ENVIRONMENT] config-set acquia_lift.settings credential.content_origin ''

   -  *Drupal 7*

      .. code-block:: none

         drush @[YOUR SITE].[ENVIRONMENT] vset acquia_lift_content_origin '[SITE ORIGIN UUID]'

      To return to the default (all content is visible), use the
      following command:

      .. code-block:: none

         drush @[YOUR SITE].[ENVIRONMENT] vdel acquia_lift_content_origin

#. Clear your Drupal website's cache using the following command:

   .. code-block:: none

      drush @[YOUR SITE].[ENVIRONMENT] cr

Now when you use the |acquia-product:leb| and refresh the page, only the
content that you have published should be displayed.
