.. include:: /common/global.rst

Remote Administration preferences
=================================

Remote Administration (RA) follows a `specific workflow </ra/workflow>`__ implemented by `automation </ra/automation>`__ that takes into account subscription-specific preferences. If you are a `Remote Administration </ra>`__ customer, setting your application update preferences correctly ensures that security updates can be smoothly integrated into your workflow.

Reviewing your RA settings
--------------------------

To review your RA application update preferences, completing the following steps:

#. Sign in to the `Acquia Cloud interface <http://cloud.acquia.com>`__.
#. Select the `application </acquia-cloud/manage#app>`__ whose Remote Administration settings you want to view.
#. In the left menu, click **RA**.

|acquia-product:ac| displays the RA update settings in place for your application.

Modifying your RA settings
--------------------------

Remote Administration customers have several available update methods, and whichever method is selected influences subsequent options.

To modify your RA settings (such as changing your update settings or removing RA from your application), complete the following steps:

#. `Go to the Remote Administration settings page for your application <#review>`__.
#. In the upper right of the page, click the **Edit** icon.
#. In the **Update process** list, click the update method you want to use with your application, from the following list:

   -  **Update and Deploy (default)** |--| When a security update is required, Acquia creates a new branch from whatever branch or tag is deployed to production, applies security updates, and pushes the branch to the repository. |br| 
      The new branch is then deployed to your `RA environment </ra/environment>`__ for testing. Acquia lets you know using a ticket that the secure branch is available for testing. Remote Administration can deploy the updates to production for you, but will not do so without your explicit approval.
   -  **Inform only** |--| Acquia informs you of pending updates using a security update notification. No further action is taken without your specific request.
   -  **Do not inform** |--| Acquia does not inform you of any pending updates. No further action is taken without your specific request. Select this method if your website uses Continuous Integration (CI).

#. Depending on your selection in the **Update process** list, |acquia-product:ac| may display additional fields regarding the implementation details for your selected method.

   .. list-table::
     :widths: 15 20 50 15
     :header-rows: 1

     * - Update method
       - Desplayed field
       - Description
       - Default value
     * - **Update and Deploy**
       - **Pause until**
       - Enter a date and time to pause Remote Administration until that time. After that time, RA will resume its normal schedule.
       - *not paused*
     * - **Update and Deploy**
       - **Update type**
       - Select from **Core** and **Core and contributed modules** to determine the portions of your application that you want to update. |br| 
         If you have features that are dependent on certain versions of contributed or custom modules, you can `implement a locking functionality <https://knowledge.acquia.com/articles/using-drush-lock-files-contributed-modules>`__ to prevent those specific modules from being updated, and then use the **Core and contributed modules** update method.
       - **Core and contributed modules**
     * - **Update and Deploy**
       - **Secondary testing environment**
       - Acquia deploys the initial security update branch to the RA environment. After you approve the branch for tagging and final testing, you can have Acquia place this tag on any environment (other than production) for final testing. A fresh copy of the production database will be copied into this environment as a part of this final, preproduction test.
       - ``Stage``
     * - **Update and Deploy**
       - **Copy files from production to testing environment**
       - Acquia strongly recommends that you click **Yes** to ensure accurate and up-to-date tests.
       - **Yes**
     * - **Update and Deploy**
       - **Copy prod database to testing environment**
       - Acquia strongly recommends that you click **Yes** to ensure accurate and up-to-date tests. |br| 
         For information about creating scrub scripts to remove sensitive data and functionality from your testing environment, see the Databases section of the `Remote Administration environment </ra/environment>`__ page.
       - **Yes**
     * - **Update and Deploy**
       - **Merge update tag into development branch**
       - Determines whether or not to merge the tested security update tag into your preferred branch. |br| 
         If you click **No** for this field, your team must ensure that the updates are merged into your code on the main branch before your code goes into production. Failure to complete this merge could result in a schema mismatch between the recently updated production data and the code that has not incorporated the updated code.
       - **Yes**
     * - **Update and Deploy**
       - **Merge development branch**
       - Acquia typically merges updates into master (Git). If you use a different workflow, enter the exact name of the branch into which the security updates should be merged.
       - ``Master``
     * - **Inform only**
       - **Pause until**
       - Enter a date and time to pause Remote Administration until that time. After that time, RA will resume its normal schedule.
       - *not paused*
     * - **Do not inform**
       - 
       - *Does not display any additional preference fields*
       - 

#. Click **Save**.

Remote Administration will now use your selected update settings for your application.
