.. include:: /common/global.rst

Code workflows with |acquia-product:ac|
=======================================

The **Code** elements of the |acquia-product:ac| Environments page
provide a user interface for deploying code from your repository to your
application's environments. When you commit a branch to your repository,
|acquia-product:ac| updates the environment running that code branch.

You should make and test changes to administrative configurations,
views, and other major application settings only in your Development or
Staging environments. Do not make or test changes in your Production
environment. If you make a change that breaks your application in the
Production environment, you might bring your live application down.

Complete the following steps when you're ready to deploy code to an
environment:

#. Check out your repository to your local computer.
#. Make changes to your application in the ``/master`` directory, or
   whatever branch you've configured to deploy for the Development
   environment. Any environment deploying a branch will deploy all
   commits to that branch immediately. This is a good reason never to
   deploy the master branch on your Production environment; code
   committed to master would then appear immediately in your live
   application, before you have had a chance to test and verify it.
#. To change the code on your servers, select one of the following
   methods:

   -  Commit changes to the currently deployed branch.
   -  Select a different repository branch or tag to deploy.

#. Deploy your code, either in the `same environment <#deploy-same>`__
   or `between environments <#move>`__.
#. 

   .. raw:: html

      <div id="update">

   | When you have release new code to an environment, you may need to
     execute any pending database updates. To do this, in your browser
     go to: ``http://[site_URL]/update.php``
   | The ``update.php`` page displays whether there are any scheduled
     database changes, which are common after core or contributed module
     updates. After applying the changes, ``update.php`` will also clear
     your application's caches. It is a good practice to clear Drupal's
     caches manually however, as this will assure you that you are
     starting from a clean state. After ensuring that Drupal's caches
     are cleared, you will also need to `clear the Varnish
     cache </acquia-cloud/performance/varnish#clear>`__. Be cautious
     before clearing caches on a production environment under load.

   .. raw:: html

      </div>

.. _deploy-same:

Deploying code in the same environment
--------------------------------------

You can deploy a different branch or tag in the same environment from
either the **Environments** page, or from the **Environments overview**
page.

-  *Using the **Environments** page*
   To switch the code deployed in an environment from one tag or branch
   to another, using the **Environments** page:

   #. In the **Code** element for the environment, click the code switch
      button.

      |The code switch|

   #. In the **Switch code** dialog, select a tag or branch from the
      **Select branch** menu and click **Continue**.
   #. In the **Switch code** confirmation dialog, click **Switch**.

   When you select a new branch or tag to deploy, that code is retrieved
   from your repository and deployed to the appropriate environment on
   the web servers. The deploy task appears in the Activity task list.
-  *From the **Environment Overview** page*
   You can deploy code on an environment or copy code from one
   environment to another using the Overview page of an environment.
   To switch the code deployed in an environment from one tag or branch
   to another, using the Overview page:

   #. On the **Environments** page, click the name of the environment to
      open that environment's **Overview** page.
   #. On the **Overview** page for the environment, click **Switch**.

      |Click Switch to deploy a different tag or branch|

   #. In the **Switch code** dialog, select a tag or branch from the
      **Select branch** menu and click **Continue**.
   #. In the **Switch code** confirmation dialog, click **Switch**.

.. _move:

Moving code from one environment to another
-------------------------------------------

To move code from one environment to another, such as ``Dev`` to
``Stage`` or from ``Stage`` to ``Prod``, use one of the following
processes, depending on your location in the |acquia-product:ac|
interface:

-  *From the **Environments page***

   #. Drag a **Code** element from one environment to another
      environment. |acquia-product:ac| creates a new tag for the head
      version of that branch (the most recently committed code version)
      and then deploys the tag in the environment you selected. For
      example, drag your **Dev** Code element to **Stage**.
   #. Optionally, you may add a ``commit message``.
   #. Click **Deploy**.

   |Deploy code by dragging it to another environment|

   When you drag your **Dev** code container to the **Stage**
   environment, |acquia-product:ac| creates a symbolic link between the
   Staging environment and the head version (the most recently committed
   code version) of trunk in your Development environment. When you
   click **Deploy**, |acquia-product:ac| creates a tag and updates the
   web server to that version of your code. The default tag format is
   ``yyyy‐mm‐dd.version`` (for example, ``tags/2016‐09‐18``). From the
   example, the next tag you create would be ``2016‐09‐18.0``.

   When you have a version that you are ready to deploy to your live
   production application, drag your code element from the **Stage**
   environment to **Prod**. If the Staging environment is running a tag,
   that same tag is deployed into Production.

-  *From the **Environment Overview** page*

   To copy code from one environment to another (creating a new tag and
   deploying it) using the Overview page:

   #. On the **Environments** page, click the name of the environment to
      open that environment's **Overview** page.
   #. On the **Overview** page for the environment, click **Deploy**.

      |Click Deploy to deploy a tag or branch from a different
      environment|

   #. In the **Deploy code** dialog, select the environment from which
      you want to copy a tag or branch, and then click **Continue**.
   #. In the **Deploy code** confirmation dialog, optionally enter a
      commit message that describes the new deployment, and then click
      **Deploy**.

.. _revert:

Reverting code
--------------

To revert code to an earlier version, complete the following steps:

#. In the **Code** element for the environment, click the code switch
   button.
#. In the **Switch code** dialog box, select the tag for the version to
   which you want to revert, and then click **Continue**.
#. In the **Switch code** confirmation dialog, click **Switch**.

When you deploy a previous branch or tag, |acquia-product:ac| retrieves
the code snapshot from your repository and then deploys it on the
appropriate environment on the web servers.

.. _related:

Related topics
--------------

-  `About your code repository </acquia-cloud/develop/repository>`__
-  `Using Live development mode to change code on your
   server </acquia-cloud/develop/livedev>`__

.. |The code switch| image:: https://cdn3.webdamdb.com/1280_sAL3kDWsK470.png?1526475719
   :width: 364px
   :height: 255px
.. |Click Switch to deploy a different tag or branch| image:: https://cdn2.webdamdb.com/1280_AyLJCXZkaYY0.png?1526475781
   :width: 1275px
   :height: 437px
.. |Deploy code by dragging it to another environment| image:: https://cdn4.webdamdb.com/1280_C08KCFDhIK11.png?1526475479
   :width: 1161px
   :height: 286px
.. |Click Deploy to deploy a tag or branch from a different environment| image:: https://cdn4.webdamdb.com/1280_U39dlNBpyz71.png?1526475604
   :width: 739px
   :height: 489px
