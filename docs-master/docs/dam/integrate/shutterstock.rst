.. include:: /common/global.rst

Integration: Shutterstock
=========================

|acquia-product:dam| supports two types of integrations with
Shutterstock. |acquia-product:dam| users can use the Shutterstock Search
integration to expand their asset searches to the vast Shutterstock
library. Shutterstock Premier customers can use the integration to have
their Shutterstock assets automatically synced to their
|acquia-product:dam| library.

For example, if you're looking for photos or video depicting active
lifestyles and wish to expand your search beyond your DAM, you can
easily toggle to the Shutterstock results and pull results from their
database.

The Shutterstock search feature is available for admins, contributors
and regular users. It must first be enabled by your admin before using.

.. _enable:

Enabling the integration
------------------------

*The information in this section applies only to users that have
`*Admin* <#role>`__ role type permissions.*

#. Sign in to |acquia-product:dam|.
#. Click the settings icon |Settings| in the top navigation, and then
   click **System Preferences**.
#. In the **Search** section, select the **Enable Shutterstock search
   results** check box.
#. Click **Save**.

   |Enable Shutterstock search|

.. _disable:

Disable or re-enable the Shutterstock Search feature
----------------------------------------------------

#. Log in to |acquia-product:dam|.
#. Choose **Add-on Settings** from the **Account**.
#. From the **Extras** tab, uncheck/check the **Enable Shutterstock
   Search** according to your preference.
#. Click **Done**.

.. _use:

Using Shutterstock Search feature
---------------------------------

If the Shutterstock Search feature is enabled, there will be a second
tab with **Shutterstock Results** when you search.

|Shutterstock results|

To download one of the Shutterstock assets, click the asset and then
click **Download** in the **Asset Details Panel**. You will need to log
in to Shutterstock to complete the download.

.. _premier:

Shutterstock Premier Sync
-------------------------

Shutterstock Premier Sync is available to any Shutterstock Premier
customer. With this integration enabled, any assets you purchase in
Shutterstock can automatically be synced to your |acquia-product:dam|
library.

To enable sync with Shutterstock premier, `contact Acquia
Support </support#contact>`__ . The |acquia-product:dam| implementation
team will work with your Shutterstock account rep to configure the
integration.

.. _faq:

Shutterstock Premier sync frequently asked questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **How long does it take for assets to sync?** Sync should be complete
   in 15-20 minutes, although thumbnail images and metadata processing
   may take a bit longer.
-  **Where will synced assets be stored?** All assets will be synced to
   the **Premier Content** folder. Sync will pull content from your
   **Download History** in Shutterstock; images, creative and footage
   can all be imported. Both licensed and comp assets can be synced,
   although, based on the nature of comps, we typically do not recommend
   clients sync them into |acquia-product:dam|. Please `contact Acquia
   Support </support#contact>`__ to decide what is best for your
   workflow and business needs.
   |Premier Content|
-  **If I have multiple accounts, do I have to sync all of them?** No,
   you can choose which accounts to sync to |acquia-product:dam|. There
   is no limit to the number of Premier accounts you can sync to your
   |acquia-product:dam| account.
-  **If multiple Premier accounts contain duplicate assets, will the
   assets be deduplicated?** Duplicate assets are handled based on the
   transaction type. Duplicate comp assets will not be synced to your
   Premier Content folder. Duplicate licensed assets will be synced,
   replacing the current version and creating multiple replications of
   the asset.
-  **Are there restrictions on the size or file types that can be
   synced?** There are no restrictions on the size of files that can be
   synced. Editorial, music and Offset assets cannot be synced.
-  **Will asset metadata also be synced?** Yes, metadata will be
   embedded for images and videos. This includes the standard fields,
   Rights Usage Terms and the four custom metadata fields that can be
   configured within Shutterstock Premier. The custom fields map to
   custom fields 17-20 in |acquia-product:dam|.

|Custom fields|

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Enable Shutterstock search| image:: https://cdn4.webdamdb.com/md_6DgO2hNDJH81.png?1526475507
   :width: 550px
   :height: 142px
.. |Shutterstock results| image:: https://cdn4.webdamdb.com/md_QkCxPqhw0zn9.png?1526475746
   :width: 550px
   :height: 353px
.. |Premier Content| image:: https://cdn4.webdamdb.com/md_kNeNfHFbap84.png?1526476099
   :width: 550px
   :height: 394px
.. |Custom fields| image:: https://cdn4.webdamdb.com/md_cW5IbCGMnjG1.png?1526475494
   :width: 550px
   :height: 134px
