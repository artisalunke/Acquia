.. include:: /common/global.rst

Managing |acquia-product:ccd| environments
==========================================

To provide increased production-ready deployment speed, reliability, and
cost efficiency, |acquia-product:ccd| enables developer teams to create
and work in additional development environments, and then remove those
on-demand environments when they're no longer required.

*CD environments* are built dynamically and are very similar to `regular
Drupal-based environments </acquia-cloud/manage/environments>`__.

Created CD environments will persist until you `delete <#delete>`__
them. For additional information about what CD environments contain, see
the following:

-  `CD environment resources and
   limitations </acquia-cloud/cd/env/resource>`__
-  `Container resources </acquia-cloud/cd/container>`__

At its initial level, |acquia-product:ccd| includes five CD environments
for your use. If you need additional CD environments, contact your
Account Manager.

You can use any of the following methods to add or remove CD
environments from your |acquia-product:ac| application:

-  :ref:`ui`
-  :ref:`pipeline`
-  :ref:`api`

.. _ui:

Managing your environments with the |acquia-product:ac| interface
-----------------------------------------------------------------

The |acquia-product:ac| interface allows you to both add and remove CD
environments from your application, as required.

.. _add:

Adding an environment with the user-interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add a CD environment to your subscription, complete the following
steps:

#. Sign in to |acquia-product:ac|, and then select the application in
   which you want to create a CD environment. To determine if an
   application already contains a CD environment, examine the
   application's card:

   |Number of CD environments|

#. From your subscription's action icons, click the **Add Environment**
   icon. |Add environment icon| If your application does not have any
   environments, an **Add environment** button will also be displayed on
   the page.
#. In the dialog box, add a label in **Enter a label for the new
   environment**.

   .. note::

    To prevent confusion, Acquia strongly recommends that you label this
    environment as a temporary environment.

#. Click **Continue**.
   |acquia-product:ac| displays an **Add environment** dialog box.

   |Select a branch|

#. In the **Select branch** list, select the branch you want to deploy
   to your |acquia-product:ccd| environment, and then click
   **Continue**.
#. If you have more than three databases in your environment,
   |acquia-product:ac| will display a dialog box labeled **Select up to
   3 databases.** Select the check boxes next to the database schemas
   that you want to add to the environment, up to a maximum of three.
#. Click **Continue**.
   |acquia-product:ac| then displays a dialog box to both confirm your
   choices and display the number of remaining CD environments.
#. Click **Add environment**.

|acquia-product:ac| will begin to create your CD environment. You can
monitor the environment's creation status in the `activity
notifications </acquia-cloud/notify>`__ section of the interface.

.. _delete:

Deleting an environment with the user interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you are finished with a CD environment, it can be deleted from
|acquia-product:ac|. To do this, complete the following steps:

#. Sign in to |acquia-product:ac|, and then click the **Trash can** icon
   for the environment that you want to remove. 

   |Delete a CD environment| 
   
   |acquia-product:ac| displays a **Remove cloned environment** dialog box.
#. In the dialog box, enter your password in the **Enter your account
   password to confirm this action** text field.
#. Click **Remove**.

or

#. Sign in to |acquia-product:ac|, and then select the CD environment
   that you want to remove.
#. From your environment's action icons, click the **Remove** icon.
   |Delete an environment|
   |acquia-product:ac| displays a **Remove cloned environment** dialog
   box.
#. In the dialog box, enter your password in the **Enter your account
   password to confirm this action** text field.
#. Click **Remove**.

|acquia-product:ac| will begin the removal of the environment. The CD
environment is no longer available for your use.

.. _pipeline:

Managing your environments with CD pipelines
--------------------------------------------

Using *pipelines*, |acquia-product:ccd| allows you to create or remove
CD environments as instructions in an executed build definition file. To
create or remove a CD environment during a pipeline job, use the
following script instruction:

``- pipelines-deploy``

For more information about building and using build definition files,
see `Creating and managing your build definition
file </acquia-cloud/develop/pipelines/yaml>`__.

Creating a CD environment with CD pipelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a CD environment, place the pipelines-deploy instruction in
the ``build`` element, similar to the following example:

.. code-block:: yaml

    build:     
      steps:
         - build_site:
               script:
                - echo "Build instructions here"
         - deploy:
                script: 
                - pipelines-deploy``

Removing a CD environment with CD pipelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To remove a CD environment, place the pipelines-deploy instruction in
either the ``pr-merged`` or ``pr-closed`` elements, similar to the
following examples:

.. code-block:: yaml

    pr-merged:     
      steps:
         - deploy:
              script:
                 - pipelines-deploy


.. code-block:: yaml

    pr-closed:
         steps: 
          - deploy:
               script:
                    - pipelines-deploy

.. _api:

Managing your environments with Cloud API v2
--------------------------------------------

Version 2 of the Cloud API provides a REST API that you can use to
manage your CD environments. You can view the list of available Cloud
API calls at the following URL:

`http://cloud.acquia.com/api-docs/ <http://cloud.acquia.com/api-docs/>`__

.. admonition:: Cloud API access note

    Visit the Cloud API documentation page for information about
    authenticating to the API, including generating an API token and
    authenticating requests.

The API includes the following methods that you can use with your CD
environments:

.. list-table::
   :widths: 50 50 
   :header-rows: 1

   * - Code
     - Description
   * - ``POST`` `/api/applications/{uuid}/environments <http://cloud.acquia.com/api-docs/#applications__uuid__environments_post>`__
     - Create a CD environment for the ``{uuid}`` application
   * - ``DELETE`` `/api/environments/{id} <http://cloud.acquia.com/api-do cs/#environments__id__delete>`__
     - Remove the ``{id}`` CD environment

For complete information about these and other methods, see the `Cloud
API v2 documentation <http://cloud.acquia.com/api-docs/cde/>`__.

.. |Number of CD environments| image:: https://cdn4.webdamdb.com/1280_EF67Y1KBvKj4.png?1526475908
   :width: 300px
.. |Add environment icon| image:: https://cdn2.webdamdb.com/1280_c1OoPAL9i91.png?1526476109
   :class: inline-img
   :width: 24px
   :height: 24px
.. |Select a branch| image:: https://cdn2.webdamdb.com/1280_YxVqEeNEpBs9.png?1526475614
   :width: 601px
   :height: 421px
.. |Delete a CD environment| image:: https://cdn2.webdamdb.com/1280_I41PhP5YezJ6.png?1526475827
   :width: 365px
   :height: 64px
.. |Delete an environment| image:: https://cdn4.webdamdb.com/1280_UafZZoRyLr41.png?1526476060
   :class: inline-img
   :width: 22px
   :height: 22px




