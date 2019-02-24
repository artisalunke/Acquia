.. include:: /common/global.rst

Adding categories and products to |acquia-product:acm|
======================================================

.. toctree::
   :hidden:
   :glob:

   /commerce/categories-products/*

|acquia-product:acm| synchronizes its data from your commerce solution
for products and categories. This means that all of your product and
inventory data remains safely stored in your commerce solution, with the
|acquia-product:ccs| ensuring communications with your Drupal website.

After you have created your products and categories in your commerce
solution, synchronization ensures that Drupal is up-to-date with your
commerce data.

.. note::

    Your commerce solution is the source of truth for all data. Data will
    always synchronize from your commerce product, to |acquia-product:acm|.
    Data must be maintained in your commerce solution your commerce solution
    administrators.

Creating categories
-------------------

Product categories are created in your commerce solution, and when
synchronized with your Drupal website, become taxonomy terms, which can
then be used in all the normal ways taxonomy can be manipulated for
display. For example, here is what your categories might look like in
Magento:

|Magento category list|

When synchronized with Drupal, the Drupal taxonomy page should appear
similar to the following:

|Drupal taxonomy terms|

For a full explanation of creating categories in Magento, see `Creating
Categories <http://docs.magento.com/m1/ce/user_guide/catalog/category-create.html>`__.

To get started quickly, or to test your integration, you can create
categories using the following steps:

#. Sign into your Magento server as an administrator.
#. Click **Products**, and then click **Categories**.
#. Select **Add Subcategory**.
#. Enter a name for the category in the **Category Name** field (which
   is a required field).
#. Click **Save** to save your new category.
   Magento will display your new category in the category list.
#. Sign in to your Drupal website as an administrator.
#. Click **Commerce > Configuration > Synchronize Categories**. If
   successful, you should receive a
   ``Category Synchronization Complete`` message.
#. Verify the synchronization by going to **Structure > Taxonomy**.
#. Next to **Product Category**, click **List terms**.

.. important::

    Synchronize your categories before synchronizing products. Failure to
    synchronize categories first will result in failure to place products
    into the correct categories.

Your categories should now be listed on the page.

Creating products in Drupal, using Magento
------------------------------------------

Similar to categories, products are also originally created in your
commerce solution. and then synchronized to your Drupal website. To
learn more about creating products in Magento, see `Creating
Products <http://docs.magento.com/m1/ce/user_guide/catalog/product-create.html>`__.

To create a basic product and add it to your Drupal website, complete
the following steps:

#. Sign into your Magento server as an administrator.
#. Click **Products**, and then click **Catalog**.
#. Click **Add Product**.
#. Fill out the fields for your product.
#. Click **Save**.
#. Sign in to your Drupal website as an administrator.
#. Go to **Commerce > Configuration > Synchronize > Synchronize Products
   (async)**. By default, your content will synchronize in batches of
   50.
#. Click **Content**.

As products synchronize from your commerce solution, they will appear in
the **Content**. You may want to refresh occasionally to review the list
of items. The data transfer may take several minutes to complete,
depending on the number of changes made to your commerce system. While
product details may be cached, product inventory information should
remain at or near real-time.

.. |Magento category list| image:: https://cdn4.webdamdb.com/1280_kU3uvggvyK02.png?-62169955200
   :width: 203px
   :height: 202px
.. |Drupal taxonomy terms| image:: https://cdn2.webdamdb.com/1280_Ik0PeQ2EAkK5.png?-62169955200
   :width: 822px
   :height: 456px
