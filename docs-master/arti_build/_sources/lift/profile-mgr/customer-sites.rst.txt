.. include:: /common/global.rst

Customer sites
==============

If you have multiple websites using the |liftlink|_
service, you may want to separate your visitor events by website, rather
than keeping all your websites' data together. Doing this can allow you
to maintain a discrete list of events for each website, and also let you
build separate visitor insights for keywords, content sections, content
types, or other taxonomies for each website.


.. |liftlink| replace:: \ |acquia-product:cha|\ 
.. _liftlink: https://www.acquia.com/products-services/acquia-lift

To organize your events by website, you will need to set up a customer
site in |acquia-product:lpm| for each of your websites.

Setting up a customer site
--------------------------

Use the following steps to set up a customer site:

#. `Sign into </lift/profile-mgr#signing>`__ the |acquia-product:lpm|
   interface, and then click the
   **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Customer sites** link.
#. Click the **Add new customer site** link.
#. Under **Customer Site Details**, enter values in the following fields
   for the new Customer Site:

   -  **Name** - The name of the website.
   -  **External ID** or **Site ID** - An identifier that you choose.
      |acquia-product:cha| can create events for the corresponding
      customer website that you create in |acquia-product:lpm|. When a
      visitor performs this action on a particular customer site, this
      External ID or Site ID is included with it.
   -  **URL** - The URL of the website, entered as a regular expression.
      For example, ``^http?://www.example.com/.*`` means any URL that
      begins with either ``http:///www.example.com/`` or
      ``https://www.example.com/``.

      You can also use regular expressions to map multiple URLs to the
      same customer site. For more information about regular
      expressions, you can use this `regular expressions cheat
      sheet <https://www.cheatography.com/davechild/cheat-sheets/regular-expressions/>`__
      as a reference guide.

#. Click **Save**.

Viewing customer sites
----------------------

To view your customer sites, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the
   **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Customer sites** link.

|acquia-product:lpm| displays a list of the customer sites that you have
created.

Viewing insights by customer site
---------------------------------

After you have created one or more customer sites, the fields that you
have set up to rank in the **Insights** tab — such as content section,
keywords, and content type — will be categorized by website. To display
a visitor's actions organized by customer site, use the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the
   **People** tab.
#. Click **Show Results**.
#. Find the visitor profile that you want to examine, and then click
   anywhere on its entry in the table.
#. On the **Person Details** page, click the **Insights** tab.
#. Use the **Customer Site** list to display the rankings information
   across the different sites this particular visitor has accessed.

Deleting a customer site
------------------------

To delete a customer site, use the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface.
#. `Delete, or associate with another website, any goals belonging to
   this website </lift/profile-mgr/goals>`__.
#. `Delete, or associate with another website, any events belonging to
   this website </lift/profile-mgr/event/category>`__.
#. In the |acquia-product:lpm| interface, click the **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Customer sites** link.
#. In the table of customer sites, find the customer site that you want
   to delete, and in the **Actions** column, click its **Delete** link.

Sending customer site information with APIs
-------------------------------------------

If you have multiple customer websites, you can pass data from each
website to the |acquia-product:cha| service by using the
|acquia-product:liftapi|, File Import API, and JavaScript API. For more
information about using the APIs to do this, see the following pages:

-  |acquia-product:liftapi| `event_import
   call <http://docs.lift.acquia.com/profilemanager/#panel_event_import>`__
-  `File Import API </lift/omni/api/file/import>`__
-  `Capturing page views </lift/javascript/view>`__
