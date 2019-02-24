.. include:: /common/global.rst

Working with organizations
==========================

Subscriptions, applications, and teams in |acquia-product:ac| are
grouped under an
`*organization* </acquia-cloud/glossary#organization>`__. An
organization can represent different business objects for different
entities. For example, all of a company's applications might be grouped
under a single organization, or separate business units within a company
whose applications are developed, deployed, and managed independently
might be set up as separate organizations.

Your organizations are set up by Acquia when you create an Acquia
subscription. Each subscription, including its applications, and each
team belongs to one (and only one) organization. A team member may be on
teams that are assigned to any number of organizations.

Viewing organizations
---------------------

To view your organizations, complete the following steps:

#. Sign in to the |acquia-product:ui|.
#. Select your organization.
#. Click **Manage** in the top menu.

The **My Organizations** page displays an information card for each
organization in which you have a role. This information card displays
the `organization's Owner and Administrators <#roles>`__, along with
additional information, based on your organization role.

-  If you are the *Owner* or an *Administrator* of the organization, the
   card displays the number of teams, roles, and subscriptions in the
   organization.

   |Administrator view of an organization's information card|

-  If you are not the *Owner* or an *Administrator* of the organization,
   the card displays the teams that you are a member of and your roles
   on each team.

   |Non-Administrator view of an organization's information card|

If you are the *Owner* or an *Administrator*, or have the *administer
team* permission (which by default a *Team lead* has), you can use the
links at the bottom of the information card to invite a member to a team
or remove a member from teams. For more information, see `Managing team
members </acquia-cloud/teams/members>`__.

To view more details about the organization, including the
organization's teams, team members, and applications, click the
organization name or the **Manage** button at the bottom of the card.

.. _roles:

Organization roles and actions
------------------------------

Each organization has a single
`Owner </acquia-cloud/glossary#owner>`__ and one or more
`Administrators </acquia-cloud/glossary#administrator>`__. The *Owner*
and *Administrators* have all permissions relating to every application
under the organization. They also have the ability to give other users
the *Administrator* role.

Use the following table to learn more about the different actions that
*Owners* and *Administrators* can take with organizations:


.. list-table::
   :widths: 33 33 33
   :header-rows: 1
   
   * - Action
     - *Owner*
     - *Administrator*
   * - `Create and remove teams </acquia-cloud/teams/teams>`__
     - |yes|
     - |yes|
   * - `Rename the organization <#rename>`__
     - |yes|
     - |yes|
   * - `Transfer organization ownership <#transfer>`__
     - |yes|
     - |no|


.. _rename:

Renaming an organization
~~~~~~~~~~~~~~~~~~~~~~~~

An organization's *Owner* and *Administrators* also have the ability to
rename an organization. To rename an organization, you must be signed in
to the |acquia-product:ui| as its *Owner* or *Administrator*.

#. On the `Organizations <https://cloud.acquia.com/app/manage>`__ page,
   select your organization.
#. Click the **Rename** icon ( |Rename icon|).
#. Enter the new name for the organization, and then click **Rename**.

.. _transfer:

Transferring ownership of an organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an *Owner*, you can transfer the ownership of an organization to one
of the organization's *Administrators*. To do this, complete the
following steps:

#. On the `Organizations <https://cloud.acquia.com/app/manage>`__ page,
   select your organization.
#. Click the **Transfer ownership** icon ( |Transfer ownership icon|).
#. In the **New owner** list, click the *Administrator* that you want to
   be the new organization *Owner*.
#. Click **Continue**.

.. |Administrator view of an organization's information card| image:: https://cdn3.webdamdb.com/310th_sm_ocd00ijCasg0.png?1526476098
   :alt: Administrator view of an organization's information card
.. |Non-Administrator view of an organization's information card| image:: https://cdn3.webdamdb.com/310th_sm_Ycuyfsa3Mw71.png?1526475799
   :alt: Non-Administrator view of an organization's information card
.. |Rename icon| image:: https://cdn2.webdamdb.com/100th_sm_s2Nb0Tpju7u3.png?1526476043
   :class: inline-img
   :width: 24px
   :height: 24px
   :alt: Rename icon
.. |Transfer ownership icon| image:: https://cdn3.webdamdb.com/100th_sm_slmxJnSdd64.png?1526475564
   :class: inline-img
   :width: 24px
   :height: 24px
   :alt: Transfer ownership icon
