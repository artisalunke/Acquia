.. include:: /common/global.rst

Using a Cloud Service Management plan
=====================================

.. container:: message-status

   Available only to |acquia-product:ace| subscribers. Contact your
   account manager for more information.

Drupal-based production environments in |acquia-product:ace| include the
ability for you to scale server sizes, based on need, by using the
|acquia-product:ac| user interface. The following Cloud Service
Management (CSM) sizes are available for your use: *Small*, *Medium* and
*Large*. Small and Medium sizes are available for annual contracts; the
Large size is available as a temporary upsize.

Each environment is rated for a certain level of traffic, based on a
typical Drupal application. You can install one or more applications
into this environment. Although having applications share an environment
can be cost-effective, a traffic spike on one application may affect the
availability of other applications installed in the same environment.

If you deploy an application on a Small environment and later need to
make the environment bigger, you can `scale up to a Medium or Large
environment <#upgrade>`__ in the |acquia-product:ac| interface, enabling
you to prepare your website in advance for, or to react to, a
`high-traffic event </support/traffic>`__ on your own terms. If you’re
running a major promotion and expect increased traffic, you can
temporarily scale up to a Large, and then scale back to a Small when the
traffic returns to normal levels.

.. note::

   You cannot downsize below the base level specified in your contract.

Viewing your CSM plan
---------------------

To review your Cloud Service Management information, complete the
following steps:

#. Sign in to the |cloud-ui|_.
#. Select an application, and then select its **Prod** (production)
   environment.

   .. note::

      CSM-related resizing is available only for production environments.

#. In the left menu, click `Stack
   Metrics </acquia-cloud/monitor/stackmetrics>`__, and then, in the
   page, click the **Manage Plan** tab.

Cloud Service Management (CSM) plan details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Manage Plan** page displays information that is specific to your
subscription's base size and current plan.

This information includes the following items:

+-----------------------------+-------------------------------------------------------------------------------------+
| Information                 | Description                                                                         |
+=============================+=====================================================================================+
| **Subscription**            | The name of this subscription                                                       |
+-----------------------------+-------------------------------------------------------------------------------------+
| **CSM Plan Name**           | The name of your CSM sizing plan                                                    |
+-----------------------------+-------------------------------------------------------------------------------------+
| **CSM Plan Base Size**      | Your base plan's size                                                               |
+-----------------------------+-------------------------------------------------------------------------------------+
| **CSM Plan Current Size**   | Your current plan's size                                                            |
+-----------------------------+-------------------------------------------------------------------------------------+
| **Application Usage**       | Number of applications in use out of the total number of available applications     |
+-----------------------------+-------------------------------------------------------------------------------------+
| **Max File Storage**        | Maximum amount of file storage available for this subscription, in gigabytes (GB)   |
+-----------------------------+-------------------------------------------------------------------------------------+
| **Max Database Storage**    | Maximum amount of database space available, in gigabytes (GB)                       |
+-----------------------------+-------------------------------------------------------------------------------------+

Next to this chart is a list of **Applications** that are utilizing
shared resources. `Stack Metrics charts </acquia-cloud/csm>`__ for
applications in this list display data that is aggregated for these
applications.

Upgrading your CSM plan
-----------------------

Each |acquia-product:ac| subscription has a *base level*. This level is
the original package for your group of applications as specified in your
contract. The following package levels are available for use:

+----------+------------------------+
| Size     | Maximum requests/day   |
+==========+========================+
| Small    | 18,000                 |
+----------+------------------------+
| Medium   | 40,000                 |
+----------+------------------------+
| Large    | 60,000                 |
+----------+------------------------+

Your current plan (**Current plan**) is highlighted, along with your
default subscription, which is labeled **Base Plan**. These labels can
be in the same card or different cards, depending on whether or not you
have upsized from your base plan.

Requests per day are dynamic requests, which are requests that directly
query the server and bypass Varnish. Applications using Varnish can
handle additional requests.

|Upgrading your plan|

Changing your plan
------------------

To change the size of the Cloud Service Management plan for your
environment, complete the following steps:

.. note::

  -  Only application owners, or users with the `Administrator
     role </acquia-cloud/teams/roles>`__, can upsize a server.
  -  When scaling up from a Small, you must scale up first to a Medium,
     and then to a Large if necessary. Websites can not scale up directly
     from a Small to a Large size.

#. `Go to the Manage Plan page. <#view>`__
#. | In the **Upgrade Cloud Service Management Plan** section, click
     **Select** for your desired plan.
   | |acquia-product:ac| will display a dialog box to confirm your plan
     change and outline the consequences of the action. For example,
     resizing to a smaller stack reduces capacity.

   |Confirming your resize|

#. Select the check box to confirm financial responsibility. The message
   states:

       By clicking here, you expressly confirm that you have the
       authorization to make this purchase on behalf of your Company and
       you acknowledge that all applicable fees shall be paid by Company
       all in accordance with the terms of the applicable agreement.

#. Click **Resize** to proceed, or **Cancel** to stop the change.

Your `task log </acquia-cloud/monitor/tasks>`__ will update with an
entry similar to the following mesaage:

``Resizing [the environment] to [new plan size]``

After the resize is complete, the task log will update again with a
message indicating a successful resize, such as the following:

``The environment has been resized to "medium".``

Your new user plan will be highlighted as the **Current plan**.

In the event of a failure `contact Acquia Support </support#contact>`__.

.. |Upgrading your plan| image:: https://cdn4.webdamdb.com/1280_DNHN59GZQA31.png?1528157258
   :alt: Upgrading your plan
.. |Confirming your resize| image:: https://cdn3.webdamdb.com/md_QdWczAbatn91.png?1528157297
   :alt: Confirming your resize
   
.. |cloud-ui| replace:: \ |acquia-product:ui|\
.. _cloud-ui: https://cloud.acquia.com

