.. include:: /common/global.rst

Managing permissions in |acquia-product:lpm|
============================================

To control your users' access to the features and functions of
|acquia-product:lpm|, you need to assign them permissions. A group of
users working on a particular project may need to share certain
permissions, but not others. To make this easier, |acquia-product:lpm|
allows you to create security groups. Every user account is assigned to
a single security group. Users assigned to the same security group share
a common set of permissions. By configuring these permissions, you can
limit the resources available to a group and control which customer
accounts a group can access.

When you create a new customer account in |acquia-product:lpm|, in
**Admin > Manage permissions**, |acquia-product:lpm| creates three
groups whose names are composed of your customer name followed by one of
the names from the following list — for example, one of your groups
might be named **ExampleInc Administrators**.

-  *Administrators* - have access to all available |acquia-product:lpm|
   features, including the ability to manage users and group security
-  *Users* - have the ability to see people's details and manage
   segments
-  *API users* - have access to API functions, and are generally used
   for API authentication

Creating a new security group
-----------------------------

Sometimes you may want to configure certain users' permissions and
access to customer accounts differently to what is created by default in
|acquia-product:lpm|. To do so, you can create a new security group. For
example, you could create a Managers security group and give members the
ability to view people and run reports, but not allow them to create
segments.

|Security Group Details page|

.. |Security Group Details page| image:: https://cdn4.webdamdb.com/1280_ooI3YLDJypT3.png?1526476095
   :width: 590px
   :height: 421px

To add a new security group, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the **Admin** tab.
#. Go to **Manage permissions > Add new security group**.
   |acquia-product:lpm| displays the Security Group Details page.
#. In the **Name** and **Description** fields, enter a name for the
   security group that you want to create, and a brief explanation of
   its intended function.
#. In the **Linked Security Resources** list, click an item that you
   want to make available to this security group as a link. For example,
   clicking **Manage Permissions Link** displays a link that members of
   this security group can click to manage the permissions of all
   security groups. Clicking **Admin tab** displays a link that allows
   users in this security group to access the **Admin** tab and its
   functions.
#. Click **Add** to add this item to the list of linked security
   resources for this security group. |acquia-product:lpm| displays the
   name of the item in a table.
#. Depending on your needs, repeat steps 4 and 5 to add more linked
   security resources to this security group.
#. In the **Linked Customers** list, click the name of a customer whose
   account you currently have permissions to access, and whose name you
   want to make available to this security group as a link. Making this
   customer available as a link means that the members of this security
   group can access this customer's account. Click **Add** to add this
   item to the table of linked customers for this security group.
#. Depending on your needs, repeat step 7 to add more customer links to
   this security group.
#. Click **Save** to create the new security group.

Managing security groups
------------------------

To list and manage security groups, complete the following steps:

#. `Sign in </lift/profile-mgr>`__ to the |acquia-product:lpm|
   interface, and then click the **Admin** tab.
#. Click the **Manage permissions** link.

|acquia-product:lpm| displays a list of security groups.

|Security group list|

.. |Security group list| image:: https://cdn4.webdamdb.com/1280_c28sbrLSTdp2.png?1526476009
   :width: 590px
   :height: 348px

To edit a security group, click its name and modify its values as
required.

To delete a security group, find the security group that you want to
remove, and then click its **Delete** link.