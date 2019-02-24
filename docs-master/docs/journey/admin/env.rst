.. include:: /common/global.rst

Creating and managing environments
==================================

An |acquia-product:aj| *environment* is a place in which to store
`connections </journey/connect>`__ for a project. Each project can have
several environments. The environment usually reflects the stage of
deployment (such as *Development*, *UAT*, *Staging*, and *Production*),
but can be called anything that you want. Environments can only be
created by users with administration privileges for the project.

Accessing a project's environments
----------------------------------

To review or modify the environments available for your project,
complete the following actions:

#. Go to the **Admin** page, and then click **Projects** in the left
   menu.
#. Find your project in the project list, and then click its project
   name.
#. In the project's detail view, click **Environments**.

|Environment overview|

Modifying your environments
---------------------------

|acquia-product:aj| displays the list of existing environments, with the
current environment is shown with a tick next to its name and stated
above the list of environments.

To create a new environment, from the project's environments detail
view, click **Add New Environment**.

To change the current environment, select the environment that you want
to switch to from the list, and then click its checkmark icon (
|Checkmark icon| ).

Deleting environments
---------------------

To delete an environment from a project (including all of its
connections), select the environment that you want to remove from the
list, and then click its trash can icon ( |Trash can icon| ).
|acquia-product:aj| will confirm the deletion.

.. note::
  You cannot delete the only environment associated with a project.

.. |Environment overview| image:: https://cdn3.webdamdb.com/1280_YVXU2EoLZA92.png?1526475716
   :width: 1280px
   :height: 723px
.. |Checkmark icon| image:: https://cdn3.webdamdb.com/1280_At2JULYleMY8.png?1526475445
   :width: 16px
   :height: 16px
.. |Trash can icon| image:: https://cdn2.webdamdb.com/1280_ojfiKCL3lCF0.png?1526475602
   :width: 16px
   :height: 16px
