.. include:: /common/global.rst

|acquia-product:acm| terminology and fields
===========================================

|acquia-product:acm| operates by using the same principles that are used
by other commerce platforms. This documentation page describes the
terminology you will encounter, and where you can find that related data
in |acquia-product:acm|.

For information about changing some of the specific configurations, see
`|acquia-product:acm| configuration
settings </commerce/configuration>`__.

Products, SKUs, and Product Options
-----------------------------------

Products are stored as Drupal nodes using the *Product* content type. As
nodes, these products often relate to single pages in your Drupal
website, and are imported from your commerce solution.

A single product will relate to one or more *SKUs* or product variants.
These are non-node entities in Drupal and contain information about a
product, including the display price and product images. SKUs are
related to *Product Options*, such as t-shirt size, and are stored as
taxonomy terms in a Drupal taxonomy vocabulary called **Product
Options**.

To display details about products, sign in to your Drupal website as an
administrator, and then complete the following steps, based on the
information you want to review:

-  *Products* – In the admin menu, click **Content**.
-  *SKUs* – Go to **Commerce > SKUs**.
-  *Product Options* – Go to **Structure > Taxonomy > SKU Product
   Option**.

Product fields
--------------

The **Product** content type contains several default fields used for
integration with your commerce solution, including the following:

-  **Title** – Product title
-  **Marketing Text** – Customer-facing body content
-  **Category** – Product categories
-  **SKUs** – One or more SKUs related to the product (not an entity
   reference field)

You can add additional fields to the product content type as needed for
your website.

To determine the stock availability of a product, Drupal needs to make a
call your commerce platform. This is then cached locally by Drupal for
each individual SKU, using Drupal's cache mechanism (which relies on
Memcache). The cache lifetime in Drupal is proportional to the number of
items in stock — the more items there are, the longer the cache
lifetime. The multiplication factor is a configured element. In the case
of ``0`` items in stock, the cache lifetime is the same as when there is
``1`` item in stock.

SKU fields
----------

Product SKUs are used to uniquely identify your products, and are
imported from your commerce solution.

-  **SKU** – SKU ID
-  **Name** – Name of the product variant
-  **Image** – Image for the product variant
-  **Display Price** – Price displayed to the customer, often the MSRP
   or similar. The actual price (Final price) will be stored in the
   Drupal database separately and synchronized through the
   |acquia-product:ccs|. When displaying a product, a product with a
   discounted price will often show the higher display price (such as
   $15) along with the current price (such as $10). The Final Price
   cannot be edited from the Drupal user interface.
-  **Media** – Raw output from the commerce backend that is processed
   into a Drupal image

You can display additional fields from the form configuration user
interface.

Product option fields
---------------------

Product options are defined in your commerce solution, and are
synchronized with Drupal.

-  **Name** – Displayed option used on the product page
-  **Description** – Description of the product
-  **Attribute ID** – An ID for product attributes
-  **Attribute Code** – Product's attribute code
-  **Attribute Option ID** – Attribute's unique option ID

Product categories
------------------

Product categories are stored as a Taxonomy Vocabulary Product Category.
This vocabulary supports a hierarchy.

-  **Name** – Displayed category name
