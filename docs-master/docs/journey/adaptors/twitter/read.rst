.. include:: /common/global.rst

Twitter: Read adaptor
=====================

The Twitter read adaptor can query the Friends, Followers or Profile of
a specified user. The user is identified by their Twitter User Id or
User Screen Name.

Creating the adaptor
--------------------

Create a **Twitter** adaptor, and when it appears for configuration, in
the **Twitter Action** list, be sure to click **Read**. For information
about creating or configuring adaptors, see |adaptors|_.

.. |adaptors| replace:: \ |acquia-product:aj| \ adaptors
.. _adaptors: /journey/adaptors

After you have created the adaptor, complete the following actions:

#. In the **Twitter Read Options** section, select one of the following
   values:

   -  **Friends**
   -  **Followers**
   -  **Profile**

#. Choose the location of the\ **User ID or User Screen Name**.
#. Choose the **Output** location for the response from Twitter.

   -  **Twitter Friends** returns the output from the `Twitter API
      ``GET friends/ids`` <https://dev.twitter.com/rest/reference/get/friends/ids>`__
      and will return an array of Twitter IDs. It will call the end
      point until no more friends are returned and so may take some time
      to respond if the user has a lot of friends. Pages are returned
      with up to 5,000 friends at a time and |acquia-product:aj| will
      attempt to download all of the pages.
   -  **Twitter Followers** returns the output from the `Twitter API
      ``GET followers/ids`` <https://dev.twitter.com/rest/reference/get/followers/ids>`__
      and will return an array of Twitter IDs. It will call the end
      point until no more friends are returned and so may take some time
      to respond if the user has a lot of friends. Pages are returned
      with up to 5,000 friends at a time and |acquia-product:aj| will
      attempt to download all of the pages.
   -  **Twitter Profile** will return a `Twitter user
      profile <https://dev.twitter.com/overview/api/users>`__ into the
      selected location.

The adaptor will return an error message of ``User not found`` if the
user screen name or ID is not known by Twitter.

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Adaptor does not have           | It is necessary to create a       |
| connection set**                  | connection and choose it from the |
|                                   | **Adaptor Connection** drop down  |
+-----------------------------------+-----------------------------------+
| **This adaptor's configuration    | No data location for the output   |
| requires a data source to be      | has been selected                 |
| set**                             |                                   |
+-----------------------------------+-----------------------------------+
